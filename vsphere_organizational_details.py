import os
import ssl
import traceback
import json
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
            if current is None: return default
            current = getattr(current, attr)
        return current if current is not None else default
    except AttributeError: return default
    except Exception: return default

def get_resource_pool_details(content):
    """Collects details about Resource Pools."""
    resource_pools_data = []
    rp_view = None
    try:
        container = content.rootFolder
        view_type = [vim.ResourcePool]
        recursive = True 
        rp_view = content.viewManager.CreateContainerView(container, view_type, recursive)
        for rp_mor in rp_view.view:
            config_info = safe_get(rp_mor, 'config', None)
            cpu_alloc = safe_get(config_info, 'cpuAllocation', None)
            mem_alloc = safe_get(config_info, 'memoryAllocation', None)
            parent_name = "N/A"
            parent_type = "N/A"
            if rp_mor.parent:
                parent_name = safe_get(rp_mor.parent, 'name', str(rp_mor.parent))
                parent_type = rp_mor.parent.__class__.__name__
            rp_details = {
                "name": safe_get(rp_mor, 'name'), "mor_id": str(rp_mor),
                "overall_status": safe_get(rp_mor, 'overallStatus'),
                "parent_name": parent_name, "parent_type": parent_type,
                "parent_mor_id": str(rp_mor.parent) if rp_mor.parent else "N/A",
                "config_name": safe_get(config_info, 'name'),
                "config_entity": str(safe_get(config_info, 'entity')) if safe_get(config_info, 'entity') else "N/A",
                "cpu_reservation_mhz": safe_get(cpu_alloc, 'reservation', 0) if cpu_alloc else 0,
                "cpu_expandable_reservation": safe_get(cpu_alloc, 'expandableReservation', False) if cpu_alloc else False,
                "cpu_limit_mhz": safe_get(cpu_alloc, 'limit', -1) if cpu_alloc else -1,
                "cpu_shares_level": safe_get(cpu_alloc, 'shares.level', 'N/A') if safe_get(cpu_alloc, 'shares') else 'N/A',
                "cpu_shares_value": safe_get(cpu_alloc, 'shares.shares', 0) if safe_get(cpu_alloc, 'shares') else 0,
                "mem_reservation_mb": safe_get(mem_alloc, 'reservation', 0) if mem_alloc else 0,
                "mem_expandable_reservation": safe_get(mem_alloc, 'expandableReservation', False) if mem_alloc else False,
                "mem_limit_mb": safe_get(mem_alloc, 'limit', -1) if mem_alloc else -1,
                "mem_shares_level": safe_get(mem_alloc, 'shares.level', 'N/A') if safe_get(mem_alloc, 'shares') else 'N/A',
                "mem_shares_value": safe_get(mem_alloc, 'shares.shares', 0) if safe_get(mem_alloc, 'shares') else 0,
                "vms_in_pool": [vm.name for vm in safe_get(rp_mor, 'vm', []) if hasattr(vm, 'name')],
                "child_resource_pools": [child_rp.name for child_rp in safe_get(rp_mor, 'resourcePool', []) if hasattr(child_rp, 'name')]
            }
            resource_pools_data.append(rp_details)
    finally:
        if rp_view: rp_view.Destroy()
    return resource_pools_data

def get_custom_attributes_for_object(obj_mor, custom_field_defs_map):
    """Helper to get custom attribute values for a single managed object."""
    attributes = {}
    custom_values_list = None
    if hasattr(obj_mor, 'summary') and hasattr(obj_mor.summary, 'customValue') and obj_mor.summary.customValue is not None:
        custom_values_list = obj_mor.summary.customValue
    elif hasattr(obj_mor, 'customValue') and obj_mor.customValue is not None:
        custom_values_list = obj_mor.customValue

    if custom_values_list:
        for cv in custom_values_list:
            field_key = cv.key
            if field_key in custom_field_defs_map:
                field_name = custom_field_defs_map[field_key].get("name", f"unknown_field_{field_key}")
                attributes[field_name] = cv.value
            else:
                attributes[f"field_key_{field_key}"] = cv.value 
    return attributes

