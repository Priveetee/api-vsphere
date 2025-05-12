import os
import ssl
import traceback
from datetime import datetime
import json # Ensure json is imported for printing

from dotenv import load_dotenv
from pyVim import connect
from pyVmomi import vim, vmodl

# Helper function to safely get attributes
def safe_get(obj, attr_path, default='N/A'):
    """Safely get a nested attribute from an object."""
    try:
        attrs = attr_path.split('.')
        current = obj
        for attr in attrs:
            if current is None:
                return default
            current = getattr(current, attr)
        return current if current is not None else default
    except AttributeError:
        return default
    except Exception:
        return default

def get_host_storage_details(host_mor):
    """
    Collects detailed storage information for a specific ESXi host.
    Focuses on Storage Adapters (HBAs, iSCSI) and basic Multipath info.
    """
    host_storage_info = {
        "host_name": safe_get(host_mor, 'name'),
        "storage_adapters": [],
        "logical_units_multipath": [],
        "iscsi_port_bindings": [] # Initialize for iSCSI port bindings
    }

    if not (host_mor and hasattr(host_mor, 'configManager') and host_mor.configManager and host_mor.configManager.storageSystem):
        print(f"Host {safe_get(host_mor, 'name', 'Unknown Host')} does not have storageSystem configManager or it's None.")
        return host_storage_info

    storage_system = host_mor.configManager.storageSystem
    storage_device_info = safe_get(storage_system, 'storageDeviceInfo', None) 

    if not storage_device_info:
        print(f"Could not retrieve storageDeviceInfo for host {safe_get(host_mor, 'name')}.")
        return host_storage_info

    hba_map_by_key = {}
    if hasattr(storage_device_info, 'hostBusAdapter') and storage_device_info.hostBusAdapter:
        for hba in storage_device_info.hostBusAdapter:
            # print(f"DEBUG: HBA Object: {hba}, Actual VMODL Class Name: {hba.__class__.__name__}")
            adapter_details = {
                "key": safe_get(hba, 'key'),
                "device": safe_get(hba, 'device'), 
                "bus": safe_get(hba, 'bus'),
                "status": safe_get(hba, 'status'),
                "model": safe_get(hba, 'model'),
                "driver": safe_get(hba, 'driver'),
                "pci": safe_get(hba, 'pci'),
                "type": hba.__class__.__name__ 
            }
            if isinstance(hba, vim.HostFibreChannelHba):
                adapter_details["node_wwn"] = "{:x}".format(safe_get(hba, 'nodeWorldWideName', 0)) if safe_get(hba, 'nodeWorldWideName', 0) != 0 else 'N/A'
                adapter_details["port_wwn"] = "{:x}".format(safe_get(hba, 'portWorldWideName', 0)) if safe_get(hba, 'portWorldWideName', 0) != 0 else 'N/A'
                adapter_details["speed_gbps"] = safe_get(hba, 'speed', 0) / 1000 if safe_get(hba, 'speed', 0) !=0 else 'N/A'
            elif isinstance(hba, vim.HostInternetScsiHba):
                adapter_details["iscsi_name"] = safe_get(hba, 'iScsiName')
                adapter_details["iscsi_alias"] = safe_get(hba, 'iScsiAlias')
            
            if hasattr(hba, 'nvmeQualifiedName'): 
                adapter_details["nvme_qualified_name"] = safe_get(hba, 'nvmeQualifiedName')
            
            host_storage_info["storage_adapters"].append(adapter_details)
            if adapter_details["key"] != 'N/A':
                hba_map_by_key[adapter_details["key"]] = adapter_details

    scsi_lun_details_map = {}
    if hasattr(storage_device_info, 'scsiLun') and storage_device_info.scsiLun:
        for scsi_lun_device in storage_device_info.scsiLun:
            scsi_lun_details_map[scsi_lun_device.key] = {
                "device_name": safe_get(scsi_lun_device, 'deviceName'),
                "canonical_name": safe_get(scsi_lun_device, 'canonicalName'),
                "vendor": safe_get(scsi_lun_device, 'vendor'),
                "model": safe_get(scsi_lun_device, 'model'),
                "lun_type": safe_get(scsi_lun_device, 'lunType'),
                "queue_depth": safe_get(scsi_lun_device, 'queueDepth'),
                "is_ssd": safe_get(scsi_lun_device, 'ssd', False),
                "is_local": safe_get(scsi_lun_device, 'localDisk', False),
                "operational_state": list(safe_get(scsi_lun_device, 'operationalState', [])),
                "capabilities_unmap": safe_get(scsi_lun_device, 'capabilities.unmap', None),
                "capabilities_zero_blocks": safe_get(scsi_lun_device, 'capabilities.zeroBlocks', None)
            }

    if hasattr(storage_device_info, 'multipathInfo') and storage_device_info.multipathInfo and \
       hasattr(storage_device_info.multipathInfo, 'lun') and storage_device_info.multipathInfo.lun:
        for lun_mp_info in storage_device_info.multipathInfo.lun: 
            lun_details = {
                "key": safe_get(lun_mp_info, 'key'),
                "id": safe_get(lun_mp_info, 'id'), 
                "lun_type_mp": safe_get(lun_mp_info, 'lunType'),
                "paths": [],
                "policy": {
                    "name": safe_get(lun_mp_info, 'policy.policy'),
                    "preferred_path_key": safe_get(lun_mp_info, 'policy.preferredPath') 
                },
                "satp": safe_get(lun_mp_info, 'policy.storageArrayTypePolicy.policy', 'N/A') 
            }
            
            scsi_lun_key_for_mp = safe_get(lun_mp_info, 'lun')
            if scsi_lun_key_for_mp in scsi_lun_details_map:
                lun_details.update(scsi_lun_details_map[scsi_lun_key_for_mp])
            
            if hasattr(lun_mp_info, 'path') and lun_mp_info.path:
                for path in lun_mp_info.path: 
                    adapter_device_name = "N/A"
                    adapter_key = safe_get(path, 'adapter')
                    if adapter_key in hba_map_by_key:
                        adapter_device_name = hba_map_by_key[adapter_key].get('device', 'N/A')

                    path_details = {
                        "key": safe_get(path, 'key'),
                        "name": safe_get(path, 'name'), 
                        "path_state": safe_get(path, 'pathState'), 
                        "state": safe_get(path, 'state'), 
                        "adapter_key": adapter_key, 
                        "adapter_device_name": adapter_device_name, 
                        "lun_target_key": safe_get(path, 'lun'), 
                        "transport_type": "N/A" 
                    }
                    
                    transport_obj = safe_get(path, 'transport', None)
                    if transport_obj:
                        transport_class_name = transport_obj.__class__.__name__
                        path_details["transport_type"] = transport_class_name
                        # print(f"DEBUG: Path Transport Object: {transport_obj}, Actual VMODL Class Name: {transport_class_name}")
                        if hasattr(transport_obj, 'portWorldWideName') and hasattr(transport_obj, 'nodeWorldWideName'):
                            path_details["fc_transport_wwnn"] = "{:x}".format(safe_get(transport_obj, 'nodeWorldWideName', 0)) if safe_get(transport_obj, 'nodeWorldWideName', 0) != 0 else 'N/A'
                            path_details["fc_transport_wwpn"] = "{:x}".format(safe_get(transport_obj, 'portWorldWideName', 0)) if safe_get(transport_obj, 'portWorldWideName', 0) != 0 else 'N/A'
                        elif hasattr(transport_obj, 'iScsiName'):
                            path_details["iscsi_transport_name"] = safe_get(transport_obj, 'iScsiName')
                            path_details["iscsi_transport_alias"] = safe_get(transport_obj, 'iScsiAlias')

                    if lun_details["policy"]["preferred_path_key"] == path_details["key"]:
                        lun_details["policy"]["preferred_path_name"] = path_details["name"]
                    lun_details["paths"].append(path_details)
            host_storage_info["logical_units_multipath"].append(lun_details)

    # Collect iSCSI Port Binding Information
    if hasattr(storage_system, 'QueryBoundVnics'): # Check if the method exists
        software_iscsi_hba_device_name = None
        for hba_detail in host_storage_info.get("storage_adapters", []):
            hba_type = hba_detail.get("type")
            hba_model = hba_detail.get("model", "").lower()
            # Heuristic for software iSCSI adapter: type is InternetScsiHba and model often contains "software"
            # or it's the one without a PCI address if multiple iSCSI HBAs exist.
            if hba_type == "vim.host.InternetScsiHba" and \
               ("software" in hba_model or hba_detail.get("pci") == "N/A" or not hba_detail.get("pci")):
                software_iscsi_hba_device_name = hba_detail.get("device")
                if software_iscsi_hba_device_name and software_iscsi_hba_device_name != 'N/A':
                    break # Found a candidate

        if software_iscsi_hba_device_name:
            # print(f"DEBUG: Attempting QueryBoundVnics for HBA: {software_iscsi_hba_device_name}")
            try:
                bound_vnics_info = storage_system.QueryBoundVnics(iScsiHbaName=software_iscsi_hba_device_name)
                if bound_vnics_info:
                    for bound_vnic_item in bound_vnics_info: # bound_vnics_info is a list of HostInternetScsiHbaHostVnicBinding
                        binding_details = {
                            "iscsi_hba_device": software_iscsi_hba_device_name,
                            "vmkernel_nic_device": safe_get(bound_vnic_item, 'vnicDevice'),
                            "vnic_key": safe_get(bound_vnic_item, 'vnic'),
                            # Additional details from the binding object itself if needed
                            # "pnic_on_vnic_uplink": safe_get(bound_vnic_item, 'pnicDevice') # This might not be directly on HostInternetScsiHbaHostVnicBinding
                        }
                        host_storage_info["iscsi_port_bindings"].append(binding_details)
            except vim.fault.NotFound:
                print(f"DEBUG: QueryBoundVnics: Software iSCSI adapter '{software_iscsi_hba_device_name}' not found by vCenter or no bindings for it on host {host_mor.name}.")
            except vmodl.fault.InvalidArgument as e:
                print(f"DEBUG: QueryBoundVnics: Invalid argument for HBA '{software_iscsi_hba_device_name}' on host {host_mor.name}. Msg: {e.msg}")
            except Exception as e:
                print(f"Error collecting iSCSI port bindings for HBA '{software_iscsi_hba_device_name}' on host {host_mor.name}: {type(e).__name__} - {e}")
                # traceback.print_exc()
        else:
            print(f"DEBUG: No suitable Software iSCSI HBA found for QueryBoundVnics on host {host_mor.name}.")
            
    return host_storage_info

