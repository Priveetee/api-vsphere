from datetime import datetime
import vsphere_collector # Import our collector module

def format_vcenter_details_md(details):
    md = ["# Document d'Architecture Technique - Infrastructure vSphere"]
    md.append(f"**Date de génération:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    md.append("## 1. Détails du vCenter Server\n")
    if details:
        for key, value in details.items():
            md.append(f"- **{key.replace('_', ' ').title()}:** {value}")
    else:
        md.append("Informations du vCenter non disponibles.")
    md.append("\n")
    return "\n".join(md)

def format_infrastructure_md(infra_data):
    md = ["## 2. Vue d'ensemble de l'Infrastructure\n"]
    if not infra_data or not infra_data.get("datacenters"):
        md.append("Aucune donnée d'infrastructure trouvée.")
        return "\n".join(md)

    for dc in infra_data["datacenters"]:
        md.append(f"### 2.1. Datacenter: {dc.get('name', 'N/A')}")
        md.append(f"- Statut Général: {dc.get('overallStatus', 'N/A')}\n")

        if dc.get("clusters"):
            md.append("#### 2.1.1. Clusters\n")
            for cluster in dc["clusters"]:
                md.append(f"##### Cluster: {cluster.get('name', 'N/A')}")
                md.append(f"- Statut Général: {cluster.get('overallStatus', 'N/A')}")
                md.append(f"- HA Activé: {cluster.get('ha_enabled', 'N/A')}")
                if cluster.get('ha_enabled') == True or str(cluster.get('ha_enabled')).lower() == 'true': # Check boolean and string 'True'
                    md.append(f"  - Contrôle d'admission HA: {cluster.get('ha_admission_control', 'N/A')}")
                    md.append(f"  - Priorité de redémarrage VM HA: {cluster.get('ha_vm_restart_priority', 'N/A')}")
                md.append(f"- DRS Activé: {cluster.get('drs_enabled', 'N/A')}")
                if cluster.get('drs_enabled') == True or str(cluster.get('drs_enabled')).lower() == 'true':
                    md.append(f"  - Comportement DRS: {cluster.get('drs_behavior', 'N/A')}")
                md.append("\n###### Hôtes ESXi\n")
                if cluster.get("hosts"):
                    md.append("| Nom de l'Hôte | Version | Build | Modèle | CPU | Mémoire (GB) | État | Connexion | Maint. |")
                    md.append("|---|---|---|---|---|---|---|---|---|")
                    for host in cluster["hosts"]:
                        cpu_info = f"{host.get('cpu_sockets', 'N/A')}S x {host.get('cpu_cores_per_socket', 'N/A')}C ({host.get('cpu_threads', 'N/A')}T) @ {host.get('cpu_mhz', 'N/A')}MHz"
                        md.append(f"| {host.get('name', 'N/A')} | {host.get('version_full', 'N/A')} | {host.get('version_build', 'N/A')} | {host.get('vendor', '')} {host.get('model', '')} | {cpu_info} | {host.get('memory_gb', 'N/A')} | {host.get('status', 'N/A')} | {host.get('connection_state', 'N/A')} | {host.get('maintenance_mode', 'N/A')} |")
                else:
                    md.append("Aucun hôte ESXi dans ce cluster.")
                md.append("\n")
        
        if dc.get("standalone_hosts"):
            md.append("#### 2.1.2. Hôtes Autonomes\n")
            md.append("| Nom de l'Hôte | Version | Build | Modèle | CPU | Mémoire (GB) | État | Connexion | Maint. |")
            md.append("|---|---|---|---|---|---|---|---|---|")
            for host in dc["standalone_hosts"]:
                cpu_info = f"{host.get('cpu_sockets', 'N/A')}S x {host.get('cpu_cores_per_socket', 'N/A')}C ({host.get('cpu_threads', 'N/A')}T) @ {host.get('cpu_mhz', 'N/A')}MHz"
                md.append(f"| {host.get('name', 'N/A')} | {host.get('version_full', 'N/A')} | {host.get('version_build', 'N/A')} | {host.get('vendor', '')} {host.get('model', '')} | {cpu_info} | {host.get('memory_gb', 'N/A')} | {host.get('status', 'N/A')} | {host.get('connection_state', 'N/A')} | {host.get('maintenance_mode', 'N/A')} |")
            md.append("\n")
    md.append("\n")
    return "\n".join(md)

def format_datastores_md(datastores_data):
    md = ["## 3. Stockage (Datastores)\n"]
    if not datastores_data:
        md.append("Aucun datastore trouvé.")
        return "\n".join(md)

    md.append("| Nom | UUID | Type | Capacité (GB) | Libre (GB) | Provisionné/Utilisé (GB) | Non Engagé (GB) | Accessible | SIOC |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for ds in datastores_data:
        provisioned_info = ds.get('provisioned_gb', ds.get('used_space_gb', 'N/A'))
        md.append(f"| {ds.get('name', 'N/A')} | {ds.get('uuid', 'N/A')} | {ds.get('type', 'N/A')} | {ds.get('capacity_gb', 'N/A')} | {ds.get('free_space_gb', 'N/A')} | {provisioned_info} | {ds.get('uncommitted_gb', 'N/A')} | {ds.get('accessible', 'N/A')} | {ds.get('storage_io_control', 'N/A')} |")
    md.append("\n")
    return "\n".join(md)

def format_networks_md(network_data):
    md = ["## 4. Réseau\n"]
    if not network_data:
        md.append("Aucune donnée réseau trouvée.")
        return "\n".join(md)

    if network_data.get("standard_port_groups"):
        md.append("### 4.1. Standard Port Groups\n")
        md.append("| Nom | Type |")
        md.append("|---|---|")
        for pg in network_data["standard_port_groups"]:
            md.append(f"| {pg.get('name', 'N/A')} | {pg.get('type', 'N/A')} |")
        md.append("\n")
    
    if network_data.get("distributed_port_groups"):
        md.append("### 4.2. Distributed Port Groups\n")
        md.append("| Nom (Clé) | DVSwitch | UUID DVS | VLAN ID | Ports Config. |")
        md.append("|---|---|---|---|---|")
        for dv_pg in network_data["distributed_port_groups"]:
            md.append(f"| {dv_pg.get('name', 'N/A')} ({dv_pg.get('key', 'N/A')}) | {dv_pg.get('dvswitch_name', 'N/A')} | {dv_pg.get('dvswitch_uuid', 'N/A')} | {dv_pg.get('vlan_id', 'N/A')} | {dv_pg.get('ports_configured', 'N/A')} |")
        md.append("\n")
    md.append("\n")
    return "\n".join(md)

def format_vms_md(vms_data):
    md = ["## 5. Machines Virtuelles\n"]
    if not vms_data:
        md.append("Aucune machine virtuelle trouvée.")
        return "\n".join(md)

    for vm in vms_data:
        md.append(f"### 5.x VM: {vm.get('name', 'N/A')}\n") # Le 'x' sera pour la numérotation
        md.append(f"- **UUID (Instance):** {vm.get('instance_uuid', 'N/A')}")
        md.append(f"- **UUID (BIOS):** {vm.get('bios_uuid', 'N/A')}")
        md.append(f"- **Chemin VMX:** `{vm.get('vmx_path', 'N/A')}`")
        md.append(f"- **OS Invité:** {vm.get('guest_os_full', 'N/A')} (ID: {vm.get('guest_os_id', 'N/A')})")
        md.append(f"- **Version VM:** {vm.get('vm_version', 'N/A')}")
        md.append(f"- **VMware Tools:** {vm.get('tools_status', 'N/A')} (Version: {vm.get('tools_version', 'N/A')}, Exécution: {vm.get('tools_running', 'N/A')})")
        md.append(f"- **État d'alimentation:** {vm.get('power_state', 'N/A')}")
        md.append(f"- **Heure de démarrage:** {vm.get('boot_time', 'N/A')}")
        md.append(f"- **Hôte Actuel:** {vm.get('host_name', 'N/A')}")
        md.append(f"- **vCPUs:** {vm.get('vcpus', 'N/A')} (Cœurs/Socket: {vm.get('cores_per_socket', 'N/A')})")
        md.append(f"- **RAM:** {vm.get('ram_mb', 'N/A')} MB")
        md.append(f"  - Réservation CPU: {vm.get('cpu_reservation_mhz', 'N/A')} MHz, Limite CPU: {vm.get('cpu_limit_mhz', 'N/A')} MHz, Partages CPU: {vm.get('cpu_shares', 'N/A')} ({vm.get('cpu_shares_level', 'N/A')})")
        md.append(f"  - Réservation Mém.: {vm.get('mem_reservation_mb', 'N/A')} MB, Limite Mém.: {vm.get('mem_limit_mb', 'N/A')} MB, Partages Mém.: {vm.get('mem_shares', 'N/A')} ({vm.get('mem_shares_level', 'N/A')})")
        md.append("\n")

        md.append("#### Disques Virtuels\n")
        if vm.get("disks"):
            md.append("| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |")
            md.append("|---|---|---|---|---|---|---|")
            for disk in vm["disks"]:
                md.append(f"| {disk.get('label', 'N/A')} ({disk.get('key', 'N/A')}) | {disk.get('capacity_gb', 'N/A')} | {disk.get('datastore_name', 'N/A')} | `{disk.get('vmdk_path', 'N/A')}` | {disk.get('disk_mode', 'N/A')} | {disk.get('thin_provisioned', 'N/A')} | {disk.get('sioc_limit_iops', 'N/A')} IOPS |")
        else:
            md.append("Aucun disque virtuel.")
        md.append("\n")

        md.append("#### Adaptateurs Réseau Virtuels\n")
        if vm.get("network_adapters"):
            md.append("| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |")
            md.append("|---|---|---|---|---|---|")
            for nic in vm["network_adapters"]:
                ips_str = ", ".join(nic.get('guest_ips', [])) if nic.get('guest_ips') else "N/A"
                md.append(f"| {nic.get('label', 'N/A')} ({nic.get('key', 'N/A')}) | {nic.get('adapter_type', 'N/A')} | `{nic.get('mac_address', 'N/A')}` | {nic.get('network_name', 'N/A')} | {nic.get('connected', 'N/A')} | {ips_str} |")
        else:
            md.append("Aucun adaptateur réseau.")
        md.append("\n---\n") # Separator for VMs
    return "\n".join(md)


def generate_markdown_dat(filename="DAT_vSphere.md"):
    print("Démarrage de la collecte de données vSphere...")
    # Appel de la fonction main de vsphere_collector pour obtenir les données
    # Le premier argument retourné 'content' n'est pas utilisé ici, mais 'collected_data' l'est.
    _, all_data = vsphere_collector.main()

    if not all_data:
        print("Échec de la collecte des données. Le document DAT ne sera pas généré.")
        return

    print("Données collectées. Génération du document Markdown...")
    
    markdown_output = []
    markdown_output.append(format_vcenter_details_md(all_data.get("vcenter_details")))
    markdown_output.append(format_infrastructure_md(all_data.get("infrastructure")))
    markdown_output.append(format_datastores_md(all_data.get("datastores")))
    markdown_output.append(format_networks_md(all_data.get("networks")))
    markdown_output.append(format_vms_md(all_data.get("vms"))) # Attention, peut être très long

    full_markdown = "\n".join(markdown_output)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_markdown)
        print(f"Document DAT généré avec succès : {filename}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier Markdown {filename}: {e}")

if __name__ == "__main__":
    generate_markdown_dat()