def get_organizational_tags_and_attributes(content, si):
    """Collects Custom Attribute definitions and values for VMs and Hosts."""
    org_data = {
        "custom_attribute_definitions": [],
        "vms_custom_attributes": [],
        "hosts_custom_attributes": [],
        "tag_categories": [], "tags": [], 
    }

    custom_field_defs_map = {} 
    if content.customFieldsManager and content.customFieldsManager.field:
        for field_def in content.customFieldsManager.field:
            definition = {
                "key": field_def.key, "name": field_def.name,
                "type": str(field_def.type), 
                "managed_object_type": str(field_def.managedObjectType)
            }
            org_data["custom_attribute_definitions"].append(definition)
            custom_field_defs_map[field_def.key] = definition
    
    vm_view = None
    try:
        vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
        for vm_mor in vm_view.view:
            if safe_get(vm_mor, 'config.template', False): continue
            vm_attributes = get_custom_attributes_for_object(vm_mor, custom_field_defs_map)
            if vm_attributes: 
                org_data["vms_custom_attributes"].append({
                    "vm_name": safe_get(vm_mor, 'name'), "vm_mor_id": str(vm_mor),
                    "attributes": vm_attributes
                })
    finally:
        if vm_view: vm_view.Destroy()

    host_view = None
    try:
        host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
        for host_mor in host_view.view:
            host_attributes = get_custom_attributes_for_object(host_mor, custom_field_defs_map)
            if host_attributes: 
                org_data["hosts_custom_attributes"].append({
                    "host_name": safe_get(host_mor, 'name'), "host_mor_id": str(host_mor),
                    "attributes": host_attributes
                })
    finally:
        if host_view: host_view.Destroy()

    print("WARNING: Tag collection requires vSphere Automation SDK or REST calls, not fully implemented with pyVmomi alone.")
    return org_data