def main_test_storage():
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

        target_host_name = "vm-esx-pp-03.bcaexpertise.org" 
        host_to_test = None

        if target_host_name:
            search_filter = content.searchIndex.FindByInventoryPath(target_host_name)
            if search_filter and isinstance(search_filter, vim.HostSystem):
                host_to_test = search_filter
            else: 
                host_view = content.viewManager.CreateContainerView(
                    content.rootFolder, [vim.HostSystem], True
                )
                for host_mor_item in host_view.view:
                    if host_mor_item.name == target_host_name:
                        host_to_test = host_mor_item
                        break
                host_view.Destroy()
            
            if not host_to_test:
                 print(f"Host '{target_host_name}' not found using inventory path or iteration.")
        else: 
            datacenter_view = content.viewManager.CreateContainerView(
                content.rootFolder, [vim.Datacenter], True
            )
            if datacenter_view.view:
                host_folder = datacenter_view.view[0].hostFolder
                host_view = content.viewManager.CreateContainerView(
                    host_folder, [vim.HostSystem], True
                )
                if host_view.view:
                    host_to_test = host_view.view[0]
                host_view.Destroy()
            datacenter_view.Destroy()

        if host_to_test:
            print(f"\n--- Collecting Storage Details for Host: {host_to_test.name} ---")
            storage_data = get_host_storage_details(host_to_test)
            
            print("\n--- Full Storage Data (JSON) ---")
            print(json.dumps(storage_data, indent=2, default=str))

            print(f"\n--- Storage Adapters (HBAs) for {host_to_test.name} ---")
            if storage_data.get("storage_adapters"):
                for adapter in storage_data["storage_adapters"]:
                    print(f"  Device: {adapter.get('device', 'N/A')}, Type: {adapter.get('type', 'N/A')}, Model: {adapter.get('model', 'N/A')}, Driver: {adapter.get('driver', 'N/A')}")
                    if adapter.get('type') == "vim.HostFibreChannelHba": # Match actual class name
                        print(f"    Node WWN: {adapter.get('node_wwn', 'N/A')}, Port WWN: {adapter.get('port_wwn', 'N/A')}, Speed: {adapter.get('speed_gbps', 'N/A')} Gbps")
                    elif adapter.get('type') == "vim.HostInternetScsiHba": # Match actual class name
                        print(f"    iSCSI Name: {adapter.get('iscsi_name', 'N/A')}")
                    if "nvme_qualified_name" in adapter:
                         print(f"    NQN: {adapter.get('nvme_qualified_name', 'N/A')}")
            else:
                print("  No storage adapters found or data incomplete.")
            
            print(f"\n--- Logical Units (LUNs) & Multipathing for {host_to_test.name} ---")
            if storage_data.get("logical_units_multipath"):
                for lun in storage_data["logical_units_multipath"]:
                    print(f"  LUN ID: {lun.get('id', 'N/A')}, Device: {lun.get('device_name', 'N/A')}, Vendor: {lun.get('vendor', 'N/A')}, Model: {lun.get('model', 'N/A')}")
                    print(f"    SATP: {lun.get('satp', 'N/A')}, Is Local: {lun.get('is_local', 'N/A')}, Is SSD: {lun.get('is_ssd', 'N/A')}, OpState: {lun.get('operational_state', [])}")
                    print(f"    Policy: {lun.get('policy', {}).get('name', 'N/A')}, Preferred Path: {lun.get('policy', {}).get('preferred_path_name', lun.get('policy', {}).get('preferred_path_key', 'N/A'))}")
                    print(f"    Paths ({len(lun.get('paths', []))} total):")
                    if lun.get('paths'):
                        for path in lun["paths"]:
                            transport_details = []
                            if "fc_transport_wwnn" in path:
                                transport_details.append(f"FC WWNN: {path['fc_transport_wwnn']}, FC WWPN: {path['fc_transport_wwpn']}")
                            if "iscsi_transport_name" in path:
                                transport_details.append(f"iSCSI Name: {path['iscsi_transport_name']}")
                            print(f"      - Name: {path.get('name', 'N/A')} (PathState: {path.get('path_state', 'N/A')}, State: {path.get('state','N/A')}) via Adapter: {path.get('adapter_device_name', path.get('adapter_key','N/A'))}, Transport: {path.get('transport_type', 'N/A')}" + (f", Details: {'; '.join(transport_details)}" if transport_details else ""))
                    else:
                        print("      No paths listed for this LUN.")
            else:
                print("  No LUNs with multipath information found or data incomplete.")

            print(f"\n--- iSCSI Port Bindings for {host_to_test.name} ---")
            if storage_data.get("iscsi_port_bindings"):
                for binding in storage_data["iscsi_port_bindings"]:
                    print(f"  HBA: {binding.get('iscsi_hba_device')}, VMkernel NIC: {binding.get('vmkernel_nic_device')}")
            else:
                print("  No iSCSI port bindings found or data incomplete.")
        else:
            print("No host selected or found for testing.")

    except vim.fault.InvalidLogin as e:
        print(f"Error: Invalid login credentials. Details: {e.msg}")
    except ConnectionRefusedError:
        print(f"Error: Connection refused to {vcenter_host}.")
    except vim.fault.HostConnectFault as e:
        print(f"Error: Could not connect to host {vcenter_host}. Details: {e.msg}")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}.")
    except Exception as e:
        print(f"Unexpected Error: {e.__class__.__name__} - {e}")
        traceback.print_exc()
    finally:
        if si:
            print("\nDisconnecting from vCenter Server...")
            connect.Disconnect(si)
            print("Successfully disconnected.")

if __name__ == "__main__":
    print("Running Host Storage Details Collector Test Script...")
    main_test_storage()

