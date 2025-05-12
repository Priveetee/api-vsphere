import os
import ssl
import traceback
from dotenv import load_dotenv
from pyVim import connect
from pyVmomi import vim, vmodl

# Helper function to safely get attributes (version simplifiée pour ce test)
def safe_get(obj, attr_path, default='N/A'):
    """Safely get a nested attribute from an object."""
    try:
        attrs = attr_path.split('.')
        current = obj
        for attr in attrs:
            if current is None or current == 'N/A': # Stop if 'N/A' encountered
                return default
            current = getattr(current, attr)
        return current if current is not None else default
    except AttributeError:
        return default
    except Exception as e:
        print(f"safe_get unexpected error: {e} while getting {attr_path} from {type(obj)}")
        return default

def debug_datastore_mounts(content):
    """Focuses on debugging ds_mor.host and mount_info.key."""
    print("\n--- Starting Datastore Host Mount Debug ---")
    ds_view = None
    try:
        ds_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.Datastore], True)
        for ds_mor in ds_view.view: # ds_mor is a Datastore MOR
            ds_name = safe_get(ds_mor, 'name', 'Unknown Datastore')
            print(f"\nInspecting Datastore: {ds_name} (MOR: {ds_mor})")

            host_mounts = safe_get(ds_mor, 'host', []) # Get the list of host mounts

            if host_mounts == 'N/A':
                print(f"  ds_mor.host is 'N/A' for datastore {ds_name}. Skipping.")
                continue
            if not isinstance(host_mounts, list):
                print(f"  ds_mor.host is not a list for datastore {ds_name} (Type: {type(host_mounts)}). Skipping.")
                continue
            if not host_mounts:
                print(f"  Datastore {ds_name} has no host mounts (ds_mor.host is empty).")
                continue

            print(f"  Found {len(host_mounts)} host mount entries for {ds_name}.")
            for i, mount_info in enumerate(host_mounts): # mount_info should be DatastoreHostMount
                print(f"  --- Mount Entry {i+1} ---")
                print(f"    mount_info object: {mount_info}")
                print(f"    mount_info type: {type(mount_info)}")

                if not hasattr(mount_info, 'key'):
                    print(f"    ERROR: mount_info object does not have 'key' attribute!")
                    continue

                host_mor_candidate = mount_info.key # This is the critical part
                
                print(f"    mount_info.key (host_mor_candidate) value: {host_mor_candidate}")
                print(f"    mount_info.key (host_mor_candidate) type: {type(host_mor_candidate)}")

                if host_mor_candidate is None:
                    print(f"    mount_info.key is None.")
                elif isinstance(host_mor_candidate, str):
                    print(f"    mount_info.key is a STRING: '{host_mor_candidate}'")
                elif hasattr(host_mor_candidate, '_moId'):
                    print(f"    mount_info.key IS A VALID MOR. _moId: {host_mor_candidate._moId}")
                    host_name = safe_get(host_mor_candidate, 'name', 'N/A (MOR name not found)')
                    print(f"      Attempting to get host name: {host_name}")
                else:
                    print(f"    mount_info.key is an object of type {type(host_mor_candidate)} but not a recognized MOR (no _moId).")

                # Tentative d'utiliser str() pour voir si cela déclenche l'erreur
                try:
                    str_representation = str(host_mor_candidate)
                    print(f"    str(host_mor_candidate): {str_representation}")
                except Exception as e_str:
                    print(f"    ERROR calling str(host_mor_candidate): {type(e_str).__name__} - {e_str}")
                
                # Tentative de comparaison (simule ce qui pourrait causer l'erreur)
                # On compare avec un MOR connu (ici, le ds_mor lui-même, juste pour le test de comparaison)
                # Dans le code réel, ce serait une comparaison avec un autre MOR.
                try:
                    # Ceci est juste pour tester la comparaison. Ne pas utiliser dans la logique réelle.
                    _ = (host_mor_candidate == ds_mor) 
                    print(f"    Comparison (host_mor_candidate == ds_mor) did not raise error.")
                except AttributeError as e_comp:
                    if '_moId' in str(e_comp):
                        print(f"    ERROR DURING COMPARISON (host_mor_candidate == ds_mor): AttributeError - '_moId'. host_mor_candidate was likely a string.")
                    else:
                        print(f"    ERROR DURING COMPARISON (host_mor_candidate == ds_mor): {type(e_comp).__name__} - {e_comp}")
                except Exception as e_comp_other:
                    print(f"    ERROR DURING COMPARISON (host_mor_candidate == ds_mor) - OTHER EXCEPTION: {type(e_comp_other).__name__} - {e_comp_other}")


    except Exception as e:
        print(f"General Error in debug_datastore_mounts: {e.__class__.__name__} - {e}")
        traceback.print_exc()
    finally:
        if ds_view:
            ds_view.Destroy()
    print("\n--- Finished Datastore Host Mount Debug ---")


def main():
    load_dotenv()
    vcenter_host = os.getenv("VCENTER_HOST")
    vcenter_user = os.getenv("VCENTER_USER")
    vcenter_password = os.getenv("VCENTER_PASSWORD")

    if not all([vcenter_host, vcenter_user, vcenter_password]):
        print("Error: VCENTER_HOST, VCENTER_USER, or VCENTER_PASSWORD not found in .env")
        return

    context = None
    if hasattr(ssl, "_create_unverified_context"):
        context = ssl._create_unverified_context()

    si = None
    try:
        print(f"Connecting to {vcenter_host} as {vcenter_user}...")
        si = connect.SmartConnect(
            host=vcenter_host, user=vcenter_user, pwd=vcenter_password, port=443, sslContext=context
        )
        print("Successfully connected!")
        content = si.content
        
        debug_datastore_mounts(content)

    except vim.fault.InvalidLogin as e:
        print(f"Error: Invalid login credentials. Details: {e.msg}")
    except ConnectionRefusedError:
        print(f"Error: Connection refused to {vcenter_host}.")
    except vmodl.fault.HostCommunication as e: 
        print(f"Host Communication Error: {e.msg}")
    except Exception as e:
        print(f"Unexpected Error: {e.__class__.__name__} - {e}")
        traceback.print_exc()
    finally:
        if si:
            print("\nDisconnecting from vCenter Server...")
            connect.Disconnect(si)
            print("Successfully disconnected.")

if __name__ == "__main__":
    print("Running Datastore Host Mount Debug Script...")
    main()