def get_dvs_details(content):
    """Collects detailed information about Distributed Virtual Switches."""
    dvs_data = []
    dvs_view = None
    try:
        dvs_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.DistributedVirtualSwitch], True)
        for dvs_mor in dvs_view.view:
            config = safe_get(dvs_mor, 'config', None)
            summary = safe_get(dvs_mor, 'summary', None)
            capability = safe_get(dvs_mor, 'capability', None)
            net_resource_mgmt = safe_get(config, 'networkResourceManagementConfig', None)
            pvlan_config = safe_get(config, 'pvlanConfig', [])
            lacp_groups = safe_get(config, 'lacpGroupConfig', [])

            dvs_detail = {
                "name": safe_get(summary, 'name'), "uuid": safe_get(summary, 'uuid'),
                "mor_id": str(dvs_mor), "version": safe_get(config, 'productInfo.version'),
                "description": safe_get(config, 'description'),
                "mtu": safe_get(summary, 'maxMtu', safe_get(config, 'maxMtu')),
                "num_ports": safe_get(summary, 'numPorts'),
                "num_hosts": len(safe_get(config, 'host', [])),
                "uplink_port_policy": {}, 
                "default_port_config": {"security_policy": {}, "vlan_info": "N/A"},
                "contact_name": safe_get(config, 'contact.name'),
                "contact_info": safe_get(config, 'contact.contact'),
                "link_discovery_protocol": "N/A", "link_discovery_operation": "N/A",
                "health_check_supported": safe_get(capability, 'healthCheckSupported', False),
                "health_check_config": [],
                "nioc_enabled": safe_get(net_resource_mgmt, 'enabled', False) if net_resource_mgmt else False,
                "nioc_version": safe_get(net_resource_mgmt, 'networkResourceManagementCapability.version') if safe_get(net_resource_mgmt, 'networkResourceManagementCapability') else 'N/A',
                "nioc_resource_pools": [],
                "private_vlans": [{"primary_vlan": pv.primaryVlanId, "secondary_vlan": pv.secondaryVlanId, "type": pv.pvlanType} for pv in pvlan_config if hasattr(pv, 'primaryVlanId')],
                "lacp_groups": [], "port_groups": []
            }
            
            uplink_port_policy_obj = safe_get(config, 'uplinkPortPolicy')
            if uplink_port_policy_obj != 'N/A':
                teaming_policy_obj = safe_get(uplink_port_policy_obj, 'policy')
                if teaming_policy_obj != 'N/A':
                    dvs_detail["uplink_port_policy"]["teaming_policy"] = safe_get(teaming_policy_obj, 'value')
                dvs_detail["uplink_port_policy"]["reverse_policy"] = safe_get(uplink_port_policy_obj, 'reversePolicy', None)
                dvs_detail["uplink_port_policy"]["notify_switches"] = safe_get(uplink_port_policy_obj, 'notifySwitches', None)
            
            default_port_conf_obj = safe_get(config, 'defaultPortConfig')
            if default_port_conf_obj != 'N/A':
                default_vlan_setting = safe_get(default_port_conf_obj, 'vlan')
                if isinstance(default_vlan_setting, vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec):
                    dvs_detail["default_port_config"]["vlan_info"] = str(safe_get(default_vlan_setting, 'vlanId', 'N/A'))
                elif isinstance(default_vlan_setting, vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec):
                    ranges = [f"{item.start}-{item.end}" for item in safe_get(default_vlan_setting, 'vlanId', []) if hasattr(item, 'start')]
                    dvs_detail["default_port_config"]["vlan_info"] = f"Trunk ({', '.join(ranges)})"
                else:
                    dvs_detail["default_port_config"]["vlan_info"] = str(default_vlan_setting)

                sec_policy = safe_get(default_port_conf_obj, 'securityPolicy')
                if sec_policy != 'N/A':
                    dvs_detail["default_port_config"]["security_policy"]["allow_promiscuous"] = safe_get(sec_policy, 'allowPromiscuous.value') if safe_get(sec_policy, 'allowPromiscuous') != 'N/A' else None
                    dvs_detail["default_port_config"]["security_policy"]["mac_changes"] = safe_get(sec_policy, 'macChanges.value') if safe_get(sec_policy, 'macChanges') != 'N/A' else None
                    dvs_detail["default_port_config"]["security_policy"]["forged_transmits"] = safe_get(sec_policy, 'forgedTransmits.value') if safe_get(sec_policy, 'forgedTransmits') != 'N/A' else None

            ldp_config = safe_get(config, 'linkDiscoveryProtocolConfig')
            if ldp_config != 'N/A':
                dvs_detail["link_discovery_protocol"] = safe_get(ldp_config, 'protocol') 
                dvs_detail["link_discovery_operation"] = safe_get(ldp_config, 'operation')

            if dvs_detail["health_check_supported"]:
                health_conf_list = safe_get(config, 'healthCheckConfig', []) # It's a list
                if isinstance(health_conf_list, list):
                    for hc in health_conf_list: # hc is DVSHealthCheckConfig
                        dvs_detail["health_check_config"].append({
                            "vlan_enabled": safe_get(hc, 'enable'), 
                            "mtu_enabled": safe_get(hc, 'enableMtu'), 
                            "teaming_enabled": safe_get(hc, 'enableTeaming'), 
                            "interval": safe_get(hc, 'interval') 
                        })
            
            if net_resource_mgmt and dvs_detail["nioc_enabled"] and hasattr(net_resource_mgmt, 'networkResourcePool'):
                for pool in net_resource_mgmt.networkResourcePool:
                    dvs_detail["nioc_resource_pools"].append({
                        "key": pool.key, "name": safe_get(pool, 'name', 'SystemDefined'),
                        "description": safe_get(pool, 'description'),
                        "allocation_shares": safe_get(pool, 'allocationInfo.shares.shares'),
                        "allocation_limit_mhz": safe_get(pool, 'allocationInfo.limit'),
                        "priority_tag": safe_get(pool, 'allocationInfo.priorityTag')
                    })
            
            for lacp_group in lacp_groups:
                dvs_detail["lacp_groups"].append({
                    "key": safe_get(lacp_group, 'key'), "name": safe_get(lacp_group, 'name'),
                    "mode": safe_get(lacp_group, 'mode'), 
                    "uplink_ports": [uplink.uplinkPortKey for uplink in safe_get(lacp_group, 'uplinkPort', []) if hasattr(uplink, 'uplinkPortKey')],
                    "load_balance_algorithm": safe_get(lacp_group, 'loadBalanceAlgorithm')
                })

            dpg_view_local = None
            try:
                dpg_view_local = content.viewManager.CreateContainerView(content.rootFolder, [vim.dvs.DistributedVirtualPortgroup], True)
                for dpg_mor in dpg_view_local.view:
                    dpg_config = safe_get(dpg_mor, 'config')
                    if dpg_config != 'N/A' and safe_get(dpg_config, 'distributedVirtualSwitch') == dvs_mor:
                        vlan_setting = safe_get(dpg_config, 'defaultPortConfig.vlan')
                        vlan_info = "N/A"
                        if isinstance(vlan_setting, vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec):
                            vlan_info = str(safe_get(vlan_setting, 'vlanId', 'N/A'))
                        elif isinstance(vlan_setting, vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec):
                            ranges = [f"{item.start}-{item.end}" for item in safe_get(vlan_setting, 'vlanId', []) if hasattr(item, 'start')]
                            vlan_info = f"Trunk ({', '.join(ranges)})"
                        dvs_detail["port_groups"].append({
                            "name": safe_get(dpg_mor, 'name'), "key": safe_get(dpg_mor, 'key'),
                            "num_ports": safe_get(dpg_config, 'numPorts'),
                            "type": safe_get(dpg_config, 'type'), 
                            "vlan_info": vlan_info, "description": safe_get(dpg_config, 'description')
                        })
            finally:
                if dpg_view_local: dpg_view_local.Destroy()
            dvs_data.append(dvs_detail)
    finally:
        if dvs_view: dvs_view.Destroy()
    return dvs_data

def main_test_org_details():
    load_dotenv()
    vcenter_host = os.getenv("VCENTER_HOST")
    vcenter_user = os.getenv("VCENTER_USER")
    vcenter_password = os.getenv("VCENTER_PASSWORD")

    if not all([vcenter_host, vcenter_user, vcenter_password]):
        print("Error: VCENTER_HOST, VCENTER_USER, or VCENTER_PASSWORD not found.")
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

        print("\n--- Collecting Resource Pool Details ---")
        rp_data = get_resource_pool_details(content)
        print("\nResource Pool Data (JSON):")
        print(json.dumps(rp_data, indent=2, default=str))
        
        print("\n--- Resource Pools Summary ---")
        for rp in rp_data:
            print(f"  Name: {rp.get('name', 'N/A')} (Status: {rp.get('overall_status', 'N/A')})")
            print(f"    Parent: {rp.get('parent_name', 'N/A')} ({rp.get('parent_type', 'N/A')})")
            print(f"    CPU: Res={rp.get('cpu_reservation_mhz','N/A')}MHz, Limit={rp.get('cpu_limit_mhz','N/A')}MHz, Shares={rp.get('cpu_shares_value','N/A')} ({rp.get('cpu_shares_level','N/A')})")
            print(f"    Memory: Res={rp.get('mem_reservation_mb','N/A')}MB, Limit={rp.get('mem_limit_mb','N/A')}MB, Shares={rp.get('mem_shares_value','N/A')} ({rp.get('mem_shares_level','N/A')})")
            vms_in_pool = rp.get('vms_in_pool', [])
            if vms_in_pool:
                print(f"    VMs: {', '.join(vms_in_pool[:3])}{'...' if len(vms_in_pool) > 3 else ''} ({len(vms_in_pool)} total)")
            child_rps = rp.get('child_resource_pools', [])
            if child_rps:
                print(f"    Child RPs: {', '.join(child_rps)}")

        print("\n--- Collecting Custom Attributes ---")
        org_info = get_organizational_tags_and_attributes(content, si)
        print("\nCustom Attribute Definitions:")
        print(json.dumps(org_info.get("custom_attribute_definitions", []), indent=2, default=str))
        print("\nVMs Custom Attributes (first 3 VMs with attributes):")
        print(json.dumps(org_info.get("vms_custom_attributes", [])[:3], indent=2, default=str))
        print("\nHosts Custom Attributes (first 3 Hosts with attributes):")
        print(json.dumps(org_info.get("hosts_custom_attributes", [])[:3], indent=2, default=str))

        print("\n--- Collecting Distributed Virtual Switch Details ---")
        dvs_info = get_dvs_details(content)
        print("\nDistributed Virtual Switch Data (JSON):")
        print(json.dumps(dvs_info, indent=2, default=str))

        print("\n--- DVS Summary ---")
        for dvs in dvs_info:
            print(f"  DVS Name: {dvs.get('name', 'N/A')} (UUID: {dvs.get('uuid', 'N/A')})")
            print(f"    Version: {dvs.get('version', 'N/A')}, MTU: {dvs.get('mtu', 'N/A')}, Num Hosts: {dvs.get('num_hosts', 'N/A')}")
            uplink_policy = dvs.get('uplink_port_policy', {})
            print(f"    Uplink Teaming Policy: {uplink_policy.get('teaming_policy', 'N/A')}")
            print(f"    Link Discovery: {dvs.get('link_discovery_protocol', 'N/A')} (Op: {dvs.get('link_discovery_operation', 'N/A')})")
            print(f"    Health Check Supported: {dvs.get('health_check_supported')}")
            if dvs.get('health_check_config'):
                print(f"    Health Check Config: {dvs.get('health_check_config')}")
            print(f"    NIOC Enabled: {dvs.get('nioc_enabled', 'N/A')}")
            lacp_groups_summary = dvs.get('lacp_groups', [])
            if lacp_groups_summary:
                print(f"    LACP Groups ({len(lacp_groups_summary)}):")
                for lacp in lacp_groups_summary[:2]: 
                    print(f"      - Name: {lacp.get('name', 'N/A')}, Mode: {lacp.get('mode', 'N/A')}")
            port_groups_summary = dvs.get('port_groups', [])
            if port_groups_summary:
                print(f"    Port Groups ({len(port_groups_summary)}): {', '.join([pg.get('name', 'N/A') for pg in port_groups_summary[:5]])}{'...' if len(port_groups_summary) > 5 else ''}")

    except vim.fault.InvalidLogin as e:
        print(f"Error: Invalid login credentials. Details: {e.msg}")
    except ConnectionRefusedError: 
        print(f"Connection Error: Connection refused to {vcenter_host}")
    except vim.fault.HostCommunication as e: 
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
    print("Running vSphere Organizational & DVS Details Collector Test Script...")
    main_test_org_details()

