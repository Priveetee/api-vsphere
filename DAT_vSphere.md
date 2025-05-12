# Document d'Architecture Technique - Infrastructure vSphere
**Date de génération:** 2025-05-09 10:23:26

## 1. Détails du vCenter Server

- **Fullname:** VMware vCenter Server 7.0.3 build-22837322
- **Version:** 7.0.3
- **Build:** 22837322
- **Apitype:** VirtualCenter
- **Apiversion:** 7.0.3.0
- **Ostype:** linux-x64
- **Instanceuuid:** 65be60bc-2751-44bf-ae6f-e6d6fe313374


## 2. Vue d'ensemble de l'Infrastructure

### 2.1. Datacenter: BCA-EXPERTISE
- Statut Général: gray

#### 2.1.1. Clusters

##### Cluster: BCA-PreProduction
- Statut Général: green
- HA Activé: True
  - Contrôle d'admission HA: True
  - Priorité de redémarrage VM HA: medium
- DRS Activé: True
  - Comportement DRS: fullyAutomated

###### Hôtes ESXi

| Nom de l'Hôte | Version | Build | Modèle | CPU | Mémoire (GB) | État | Connexion | Maint. |
|---|---|---|---|---|---|---|---|---|
| vm-esx-pp-03.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 20C (80T) @ 2394MHz | 767.66 | green | connected | False |
| vm-esx-pp-01.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 20C (80T) @ 2394MHz | 767.66 | green | connected | False |
| vm-esx-pp-04.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 20C (80T) @ 2394MHz | 767.66 | green | connected | False |
| vm-esx-pp-02.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 20C (80T) @ 2394MHz | 767.66 | green | connected | False |


##### Cluster: BCA-Production
- Statut Général: green
- HA Activé: True
  - Contrôle d'admission HA: True
  - Priorité de redémarrage VM HA: medium
- DRS Activé: True
  - Comportement DRS: fullyAutomated

###### Hôtes ESXi

| Nom de l'Hôte | Version | Build | Modèle | CPU | Mémoire (GB) | État | Connexion | Maint. |
|---|---|---|---|---|---|---|---|---|
| vm-esx-p-01.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |
| vm-esx-p-02.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |
| vm-esx-p-08.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2295MHz | 767.66 | green | connected | False |
| vm-esx-p-09.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2295MHz | 767.66 | green | connected | False |
| vm-esx-p-03.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |
| vm-esx-p-05.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |
| vm-esx-p-04.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |
| vm-esx-p-07.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2295MHz | 767.66 | green | connected | False |
| vm-esx-p-06.bcaexpertise.org | VMware ESXi 7.0.3 build-23794027 | 23794027 | HPE ProLiant DL360 Gen10 | 2S x 16C (64T) @ 2095MHz | 767.66 | green | connected | False |


##### Cluster: 0-BCA-Pri
- Statut Général: green
- HA Activé: False
- DRS Activé: False

###### Hôtes ESXi

Aucun hôte ESXi dans ce cluster.




## 3. Stockage (Datastores)

| Nom | UUID | Type | Capacité (GB) | Libre (GB) | Provisionné/Utilisé (GB) | Non Engagé (GB) | Accessible | SIOC |
|---|---|---|---|---|---|---|---|---|
| DS_P_REPLI_01 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2902.79 | 4107.02 | 866.06 | True | N/A |
| DS_PP_REPLI_07 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 3006.85 | 1695.48 | 606.58 | True | N/A |
| DS_PP_REPLI_02 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2789.62 | 1655.17 | 349.04 | True | N/A |
| Witness-PreProd-PAR1 | (vim.CustomFieldsManager.Value) [] | VMFS | 9.75 | 5.93 | 3.82 | 0.0 | True | N/A |
| DS_P_REPLI_11 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2868.95 | 1359.41 | 132.61 | True | N/A |
| DS_PP_REPLI_03 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2836.0 | 1667.66 | 407.91 | True | N/A |
| DS_P_REPLI_14 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2312.1 | 1904.64 | 120.99 | True | N/A |
| DS_PP_REPLI_11 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2921.6 | 4009.72 | 787.57 | True | N/A |
| DS_P_REPLI_13 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2592.21 | 1772.59 | 269.05 | True | N/A |
| DS_PP_REPLI_08 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 1201.5 | 3061.99 | 167.74 | True | N/A |
| DS_PXMX_BKP_REPLI_1 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 4.07 | 6139.68 | 0.0 | True | N/A |
| DS_PP_REPLI_10 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2955.59 | 1451.52 | 311.36 | True | N/A |
| DS_P_REPLI_10 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2945.39 | 3354.56 | 156.2 | True | N/A |
| DS_P_REPLI_02 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 3571.71 | 3023.6 | 451.56 | True | N/A |
| DS_P_REPLI_12 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2170.08 | 4360.22 | 386.55 | True | N/A |
| DS_P_REPLI_05 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2916.97 | 1336.24 | 157.46 | True | N/A |
| NFS_PP_01 | (vim.CustomFieldsManager.Value) [] | NFS | 3404.8 | 3025.49 | 735.44 | 356.13 | True | N/A |
| DS_P_03 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 3048.07 | 3715.22 | 619.54 | True | N/A |
| DS_P_REPLI_07 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2711.44 | 3584.98 | 152.67 | True | N/A |
| Witness-Prod-PAR1 | (vim.CustomFieldsManager.Value) [] | VMFS | 9.75 | 3.6 | 6.15 | N/A | True | N/A |
| Witness-Prod-PAR5 | (vim.CustomFieldsManager.Value) [] | VMFS | 9.75 | 2.67 | 7.08 | N/A | True | N/A |
| DS_P_REPLI_04 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2752.48 | 3951.13 | 559.86 | True | N/A |
| DS_P_02 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2756.36 | 4163.04 | 775.65 | True | N/A |
| DS_P_REPLI_08 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2753.33 | 3565.31 | 174.89 | True | N/A |
| DS_PP_REPLI_06 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 1734.45 | 2505.57 | 144.27 | True | N/A |
| DS_P_REPLI_15 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2209.97 | 2098.56 | 212.78 | True | N/A |
| DS_PP_REPLI_01 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 1912.36 | 7123.89 | 2892.5 | True | N/A |
| DS_P_05 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 4111.08 | 2032.67 | 0.0 | True | N/A |
| Witness-PreProd-PAR5 | (vim.CustomFieldsManager.Value) [] | VMFS | 9.75 | 4.93 | 4.82 | 0.0 | True | N/A |
| DS_P_REPLI_03 | (vim.CustomFieldsManager.Value) [] | VMFS | 6143.75 | 2885.98 | 3547.87 | 290.1 | True | N/A |
| DS_PP_REPLI_04 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2097.37 | 2099.53 | 101.15 | True | N/A |
| DS_P_REPLI_06 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 2738.36 | 1430.12 | 72.73 | True | N/A |
| DS_PP_REPLI_05 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 3168.53 | 971.5 | 44.28 | True | N/A |
| DS_PP_REPLI_09 | (vim.CustomFieldsManager.Value) [] | VMFS | 4095.75 | 1945.35 | 2749.35 | 598.95 | True | N/A |


## 4. Réseau

### 4.1. Standard Port Groups

| Nom | Type |
|---|---|
| VM Network | Standard Port Group |
| VM-VLAN-MGMT | Standard Port Group |
| VM_Local | Standard Port Group |


### 4.2. Distributed Port Groups

| Nom (Clé) | DVSwitch | UUID DVS | VLAN ID | Ports Config. |
|---|---|---|---|---|
| PROD_DPortGroup_22 (dvportgroup-180105) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 22 | 48 |
| PROD_DPortGroup_20 (dvportgroup-180103) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 20 | 48 |
| DMZ-PRIVEE-Prod-DPortGroup (dvportgroup-105) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 0 | 48 |
| DMZ-Prod-DPortGroup (dvportgroup-67) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 0 | 48 |
| PROD_DPortGroup_40 (dvportgroup-229599) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 40 | 48 |
| DPortGroup_22 (dvportgroup-179018) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 22 | 8 |
| DPortGroup_2001 (dvportgroup-178068) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 2001 | 48 |
| DPortGroup_21 (dvportgroup-178070) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 21 | 48 |
| PROD_DPortGroup_2000 (dvportgroup-180102) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 2000 | 48 |
| BCA-DSwitch-DVUplinks-65 (dvportgroup-66) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | Trunk (0-4094) | 54 |
| VM-Prod-DPortGroup (dvportgroup-68) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 0 | 256 |
| VM-PP-DPortGroup (dvportgroup-72) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 0 | 256 |
| DMZ-PP-DPortGroup (dvportgroup-71) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 0 | 48 |
| DPortGroup_2002 (dvportgroup-178069) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 2002 | 48 |
| DPortGroup_20 (dvportgroup-178012) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 20 | 48 |
| DMZ-PRIVEE-PP-DPortGroup (dvportgroup-106) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | 0 | 48 |
| PROD_DPortGroup_21 (dvportgroup-180104) | BCA-Prod-DSwitch | 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86 | 21 | 48 |
| BCA-PP-DSwitch-DVUplinks-69 (dvportgroup-70) | BCA-PP-DSwitch | 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49 | Trunk (0-4094) | 24 |




## 5. Machines Virtuelles

### 5.x VM: srv-talend-tac-01-pro

- **UUID (Instance):** 501ac84b-b938-c4bd-2031-17e2826b82e0
- **UUID (BIOS):** 421a1a8f-16ce-2bba-6ae9-5ec4daa1a4b7
- **Chemin VMX:** `[DS_P_02] srv-talend-tac-01-pro/srv-talend-tac-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 03:49:39 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_02 | `[DS_P_02] srv-talend-tac-01-pro/srv-talend-tac-01-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:dd:46` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.36 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:dd46 (Prefix: 64, State: unknown) |

---

### 5.x VM: TALEND-JOBSERVEUR-PRO-01

- **UUID (Instance):** 501a218c-f791-40a6-12b8-75da6c1ade03
- **UUID (BIOS):** 564da615-c6bd-2fbb-39c0-93a8d5736ad5
- **Chemin VMX:** `[DS_P_REPLI_10] TALEND-JOBSERVEUR-PRO-01/TALEND-JOBSERVEUR-PRO-01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-05 14:29:20 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 90.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] TALEND-JOBSERVEUR-PRO-01/TALEND-JOBSERVEUR-PRO-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:82:7C` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: k8s-rke2-prod-worker06

- **UUID (Instance):** 501a91ce-640d-3a4d-0da0-0b915b8644f7
- **UUID (BIOS):** 421a2eab-13ef-f926-b156-a851d258ba89
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker06/k8s-rke2-prod-worker06.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:42 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker06/k8s-rke2-prod-worker06.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:13:a4` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.138 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:13a4 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-iwemc-01

- **UUID (Instance):** 501a00a5-9dd8-c99a-e49e-1583b5a9daae
- **UUID (BIOS):** 421ac1bd-42be-f131-7a9e-605493ad4e6c
- **Chemin VMX:** `[DS_P_REPLI_01] srv-iwemc-01/srv-iwemc-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:37:29 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-iwemc-01/srv-iwemc-01.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:82:70` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::432:9fd2:6db1:175d (Prefix: 64, State: unknown), 172.16.220.54 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_prod_master02

- **UUID (Instance):** 501a228a-4dbe-1e0d-902b-90c801fdd2a0
- **UUID (BIOS):** 421a9643-7b4b-452c-973a-5ce23dab6eed
- **Chemin VMX:** `[DS_P_02] k8s_prod_master02/k8s_prod_master02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 03:49:43 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_master02/k8s_prod_master02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2d:b5` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.131 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2db5 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-worker04

- **UUID (Instance):** 501a4c93-8952-9adb-b5e4-5eae818ed4a4
- **UUID (BIOS):** 421a06ec-ca0e-0c2b-fdf5-48ac1548b3ff
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker04/k8s-rke2-prod-worker04.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:39 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker04/k8s-rke2-prod-worker04.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:be:27` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.136 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:be27 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I151(24.04)

- **UUID (Instance):** 501a04ea-417e-da79-a8f7-7e89c3a209f5
- **UUID (BIOS):** 421a41b3-9868-f98c-0731-e5fdb383c905
- **Chemin VMX:** `[DS_P_REPLI_05] S00I151(24.04)/S00I151(24.04).vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-26 10:55:16 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I151(24.04)/S00I151(24.04).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bd:7b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.51 (Prefix: 16, State: preferred), fe80::250:56ff:fe9a:bd7b (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-securite-pro

- **UUID (Instance):** 501afc7c-3b63-88e5-79e7-ebb8eac1549d
- **UUID (BIOS):** 421ad826-ab61-9d02-20b7-381be641bcc3
- **Chemin VMX:** `[DS_P_REPLI_04] srv-securite-pro/srv-securite-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-16 09:35:54 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-securite-pro/srv-securite-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:13:64` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.64 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1364 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-talend-tac-02-pro

- **UUID (Instance):** 501a30f0-2cad-85aa-4723-0d53af78ab43
- **UUID (BIOS):** 421adb84-cb25-ab84-654a-55de3d37ce7a
- **Chemin VMX:** `[DS_P_03] srv-talend-tac-02-pro/srv-talend-tac-02-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 08:11:12 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_03 | `[DS_P_03] srv-talend-tac-02-pro/srv-talend-tac-02-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:c0:e6` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.37 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:c0e6 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-proxmox-backup-server

- **UUID (Instance):** 501a008b-a3ef-a100-ff5c-97b85ed52dbd
- **UUID (BIOS):** 421aa19b-64eb-8c61-d7ce-58d2b1968221
- **Chemin VMX:** `[DS_PXMX_BKP_REPLI_1] srv-proxmox-backup-server/srv-proxmox-backup-server.vmx`
- **OS Invité:** Debian GNU/Linux 11 (64-bit) (ID: debian11_64Guest)
- **Version VM:** vmx-19
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-06 10:27:14 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PXMX_BKP_REPLI_1 | `[DS_PXMX_BKP_REPLI_1] srv-proxmox-backup-server/srv-proxmox-backup-server.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 6062.08 | DS_PXMX_BKP_REPLI_1 | `[DS_PXMX_BKP_REPLI_1] srv-proxmox-backup-server/srv-proxmox-backup-server_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b5:96` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: k8s_prod_master03

- **UUID (Instance):** 501a200c-568b-490e-15ed-997c9c5756a6
- **UUID (BIOS):** 421a57d5-8dea-7614-7d5e-ca9dc5ca3e72
- **Chemin VMX:** `[DS_P_05] k8s_prod_master03/k8s_prod_master03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:39 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] k8s_prod_master03/k8s_prod_master03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:61:9f` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.132 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:619f (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-worker07

- **UUID (Instance):** 501aad56-19f6-3042-3731-2f9fe11f8370
- **UUID (BIOS):** 421a0598-2ebd-7bac-3a99-ad68ea696e5a
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker07/k8s-rke2-prod-worker07.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:48:08 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker07/k8s-rke2-prod-worker07.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2d:0b` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.139 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2d0b (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocCore-pro-1

- **UUID (Instance):** 501ab50c-d1d5-7a94-811e-72a93e88bfe6
- **UUID (BIOS):** 421aee52-5adb-07d7-dfe8-8b76eb58f145
- **Chemin VMX:** `[DS_P_REPLI_05] BdocCore-pro-1/BdocCore-pro-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:52 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] BdocCore-pro-1/BdocCore-pro-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] BdocCore-pro-1/BdocCore-pro-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:B3:58` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: PSQL_PRO

- **UUID (Instance):** 5039a0c7-7d7f-731e-d190-b9aaa3739c9b
- **UUID (BIOS):** 4239d35b-6be6-1931-e433-538b0b012216
- **Chemin VMX:** `[DS_P_REPLI_01] PSQL_PRO/PSQL_PRO.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] PSQL_PRO/PSQL_PRO.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:0d:d9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: k8s_prod_worker02

- **UUID (Instance):** 501a8f6e-2e19-e434-d3a7-d9b3acc8a7d2
- **UUID (BIOS):** 421aa6dc-3ddc-2773-dac4-d072c2311e58
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker02/k8s_prod_worker02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 10:56:08 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker02/k8s_prod_worker02.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1024.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker02/k8s_prod_worker02_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bd:9c` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.134 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bd9c (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker09

- **UUID (Instance):** 501afbd6-b6f5-4cdc-3ca3-1d5af7dc21c0
- **UUID (BIOS):** 421afb62-6ab8-5404-d06f-5b58be7b19b8
- **Chemin VMX:** `[DS_P_03] k8s_prod_worker09/k8s_prod_worker09.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-09-04 13:16:58 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_prod_worker09/k8s_prod_worker09.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:df:1e` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.139 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:df1e (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I35

- **UUID (Instance):** 503918ca-b922-eca7-fa83-1f144f7e2b53
- **UUID (BIOS):** 423992c6-4d5e-770e-99b1-f25a454fb72a
- **Chemin VMX:** `[DS_P_REPLI_14] S00I35/S00I35.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:13:47 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I35/S00I35.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I35/S00I35_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:b9:22:e5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.184 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_prod_worker11

- **UUID (Instance):** 501a5e7f-2d05-c7a5-67ef-e944c73f78b2
- **UUID (BIOS):** 421a5f47-5b42-2d87-1ab5-8b52133a3877
- **Chemin VMX:** `[DS_P_03] k8s_prod_worker11/k8s_prod_worker11.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 08:11:16 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_prod_worker11/k8s_prod_worker11.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:08:b1` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.141 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8b1 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00A03

- **UUID (Instance):** 501acc97-b8f2-be0f-3df2-bf9c001132aa
- **UUID (BIOS):** 421a9496-7c04-02a6-02f4-3726ddebd092
- **Chemin VMX:** `[DS_P_REPLI_03] S00A03/S00A03.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:14:01 UTC
- **Hôte Actuel:** vm-esx-p-06.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00A03/S00A03_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 400.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00A03/S00A03_5.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 200.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00A03/S00A03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9A:A8:87` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: VA001

- **UUID (Instance):** 501a0691-e0c8-ce96-41ad-d9d3e3ae9904
- **UUID (BIOS):** 421a2f02-385f-35f1-5cd2-493cf369eb4e
- **Chemin VMX:** `[DS_P_REPLI_02] VA001/VA001.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-09
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 04:04:57 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 1024 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 10240 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 6.5 | DS_P_REPLI_02 | `[DS_P_REPLI_02] VA001/VA001.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 0.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] VA001/VA001_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ef:e0` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.250.53 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-robotmel-03

- **UUID (Instance):** 501a8e44-b314-8a7f-25db-a545a0e710ce
- **UUID (BIOS):** 564d8a3a-747b-d946-b1a8-ded207f3824c
- **Chemin VMX:** `[DS_P_REPLI_04] srv-robotmel-03/srv-robotmel-03.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-04 03:02:35 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 8)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-robotmel-03/srv-robotmel-03.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-robotmel-03/srv-robotmel-03_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:23:F9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: SRVBCA-DHCP1

- **UUID (Instance):** 5039e197-d836-3c4d-144d-b639546d57d3
- **UUID (BIOS):** 4239652f-6e0a-ac92-3bb9-6951a9b5f5db
- **Chemin VMX:** `[DS_P_REPLI_01] SRVBCA-DHCP1/SRVBCA-DHCP1.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:38:41 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] SRVBCA-DHCP1/SRVBCA-DHCP1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:18:ba` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::9478:13a5:3cb2:a9a1 (Prefix: 64, State: unknown), 172.16.210.72 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-harbor-pro-01

- **UUID (Instance):** 501a2412-4045-6897-2002-b150480c568a
- **UUID (BIOS):** 421a296b-4e12-aad0-a2fe-63fbf3cf82dd
- **Chemin VMX:** `[DS_P_REPLI_15] srv-harbor-pro-02/srv-harbor-pro-02.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-13 14:29:42 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] srv-harbor-pro-02/srv-harbor-pro-02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:5b:7f` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.125 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:5b7f (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-mongo-pro-2

- **UUID (Instance):** 501a0f98-1cf4-1ad1-27c8-84be4a114cef
- **UUID (BIOS):** 421abf4b-8a9e-fe18-54ae-ce5a832110a6
- **Chemin VMX:** `[DS_P_REPLI_07] srv-mongo-pro-2/srv-mongo-pro-2.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-29 10:48:24 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 250.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] srv-mongo-pro-2/srv-mongo-pro-2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:61:fa` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.105 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:61fa (Prefix: 64, State: unknown) |

---

### 5.x VM: SRV-IHM-PRO-01

- **UUID (Instance):** 501a48e9-a843-61e9-846c-98e03ae422c6
- **UUID (BIOS):** 421a93d1-eb98-ca58-1113-16bc36b8cea7
- **Chemin VMX:** `[DS_P_REPLI_10] SRV-IHM-PRO-01/SRV-IHM-PRO-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:42:36 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] SRV-IHM-PRO-01/SRV-IHM-PRO-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] SRV-IHM-PRO-01/SRV-IHM-PRO-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b5:f0` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::9961:6572:b1f8:1e3b (Prefix: 64, State: unknown), 172.16.210.230 (Prefix: 16, State: preferred) |

---

### 5.x VM: S00I234

- **UUID (Instance):** 501afd1c-7cd9-0647-3ab2-d15d36255a3c
- **UUID (BIOS):** 421aa210-520a-e1d4-52ea-d31786f04523
- **Chemin VMX:** `[DS_P_REPLI_13] S00I234/S00I234.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:42:58 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I234/S00I234.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I234/S00I234_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:9b:b8` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::8ed5:c115:e9e8:3cfd (Prefix: 64, State: unknown), 172.16.250.239 (Prefix: 24, State: preferred) |

---

### 5.x VM: Exchange-edge-01

- **UUID (Instance):** 501ad85d-337c-cbfb-7e4c-ef0f60138e89
- **UUID (BIOS):** 421a561d-9525-a0df-f2d9-a768b445f5d7
- **Chemin VMX:** `[DS_P_REPLI_14] Exchange-edge-01/Exchange-edge-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 17:42:56 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 150.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] Exchange-edge-01/Exchange-edge-01_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:fe:a9` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::748a:b392:5c36:9bf5 (Prefix: 64, State: unknown), 192.168.1.81 (Prefix: 24, State: preferred) |

---

### 5.x VM: SRVBCA-DHCP2

- **UUID (Instance):** 503918a5-4d2a-9b2f-4253-4ad3336fdb5c
- **UUID (BIOS):** 42391d65-7c09-5f4d-32e9-fb99558c0e70
- **Chemin VMX:** `[DS_P_REPLI_01] SRVBCA-DHCP2/SRVBCA-DHCP2.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:17:52 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] SRVBCA-DHCP2/SRVBCA-DHCP2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:13:35` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::209b:f601:aa29:3480 (Prefix: 64, State: unknown), 172.16.210.73 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-runner-pro-01

- **UUID (Instance):** 501a7691-e345-6027-60ce-90afa6406b67
- **UUID (BIOS):** 564ded2b-b5be-3b36-347b-5a56ed76d284
- **Chemin VMX:** `[DS_P_REPLI_13] srv-runner-pro-01/srv-runner-pro-01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-26 10:43:53 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] srv-runner-pro-01/srv-runner-pro-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] srv-runner-pro-01/srv-runner-pro-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:fc:8d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.167 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:fc8d (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I210 (JON VAL REC PRO)

- **UUID (Instance):** 503949bd-9cad-bc0f-5786-7d68c3cfc8b2
- **UUID (BIOS):** 4239f49a-d628-3cb7-2c21-10cefc5349dc
- **Chemin VMX:** `[DS_P_03] S00I210 (JON VAL REC PRO)/S00I210 (JON VAL REC PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 16:11:59 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_03 | `[DS_P_03] S00I210 (JON VAL REC PRO)/S00I210 (JON VAL REC PRO).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:3a:a2` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.2.100 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:3aa2 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-worker03

- **UUID (Instance):** 501a57e6-60c3-aeb0-0204-f5b3e2ea79cb
- **UUID (BIOS):** 421ad0ba-f9bf-d6f0-148e-4cd1cd08174c
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker03/k8s-rke2-prod-worker03.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker03/k8s-rke2-prod-worker03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:7f:62` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.135 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7f62 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-automator-core-prod

- **UUID (Instance):** 501a1531-b586-dd90-3e7b-3f4624ccaef0
- **UUID (BIOS):** 421a5700-5bb1-30f6-32c8-fa9654de7d8c
- **Chemin VMX:** `[DS_P_REPLI_10] srv-automator-core-prod/srv-automator-core-prod.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-11 10:01:51 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] srv-automator-core-prod/srv-automator-core-prod.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:79:a1` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.136 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:79a1 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I75

- **UUID (Instance):** 501ac744-8663-5c3a-8475-f990ad18acd6
- **UUID (BIOS):** 421a60cd-9283-8490-5f88-24a1dbad7e11
- **Chemin VMX:** `[DS_P_REPLI_03] S00I75/S00I75.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-16 01:17:20 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00I75/S00I75.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00I75/S00I75_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:95:37` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::97d9:9ff1:77ce:2189 (Prefix: 64, State: unknown), 172.16.210.75 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-robotmel-02

- **UUID (Instance):** 501a781a-93fb-b052-bccc-16e4173557a0
- **UUID (BIOS):** 421ab5f6-5002-1d59-49cd-e1e714ae94cd
- **Chemin VMX:** `[DS_P_REPLI_01] srv-robotmel-02/srv-robotmel-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-04 03:01:36 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 8)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-robotmel-02/srv-robotmel-02.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-robotmel-02/srv-robotmel-02_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a4:b2` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::a9c6:6f1a:783f:d098 (Prefix: 64, State: unknown), 172.16.220.42 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I402(JBOSS EAP 7 V4 PRO)

- **UUID (Instance):** 50399ef2-e69d-caff-5746-39defbe4262a
- **UUID (BIOS):** 564db6f3-69dd-694b-4f21-2c3120f81e86
- **Chemin VMX:** `[DS_P_03] S00I402(JBOSS EAP 7 V4 PRO)/S00I402(JBOSS EAP 7 V4 PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-25 19:08:28 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 15360 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 153600 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 62.0 | DS_P_03 | `[DS_P_03] S00I402(JBOSS EAP 7 V4 PRO)/S00I402(JBOSS EAP 7 V4 PRO).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_03 | `[DS_P_03] S00I402(JBOSS EAP 7 V4 PRO)/S00I402(JBOSS EAP 7 V4 PRO)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:5c:47` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.2.93 (Prefix: 24, State: preferred), 192.168.2.94 (Prefix: 32, State: preferred), 192.168.2.95 (Prefix: 32, State: preferred), fe80::250:56ff:feb9:5c47 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I25(EVA +E2000)

- **UUID (Instance):** 502dddf6-c27a-1e54-047e-0558f5ccc6df
- **UUID (BIOS):** 422dd247-51bd-f71d-a394-79b430c344cb
- **Chemin VMX:** `[DS_P_02] S00I25(EVA +E2000)/S00I25(EVA +E2000).vmx`
- **OS Invité:** Red Hat Enterprise Linux 5 (64-bit) (ID: rhel5_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10358, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_02 | `[DS_P_02] S00I25(EVA +E2000)/S00I25(EVA +E2000).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_02 | `[DS_P_02] S00I25(EVA +E2000)/S00I25(EVA +E2000)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:ad:00:1e` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.25 (Prefix: 16, State: preferred), fe80::250:56ff:fead:1e (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-worker05

- **UUID (Instance):** 501ae6be-c590-c469-f391-fc44a50b6344
- **UUID (BIOS):** 421a6cea-d174-7b27-0bae-a5a96d410bb6
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker05/k8s-rke2-prod-worker05.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:38:57 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker05/k8s-rke2-prod-worker05.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:06:e1` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.137 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6e1 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-monitoring-01

- **UUID (Instance):** 501a4f1e-a250-2023-9c5e-7f490c5b3365
- **UUID (BIOS):** 421a8cd2-2070-2399-f980-73176f03cc84
- **Chemin VMX:** `[DS_P_REPLI_08] srv-monitoring-01/srv-monitoring-01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-01 11:38:54 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 120.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] srv-monitoring-01/srv-monitoring-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:cf:c9` | DVPortGroup: dvportgroup-180105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.3.10 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:cfc9 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00L79(DU)_20250213

- **UUID (Instance):** 501aac30-51f3-9081-50ab-25db2a5f2490
- **UUID (BIOS):** 421a1104-5bba-9461-6029-7259c8a80461
- **Chemin VMX:** `[DS_P_REPLI_03] S00L79(DU)_20250213/S00L79(DU)_20250213.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-19
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-15 23:38:25 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00L79(DU)_20250213/S00L79(DU)_20250213.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00L79(DU)_20250213/S00L79(DU)_20250213_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 10.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00L79(DU)_20250213/S00L79(DU)_20250213_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:cb:f5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.78 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:cbf5 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker07

- **UUID (Instance):** 501a2546-a74d-4629-103c-d8add1622dcf
- **UUID (BIOS):** 421a4702-d854-133c-f05f-22879c38d2f6
- **Chemin VMX:** `[DS_P_05] k8s_prod_worker07/k8s_prod_worker07.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-13 12:05:14 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] k8s_prod_worker07/k8s_prod_worker07.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:0a:31` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.137 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a31 (Prefix: 64, State: unknown) |

---

### 5.x VM: TALEND-TAC-PRO-02

- **UUID (Instance):** 501ad4e7-fa9f-94fe-6201-9b4d90f20e92
- **UUID (BIOS):** 564de539-6887-7534-e763-832239dadce1
- **Chemin VMX:** `[DS_P_REPLI_11] TALEND-TAC-PRO-02/TALEND-TAC-PRO-02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] TALEND-TAC-PRO-02/TALEND-TAC-PRO-02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:2A:52` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: Exchange-adm-01

- **UUID (Instance):** 501a9adb-9588-89aa-e2fe-c2d9c86ef6a4
- **UUID (BIOS):** 421a2e5c-f175-2b71-07ed-6e5a64e70a2e
- **Chemin VMX:** `[DS_P_REPLI_13] Exchange-adm-01/Exchange-adm-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:27:06 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 150.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] Exchange-adm-01/Exchange-adm-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2002) | 500.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] Exchange-adm-01/Exchange-adm-01_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:3d:0d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::8c19:10fd:d9d6:638c (Prefix: 64, State: unknown), 172.16.220.48 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-stserver-01

- **UUID (Instance):** 501a1f6e-377f-4425-f8cf-eb493c077aff
- **UUID (BIOS):** 421a54c9-0a93-bc33-f5bf-e7bbc7048ca3
- **Chemin VMX:** `[DS_P_REPLI_10] srv-stcore-01/srv-stcore-01.vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-27 11:11:49 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] srv-stcore-01/srv-stcore-01-000001.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 25.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] srv-stcore-01/srv-stcore-01_1-000001.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:38:e2` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.27 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:38e2 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker05

- **UUID (Instance):** 501adbe2-c2e3-e122-9da0-32f6426077ed
- **UUID (BIOS):** 421a45ab-c3c1-ecaa-1f25-96abbd248150
- **Chemin VMX:** `[DS_P_05] k8s_prod_worker05/k8s_prod_worker05.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-09-30 09:39:08 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] k8s_prod_worker05/k8s_prod_worker05.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:45:aa` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.129 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:45aa (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker16

- **UUID (Instance):** 501a9fa5-db0d-d71d-9d6d-0bafe0661e6d
- **UUID (BIOS):** 421a8a2c-fe69-3235-6927-2b661c9a1dbc
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker16/k8s_prod_worker16.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12325, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 10:56:28 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker16/k8s_prod_worker16.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:fb:96` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.146 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:fb96 (Prefix: 64, State: unknown) |

---

### 5.x VM: PSQL_ODS_PRO

- **UUID (Instance):** 501ac7a8-53c1-bf76-5ad0-ccd180a51e62
- **UUID (BIOS):** 564d2206-7ea3-d1e5-906e-137e9c756ecb
- **Chemin VMX:** `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-06 11:14:20 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 8)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 225.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 5 (2004) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_4.vmdk` | persistent | False | -1 IOPS |
| Hard disk 6 (2005) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_5.vmdk` | persistent | False | -1 IOPS |
| Hard disk 7 (2006) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_6.vmdk` | persistent | False | -1 IOPS |
| Hard disk 8 (2008) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_7.vmdk` | persistent | False | -1 IOPS |
| Hard disk 9 (2009) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_8.vmdk` | persistent | False | -1 IOPS |
| Hard disk 10 (2010) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_9.vmdk` | persistent | False | -1 IOPS |
| Hard disk 11 (2011) | 80.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_10.vmdk` | persistent | False | -1 IOPS |
| Hard disk 12 (2012) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_11.vmdk` | persistent | False | -1 IOPS |
| Hard disk 13 (2013) | 110.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_12.vmdk` | persistent | False | -1 IOPS |
| Hard disk 14 (2014) | 30.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_13.vmdk` | persistent | False | -1 IOPS |
| Hard disk 15 (2015) | 20.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_14.vmdk` | persistent | False | -1 IOPS |
| Hard disk 16 (131088) | 200.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_15.vmdk` | persistent | False | -1 IOPS |
| Hard disk 17 (131089) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_16.vmdk` | persistent | False | -1 IOPS |
| Hard disk 18 (131090) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_17.vmdk` | persistent | False | -1 IOPS |
| Hard disk 19 (131091) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_18.vmdk` | persistent | False | -1 IOPS |
| Hard disk 20 (131092) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_19.vmdk` | persistent | False | -1 IOPS |
| Hard disk 21 (131093) | 50.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_20.vmdk` | persistent | False | -1 IOPS |
| Hard disk 22 (131094) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_ODS_PRO/PSQL_ODS_PRO_21.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:96:99` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00i105S

- **UUID (Instance):** 501a8934-0ca7-f21f-5e59-d56a0e2d8e39
- **UUID (BIOS):** 421a6c3a-5710-2476-ee72-03f3f07016ea
- **Chemin VMX:** `[DS_P_REPLI_01] S00i105S/S00i105S.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-20 08:34:05 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 2)
- **RAM:** 24576 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 245760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00i105S/S00i105S.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:8D:FE` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: vCLS-4d62c850-31a5-422a-8c99-6e62f7e0875b

- **UUID (Instance):** 501a02d7-46f9-167f-ac69-e98553d49037
- **UUID (BIOS):** 421a680c-2a52-b956-72e6-4d8474eaac9d
- **Chemin VMX:** `[DS_P_03] vCLS-4d62c850-31a5-422a-8c99-6e62f7e0875b/vCLS-4d62c850-31a5-422a-8c99-6e62f7e0875b.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-27 14:19:43 UTC
- **Hôte Actuel:** vm-esx-p-07.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | DS_P_03 | `[DS_P_03] vCLS-4d62c850-31a5-422a-8c99-6e62f7e0875b/vCLS-4d62c850-31a5-422a-8c99-6e62f7e0875b.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: vCLS-86a87324-5225-4252-8bef-14782a8d5be5

- **UUID (Instance):** 501a14b5-62c5-d4b8-8a47-9de88050da7d
- **UUID (BIOS):** 421a7467-ab74-bc63-59a2-d08dc5aba58e
- **Chemin VMX:** `[DS_P_03] vCLS-86a87324-5225-4252-8bef-14782a8d5be5/vCLS-86a87324-5225-4252-8bef-14782a8d5be5.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-27 14:19:13 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | DS_P_03 | `[DS_P_03] vCLS-86a87324-5225-4252-8bef-14782a8d5be5/vCLS-86a87324-5225-4252-8bef-14782a8d5be5.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: S00I20

- **UUID (Instance):** 501ab70a-6063-c3e0-ff5b-c31f53eecf6e
- **UUID (BIOS):** 421a80fa-2504-d80d-1142-58ac7ab91513
- **Chemin VMX:** `[DS_P_REPLI_12] S00I20/S00I20.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-29 18:06:53 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_2.vmdk` | persistent | True | -1 IOPS |
| Hard disk 4 (2003) | 60.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 5 (2004) | 60.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_4.vmdk` | persistent | True | -1 IOPS |
| Hard disk 6 (2005) | 60.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_5.vmdk` | persistent | True | -1 IOPS |
| Hard disk 7 (2006) | 50.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_6.vmdk` | persistent | True | -1 IOPS |
| Hard disk 8 (2008) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_7.vmdk` | persistent | False | -1 IOPS |
| Hard disk 9 (2009) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_8.vmdk` | persistent | True | -1 IOPS |
| Hard disk 10 (2010) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_9.vmdk` | persistent | True | -1 IOPS |
| Hard disk 11 (2011) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I20/S00I20_10.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:33:01:D0` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00I260(WS-TELEPHONIE)

- **UUID (Instance):** 5039b251-3e0f-8a51-ff76-4a9a89e9f9a6
- **UUID (BIOS):** 564da541-5a62-4700-cc8b-ee61bf0881b2
- **Chemin VMX:** `[DS_P_REPLI_07] S00I260(WS-TELEPHONIE)/S00I260(WS-TELEPHONIE).vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:17:52 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I260(WS-TELEPHONIE)/S00I260(WS-TELEPHONIE).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:b9:0c:01` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::619d:168a:ee1b:8fba (Prefix: 64, State: unknown), 172.16.220.60 (Prefix: 16, State: preferred) |

---

### 5.x VM: nbu-master-02

- **UUID (Instance):** 501a59d1-7517-d001-146c-dbf0409e388d
- **UUID (BIOS):** 421af484-86cf-5917-383b-e55324c449ff
- **Chemin VMX:** `[DS_P_REPLI_04] nbu-master-02/nbu-master-02.vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-20 12:02:59 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 24576 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 245760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 110.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] nbu-master-02/nbu-master-02.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] nbu-master-02/nbu-master-02_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:99:0b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.133 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:990b (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I239PRO

- **UUID (Instance):** 501a26fa-86c3-457a-aac8-a0c2f3e353b9
- **UUID (BIOS):** 421a9709-890e-0367-fc25-3acbe7267ad6
- **Chemin VMX:** `[DS_P_REPLI_11] S00I239PRO/S00I239PRO.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:39:30 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I239PRO/S00I239PRO.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I239PRO/S00I239PRO_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:34:69` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::5c60:2fc1:50e3:8eca (Prefix: 64, State: unknown), 172.16.210.207 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-webdav-01

- **UUID (Instance):** 501ace5f-f099-6383-f958-bac068d251ac
- **UUID (BIOS):** 421a8d5b-46be-306e-b426-aabd0436573a
- **Chemin VMX:** `[DS_P_REPLI_11] srv-webdav-01/srv-webdav-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:29:18 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] srv-webdav-01/srv-webdav-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:D9:32` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: k8s-rke2-prod-worker02

- **UUID (Instance):** 501afad9-8233-7c75-4839-dddd4675610b
- **UUID (BIOS):** 421a9b34-fa22-ab26-6985-707877dbe5fa
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker02/k8s-rke2-prod-worker02.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:41 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker02/k8s-rke2-prod-worker02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:24:a6` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.134 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:24a6 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-stedge-01

- **UUID (Instance):** 501a67b3-f31e-9d66-7aae-1cc1122276c5
- **UUID (BIOS):** 421a3192-8f5e-9b59-858d-096dd9ae92fd
- **Chemin VMX:** `[DS_P_REPLI_07] srv-stedge-01/srv-stedge-01.vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-27 11:11:20 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] srv-stedge-01/srv-stedge-01-000001.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b0:67` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.27 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:b067 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker12

- **UUID (Instance):** 501a6d16-b16f-4e12-ef4e-ff58b4b47f58
- **UUID (BIOS):** 421a67b1-cbd0-2740-345b-98bea2727e7a
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker12/k8s_prod_worker12.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-07-12 14:32:12 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker12/k8s_prod_worker12.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:74:8e` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.142 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:748e (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker08

- **UUID (Instance):** 501a587e-c268-1cbd-63fc-a756aacf3891
- **UUID (BIOS):** 421a85a6-b92c-834d-81cb-fad6b8a80b4d
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker08/k8s_prod_worker08.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-06-12 12:07:12 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker08/k8s_prod_worker08.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:cd:19` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.138 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:cd19 (Prefix: 64, State: unknown) |

---

### 5.x VM: Exchange-adm-02

- **UUID (Instance):** 501aad50-ea23-406a-b802-14c37e43750b
- **UUID (BIOS):** 421a7c6d-8bfb-f8b2-ac01-8e6cb1f12e87
- **Chemin VMX:** `[DS_P_REPLI_15] Exchange-adm-02/Exchange-adm-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:11:46 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 150.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] Exchange-adm-02/Exchange-adm-02_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2002) | 500.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] Exchange-adm-02/Exchange-adm-02_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:21:6a` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::4096:5ba1:a74c:a586 (Prefix: 64, State: unknown), 172.16.220.49 (Prefix: 16, State: preferred), 172.16.220.51 (Prefix: 16, State: preferred) |

---

### 5.x VM: S00I202 (JBOSS EAP 5.2 V3 PRO)

- **UUID (Instance):** 501a033e-d44e-bf5a-fab7-b566ac1a86d5
- **UUID (BIOS):** 421a5157-b66a-f243-54a4-bf1d349ab100
- **Chemin VMX:** `[DS_P_03] S00I202 (JBOSS EAP 5.2 V3 PRO)/S00I202 (JBOSS EAP 5.2 V3 PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-29 15:39:34 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_03 | `[DS_P_03] S00I202 (JBOSS EAP 5.2 V3 PRO)/S00I202 (JBOSS EAP 5.2 V3 PRO).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_03 | `[DS_P_03] S00I202 (JBOSS EAP 5.2 V3 PRO)/S00I202 (JBOSS EAP 5.2 V3 PRO)_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 10.0 | DS_P_03 | `[DS_P_03] S00I202 (JBOSS EAP 5.2 V3 PRO)/S00I202 (JBOSS EAP 5.2 V3 PRO)_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:0c:4a` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.2.63 (Prefix: 24, State: preferred), 192.168.2.64 (Prefix: 32, State: preferred), 192.168.2.65 (Prefix: 32, State: preferred), fe80::250:56ff:fe9a:c4a (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I06A

- **UUID (Instance):** 5039a234-74eb-c737-1f24-a821ff30de31
- **UUID (BIOS):** 42398981-1c86-cadf-8b7f-35e5e30edb13
- **Chemin VMX:** `[DS_P_REPLI_08] S00I06A/S00I06A.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11269, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-17 12:40:13 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I06A/S00I06A.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I06A/S00I06A_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 10.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I06A/S00I06A_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:15:f7` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.12 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:15f7 (Prefix: 64, State: unknown) |

---

### 5.x VM: nbu-master-01

- **UUID (Instance):** 501afc1c-6ade-c108-8945-5b2056225ee5
- **UUID (BIOS):** 421a9c2b-0178-3091-5d13-483859c40a17
- **Chemin VMX:** `[DS_P_REPLI_02] nbu-master-01/nbu-master-01.vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-20 11:22:39 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 24576 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 245760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 110.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] nbu-master-01/nbu-master-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] nbu-master-01/nbu-master-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:46:93` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.132 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:4693 (Prefix: 64, State: unknown) |

---

### 5.x VM: cegid-trt-pro

- **UUID (Instance):** 501ae4d7-eb02-4ac5-3238-0713aa4873e4
- **UUID (BIOS):** 421a7e63-4ed4-2056-5df7-40ae5e07c4f8
- **Chemin VMX:** `[DS_P_REPLI_01] cegid-trt-pro/cegid-trt-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:36:06 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] cegid-trt-pro/cegid-trt-pro_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] cegid-trt-pro/cegid-trt-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:33:27` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::bb43:ef9e:7289:d9a2 (Prefix: 64, State: unknown), 172.16.220.25 (Prefix: 24, State: preferred) |

---

### 5.x VM: IES_POC_BI

- **UUID (Instance):** 501a2840-dcb4-144d-9cbd-9b3d45f5d266
- **UUID (BIOS):** 421a7403-d104-d55e-d031-fde46477acf3
- **Chemin VMX:** `[DS_P_REPLI_08] IES_POC_BI/IES_POC_BI.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-04 11:01:11 UTC
- **Hôte Actuel:** vm-esx-p-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 2)
- **RAM:** 98304 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 4096 MB, Limite Mém.: -1 MB, Partages Mém.: 983040 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 170.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] IES_POC_BI/IES_POC_BI.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 700.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] IES_POC_BI/IES_POC_BI_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:b8:1b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::68cd:959f:b3c3:b716 (Prefix: 64, State: unknown), 172.16.220.179 (Prefix: 24, State: preferred) |

---

### 5.x VM: VM-VCSA-01

- **UUID (Instance):** 527573df-8414-a4a5-966b-19e53bdccc8f
- **UUID (BIOS):** 564d4817-6764-aab0-cb71-defc0113dcc9
- **Chemin VMX:** `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-10
- **VMware Tools:** toolsOk (Version: 12325, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-27 13:27:12 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 19456 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 194560 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 48.56 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 5.74 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 25.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 50.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 5 (2004) | 10.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_4.vmdk` | persistent | False | -1 IOPS |
| Hard disk 6 (2005) | 10.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_5.vmdk` | persistent | False | -1 IOPS |
| Hard disk 7 (2006) | 15.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_6.vmdk` | persistent | False | -1 IOPS |
| Hard disk 8 (2008) | 25.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_7.vmdk` | persistent | False | -1 IOPS |
| Hard disk 9 (2009) | 1.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_8.vmdk` | persistent | False | -1 IOPS |
| Hard disk 10 (2010) | 10.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_9.vmdk` | persistent | False | -1 IOPS |
| Hard disk 11 (2011) | 10.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_10.vmdk` | persistent | False | -1 IOPS |
| Hard disk 12 (2012) | 100.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_11.vmdk` | persistent | False | -1 IOPS |
| Hard disk 13 (2013) | 50.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_12.vmdk` | persistent | False | -1 IOPS |
| Hard disk 14 (2014) | 25.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_13.vmdk` | persistent | False | -1 IOPS |
| Hard disk 15 (2015) | 15.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_14.vmdk` | persistent | False | -1 IOPS |
| Hard disk 16 (2016) | 100.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_15.vmdk` | persistent | False | -1 IOPS |
| Hard disk 17 (2017) | 200.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] VM-VCSA-01/VM-VCSA-01_16.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:0c:29:13:dc:c9` | VM-VLAN-MGMT | True | 172.16.230.20 (Prefix: 24, State: preferred) |

---

### 5.x VM: BdocCore-pro-2

- **UUID (Instance):** 501ae7d7-bd5e-016f-02e5-536b53c3d3de
- **UUID (BIOS):** 421acdcd-3674-4783-b0e7-fa3943db8e65
- **Chemin VMX:** `[DS_P_REPLI_06] BdocCore-pro-2/BdocCore-pro-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:37:42 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] BdocCore-pro-2/BdocCore-pro-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] BdocCore-pro-2/BdocCore-pro-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f4:43` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::d20c:f93e:20bc:cdfe (Prefix: 64, State: unknown), 172.16.220.75 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-adfs-02

- **UUID (Instance):** 501a82c3-3b4e-743b-84c9-aa80bcba05a1
- **UUID (BIOS):** 421afd6a-c0e0-ae01-2c28-da044c78a6e8
- **Chemin VMX:** `[DS_P_REPLI_01] srv-adfs-02/srv-adfs-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:36:02 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-adfs-02/srv-adfs-02.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:d3:4c` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::e481:a558:bcae:dac4 (Prefix: 64, State: unknown), 172.16.250.16 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-concentrateur-pro

- **UUID (Instance):** 501a0d15-669f-c1d3-54b5-65d7607dd8d1
- **UUID (BIOS):** 421aae20-01d5-f333-e2f1-a5ec9a0ec0cf
- **Chemin VMX:** `[DS_P_REPLI_05] srv-concentrateur-pro-new/srv-concentrateur-pro-new.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-04 10:36:51 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] srv-concentrateur-pro-new/srv-concentrateur-pro-new.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:89:E6` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-infra-01

- **UUID (Instance):** 501ad22a-802b-57a2-8c34-cb20c7e16771
- **UUID (BIOS):** 421a5194-4f7e-9c9f-ff85-8bf47e0d534e
- **Chemin VMX:** `[DS_P_REPLI_01] srv-infra-01/srv-infra-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:40:23 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-infra-01/srv-infra-01.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:79:f5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::3bba:81de:79f:7181 (Prefix: 64, State: unknown), 172.16.210.79 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s-rke2-prod-master02

- **UUID (Instance):** 501a4c35-4173-552f-f549-53a080187493
- **UUID (BIOS):** 421add70-b5ec-3136-ab59-ec121ee6ad19
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-master02/k8s-rke2-prod-master02.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:29:04 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-master02/k8s-rke2-prod-master02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1b:ad` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.131 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1bad (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I134(SMTB)

- **UUID (Instance):** 50396f57-88ee-0366-1b31-5eb111609003
- **UUID (BIOS):** 564d5076-da95-a6bd-ad9d-86950e93ac11
- **Chemin VMX:** `[DS_P_REPLI_01] S00I134(SMTB)/S00I134(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I134(SMTB)/S00I134(SMTB).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:3d:25` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.134 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_support_worker02

- **UUID (Instance):** 501a1048-8acc-42c6-2a4e-f4efd7152f41
- **UUID (BIOS):** 564dd0ce-77fb-6ffb-58f1-a4db16383715
- **Chemin VMX:** `[DS_P_02] k8s_support_worker02/k8s_support_worker02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-07 08:37:18 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_support_worker02/k8s_support_worker02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:24:3d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.112 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:243d (Prefix: 64, State: unknown) |

---

### 5.x VM: VA002

- **UUID (Instance):** 501a0870-3eda-f37c-311d-b12d1ab945ea
- **UUID (BIOS):** 421a00e1-5cbd-774b-c9fc-039eda58c7ab
- **Chemin VMX:** `[DS_P_REPLI_11] VA002/VA002.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-09
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 1024 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 10240 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 6.5 | DS_P_REPLI_11 | `[DS_P_REPLI_11] VA002/VA002.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 0.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] VA002/VA002_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a7:12` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.53 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I131(SMTB)

- **UUID (Instance):** 5039e3eb-4869-8294-1505-52e1bfe6a194
- **UUID (BIOS):** 423974de-a45e-6a33-f346-d90fd2f2e0d9
- **Chemin VMX:** `[DS_P_REPLI_04] S00I131(SMTB)/S00I131(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 65.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] S00I131(SMTB)/S00I131(SMTB).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:06:2b` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.131 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_support_master02

- **UUID (Instance):** 501a7540-06c5-f870-58e7-737a99ae3228
- **UUID (BIOS):** 421a99f0-7e74-ce45-afd7-cabb6169c653
- **Chemin VMX:** `[DS_P_02] k8s_support_master02/k8s_support_master02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-22 11:00:45 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_support_master02/k8s_support_master02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a6:90` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.109 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a690 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I02

- **UUID (Instance):** 503990d4-7dcb-931c-6c61-ed3a1179afd3
- **UUID (BIOS):** 42390062-4492-e15f-d40e-db57a2b3d144
- **Chemin VMX:** `[DS_P_REPLI_01] S00I02/S00I02.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:16:57 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I02/S00I02.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:11:31` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::35c9:8e35:33f6:8651 (Prefix: 64, State: unknown), 172.16.220.11 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_support_worker01

- **UUID (Instance):** 501ac773-29ed-a69a-14fd-5d1222c0f86c
- **UUID (BIOS):** 564d51af-82e2-e17f-2392-52a8464ed7a3
- **Chemin VMX:** `[DS_P_03] k8s_support_worker01/k8s_support_worker01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-22 11:02:12 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_support_worker01/k8s_support_worker01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:95:4b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.111 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:954b (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_support_master03

- **UUID (Instance):** 501aebf4-30b5-6be9-22aa-dce57c6220a9
- **UUID (BIOS):** 421a73f7-9b17-e2ea-e3de-5b8635ed6bce
- **Chemin VMX:** `[DS_P_03] k8s_support_master03/k8s_support_master03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-22 11:02:11 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_support_master03/k8s_support_master03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e2:df` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.110 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e2df (Prefix: 64, State: unknown) |

---

### 5.x VM: P00P26

- **UUID (Instance):** 501a4582-1cdd-7a48-cda8-b3bac300b1d6
- **UUID (BIOS):** 421a5cc9-9698-46d2-7e69-45b1061d7953
- **Chemin VMX:** `[DS_P_REPLI_06] P00P26/P00P26.vmx`
- **OS Invité:** Microsoft Windows 10 (64-bit) (ID: windows9_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-27 09:20:45 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 110.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] P00P26/P00P26.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ce:50` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::f539:d9d8:f518:cd29 (Prefix: 64, State: unknown), 172.16.250.155 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_support_master01

- **UUID (Instance):** 501a49b3-22f6-df88-3c6b-7f658069a7ef
- **UUID (BIOS):** 564d6865-bb0f-465d-9cf3-fbcb60d1f096
- **Chemin VMX:** `[DS_P_03] k8s_support_master01/k8s_support_master01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-22 11:00:39 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_support_master01/k8s_support_master01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:67:b5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.108 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:67b5 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I235

- **UUID (Instance):** 501ac421-6b35-192e-bd5d-51a1a3c32fe2
- **UUID (BIOS):** 421ac11b-44b5-a37c-7ef3-79065d31dd86
- **Chemin VMX:** `[DS_P_REPLI_13] S00I235/S00I235.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:39:39 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I235/S00I235.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I235/S00I235_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f0:f3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::8ed:8ca2:6101:4e5d (Prefix: 64, State: unknown), 172.16.250.240 (Prefix: 24, State: preferred) |

---

### 5.x VM: PSQL_BIGMAX_PRO_SEC

- **UUID (Instance):** 501a4b12-149c-d70d-4f55-777bc83d3d8f
- **UUID (BIOS):** 421a6230-a561-5563-4ba9-84e1702aaadf
- **Chemin VMX:** `[DS_P_REPLI_06] PSQL_BIGMAX_PRO_SEC/PSQL_BIGMAX_PRO_SEC.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] PSQL_BIGMAX_PRO_SEC/PSQL_BIGMAX_PRO_SEC.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] PSQL_BIGMAX_PRO_SEC/PSQL_BIGMAX_PRO_SEC_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] PSQL_BIGMAX_PRO_SEC/PSQL_BIGMAX_PRO_SEC_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 60.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] PSQL_BIGMAX_PRO_SEC/PSQL_BIGMAX_PRO_SEC_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:0B:41` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: Srv-Pki-inter-01

- **UUID (Instance):** 501a428f-6a22-5060-b2ce-a2c82ecf315a
- **UUID (BIOS):** 421a8642-8796-f963-da60-628460b1e55a
- **Chemin VMX:** `[DS_P_REPLI_02] Srv-Pki-inter-01/Srv-Pki-inter-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:34:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] Srv-Pki-inter-01/Srv-Pki-inter-01.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] Srv-Pki-inter-01/Srv-Pki-inter-01_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 2.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] Srv-Pki-inter-01/Srv-Pki-inter-01_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:8a:61` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::e499:1ec7:10be:788c (Prefix: 64, State: unknown), 172.16.220.44 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I86 (Concentrateur.bca.fr )

- **UUID (Instance):** 501a04b7-6a26-8050-4738-045886ecf5c4
- **UUID (BIOS):** 421a057c-79a6-1238-7fa4-6aabf4943f10
- **Chemin VMX:** `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )/S00I86 (Concentrateur.bca.fr ).vmx`
- **OS Invité:** Red Hat Enterprise Linux 4 (32-bit) (ID: rhel4Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2776 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 27760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )/S00I86 (Concentrateur.bca.fr ).vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )/S00I86 (Concentrateur.bca.fr )_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9a:e6:0b` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.100 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e60b (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker06

- **UUID (Instance):** 501aca56-319b-9b1f-3f49-b68659ae35cc
- **UUID (BIOS):** 421a202a-f7d6-6c46-3e0d-8f68fe6dd797
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker06/k8s_prod_worker06.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-18 09:31:52 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 12 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 12000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker06/k8s_prod_worker06.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:67:d9` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.136 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:67d9 (Prefix: 64, State: unknown) |

---

### 5.x VM: BCA-FILER-TOOLS

- **UUID (Instance):** 501a03c2-915c-58ce-6bb8-15abbbf1e9c7
- **UUID (BIOS):** 421acf7a-2dad-c436-7a6c-60e8c1a09e29
- **Chemin VMX:** `[DS_P_REPLI_05] BCA-FILER-TOOLS/BCA-FILER-TOOLS.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-07 07:49:28 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 150.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] BCA-FILER-TOOLS/BCA-FILER-TOOLS.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:67:27` | VM-VLAN-MGMT | True | 172.16.210.190 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-mssql19-pro

- **UUID (Instance):** 501aa41e-ee75-45a8-5b45-00eed8efa9da
- **UUID (BIOS):** 421a44e3-8080-3cb1-74dc-53ba90f24380
- **Chemin VMX:** `[DS_P_REPLI_06] srv-mssql19-pro/srv-mssql19-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:59 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 150.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] srv-mssql19-pro/srv-mssql19-pro.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] srv-mssql19-pro/srv-mssql19-pro_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 40.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] srv-mssql19-pro/srv-mssql19-pro_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:80:51` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::279a:96f6:7a3:65dd (Prefix: 64, State: unknown), 172.16.210.158 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I78

- **UUID (Instance):** 501aa855-e985-4dd7-f207-339d57e24fd8
- **UUID (BIOS):** 421a19c1-2bf7-bfbc-f05b-d866397d27d9
- **Chemin VMX:** `[DS_P_REPLI_08] S00I78/S00I78.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:51 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I78/S00I78.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I78/S00I78_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a3:b6` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::c0c8:4bf8:7dd1:9a62 (Prefix: 64, State: unknown), 172.16.210.78 (Prefix: 16, State: preferred) |

---

### 5.x VM: dwh-pbi-pro

- **UUID (Instance):** 501abf46-4b89-5840-e8ab-a5ba31100c6a
- **UUID (BIOS):** 421a0154-25db-f0a5-1578-2332e7fa84c8
- **Chemin VMX:** `[DS_P_REPLI_01] dwh-pbi-pro/dwh-pbi-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:32:57 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] dwh-pbi-pro/dwh-pbi-pro.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] dwh-pbi-pro/dwh-pbi-pro_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:5a:bd` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::42f:b035:5bc8:fa69 (Prefix: 64, State: unknown), 172.16.250.182 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s_prod_worker13

- **UUID (Instance):** 501a83a3-d8c8-1a7b-076d-598fa89a6672
- **UUID (BIOS):** 421a0115-89a3-6cae-69e0-4ccea88f1679
- **Chemin VMX:** `[DS_P_05] k8s_prod_worker13/k8s_prod_worker13.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-29 12:31:36 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] k8s_prod_worker13/k8s_prod_worker13.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f9:4b` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.143 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f94b (Prefix: 64, State: unknown) |

---

### 5.x VM: Srvbca-schedul1

- **UUID (Instance):** 501a4389-2d33-a076-a835-b457e4322a02
- **UUID (BIOS):** 421a0921-79f6-d02b-ad4e-e631ea7db92b
- **Chemin VMX:** `[DS_P_REPLI_01] Srvbca-schedul1/Srvbca-schedul1.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:13:24 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 10240 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 102400 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] Srvbca-schedul1/Srvbca-schedul1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 200.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] Srvbca-schedul1/Srvbca-schedul1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:56:f3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::d40:3ae0:b367:251c (Prefix: 64, State: unknown), 172.16.210.41 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-nexus-pro

- **UUID (Instance):** 501a9e8e-395a-9e94-371f-136e28361397
- **UUID (BIOS):** 421a22a6-d0ed-20f1-1f64-90bdae5cbaf4
- **Chemin VMX:** `[DS_P_REPLI_07] srv-nexus-pro/srv-nexus-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 500.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] srv-nexus-pro/srv-nexus-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a3:07` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.250.140 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a307 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-ndf-01

- **UUID (Instance):** 501a71f4-1dc1-861f-f401-fff5b5fa75d3
- **UUID (BIOS):** 421aa564-7433-e244-b438-a4fbd557936d
- **Chemin VMX:** `[DS_P_REPLI_01] srv-ndf-01/srv-ndf-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-ndf-01/srv-ndf-01.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-ndf-01/srv-ndf-01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:68:f6` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: S00I203 (JBOSS EAP 5.2 V3 PRO)

- **UUID (Instance):** 501a3f89-8004-9db7-d6c6-9a19e9dd5512
- **UUID (BIOS):** 421adf9e-e9c7-4101-33e2-fee8fa49d690
- **Chemin VMX:** `[DS_P_02] S00I203 (JBOSS EAP 5.2 V3 PRO)/S00I203 (JBOSS EAP 5.2 V3 PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 05:37:02 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_02 | `[DS_P_02] S00I203 (JBOSS EAP 5.2 V3 PRO)/S00I203 (JBOSS EAP 5.2 V3 PRO).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_02 | `[DS_P_02] S00I203 (JBOSS EAP 5.2 V3 PRO)/S00I203 (JBOSS EAP 5.2 V3 PRO)_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 10.0 | DS_P_02 | `[DS_P_02] S00I203 (JBOSS EAP 5.2 V3 PRO)/S00I203 (JBOSS EAP 5.2 V3 PRO)_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:A6:7B` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: NETAPP-OCUM-01

- **UUID (Instance):** 501a8480-5ab9-ca44-04ba-3075fc00341f
- **UUID (BIOS):** 421a2a56-b93a-5510-24e2-6b44084d1305
- **Chemin VMX:** `[DS_P_REPLI_05] NETAPP-OCUM-01/NETAPP-OCUM-01.vmx`
- **OS Invité:** Other (32-bit) (ID: otherGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] NETAPP-OCUM-01/NETAPP-OCUM-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 12.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] NETAPP-OCUM-01/NETAPP-OCUM-01_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 50.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] NETAPP-OCUM-01/NETAPP-OCUM-01_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 30.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] NETAPP-OCUM-01/NETAPP-OCUM-01_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:82:d9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: cegid-bdd-pro

- **UUID (Instance):** 501a23f0-aac7-bde2-c3d7-fc03ac83a1fa
- **UUID (BIOS):** 421aa10d-b2cd-75bc-1cf9-812ec3e5d593
- **Chemin VMX:** `[DS_P_REPLI_12] cegid-bdd-pro/cegid-bdd-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:20 UTC
- **Hôte Actuel:** vm-esx-p-05.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 4)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] cegid-bdd-pro/cegid-bdd-pro_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 210.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] cegid-bdd-pro/cegid-bdd-pro.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2003) | 80.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] cegid-bdd-pro/cegid-bdd-pro_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:89:e0` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::eb82:84d3:b262:bc6f (Prefix: 64, State: unknown), 172.16.220.23 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I19(SYBASE-LICENCE)

- **UUID (Instance):** 5039b33a-bbd5-b2aa-60a8-76f3321066de
- **UUID (BIOS):** 42393823-3a2c-b1b0-6ef6-8d6974f48fb3
- **Chemin VMX:** `[DS_P_REPLI_03] S00I19(SYBASE-LICENCE)/S00I19(SYBASE-LICENCE).vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-07 13:33:40 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00I19(SYBASE-LICENCE)/S00I19(SYBASE-LICENCE).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b7:0c:48` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::f109:2f8c:3d2a:676a (Prefix: 64, State: unknown), 172.16.210.19 (Prefix: 16, State: preferred) |

---

### 5.x VM: S00I40(UNIVIEWER)

- **UUID (Instance):** 501a87e6-f79e-921e-da42-7c7e3eb97c44
- **UUID (BIOS):** 421a1ec2-e04d-1586-a53c-0c07bcaee85d
- **Chemin VMX:** `[DS_P_REPLI_14] S00I40/S00I40.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-29 21:30:56 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I40/S00I40_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:5a:b8` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::971f:b311:607e:7838 (Prefix: 64, State: unknown), 172.16.210.40 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdocmongo-pro2

- **UUID (Instance):** 501ad8a3-8feb-761a-ad30-6d51acecd0e7
- **UUID (BIOS):** 421a3fd2-23c1-6ced-0d5a-1253ff3d02a3
- **Chemin VMX:** `[DS_P_05] srv-bdocmongo-pro2/srv-bdocmongo-pro2.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:39 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] srv-bdocmongo-pro2/srv-bdocmongo-pro2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:47:ec` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.102 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:47ec (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocInter-pro-2

- **UUID (Instance):** 501a6292-96f4-a03c-2a28-709473a5e1e8
- **UUID (BIOS):** 421a2fcb-b3a9-0263-4381-fca2c6ad614d
- **Chemin VMX:** `[DS_P_REPLI_02] BdocInter-pro-2/BdocInter-pro-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:17 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] BdocInter-pro-2/BdocInter-pro-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] BdocInter-pro-2/BdocInter-pro-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ec:de` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.71 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bigmaxmongo-pro1

- **UUID (Instance):** 501a4037-1ca4-72da-9074-e5e0a7b961f5
- **UUID (BIOS):** 421a81e1-9816-bcf5-346e-95762b655e34
- **Chemin VMX:** `[DS_P_REPLI_04] srv-bigmaxmongo-pro1/srv-bigmaxmongo-pro1.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 08:11:12 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-bigmaxmongo-pro1/srv-bigmaxmongo-pro1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a2:cc` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.106 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a2cc (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocWeb-pro-1

- **UUID (Instance):** 501afb45-b67c-dd8d-1e25-a433373ebe7d
- **UUID (BIOS):** 421a4eca-fa43-e615-6036-c7f330976328
- **Chemin VMX:** `[DS_P_REPLI_02] BdocWeb-pro-1/BdocWeb-pro-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:18 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] BdocWeb-pro-1/BdocWeb-pro-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] BdocWeb-pro-1/BdocWeb-pro-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:13:A9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00I413(NOUVEL INTRANET V4)

- **UUID (Instance):** 50393e69-b624-51ec-f189-1f9caeddb142
- **UUID (BIOS):** 42398897-904c-670c-6d73-f4dbf54ec470
- **Chemin VMX:** `[DS_P_REPLI_01] S00I413(NOUVEL INTRANET V4)/S00I413(NOUVEL INTRANET V4).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 07:41:45 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I413(NOUVEL INTRANET V4)/S00I413(NOUVEL INTRANET V4).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:40:db` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.164 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:40db (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-master03

- **UUID (Instance):** 501a642a-70d7-4f53-9f57-10b3ee2a7578
- **UUID (BIOS):** 421a6d16-0df4-7c9d-fe48-9ddf440488c7
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-master03/k8s-rke2-prod-master03.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:38:45 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-master03/k8s-rke2-prod-master03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:10:50` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.132 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1050 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I197(BCA_RS NEW)

- **UUID (Instance):** 501a88f2-2d76-489b-01ca-a79746de6370
- **UUID (BIOS):** 421acedd-68c9-a7a5-035c-667532a0357d
- **Chemin VMX:** `[DS_P_REPLI_03] S00I197(BCA_RS NEW)/S00I197(BCA_RS NEW).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-08
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 15:24:09 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00I197(BCA_RS NEW)/S00I197(BCA_RS NEW).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:03:5C:14` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00I76

- **UUID (Instance):** 501ab352-5011-8be8-7269-77d98f54947c
- **UUID (BIOS):** 421a0b22-31a3-46cb-eb9f-043d13890310
- **Chemin VMX:** `[DS_P_REPLI_11] S00I76/S00I76.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:03 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I76/S00I76.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I76/S00I76_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:81:55` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::70e8:1f95:78f1:2e37 (Prefix: 64, State: unknown), 172.16.210.76 (Prefix: 16, State: preferred) |

---

### 5.x VM: cegid-web-pro

- **UUID (Instance):** 501a29a6-c57e-9ac1-4953-d5fbefbbf5bd
- **UUID (BIOS):** 421ac063-db4c-44df-2714-b525d2fc2a46
- **Chemin VMX:** `[DS_P_REPLI_02] cegid-web-pro/cegid-web-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:40 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] cegid-web-pro/cegid-web-pro_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] cegid-web-pro/cegid-web-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:dc:f0` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::96fa:c03a:5c15:6f6 (Prefix: 64, State: unknown), 172.16.220.26 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I233

- **UUID (Instance):** 501abaa5-13a7-657f-bc6c-5162855c861a
- **UUID (BIOS):** 421a31a6-720e-4633-1fc6-73ce69c6c898
- **Chemin VMX:** `[DS_P_REPLI_13] S00I233/S00I233.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:41:15 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I233/S00I233.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I233/S00I233_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:84:dc` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::cb61:97d1:3ba1:b87f (Prefix: 64, State: unknown), 172.16.250.233 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_prod_worker15

- **UUID (Instance):** 501a3d01-6afa-bc71-366c-ea3e8bafbd29
- **UUID (BIOS):** 421a046a-5fdf-dda3-a00e-57d69c32e986
- **Chemin VMX:** `[DS_P_03] k8s_prod_worker15/k8s_prod_worker15.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12325, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-29 10:02:55 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_prod_worker15/k8s_prod_worker15.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f0:11` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.145 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f011 (Prefix: 64, State: unknown) |

---

### 5.x VM: PSQL_ODS_PRO2

- **UUID (Instance):** 501ac09a-9c34-2633-0f61-71a865cda78e
- **UUID (BIOS):** 421ab060-ac43-e4da-08c9-7039fbea26a0
- **Chemin VMX:** `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-09 00:35:48 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 8)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 225.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 5 (2004) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_4.vmdk` | persistent | False | -1 IOPS |
| Hard disk 6 (2005) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_5.vmdk` | persistent | False | -1 IOPS |
| Hard disk 7 (2006) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_6.vmdk` | persistent | False | -1 IOPS |
| Hard disk 8 (2008) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_7.vmdk` | persistent | False | -1 IOPS |
| Hard disk 9 (2009) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_8.vmdk` | persistent | False | -1 IOPS |
| Hard disk 10 (2010) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_9.vmdk` | persistent | False | -1 IOPS |
| Hard disk 11 (2011) | 80.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_10.vmdk` | persistent | False | -1 IOPS |
| Hard disk 12 (2012) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_11.vmdk` | persistent | False | -1 IOPS |
| Hard disk 13 (2013) | 110.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_12.vmdk` | persistent | False | -1 IOPS |
| Hard disk 14 (2014) | 30.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_13.vmdk` | persistent | False | -1 IOPS |
| Hard disk 15 (2015) | 20.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_14.vmdk` | persistent | False | -1 IOPS |
| Hard disk 16 (131088) | 200.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_15.vmdk` | persistent | False | -1 IOPS |
| Hard disk 17 (131089) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_16.vmdk` | persistent | False | -1 IOPS |
| Hard disk 18 (131090) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_17.vmdk` | persistent | False | -1 IOPS |
| Hard disk 19 (131091) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_18.vmdk` | persistent | False | -1 IOPS |
| Hard disk 20 (131092) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_19.vmdk` | persistent | False | -1 IOPS |
| Hard disk 21 (131093) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_20.vmdk` | persistent | False | -1 IOPS |
| Hard disk 22 (131094) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] PSQL_ODS_PRO2/PSQL_ODS_PRO2_21.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:5e:93` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.15 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:5e93 (Prefix: 64, State: unknown) |

---

### 5.x VM: TALEND-TAC-PRO-01

- **UUID (Instance):** 501a2f63-ae27-74b0-7c6c-0c6e628e3043
- **UUID (BIOS):** 564d2e4f-cc1d-ad03-f4f7-eb35493c90e4
- **Chemin VMX:** `[DS_P_REPLI_11] TALEND-TAC-PRO-01/TALEND-TAC-PRO-01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] TALEND-TAC-PRO-01/TALEND-TAC-PRO-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:D5:C7` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: dwh-ssas-pro

- **UUID (Instance):** 501ad8f0-fc3c-51a3-c568-eed98e442979
- **UUID (BIOS):** 421a36ce-7199-9b74-8c5a-01d4f9d3fc65
- **Chemin VMX:** `[DS_P_REPLI_03] dwh-ssas-pro/dwh-ssas-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:34:52 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 98304 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 983040 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] dwh-ssas-pro/dwh-ssas-pro_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] dwh-ssas-pro/dwh-ssas-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9A:C1:26` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: IES_SSAS_P

- **UUID (Instance):** 501a8fee-65e5-5efb-7953-aad5cef5d6e4
- **UUID (BIOS):** 421a5975-a8c0-ae36-33ae-4fcb2ddb5c1b
- **Chemin VMX:** `[DS_P_REPLI_12] IES_SSAS_P/IES_SSAS_P.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-07 10:30:59 UTC
- **Hôte Actuel:** vm-esx-p-03.bcaexpertise.org
- **vCPUs:** 12 (Cœurs/Socket: 6)
- **RAM:** 163840 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 12000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1638400 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] IES_SSAS_P/IES_SSAS_P.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ca:98` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::c146:87e:2340:7128 (Prefix: 64, State: unknown), 172.16.210.191 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-dsm-01

- **UUID (Instance):** 501a3c9a-1bfa-ad4d-4745-d9b648d1a70e
- **UUID (BIOS):** 421a2e21-d986-97b1-0ff6-504d891be639
- **Chemin VMX:** `[DS_P_REPLI_13] srv-dsm-01/srv-dsm-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-05 03:00:36 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] srv-dsm-01/srv-dsm-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] srv-dsm-01/srv-dsm-01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:95:36` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.177 (Prefix: 24, State: preferred) |

---

### 5.x VM: BONITA-01

- **UUID (Instance):** 50398c0f-33cb-a84e-b9bd-660bdb6840bf
- **UUID (BIOS):** 42395df7-b602-0900-02a7-25238c4a8497
- **Chemin VMX:** `[DS_P_REPLI_08] BONITA-01/BONITA-01.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-06 15:21:00 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] BONITA-01/BONITA-01.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] BONITA-01/BONITA-01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:13:8b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::8413:99ae:323e:90e7 (Prefix: 64, State: unknown), 172.16.220.137 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-mongo-pro

- **UUID (Instance):** 501a16b4-a9c8-cbbf-61f3-34ff3e58dae0
- **UUID (BIOS):** 421a5690-0399-9676-560c-87d4386f1288
- **Chemin VMX:** `[DS_P_REPLI_04] srv-mongo-pro/srv-mongo-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-29 10:48:04 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 400.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-mongo-pro/srv-mongo-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b4:fd` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.104 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:b4fd (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bdocmongo-pro1

- **UUID (Instance):** 501a5783-5f46-e8e0-e9f1-4119820caad3
- **UUID (BIOS):** 421abfe6-ea69-45a9-58d4-bd6364d0412e
- **Chemin VMX:** `[DS_P_05] srv-bdocmongo-pro1/srv-bdocmongo-pro1.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] srv-bdocmongo-pro1/srv-bdocmongo-pro1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:80:44` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.101 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8044 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I236

- **UUID (Instance):** 501aff44-bd0f-7e8b-35bd-f8d045dc41f5
- **UUID (BIOS):** 421abaf9-590f-4a81-0a12-6caf11b186fe
- **Chemin VMX:** `[DS_P_REPLI_12] S00I236/S00I236.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:42:12 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I236/S00I236.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] S00I236/S00I236_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:29:66` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::1ac4:aa5:346d:28c9 (Prefix: 64, State: unknown), 172.16.250.242 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bigmaxmongo-proa

- **UUID (Instance):** 501a344e-f6dc-146b-fdbb-c615ba4d2e1e
- **UUID (BIOS):** 421a10bf-cbb2-0b5e-5b61-a3da1384ccc1
- **Chemin VMX:** `[DS_P_REPLI_04] srv-bigmaxmongo-proa/srv-bigmaxmongo-proa.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:42 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-bigmaxmongo-proa/srv-bigmaxmongo-proa.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:78:47` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.108 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7847 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I237

- **UUID (Instance):** 501a82f2-4601-0363-a357-7cb9c4b1cd5d
- **UUID (BIOS):** 421a8b12-eb62-1f86-ee1d-1266683663aa
- **Chemin VMX:** `[DS_P_REPLI_11] S00I237/S00I237.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:44:56 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I237/S00I237.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] S00I237/S00I237_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f7:d5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::2a90:565b:2752:afb5 (Prefix: 64, State: unknown), 172.16.210.208 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I135(SMTB)

- **UUID (Instance):** 5039cac6-e092-4c0b-b8a0-9b4feb6c898b
- **UUID (BIOS):** 42390139-6ab7-dad0-f387-07bba49db058
- **Chemin VMX:** `[DS_P_REPLI_07] S00I135(SMTB)/S00I135(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 20:25:21 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I135(SMTB)/S00I135(SMTB).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:2f:6c` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.135 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I130(SMTB)

- **UUID (Instance):** 50397ae9-c95e-f39e-1aaf-c9def872041e
- **UUID (BIOS):** 4239fe90-9e3e-b13b-27c9-a639b6c205a9
- **Chemin VMX:** `[DS_P_REPLI_08] S00I130(SMTB)/S00I130(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-02 00:35:54 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] S00I130(SMTB)/S00I130(SMTB).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:6b:b2` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.130 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I136(SMTB)

- **UUID (Instance):** 5039d791-4bc1-d429-b301-322b6f774712
- **UUID (BIOS):** 42399321-7af4-e158-a52a-4f1cf9cc7149
- **Chemin VMX:** `[DS_P_REPLI_07] S00I136(SMTB)/S00I136(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 11:33:11 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I136(SMTB)/S00I136(SMTB).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:23:4f` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.136 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-ead-pro-01

- **UUID (Instance):** 501af612-e59f-f874-4e9c-eec6b27d94f6
- **UUID (BIOS):** 421a55aa-9c76-a070-9856-73f325c13274
- **Chemin VMX:** `[DS_P_REPLI_04] srv-ead-pro-01/srv-ead-pro-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:38:07 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-ead-pro-01/srv-ead-pro-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-ead-pro-01/srv-ead-pro-01_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 200.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-ead-pro-01/srv-ead-pro-01_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ab:b3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::637b:fde3:1f8:5848 (Prefix: 64, State: unknown), 172.16.220.22 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-refdiva-01

- **UUID (Instance):** 501afc5e-d5cb-6581-426d-e5bb04949959
- **UUID (BIOS):** 421af09d-1bf4-3029-5626-4765ac3f0324
- **Chemin VMX:** `[DS_P_REPLI_04] srv-refdiva-01/srv-refdiva-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:44:05 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-refdiva-01/srv-refdiva-01.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:a4:fd` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::ca9:259b:2881:2520 (Prefix: 64, State: unknown), 172.16.220.149 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-dns-externe-pro

- **UUID (Instance):** 501ae0a9-39cb-d6c4-f6e8-b88bac59f1db
- **UUID (BIOS):** 421a77da-2032-bcdf-7c69-28e9a75f8eb1
- **Chemin VMX:** `[DS_P_REPLI_11] srv-dns-externe-pro/srv-dns-externe-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-08-02 10:16:52 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] srv-dns-externe-pro/srv-dns-externe-pro-000001.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:63:87` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.4 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6387 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I86 (Concentrateur.bca.fr )_20240601

- **UUID (Instance):** 501a804c-a88a-bc2a-ca3d-b8bb3b0df220
- **UUID (BIOS):** 421a1e86-77da-212a-06f5-e2341ec3d99c
- **Chemin VMX:** `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )_20240601/S00I86 (Concentrateur.bca.fr )_20240601.vmx`
- **OS Invité:** Red Hat Enterprise Linux 4 (32-bit) (ID: rhel4Guest)
- **Version VM:** vmx-19
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-21 12:54:03 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2776 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 27760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )_20240601/S00I86 (Concentrateur.bca.fr )_20240601.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I86 (Concentrateur.bca.fr )_20240601/S00I86 (Concentrateur.bca.fr )_20240601_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9a:81:12` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | 172.16.220.190 (Prefix: 16, State: preferred), fe80::250:56ff:fe9a:8112 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I30(PRTG)

- **UUID (Instance):** 501a3a80-0999-ca18-b8cd-12ee36c55fe9
- **UUID (BIOS):** 421a994f-0887-6637-6040-2acfd09e3656
- **Chemin VMX:** `[DS_P_REPLI_10] S00I30(PRTG)/S00I30(PRTG).vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:39:08 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 120.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] S00I30(PRTG)/S00I30(PRTG).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:12:59` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::b221:898d:1559:a28f (Prefix: 64, State: unknown), 172.16.210.30 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-metier-pro1

- **UUID (Instance):** 501aa2d5-f29f-ee26-e603-b2d128815542
- **UUID (BIOS):** 421a90d4-59df-c2f8-b8e8-ce57a0bd1a65
- **Chemin VMX:** `[DS_P_REPLI_01] srv-metier-pro1/srv-metier-pro1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:44:35 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-metier-pro1/srv-metier-pro1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-metier-pro1/srv-metier-pro1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9A:20:BA` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00I132(SMTB)

- **UUID (Instance):** 50393cc2-c4ec-1db2-2066-faf031e64226
- **UUID (BIOS):** 4239c87e-3a0d-b448-fe7d-86c3e9984780
- **Chemin VMX:** `[DS_P_REPLI_03] S00I132(SMTB)/S00I132(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 07:41:47 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00I132(SMTB)/S00I132(SMTB).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:75:49` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.132 (Prefix: 24, State: preferred) |

---

### 5.x VM: Master-SNB-5.0.0-Ubuntu20-04_En-US

- **UUID (Instance):** 501ae6a1-705b-5be2-34cd-1b862c56b60a
- **UUID (BIOS):** 421aa1c5-950c-a8bc-8ff8-6f3aa0096f81
- **Chemin VMX:** `[DS_P_REPLI_04] Master-SNB-5.0.0-Ubuntu20-04_En-US/Master-SNB-5.0.0-Ubuntu20-04_En-US.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-13
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-11 11:32:12 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 1024 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 10240 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 20.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] Master-SNB-5.0.0-Ubuntu20-04_En-US/Master-SNB-5.0.0-Ubuntu20-04_En-US.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2a:9c` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.134 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2a9c (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I133(SMTB)

- **UUID (Instance):** 50391333-8703-5a98-ea82-518386a5b2db
- **UUID (BIOS):** 42398bcc-f419-0066-ff2f-268780bd7df9
- **Chemin VMX:** `[DS_P_REPLI_01] S00I133(SMTB)/S00I133(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I133(SMTB)/S00I133(SMTB).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:1d:44` | DVPortGroup: dvportgroup-229599 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.4.133 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I232

- **UUID (Instance):** 501a68ea-811f-e642-f13c-fcbaaa3ea075
- **UUID (BIOS):** 421ae6ba-15b3-5ddd-46d0-1dbc0a65c6ad
- **Chemin VMX:** `[DS_P_REPLI_13] S00I232/S00I232.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:42:41 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I232/S00I232.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] S00I232/S00I232_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:39:f6` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::7a78:92f2:698d:2667 (Prefix: 64, State: unknown), 172.16.250.232 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdoc-mysql-03-pro

- **UUID (Instance):** 501af438-6a95-59e0-ca48-b583e1d7ec30
- **UUID (BIOS):** 421a32c9-d6ad-1945-58ac-07badfd69e9e
- **Chemin VMX:** `[DS_P_REPLI_12] srv-bdoc-mysql-03-pro/srv-bdoc-mysql-03-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-25 20:41:11 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] srv-bdoc-mysql-03-pro/srv-bdoc-mysql-03-pro.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] srv-bdoc-mysql-03-pro/srv-bdoc-mysql-03-pro_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:90:e1` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.92 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:90e1 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-rabbitmq-pro

- **UUID (Instance):** 501a79b3-1240-1b31-33b3-ae82ec5c127d
- **UUID (BIOS):** 421ac703-dd77-d7b4-e209-ef6718383d71
- **Chemin VMX:** `[DS_P_REPLI_01] srv-rabbitmq-pro/srv-rabbitmq-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 10:43:00 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-rabbitmq-pro/srv-rabbitmq-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:56:6c` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.140 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:566c (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bdocmongo-proa

- **UUID (Instance):** 501acd50-e086-3647-3fa8-1d55c92a0479
- **UUID (BIOS):** 421ab759-38bf-39f8-fdd1-d61fcaa4e12a
- **Chemin VMX:** `[DS_P_05] srv-bdocmongo-proa/srv-bdocmongo-proa.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-09 14:42:21 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] srv-bdocmongo-proa/srv-bdocmongo-proa.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b6:24` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.103 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:b624 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I408 (bca.fr-lea-expertise.fr)

- **UUID (Instance):** 50398196-6776-9324-0fe4-a94bd3c3bbfb
- **UUID (BIOS):** 42394511-2650-ffbb-0ce6-c9ff7a7f3f1b
- **Chemin VMX:** `[DS_P_REPLI_01] S00I408 (bca.fr-lea-expertise.fr)/S00I408 (bca.fr-lea-expertise.fr).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-15 06:22:07 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I408 (bca.fr-lea-expertise.fr)/S00I408 (bca.fr-lea-expertise.fr).vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00I408 (bca.fr-lea-expertise.fr)/S00I408 (bca.fr-lea-expertise.fr)_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:5e:78` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.66 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:5e78 (Prefix: 64, State: unknown) |

---

### 5.x VM: PSQL_BIGMAX_PRO

- **UUID (Instance):** 501ad0be-be04-05f7-9260-79016e77fa9b
- **UUID (BIOS):** 421a5229-563a-75b1-69d4-892ce9e1b4ab
- **Chemin VMX:** `[DS_P_REPLI_10] PSQL_BIGMAX_PRO/PSQL_BIGMAX_PRO.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-25 19:08:28 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_BIGMAX_PRO/PSQL_BIGMAX_PRO.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_BIGMAX_PRO/PSQL_BIGMAX_PRO_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_BIGMAX_PRO/PSQL_BIGMAX_PRO_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 60.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] PSQL_BIGMAX_PRO/PSQL_BIGMAX_PRO_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:50:19` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: BdocAgent-pro-1

- **UUID (Instance):** 501a5627-7c54-d5f4-b6d2-a81d397fd26f
- **UUID (BIOS):** 421a53a5-a6ce-f73f-5bfb-5913c7a79326
- **Chemin VMX:** `[DS_P_REPLI_10] BdocAgent-pro-1/BdocAgent-pro-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:41:42 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] BdocAgent-pro-1/BdocAgent-pro-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_10 | `[DS_P_REPLI_10] BdocAgent-pro-1/BdocAgent-pro-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:6B:14` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: k8s-rke2-prod-master01

- **UUID (Instance):** 501abc55-3c2c-9655-ab22-1e7b18778932
- **UUID (BIOS):** 421a4cf4-2a7e-62e8-17ff-026cb7dd1ca6
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-master01/k8s-rke2-prod-master01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:16:50 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-master01/k8s-rke2-prod-master01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:71:db` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.130 (Prefix: 24, State: preferred), 192.168.60.13 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:71db (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I140

- **UUID (Instance):** 501a750a-50f8-529e-46f4-0582b17e088d
- **UUID (BIOS):** 421a968f-911a-fb76-de29-8d95c6d8547b
- **Chemin VMX:** `[DS_P_REPLI_05] S00I140/S00I140.vmx`
- **OS Invité:** Red Hat Enterprise Linux 7 (64-bit) (ID: rhel7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11269, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-05 13:30:52 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I140/S00I140.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:1E:0A` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: P00P24 (Prolival Exploitation)

- **UUID (Instance):** 5039e923-24dd-baa0-927b-b6be74d5552e
- **UUID (BIOS):** 4239f04a-1e73-3636-7175-5eab4e81f0a0
- **Chemin VMX:** `[DS_P_REPLI_11] P00P24/P00P24.vmx`
- **OS Invité:** Microsoft Windows 8.x (64-bit) (ID: windows8_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 19:15:17 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] P00P24/P00P24.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:6b:9e` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::50ef:e37d:22e:944 (Prefix: 64, State: unknown), 172.16.250.24 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I201 (JBOSS EAP 5.2 V3 PRO)

- **UUID (Instance):** 5039e3b7-0602-e9fd-00de-10c67ac9dd8e
- **UUID (BIOS):** 564de113-5b38-f26d-2c7d-8786fc482065
- **Chemin VMX:** `[DS_P_02] S00I201 (JBOSS EAP 5.2 V3 PRO)/S00I201 (JBOSS EAP 5.2 V3 PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-29 17:04:50 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_02 | `[DS_P_02] S00I201 (JBOSS EAP 5.2 V3 PRO)/S00I201 (JBOSS EAP 5.2 V3 PRO).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_02 | `[DS_P_02] S00I201 (JBOSS EAP 5.2 V3 PRO)/S00I201 (JBOSS EAP 5.2 V3 PRO)_1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2002) | 10.0 | DS_P_02 | `[DS_P_02] S00I201 (JBOSS EAP 5.2 V3 PRO)/S00I201 (JBOSS EAP 5.2 V3 PRO)_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:B9:6A:A0` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: SRVSCCM02

- **UUID (Instance):** 501a57db-9a68-5926-2fda-34a382d35b1c
- **UUID (BIOS):** 564d44a0-dcfe-f18e-53d1-8566e2bacf36
- **Chemin VMX:** `[DS_P_REPLI_01] SRVSCCM02/SRVSCCM02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-22 02:00:33 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 250.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] SRVSCCM02/SRVSCCM02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b5:da` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::e566:664e:fe98:befa (Prefix: 64, State: unknown), 172.16.220.34 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-wap-02

- **UUID (Instance):** 501a5f03-2fb6-dd27-d0ad-cf2f07b30121
- **UUID (BIOS):** 421a7972-ac92-d304-9e33-566df06d465a
- **Chemin VMX:** `[DS_P_REPLI_01] srv-wap-02/srv-wap-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 22:40:12 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-wap-02/srv-wap-02.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:47:45` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.86 (Prefix: 24, State: preferred), 192.168.1.76 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I608(Experveo-Classicexpert)

- **UUID (Instance):** 501a1fa8-1a4d-114e-a965-9ad9eac3c19a
- **UUID (BIOS):** 564d6c2e-c02d-55a3-81d2-9b873a9b0ef4
- **Chemin VMX:** `[DS_P_REPLI_04] S00I608(Experveo-Classicexpert)/S00I608(Experveo-Classicexpert).vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-09 14:46:02 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] S00I608(Experveo-Classicexpert)/S00I608(Experveo-Classicexpert)_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e1:cd` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.142 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e1cd (Prefix: 64, State: unknown) |

---

### 5.x VM: HiveManager

- **UUID (Instance):** 503981ce-6855-a903-7278-fbf87c3b41f1
- **UUID (BIOS):** 423956f7-a455-1d1a-35f2-8c7a80612e92
- **Chemin VMX:** `[DS_P_REPLI_02] HiveManager/HiveManager.vmx`
- **OS Invité:** Other Linux (64-bit) (ID: otherLinux64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10309, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-25 20:41:11 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (3000) | 238.28 | DS_P_REPLI_02 | `[DS_P_REPLI_02] HiveManager/HiveManager.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:5a:7d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.50 (Prefix: 24, State: preferred) |

---

### 5.x VM: BdocWeb-pro-2

- **UUID (Instance):** 501a5cf2-1623-7112-db60-74da5ec22d09
- **UUID (BIOS):** 564dcc3e-e220-139f-2e3f-546b6c732367
- **Chemin VMX:** `[DS_P_REPLI_07] BdocWeb-pro-2/BdocWeb-pro-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:37:31 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] BdocWeb-pro-2/BdocWeb-pro-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] BdocWeb-pro-2/BdocWeb-pro-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:5F:20` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-talend-jobserveur-02-pro

- **UUID (Instance):** 501a24d1-eb26-e95f-6cdf-9ab4bca2c8cd
- **UUID (BIOS):** 421a87ed-1380-78c1-7e64-fd8d8986b5e0
- **Chemin VMX:** `[DS_P_REPLI_02] srv-talend-jobserveur-02-pro/srv-talend-jobserveur-02-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-11 04:43:54 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-talend-jobserveur-02-pro/srv-talend-jobserveur-02-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e1:6c` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.39 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e16c (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-adfs-01

- **UUID (Instance):** 501ac9a9-95f5-53ce-fb90-6e888c5d59df
- **UUID (BIOS):** 421adfc0-c172-c170-1885-8280ba84af68
- **Chemin VMX:** `[DS_P_REPLI_05] srv-adfs-01/srv-adfs-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:42:43 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] srv-adfs-01/srv-adfs-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] srv-adfs-01/srv-adfs-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:e4:38` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::ff4c:693d:5ac2:32c0 (Prefix: 64, State: unknown), 172.16.250.12 (Prefix: 16, State: preferred) |

---

### 5.x VM: BdocInter-pro-1

- **UUID (Instance):** 501a8597-31f7-2b06-c891-a44850c9326e
- **UUID (BIOS):** 421a31fc-2ce5-c163-5b74-4d2c90c993e3
- **Chemin VMX:** `[DS_P_REPLI_03] BdocInter-pro-1/BdocInter-pro-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:41:06 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] BdocInter-pro-1/BdocInter-pro-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] BdocInter-pro-1/BdocInter-pro-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:B2:2E` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: IES_P_BI

- **UUID (Instance):** 501abd61-07a6-0b5b-2982-45f8e0bdbda9
- **UUID (BIOS):** 421ac8a0-30dd-2935-63ab-cbeeaf6a793f
- **Chemin VMX:** `[DS_P_REPLI_01] IES_P_BI/IES_P_BI.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 02:27:22 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 2)
- **RAM:** 98304 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 983040 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 180.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] IES_P_BI/IES_P_BI.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 250.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] IES_P_BI/IES_P_BI_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:23:75` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::59ad:c601:4543:d471 (Prefix: 64, State: unknown), 172.16.220.178 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s_prod_worker10

- **UUID (Instance):** 501af304-356f-a8fa-d256-5f6db22be1d9
- **UUID (BIOS):** 421a53c3-6e87-2c0f-7795-784ea0b63bfd
- **Chemin VMX:** `[DS_P_REPLI_02] k8s_prod_worker10/k8s_prod_worker10.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-14 11:29:00 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] k8s_prod_worker10/k8s_prod_worker10.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:08:64` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.140 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:864 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-talend-jobserveur-01-pro

- **UUID (Instance):** 501ae103-61d8-2361-69b8-d10b6f69c435
- **UUID (BIOS):** 421aa60e-95e6-141f-a098-126dcccca027
- **Chemin VMX:** `[DS_P_REPLI_11] srv-talend-jobserveur-01-pro/srv-talend-jobserveur-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-11 04:46:01 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] srv-talend-jobserveur-01-pro/srv-talend-jobserveur-01-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2f:e4` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.38 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2fe4 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-postgres-01-pro

- **UUID (Instance):** 501a4c78-6da8-c4cc-9e0b-f4a08d7f6da7
- **UUID (BIOS):** 421afded-a803-19dc-64f0-afe52b1f10ee
- **Chemin VMX:** `[DS_P_03] srv-postgres-01-pro/srv-postgres-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-15 08:26:08 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 12 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 12000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_P_03 | `[DS_P_03] srv-postgres-01-pro/srv-postgres-01-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bf:8f` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.139 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bf8f (Prefix: 64, State: unknown) |

---

### 5.x VM: S00B135

- **UUID (Instance):** 501a88fa-b164-7ff7-f441-5a5b7db4251a
- **UUID (BIOS):** 421ac9ae-6d21-1e2d-e2ee-6fb133169239
- **Chemin VMX:** `[DS_P_REPLI_01] S00B135/S00B135.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:46:10 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00B135/S00B135.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00B135/S00B135_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 300.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00B135/S00B135_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:9e:fc` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::e38a:ed60:941c:e1fe (Prefix: 64, State: unknown), 172.16.220.135 (Prefix: 24, State: preferred) |

---

### 5.x VM: vCLS-7378d671-6e93-4de1-b1bc-bfd94bdc74b8

- **UUID (Instance):** 501a079a-83c7-b450-e245-56d8a29a4a27
- **UUID (BIOS):** 421af646-07f1-5563-bf23-5475a85cda4a
- **Chemin VMX:** `[DS_P_REPLI_13] vCLS-7378d671-6e93-4de1-b1bc-bfd94bdc74b8/vCLS-7378d671-6e93-4de1-b1bc-bfd94bdc74b8.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-06 12:53:44 UTC
- **Hôte Actuel:** vm-esx-p-09.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | DS_P_REPLI_13 | `[DS_P_REPLI_13] vCLS-7378d671-6e93-4de1-b1bc-bfd94bdc74b8/vCLS-7378d671-6e93-4de1-b1bc-bfd94bdc74b8.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: k8s_prod_master01

- **UUID (Instance):** 501a2ff9-66e0-4158-a41c-b754c8cf8e62
- **UUID (BIOS):** 421a09d8-102b-6eb5-12ff-582c518d8187
- **Chemin VMX:** `[DS_P_03] k8s_prod_master01/k8s_prod_master01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 03:49:45 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_prod_master01/k8s_prod_master01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:82:96` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.130 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8296 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-wap-01

- **UUID (Instance):** 501a40eb-2164-5dbd-1724-1ae724db46a5
- **UUID (BIOS):** 421a713c-a915-cd40-3861-0d519752b361
- **Chemin VMX:** `[DS_P_REPLI_01] srv-wap-01/srv-wap-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 15:23:02 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] srv-wap-01/srv-wap-01.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:8d:70` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::3f78:ab6f:e30e:49c3 (Prefix: 64, State: unknown), 192.168.1.85 (Prefix: 24, State: preferred), 192.168.1.76 (Prefix: 24, State: preferred) |

---

### 5.x VM: SRV-IHM-PRO-02

- **UUID (Instance):** 501a4c6d-48a0-9fc3-9031-bb542c41c494
- **UUID (BIOS):** 421ad1fa-46c6-52b4-4775-9fa485fe5d05
- **Chemin VMX:** `[DS_P_REPLI_02] SRV-IHM-PRO-02/SRV-IHM-PRO-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:41:34 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] SRV-IHM-PRO-02/SRV-IHM-PRO-02_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] SRV-IHM-PRO-02/SRV-IHM-PRO-02_4.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:69:d3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::c1ca:8194:3a62:f0ac (Prefix: 64, State: unknown), 172.16.210.231 (Prefix: 16, State: preferred) |

---

### 5.x VM: S00I410(JBOSS EAP 7 V4 ADMPRO)

- **UUID (Instance):** 5039e10b-7988-5142-e94a-d83b9a8ca11a
- **UUID (BIOS):** 564d1e2c-ce00-5d95-4c52-219afea31505
- **Chemin VMX:** `[DS_P_03] S00I410(JBOSS EAP 7 V4 ADMPRO)/S00I410(JBOSS EAP 7 V4 ADMPRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 22:18:13 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_03 | `[DS_P_03] S00I410(JBOSS EAP 7 V4 ADMPRO)/S00I410(JBOSS EAP 7 V4 ADMPRO).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:3e:bd` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.2.96 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:3ebd (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I87(GAD)

- **UUID (Instance):** 503976a0-95bc-23b3-6eb5-5de435fb51da
- **UUID (BIOS):** 564d0728-1535-052d-2aef-eaaed65f0d71
- **Chemin VMX:** `[DS_P_REPLI_07] S00I87(GAD)/S00I87(GAD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 5 (64-bit) (ID: rhel5_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10358, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-07-12 14:32:14 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I87(GAD)/S00I87(GAD).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:7a:92` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.87 (Prefix: 16, State: preferred), fe80::250:56ff:feb9:7a92 (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocAgent-pro-2

- **UUID (Instance):** 501a7c44-33ab-aefa-0894-330f924fd6b7
- **UUID (BIOS):** 421acc01-1b72-baae-0a9f-f926b3120afb
- **Chemin VMX:** `[DS_P_REPLI_01] BdocAgent-pro-2/BdocAgent-pro-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:39:50 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] BdocAgent-pro-2/BdocAgent-pro-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] BdocAgent-pro-2/BdocAgent-pro-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:7F:5A` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-talend-nexus-slave-pro

- **UUID (Instance):** 501ae6d7-31a3-f0b3-1930-c8be14b98182
- **UUID (BIOS):** 421a9884-671d-2d38-80be-c19dd715ec05
- **Chemin VMX:** `[DS_P_REPLI_02] srv-talend-nexus-slave-pro/srv-talend-nexus-slave-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-07-25 11:35:00 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 240.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-talend-nexus-slave-pro/srv-talend-nexus-slave-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a1:9f` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.250.248 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a19f (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-concentrateur-pro.OLD.040425

- **UUID (Instance):** 501a4b26-7ac0-12e7-c54f-0776b330dabd
- **UUID (BIOS):** 421a0366-98a3-5b66-545b-a025de10f4a0
- **Chemin VMX:** `[DS_P_REPLI_02] srv-concentrateur-pro-20250220/srv-concentrateur-pro-20250220.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-19
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-concentrateur-pro-20250220/srv-concentrateur-pro-20250220.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:7e:8b` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: S00L79(DU)

- **UUID (Instance):** 5039ca5e-659c-ee34-c91a-35c58b235126
- **UUID (BIOS):** 42390528-425b-2452-30f9-8dfb879b10da
- **Chemin VMX:** `[DS_P_REPLI_03] S00L79(DU)/S00L79(DU).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00L79(DU)/S00L79(DU).vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] S00L79(DU)/S00L79(DU)_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:1d:2d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: k8s_prod_worker14

- **UUID (Instance):** 501aeb27-c560-0144-8d9e-8130700b7ff3
- **UUID (BIOS):** 421a4707-6028-2099-6bf4-b716ca5f2deb
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker14/k8s_prod_worker14.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12325, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 10:56:29 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker14/k8s_prod_worker14.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:49:0F` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: S00I106(concentrateurBCA)

- **UUID (Instance):** 50398e13-4037-a877-207e-737c640819b0
- **UUID (BIOS):** 42396982-1f7b-b6e5-a97e-e8eb51c15190
- **Chemin VMX:** `[DS_P_REPLI_07] S00I106(concentrateurBCA)/S00I106(concentrateurBCA).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I106(concentrateurBCA)/S00I106(concentrateurBCA).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:4f:a3` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: Bdoc-Design-01

- **UUID (Instance):** 501aeb27-879d-fe27-4d1d-83632906bdb6
- **UUID (BIOS):** 421aa108-5131-83cf-9707-c3d0de033f88
- **Chemin VMX:** `[DS_P_REPLI_01] Bdoc-Design-01/Bdoc-Design-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:57:29 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 24576 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 245760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] Bdoc-Design-01/Bdoc-Design-01.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 200.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] Bdoc-Design-01/Bdoc-Design-01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:32:83` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::e0b6:bfd3:cf87:7e61 (Prefix: 64, State: unknown), 172.16.250.160 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I401(JBOSS EAP 7 V4 PRO)

- **UUID (Instance):** 5039ba9b-8728-52fa-3500-6a5b73167dab
- **UUID (BIOS):** 4239b5c5-1071-1d34-9d0e-c6fc3a930373
- **Chemin VMX:** `[DS_P_02] S00I401(JBOSS EAP 7 V4 PRO)/S00I401(JBOSS EAP 7 V4 PRO).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-25 20:41:12 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 15360 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 153600 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_02 | `[DS_P_02] S00I401(JBOSS EAP 7 V4 PRO)/S00I401(JBOSS EAP 7 V4 PRO).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_P_02 | `[DS_P_02] S00I401(JBOSS EAP 7 V4 PRO)/S00I401(JBOSS EAP 7 V4 PRO)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:37:dd` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.2.90 (Prefix: 24, State: preferred), 192.168.2.91 (Prefix: 32, State: preferred), 192.168.2.92 (Prefix: 32, State: preferred), fe80::250:56ff:feb9:37dd (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-manager-01-pro

- **UUID (Instance):** 501aab06-0b1b-3795-3021-f471ed718588
- **UUID (BIOS):** 421a10b0-1edc-5c91-f080-4c9e8698447f
- **Chemin VMX:** `[DS_P_02] srv-docker-manager-01-pro/srv-docker-manager-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-07 14:44:36 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 153600 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1536000 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_02 | `[DS_P_02] srv-docker-manager-01-pro/srv-docker-manager-01-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:9d:42` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.124 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:9d42 (Prefix: 64, State: unknown) |

---

### 5.x VM: s00i196 (BCAPRO_BCASIV_ASE15.7)

- **UUID (Instance):** 501a42ea-2c24-980e-a1e5-e2b9b74749ea
- **UUID (BIOS):** 421ac637-54c9-c44c-e493-141560f6a56f
- **Chemin VMX:** `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:39 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 28 (Cœurs/Socket: 1)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 28000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 70.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7)_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 740.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7)_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 300.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7)_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 5 (2004) | 10.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] s00i196 (BCAPRO_BCASIV_ASE15.7)_1/s00i196 (BCAPRO_BCASIV_ASE15.7)_4.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9d:de:43` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.196 (Prefix: 16, State: preferred), 172.16.220.83 (Prefix: 32, State: preferred), 172.16.220.189 (Prefix: 32, State: preferred), fe80::250:56ff:fe9d:de43 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-worker-02-pro

- **UUID (Instance):** 501ad52a-6336-7b33-5c6e-7f630ef5a445
- **UUID (BIOS):** 421a4507-928b-c092-808f-55a988de6bee
- **Chemin VMX:** `[DS_P_03] srv-docker-worker-02-pro/srv-docker-worker-02-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-07 14:21:57 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 153600 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1536000 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_03 | `[DS_P_03] srv-docker-worker-02-pro/srv-docker-worker-02-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:87:fd` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.128 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:87fd (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker03

- **UUID (Instance):** 501aadb8-c98f-1aee-1b22-1f1fdc08c90d
- **UUID (BIOS):** 564d8714-4f37-f75c-b0fa-16cb42b32f73
- **Chemin VMX:** `[DS_P_03] k8s_prod_worker03/k8s_prod_worker03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-06 12:45:12 UTC
- **Hôte Actuel:** vm-esx-p-08.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_prod_worker03/k8s_prod_worker03.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1024.0 | DS_P_03 | `[DS_P_03] k8s_prod_worker03/k8s_prod_worker03_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ae:20` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.135 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ae20 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-robotmel-01

- **UUID (Instance):** 501af993-5b73-fffb-7c29-7a7253aa50ac
- **UUID (BIOS):** 421ada18-eb0b-f12c-61ff-2d6535d41f3d
- **Chemin VMX:** `[DS_P_REPLI_03] srv-robotmel-01/srv-robotmel-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-05-04 03:00:27 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 2)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] srv-robotmel-01/srv-robotmel-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] srv-robotmel-01/srv-robotmel-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:61:2e` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::5855:2c79:d7bb:1e84 (Prefix: 64, State: unknown), 172.16.220.41 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I82(EAD)

- **UUID (Instance):** 50393522-f1f8-949c-2dce-0bda4ebb29ad
- **UUID (BIOS):** 564db9ee-ccb1-0944-054c-50c2eeee4a2f
- **Chemin VMX:** `[DS_P_REPLI_07] S00I82(EAD)/S00I82(EAD).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:37 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 32.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] S00I82(EAD)/S00I82(EAD).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:0f:9a` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.82 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-autom-pro

- **UUID (Instance):** 501aeca9-8e44-ef65-31dd-2318bafee04c
- **UUID (BIOS):** 421af6d6-b8e9-bc04-5347-92fbe4812b7e
- **Chemin VMX:** `[DS_P_REPLI_05] autom-pro/autom-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-17 12:55:26 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] autom-pro/autom-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:11:e5` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.139 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:11e5 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-uniflow

- **UUID (Instance):** 501ae8d0-7fd3-bf84-1827-ff76f0d88f47
- **UUID (BIOS):** 421ad24d-14b6-c8ea-8a4b-a22c176c0e7c
- **Chemin VMX:** `[DS_P_REPLI_02] srv-uniflow/srv-uniflow.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:41:43 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 120.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-uniflow/srv-uniflow.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-uniflow/srv-uniflow_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1e:28` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::af9c:598f:903a:328b (Prefix: 64, State: unknown), 172.16.210.188 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00A04

- **UUID (Instance):** 501a2c52-aec0-8e84-e8c2-c9ce4b1dc51d
- **UUID (BIOS):** 421a6966-22bc-be1c-75c8-3962905e3d5e
- **Chemin VMX:** `[DS_P_REPLI_01] S00A04/S00A04.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-17 12:12:04 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00A04/S00A04.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] S00A04/S00A04_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9A:AC:F3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: k8s_support_worker03

- **UUID (Instance):** 501a6384-7b4c-a816-6593-d85170cc2bf9
- **UUID (BIOS):** 421af65b-4b71-f80c-29e2-35d05d30201a
- **Chemin VMX:** `[DS_P_03] k8s_support_worker03/k8s_support_worker03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-22 11:02:21 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_03 | `[DS_P_03] k8s_support_worker03/k8s_support_worker03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2b:f3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.113 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2bf3 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I99(RVBD-CMC)

- **UUID (Instance):** 50398f1b-565e-998d-8dc7-362610ed1d7e
- **UUID (BIOS):** 4239961a-9fa2-84a8-e320-3d918c7af75d
- **Chemin VMX:** `[DS_P_REPLI_05] S00I99(RVBD-CMC)/S00I99(RVBD-CMC).vmx`
- **OS Invité:** Other 2.6.x Linux (64-bit) (ID: other26xLinux64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9216, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 22.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I99(RVBD-CMC)/S00I99(RVBD-CMC).vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I99(RVBD-CMC)/S00I99(RVBD-CMC)_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 2.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I99(RVBD-CMC)/S00I99(RVBD-CMC)_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:7b:ec` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.200.9 (Prefix: 24, State: preferred), fe80::250:56ff:feb9:7bec (Prefix: 64, State: unknown) |
| Network adapter 2 (4001) | vim.vm.device.VirtualE1000 | `00:50:56:b9:17:1d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)

- **UUID (Instance):** 501a9834-85b3-0453-da0d-059ade4461df
- **UUID (BIOS):** 421aba9f-23b0-2850-d7de-9d9926f01f3a
- **Chemin VMX:** `[DS_P_REPLI_03] s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)/s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-08
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 16:20:52 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 16 (Cœurs/Socket: 16)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 16000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)/s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)_4.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 70.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)/s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)_6.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 740.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)/s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)_8.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 300.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)/s00i196s (BCAPRO_SEC_BCASIV_SEC_ASE15.7)_10.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:03:35:13` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.195 (Prefix: 16, State: preferred), 172.16.220.86 (Prefix: 32, State: preferred), 172.16.220.84 (Prefix: 32, State: preferred), fe80::250:56ff:fe03:3513 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-worker-01-pro

- **UUID (Instance):** 501a7d67-556d-5104-315f-9ceb91439787
- **UUID (BIOS):** 421afe81-80af-9677-8c35-6ba97de7b402
- **Chemin VMX:** `[DS_P_02] srv-docker-worker-01-pro/srv-docker-worker-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-07 14:27:28 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 153600 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1536000 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_02 | `[DS_P_02] srv-docker-worker-01-pro/srv-docker-worker-01-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:6f:b9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.127 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6fb9 (Prefix: 64, State: unknown) |

---

### 5.x VM: cegid-sgtw-pro

- **UUID (Instance):** 501a956e-af34-a9a8-0a6d-74e5aee39217
- **UUID (BIOS):** 421ab8e0-3100-b59a-94c2-4d64ea0ac8d6
- **Chemin VMX:** `[DS_P_REPLI_01] cegid-sgtw-pro/cegid-sgtw-pro.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:36:59 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] cegid-sgtw-pro/cegid-sgtw-pro_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_01 | `[DS_P_REPLI_01] cegid-sgtw-pro/cegid-sgtw-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ff:37` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::cbda:1ad7:de30:f83 (Prefix: 64, State: unknown), 172.16.220.24 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I207

- **UUID (Instance):** 501a7c6c-4096-864f-9b51-60c41895300c
- **UUID (BIOS):** 421a2b83-72bf-3068-c89c-5fcdb354161c
- **Chemin VMX:** `[DS_P_REPLI_14] S00I207/S00I207.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I207/S00I207.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I207/S00I207_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 20.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I207/S00I207_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 80.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] S00I207/S00I207_3.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:61:0c` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: srv-docker-manager-02-pro

- **UUID (Instance):** 501a1ae5-f044-1e18-ae09-50b19dd31029
- **UUID (BIOS):** 421a2032-b712-c790-b60f-778ee98d61b6
- **Chemin VMX:** `[DS_P_03] srv-docker-manager-02-pro/srv-docker-manager-02-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-07 14:38:56 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 153600 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1536000 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_03 | `[DS_P_03] srv-docker-manager-02-pro/srv-docker-manager-02-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bf:16` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.125 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bf16 (Prefix: 64, State: unknown) |

---

### 5.x VM: DWH-SQL-PRO

- **UUID (Instance):** 501aa664-da53-c48a-5984-da3288f88849
- **UUID (BIOS):** 564dceb4-2da1-f947-0641-40763e02dcf0
- **Chemin VMX:** `[DS_P_REPLI_12] DWH-SQL-PRO/DWH-SQL-PRO.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:36:49 UTC
- **Hôte Actuel:** vm-esx-p-02.bcaexpertise.org
- **vCPUs:** 12 (Cœurs/Socket: 2)
- **RAM:** 131072 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 12000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1310720 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] DWH-SQL-PRO/DWH-SQL-PRO.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1433.6 | DS_P_REPLI_12 | `[DS_P_REPLI_12] DWH-SQL-PRO/DWH-SQL-PRO_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 500.0 | DS_P_REPLI_12 | `[DS_P_REPLI_12] DWH-SQL-PRO/DWH-SQL-PRO_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:60:6b` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::70b0:1c4c:7ed3:680f (Prefix: 64, State: unknown), 172.16.210.225 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I97(NOUVEAU SRVMOBILINK RHEL7.9)

- **UUID (Instance):** 501a79e2-9537-a675-a568-9e20938d3eec
- **UUID (BIOS):** 421a92b6-506d-6499-243d-37806c1b5f9e
- **Chemin VMX:** `[DS_P_REPLI_05] S00I97(NOUVEAU SRVMOBILINK RHEL7.9)/S00I97(NOUVEAU SRVMOBILINK RHEL7.9).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-08
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] S00I97(NOUVEAU SRVMOBILINK RHEL7.9)/S00I97(NOUVEAU SRVMOBILINK RHEL7.9).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:be:c8` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.97 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bec8 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-kms-01

- **UUID (Instance):** 501abcde-149c-dc38-4cc6-67841534b937
- **UUID (BIOS):** 421a82e5-3363-c7ed-037f-cf22d6adc444
- **Chemin VMX:** `[DS_P_REPLI_02] srv-kms-01/srv-kms-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:59:02 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-kms-01/srv-kms-01.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:85:30` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::9739:bb96:6821:bfb1 (Prefix: 64, State: unknown), 172.16.210.66 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-observium-pro

- **UUID (Instance):** 501a5276-469c-bf36-13d4-176d0a5e9589
- **UUID (BIOS):** 421a007a-7dd6-a6dd-1969-62bd1ac4858f
- **Chemin VMX:** `[DS_P_REPLI_04] srv-observium-pro/srv-observium-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-observium-pro/srv-observium-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:4f:25` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.208 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:4f25 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker04

- **UUID (Instance):** 501a04a7-1a89-9340-411d-e26955681e10
- **UUID (BIOS):** 421aba1e-d704-b07a-9afe-6bb642cb2fb3
- **Chemin VMX:** `[DS_P_02] k8s_prod_worker04/k8s_prod_worker04.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 08:11:12 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_02 | `[DS_P_02] k8s_prod_worker04/k8s_prod_worker04.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:99:e9` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.128 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:99e9 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-prod-worker01

- **UUID (Instance):** 501aa95e-ca54-8004-ee8a-0347f407650d
- **UUID (BIOS):** 421a5f56-0a6f-37ae-4519-cf1e70314418
- **Chemin VMX:** `[DS_P_REPLI_15] k8s-rke2-prod-worker01/k8s-rke2-prod-worker01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 10:06:37 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_15 | `[DS_P_REPLI_15] k8s-rke2-prod-worker01/k8s-rke2-prod-worker01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ba:08` | DVPortGroup: dvportgroup-180102 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.60.133 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ba08 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bigmaxmongo-pro2

- **UUID (Instance):** 501adc51-1328-74c9-d231-13bfef181118
- **UUID (BIOS):** 421a70c2-c78d-8258-15d0-c80d2c0c857c
- **Chemin VMX:** `[DS_P_REPLI_04] srv-bigmaxmongo-pro2/srv-bigmaxmongo-pro2.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] srv-bigmaxmongo-pro2/srv-bigmaxmongo-pro2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e6:2a` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.107 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e62a (Prefix: 64, State: unknown) |

---

### 5.x VM: SRVSCCM01

- **UUID (Instance):** 501a32c3-7a97-56fe-bba5-bb7ea94d104b
- **UUID (BIOS):** 421abca9-f5b3-da3f-9969-59b78743fc47
- **Chemin VMX:** `[DS_P_REPLI_04] SRVSCCM01/SRVSCCM01.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-22 02:01:04 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 220.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] SRVSCCM01/SRVSCCM01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1536.0 | DS_P_REPLI_04 | `[DS_P_REPLI_04] SRVSCCM01/SRVSCCM01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:29:a6` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::eda0:341:5816:a1df (Prefix: 64, State: unknown), 172.16.220.30 (Prefix: 24, State: preferred) |
| Network adapter 2 (4001) | vim.vm.device.VirtualVmxnet3 | `00:50:56:b9:7a:55` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-gitlab-pro

- **UUID (Instance):** 501aa553-7bbb-2de6-87e6-1e81da143243
- **UUID (BIOS):** 421a8e47-e2bf-9c9e-0b04-91cae2d46ae4
- **Chemin VMX:** `[DS_P_REPLI_08] srv-gitlab-pro/srv-gitlab-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-26 10:51:20 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 2)
- **RAM:** 24576 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 245760 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 800.0 | DS_P_REPLI_08 | `[DS_P_REPLI_08] srv-gitlab-pro/srv-gitlab-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:23:38` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.107 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2338 (Prefix: 64, State: unknown) |

---

### 5.x VM: FortiAnalyzer-VM

- **UUID (Instance):** 50393554-ca14-d52b-6827-b47c974f3c8f
- **UUID (BIOS):** 4239f340-ebf6-bf62-4236-38d74e35178d
- **Chemin VMX:** `[DS_P_REPLI_11] FortiAnalyzer-VM/FortiAnalyzer-VM.vmx`
- **OS Invité:** Other 2.6.x Linux (64-bit) (ID: other26xLinux64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 2147483647, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 08:11:11 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] FortiAnalyzer-VM/FortiAnalyzer-VM.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 80.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] FortiAnalyzer-VM/FortiAnalyzer-VM_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 200.0 | DS_P_REPLI_11 | `[DS_P_REPLI_11] FortiAnalyzer-VM/FortiAnalyzer-VM_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:79:7e` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.54 (Prefix: 24, State: preferred) |
| Network adapter 2 (4001) | vim.vm.device.VirtualE1000 | `00:50:56:b9:7e:23` | DVPortGroup: dvportgroup-105 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |
| Network adapter 3 (4002) | vim.vm.device.VirtualE1000 | `00:50:56:b9:3c:6d` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |
| Network adapter 4 (4003) | vim.vm.device.VirtualE1000 | `00:50:56:b9:4b:cc` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-bdoc-mysql-02-pro

- **UUID (Instance):** 501a0713-0459-0a71-9d7c-35db47eb4c0c
- **UUID (BIOS):** 421aa4f2-b22c-a37d-d166-04964d97ac3d
- **Chemin VMX:** `[DS_P_REPLI_02] srv-bdoc-mysql-02-pro/srv-bdoc-mysql-02-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 07:56:13 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-bdoc-mysql-02-pro/srv-bdoc-mysql-02-pro.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] srv-bdoc-mysql-02-pro/srv-bdoc-mysql-02-pro_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:35:c3` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.220.91 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:35c3 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_prod_worker01

- **UUID (Instance):** 501a80bf-4db8-3eb7-9153-c813047f96a9
- **UUID (BIOS):** 421aac64-2c11-2f27-cf57-3a776b4005f7
- **Chemin VMX:** `[DS_P_05] k8s_prod_worker01/k8s_prod_worker01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-25 14:04:01 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_05 | `[DS_P_05] k8s_prod_worker01/k8s_prod_worker01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1024.0 | DS_P_05 | `[DS_P_05] k8s_prod_worker01/k8s_prod_worker01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:71:29` | DVPortGroup: dvportgroup-67 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 192.168.1.133 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7129 (Prefix: 64, State: unknown) |

---

### 5.x VM: sage-immo-01

- **UUID (Instance):** 501aa23d-3916-e413-7293-a3e3655fff32
- **UUID (BIOS):** 421a7df8-c74a-98af-5feb-8c2f9d934521
- **Chemin VMX:** `[DS_P_REPLI_14] sage-immo-01/sage-immo-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:36:15 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] sage-immo-01/sage-immo-01_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_P_REPLI_14 | `[DS_P_REPLI_14] sage-immo-01/sage-immo-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:62:54` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | fe80::b349:8efc:5b1:8cee (Prefix: 64, State: unknown), 172.16.210.74 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-jenkins-devops-pro

- **UUID (Instance):** 501a957a-efb9-78a1-610d-4e7b7dfe9a34
- **UUID (BIOS):** 421aa67a-c538-0e4a-33e2-e032cad7281b
- **Chemin VMX:** `[DS_P_REPLI_06] srv-jenkins-devops-pro/srv-jenkins-devops-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-09-14 10:12:12 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 3 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 3000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 170.0 | DS_P_REPLI_06 | `[DS_P_REPLI_06] srv-jenkins-devops-pro/srv-jenkins-devops-pro.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:47:2e` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.250.105 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:472e (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bdoc-mysql-01-pro

- **UUID (Instance):** 501a3015-d862-f82f-9ce4-50811de5ab07
- **UUID (BIOS):** 421a93ec-c82d-1645-633e-09420b93641d
- **Chemin VMX:** `[DS_P_REPLI_03] srv-bdoc-mysql-01-pro/srv-bdoc-mysql-01-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-12-07 04:16:38 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] srv-bdoc-mysql-01-pro/srv-bdoc-mysql-01-pro.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_P_REPLI_03 | `[DS_P_REPLI_03] srv-bdoc-mysql-01-pro/srv-bdoc-mysql-01-pro_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:5F:9A` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: srv-docker-manager-03-pro

- **UUID (Instance):** 501a3811-22dc-c964-5cb1-1c7999ca9f68
- **UUID (BIOS):** 421ae5c0-5d71-e484-ec70-012a3280d7b8
- **Chemin VMX:** `[DS_P_02] srv-docker-manager-03-pro/srv-docker-manager-03-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-07 14:32:31 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 153600 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1536000 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | DS_P_02 | `[DS_P_02] srv-docker-manager-03-pro/srv-docker-manager-03-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ca:97` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | 172.16.210.126 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ca97 (Prefix: 64, State: unknown) |

---

### 5.x VM: Srv-Pki-root-01

- **UUID (Instance):** 501afe5a-f3af-01bc-5a70-3057feb5a980
- **UUID (BIOS):** 421ab80a-b720-1952-028d-dfe89186cae9
- **Chemin VMX:** `[DS_P_REPLI_05] Srv-Pki-root-01/Srv-Pki-root-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] Srv-Pki-root-01/Srv-Pki-root-01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f6:19` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: P00P25

- **UUID (Instance):** 50394967-c816-8592-b2f7-f63ad73a3065
- **UUID (BIOS):** 42390f13-f9b4-16fa-a0c1-51a4d53bac61
- **Chemin VMX:** `[DS_P_REPLI_05] P00P25/P00P25.vmx`
- **OS Invité:** Microsoft Windows 7 (64-bit) (ID: windows7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 11365, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] P00P25/P00P25.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 30.0 | DS_P_REPLI_05 | `[DS_P_REPLI_05] P00P25/P00P25_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:b9:56:46` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: S00I105

- **UUID (Instance):** 501a729c-9751-4e39-2c61-6125c94ea702
- **UUID (BIOS):** 421adcc9-9306-2991-8e0c-7d0f28e15ec4
- **Chemin VMX:** `[DS_P_REPLI_02] S00I105/S00I105.vmx`
- **OS Invité:** Debian GNU/Linux 10 (64-bit) (ID: debian10_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-26 21:53:07 UTC
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 92160 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 921600 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] S00I105/S00I105.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] S00I105/S00I105_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 150.0 | DS_P_REPLI_02 | `[DS_P_REPLI_02] S00I105/S00I105_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:7F:12` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | True | N/A |

---

### 5.x VM: TALEND-JOBSERVEUR-PRO-02

- **UUID (Instance):** 501a3219-7ae2-1916-fcb5-6526e0ba7e8b
- **UUID (BIOS):** 564d14ff-5766-8e53-de19-75e08740bcb5
- **Chemin VMX:** `[DS_P_REPLI_07] TALEND-JOBSERVEUR-PRO-02/TALEND-JOBSERVEUR-PRO-02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-p-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 90.0 | DS_P_REPLI_07 | `[DS_P_REPLI_07] TALEND-JOBSERVEUR-PRO-02/TALEND-JOBSERVEUR-PRO-02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:9E:F9` | DVPortGroup: dvportgroup-68 (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: srv-bigmaxmongo-pp1

- **UUID (Instance):** 501a5d8e-382f-f881-3a37-7812e02257e1
- **UUID (BIOS):** 421a220b-6cb7-bdc0-2923-46a36089f3a9
- **Chemin VMX:** `[DS_PP_REPLI_03] srv-bigmaxmongo-pp1/srv-bigmaxmongo-pp1.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:42:28 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-bigmaxmongo-pp1/srv-bigmaxmongo-pp1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:92:97` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.75 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:9297 (Prefix: 64, State: unknown) |

---

### 5.x VM: SRV-DSM-02

- **UUID (Instance):** 501a0e5e-963c-a82a-f229-0af387edcb82
- **UUID (BIOS):** 421ab694-5b7f-cac7-42f4-d48d740adec3
- **Chemin VMX:** `[DS_PP_REPLI_04] SRV-DSM-02/SRV-DSM-02.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] SRV-DSM-02/SRV-DSM-02_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 300.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] SRV-DSM-02/SRV-DSM-02_5.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:95:db` | DVPortGroup: N/A (DVS: 50 1a b2 df 2d 0b bb 31-a6 27 3a 08 2e 4a c3 86) | False | N/A |

---

### 5.x VM: BdocAgent-pre-2

- **UUID (Instance):** 501af705-3bdd-c69c-0b71-656d21845a67
- **UUID (BIOS):** 421a5621-a74a-87b0-64ed-d26d86a04c42
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocAgent-pre-2/BdocAgent-pre-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 12:25:10 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocAgent-pre-2/BdocAgent-pre-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocAgent-pre-2/BdocAgent-pre-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:db:8f` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::5786:20f9:3f1e:9e42 (Prefix: 64, State: unknown), 172.16.250.192 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s_preprod_worker03

- **UUID (Instance):** 501a5559-a7b7-56ff-86c5-c4f98b21f1b8
- **UUID (BIOS):** 564da37a-8b8d-a923-3aef-06736af3759b
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker03/k8s_preprod_worker03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-11 13:11:20 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker03/k8s_preprod_worker03.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker03/k8s_preprod_worker03_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:79:54` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.125 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7954 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker01

- **UUID (Instance):** 501a3cb0-de28-4c57-0df1-ad84ae2e9dc9
- **UUID (BIOS):** 564dce9f-7e36-9b57-0b24-e8b338ee63d9
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker01/k8s_preprod_worker01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:28:48 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker01/k8s_preprod_worker01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker01/k8s_preprod_worker01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:33:53` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.123 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:3353 (Prefix: 64, State: unknown) |

---

### 5.x VM: dwh-pbi-pp

- **UUID (Instance):** 501ae7cd-fc8c-c196-e688-e8b68c049d94
- **UUID (BIOS):** 421a9054-b955-1580-8e88-aebc86a697d5
- **Chemin VMX:** `[DS_PP_REPLI_01] dwh-pbi-pp/dwh-pbi-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:05:40 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] dwh-pbi-pp/dwh-pbi-pp_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] dwh-pbi-pp/dwh-pbi-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:80:b4` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::77d3:4d68:f98a:df76 (Prefix: 64, State: unknown), 172.16.250.181 (Prefix: 24, State: preferred) |

---

### 5.x VM: cegid-web-pp

- **UUID (Instance):** 501a9b0a-d06e-e9ca-298f-7d44b136905d
- **UUID (BIOS):** 421ae232-3aab-ba7d-b4a1-3ab8c3bd36f8
- **Chemin VMX:** `[DS_PP_REPLI_07] cegid-web-pp/cegid-web-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:20:24 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] cegid-web-pp/cegid-web-pp_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] cegid-web-pp/cegid-web-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:8b:95` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::321c:58c6:6c17:853b (Prefix: 64, State: unknown), 172.16.250.216 (Prefix: 24, State: preferred) |

---

### 5.x VM: BdocCore-pre-2

- **UUID (Instance):** 501aaf04-4977-ee90-d61f-b38b2921c2f2
- **UUID (BIOS):** 421a744c-bd86-5ac3-5ae4-ffa2c9502dfc
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocCore-pre-2/BdocCore-pre-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 12:25:24 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocCore-pre-2/BdocCore-pre-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocCore-pre-2/BdocCore-pre-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:d8:cd` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::aa2b:2dfd:4105:f6be (Prefix: 64, State: unknown), 172.16.250.190 (Prefix: 16, State: preferred) |

---

### 5.x VM: S00I202PP (JBOSS EAP 5.2 V3 PREPROD)

- **UUID (Instance):** 501ac143-2d1a-abc0-0567-fff9b1d59161
- **UUID (BIOS):** 564d33cc-95ea-9cde-b8c3-f28cddf7170b
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I202PP (JBOSS EAP 5.2 V3 PREPROD)/S00I202PP (JBOSS EAP 5.2 V3 PREPROD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:27 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I202PP (JBOSS EAP 5.2 V3 PREPROD)/S00I202PP (JBOSS EAP 5.2 V3 PREPROD).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I202PP (JBOSS EAP 5.2 V3 PREPROD)/S00I202PP (JBOSS EAP 5.2 V3 PREPROD)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:91:17` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.33 (Prefix: 24, State: preferred), 192.168.2.34 (Prefix: 32, State: preferred), 192.168.2.35 (Prefix: 32, State: preferred), fe80::250:56ff:fe9a:9117 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I203PP (JBOSS EAP 5.2 V3 PREPROD)

- **UUID (Instance):** 501a5393-8888-8a9c-9a13-bb76e03650e1
- **UUID (BIOS):** 421a6c88-c014-ffc3-69d4-8ba4a7152062
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I203PP (JBOSS EAP 5.2 V3 PREPROD)/S00I203PP (JBOSS EAP 5.2 V3 PREPROD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:30 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I203PP (JBOSS EAP 5.2 V3 PREPROD)/S00I203PP (JBOSS EAP 5.2 V3 PREPROD).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I203PP (JBOSS EAP 5.2 V3 PREPROD)/S00I203PP (JBOSS EAP 5.2 V3 PREPROD)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:D3:73` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: S00I402PP (JBOSS EAP 7 V4 PREPROD)

- **UUID (Instance):** 501abf82-4651-5e3a-28ad-07d263ae6850
- **UUID (BIOS):** 564ddfc8-3eaa-5c07-85bd-ed503681b870
- **Chemin VMX:** `[DS_PP_REPLI_11] S00I402PP (JBOSS EAP 7 V4 PREPROD)/S00I402PP (JBOSS EAP 7 V4 PREPROD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:30 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 10240 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 102400 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I402PP (JBOSS EAP 7 V4 PREPROD)/S00I402PP (JBOSS EAP 7 V4 PREPROD).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:26:63:83` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.73 (Prefix: 24, State: preferred), 192.168.2.74 (Prefix: 32, State: preferred), 192.168.2.75 (Prefix: 32, State: preferred), fe80::250:56ff:fe26:6383 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-mongo-01-pp

- **UUID (Instance):** 501a47cc-58b2-6ef8-a754-b78436ef6240
- **UUID (BIOS):** 421a8a68-0140-8a6d-38b6-26dd9a4a5fdf
- **Chemin VMX:** `[DS_PP_REPLI_06] srv-mongo-01-pp/srv-mongo-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-17 13:56:51 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 75.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] srv-mongo-01-pp/srv-mongo-01-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1d:67` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.100 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1d67 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-talend-tac-02-pp

- **UUID (Instance):** 501a2077-34e7-bbf6-a874-17c6ff2cb3bc
- **UUID (BIOS):** 421a9781-14f5-caa4-61e2-5ae4b97467d6
- **Chemin VMX:** `[DS_PP_REPLI_05] srv-talend-tac-02-pp/srv-talend-tac-02-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-25 06:17:17 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_05 | `[DS_PP_REPLI_05] srv-talend-tac-02-pp/srv-talend-tac-02-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:21:f1` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.209 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:21f1 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-worker01

- **UUID (Instance):** 501aaf89-2aae-196b-5091-6e2b26ea3da2
- **UUID (BIOS):** 421a00ad-aacc-0828-cfcb-ea81b5cad5d4
- **Chemin VMX:** `[DS_PP_REPLI_03] k8s-rke2-preprod-worker01/k8s-rke2-preprod-worker01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:18:17 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] k8s-rke2-preprod-worker01/k8s-rke2-preprod-worker01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:35:b4` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.123 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:35b4 (Prefix: 64, State: unknown) |

---

### 5.x VM: s00I239PP( ancien SRV-RPTRT-PP)

- **UUID (Instance):** 501a3d20-5644-b3d9-e356-323f503e4102
- **UUID (BIOS):** 421aa05f-4930-c4ae-7878-3cb453e8bf0f
- **Chemin VMX:** `[DS_PP_REPLI_11] SRV-RPTRT-PP/SRV-RPTRT-PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:37:13 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-RPTRT-PP/SRV-RPTRT-PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-RPTRT-PP/SRV-RPTRT-PP_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:3b:0e` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::25c1:37ae:72bc:b12 (Prefix: 64, State: unknown), 172.16.210.206 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-mongo-pp (200)

- **UUID (Instance):** 501ad350-64c8-f14a-96fb-24a1d8ce7c94
- **UUID (BIOS):** 421ac9ec-12af-0a18-641d-5574f747b063
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-mongo-pp (200)/srv-mongo-pp (200).vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:19:45 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-mongo-pp (200)/srv-mongo-pp (200).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f0:09` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.94 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f009 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-mssql19-pp

- **UUID (Instance):** 501a9da2-b624-687f-791a-50559d565269
- **UUID (BIOS):** 421a13db-7cc9-92b9-0eb2-1ea7d029cfd6
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-mssql19-pp/srv-mssql19-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:55:57 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-mssql19-pp/srv-mssql19-pp.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-mssql19-pp/srv-mssql19-pp_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:4f:64` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::bcae:d687:4485:f8eb (Prefix: 64, State: unknown), 172.16.250.158 (Prefix: 24, State: preferred) |

---

### 5.x VM: SRV-RPSRV-PP

- **UUID (Instance):** 501af560-c9a0-dbd5-3ae4-12f62fa4e504
- **UUID (BIOS):** 421a832e-6043-bca5-9e86-1fe2396d088a
- **Chemin VMX:** `[DS_PP_REPLI_11] SRV-RPSRV-PP/SRV-RPSRV-PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:37:35 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-RPSRV-PP/SRV-RPSRV-PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-RPSRV-PP/SRV-RPSRV-PP_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1f:8a` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::3b2f:1282:7215:d37b (Prefix: 64, State: unknown), 172.16.210.205 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-metier-int1

- **UUID (Instance):** 501ad535-6cf1-515e-47ae-7636df119775
- **UUID (BIOS):** 421aabcd-1857-06a9-8b4e-2edd93e20f66
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-metier-int1/srv-metier-int1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-metier-int1/srv-metier-int1-000001.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-metier-int1/srv-metier-int1_1-000001.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:58:a9` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I80I(EAD ExportImport)

- **UUID (Instance):** 50264273-c961-d11f-5104-3428679172cd
- **UUID (BIOS):** 564dbe64-49d4-a54a-216e-34b9127c0b5d
- **Chemin VMX:** `[DS_PP_REPLI_03] S00I80I(EAD ExportImport)/S00I80I(EAD ExportImport).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10252, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] S00I80I(EAD ExportImport)/S00I80I(EAD ExportImport).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:a6:7a:3e` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: PSQL_ODS_PP

- **UUID (Instance):** 501a2c2c-67e9-6d10-cd8f-baa0aecd5276
- **UUID (BIOS):** 421a2d38-754e-c9f2-d5d9-40f0065ad71a
- **Chemin VMX:** `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-07 12:40:17 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 4 (2003) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 5 (2004) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_4.vmdk` | persistent | False | -1 IOPS |
| Hard disk 6 (2005) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_5.vmdk` | persistent | False | -1 IOPS |
| Hard disk 7 (2006) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_6.vmdk` | persistent | False | -1 IOPS |
| Hard disk 8 (2008) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_7.vmdk` | persistent | False | -1 IOPS |
| Hard disk 9 (2009) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_8.vmdk` | persistent | False | -1 IOPS |
| Hard disk 10 (2010) | 120.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_9.vmdk` | persistent | False | -1 IOPS |
| Hard disk 11 (2011) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_10.vmdk` | persistent | False | -1 IOPS |
| Hard disk 12 (2012) | 500.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_11.vmdk` | persistent | False | -1 IOPS |
| Hard disk 13 (2013) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_ODS_PP/PSQL_ODS_PP_12.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:A1:2C` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: dwh-ssas-pp

- **UUID (Instance):** 501aff60-2e16-ac16-c343-5c454b91815a
- **UUID (BIOS):** 421a38b2-9e2a-a7ba-e1ab-f13e41bbcc5c
- **Chemin VMX:** `[DS_PP_REPLI_04] dwh-ssas-pp/dwh-ssas-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:56:56 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 98304 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 983040 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] dwh-ssas-pp/dwh-ssas-pp_3.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 150.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] dwh-ssas-pp/dwh-ssas-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:02:c0` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::5b3:e814:ac10:8a36 (Prefix: 64, State: unknown), 172.16.250.176 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s_preprod_worker11

- **UUID (Instance):** 501add8e-8c88-bd90-9355-e7a2e4e10d54
- **UUID (BIOS):** 421aaa6b-98ed-fffc-db9c-fe4513e5034e
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker11/k8s_preprod_worker11.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:28:36 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker11/k8s_preprod_worker11.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ff:7e` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.133 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ff7e (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker12

- **UUID (Instance):** 501a4d84-bfb5-90d9-52c0-f6c174a77831
- **UUID (BIOS):** 564da877-5fa2-7d89-d119-13ea9bacef1c
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker12/k8s_preprod_worker12.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-04 15:09:51 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker12/k8s_preprod_worker12.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:9c:06` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.134 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:9c06 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I130D(SMTB)

- **UUID (Instance):** 501bdda7-11ff-0d5e-30d2-0e578709f726
- **UUID (BIOS):** 421b3317-11ed-7632-5fb8-a48ef38b82e9
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I130D(SMTB)/S00I130D(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 9356, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I130D(SMTB)/S00I130D(SMTB).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9b:00:2b` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: srv-dns-externe-rec

- **UUID (Instance):** 501ab711-96c0-6f27-946d-05d4531426bf
- **UUID (BIOS):** 421a7b65-dc38-3ace-2af0-b99e6b9fd19d
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-dns-externe-rec/srv-dns-externe-rec.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-dns-externe-rec/srv-dns-externe-rec.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f0:31` | DVPortGroup: dvportgroup-71 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I48I(LACOUR)

- **UUID (Instance):** 5026e8ad-50e6-5071-0488-93ec2d15f7e5
- **UUID (BIOS):** 564debcf-12a4-362b-183c-7145c82cc129
- **Chemin VMX:** `[DS_PP_REPLI_07] S00I48I(LACOUR)/S00I48I(LACOUR).vmx`
- **OS Invité:** Microsoft Windows Server 2008 R2 (64-bit) (ID: windows7Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 140.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] S00I48I(LACOUR)/S00I48I(LACOUR).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:a6:69:e7` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I80Q(EAD Import Export)

- **UUID (Instance):** 501b55f6-356a-0e7c-2546-9e60f699ec36
- **UUID (BIOS):** 421b96fc-f518-4ac6-c60e-7c34f3f9a7bb
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I80Q(EAD Import Export)/S00I80Q(EAD Import Export).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10252, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I80Q(EAD Import Export)/S00I80Q(EAD Import Export).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9b:00:18` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: TALEND-JOBSERVEUR-PP-02

- **UUID (Instance):** 501a9b93-7956-5d2a-a5e1-84c67dfca5d1
- **UUID (BIOS):** 564dd629-4e60-3059-2b1a-b63d6dbb3024
- **Chemin VMX:** `[DS_PP_REPLI_02] TALEND-JOBSERVEUR-PP-02_AVTPATCH/TALEND-JOBSERVEUR-PP-02_AVTPATCH.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 90.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] TALEND-JOBSERVEUR-PP-02_AVTPATCH/TALEND-JOBSERVEUR-PP-02_AVTPATCH.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:41:76` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: srv-docker-worker-01-pp

- **UUID (Instance):** 501a0663-e09a-326b-5a75-ac3649078c1e
- **UUID (BIOS):** 421a4c94-ce16-8c1c-ae8f-4c26f87f63fe
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-docker-worker-01-pp/srv-docker-worker-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-08 14:43:09 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 122880 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1228800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-docker-worker-01-pp/srv-docker-worker-01-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:71:bf` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.46 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:71bf (Prefix: 64, State: unknown) |

---

### 5.x VM: TALEND-JOBSERVEUR-PP-01

- **UUID (Instance):** 501a1436-9cfb-c81e-12fd-bcacf5c09107
- **UUID (BIOS):** 421a42e5-c4b9-2c84-eb9e-c5bfc3e480fc
- **Chemin VMX:** `[DS_PP_REPLI_02] TALEND-JOBSERVER-PP-01_AVTPATCH/TALEND-JOBSERVER-PP-01_AVTPATCH.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 90.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] TALEND-JOBSERVER-PP-01_AVTPATCH/TALEND-JOBSERVER-PP-01_AVTPATCH.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:15:a8` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I82R(EAD Import Export)

- **UUID (Instance):** 50260548-14d8-f2ea-c6e0-17d45f136488
- **UUID (BIOS):** 564d342e-4e0c-aefd-fc29-f46ee09ceade
- **Chemin VMX:** `[DS_PP_REPLI_04] S00I82R(EAD Import Export)/S00I82R(EAD Import Export).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10252, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I82R(EAD Import Export)/S00I82R(EAD Import Export).vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:a6:24:5b` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: TALEND-TAC-PP-02

- **UUID (Instance):** 501ad2f6-d6f0-4d49-08dc-b02d66f614fe
- **UUID (BIOS):** 421a44b9-985c-098f-f89c-d6f60885d977
- **Chemin VMX:** `[DS_PP_REPLI_11] TALEND-TAC-PP-02/TALEND-TAC-PP-02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] TALEND-TAC-PP-02/TALEND-TAC-PP-02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:9c:b2` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I25PP

- **UUID (Instance):** 501a5f40-1592-3a2b-8a6a-21faedc97e05
- **UUID (BIOS):** 564dad05-4908-1a15-88f5-87af3943c885
- **Chemin VMX:** `[DS_PP_REPLI_11] S00I25PP/S00I25PP.vmx`
- **OS Invité:** Red Hat Enterprise Linux 5 (64-bit) (ID: rhel5_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10358, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:25:03 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I25PP/S00I25PP.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 15.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I25PP/S00I25PP_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:4F:EE` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: srv-vaultwarden-pp

- **UUID (Instance):** 501a1f7e-e1d5-7f51-ca65-b07b92c50b76
- **UUID (BIOS):** 421a6c6e-9a2d-dcea-7125-64318ef2bedf
- **Chemin VMX:** `[NFS_PP_01] srv-vaultwarden-pp/srv-vaultwarden-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12421, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | NFS_PP_01 | `[NFS_PP_01] srv-vaultwarden-pp/srv-vaultwarden-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:96:c1` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I86-Dev

- **UUID (Instance):** 5039ddd7-10e7-9c80-3400-c6cc236eff04
- **UUID (BIOS):** 4239984c-c8cf-aa8f-2ef1-3d1f3c58d329
- **Chemin VMX:** `[DS_PP_REPLI_07] S00I86-Dev/S00I86-Dev.vmx`
- **OS Invité:** Red Hat Enterprise Linux 4 (32-bit) (ID: rhel4Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 9356, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] S00I86-Dev/S00I86-Dev.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:b9:52:d6` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: vCLS-d37360c3-d31c-473a-b708-4bfa40d56083

- **UUID (Instance):** 501a5025-230c-4cbb-f5ac-2a017cfb6ca4
- **UUID (BIOS):** 421a74cf-8aa4-c3ad-a28e-dec292c62aff
- **Chemin VMX:** `[NFS_PP_01] vCLS-d37360c3-d31c-473a-b708-4bfa40d56083/vCLS-d37360c3-d31c-473a-b708-4bfa40d56083.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-06 12:28:26 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | NFS_PP_01 | `[NFS_PP_01] vCLS-d37360c3-d31c-473a-b708-4bfa40d56083/vCLS-d37360c3-d31c-473a-b708-4bfa40d56083.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: TALEND-TAC-PP-01

- **UUID (Instance):** 501afbf4-544c-842b-8d16-9a66c8de923c
- **UUID (BIOS):** 564d4269-0973-2038-bd2f-720ea4b8d375
- **Chemin VMX:** `[DS_PP_REPLI_10] TALEND-TAC-PP-01-BCK/TALEND-TAC-PP-01-BCK.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_10 | `[DS_PP_REPLI_10] TALEND-TAC-PP-01-BCK/TALEND-TAC-PP-01-BCK.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:6c:87` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I194V (Nouveau SVN JIRA 6.3.13)

- **UUID (Instance):** 5026d621-56bd-c692-7f33-c56da5fc7b8f
- **UUID (BIOS):** 564d573d-b03e-a52c-7eaf-c7b621824bfc
- **Chemin VMX:** `[DS_PP_REPLI_03] S00I194V (Nouveau SVN %2fJIRA 6.3.13)/S00I194V (Nouveau SVN %2fJIRA 6.3.13).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] S00I194V (Nouveau SVN %2fJIRA 6.3.13)/S00I194V (Nouveau SVN %2fJIRA 6.3.13).vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] S00I194V (Nouveau SVN %2fJIRA 6.3.13)/S00I194V (Nouveau SVN %2fJIRA 6.3.13)_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 60.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] S00I194V (Nouveau SVN %2fJIRA 6.3.13)/S00I194V (Nouveau SVN %2fJIRA 6.3.13)_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:a6:42:03` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: srv-ise-nac-eval

- **UUID (Instance):** 501a4928-89bf-eff4-0790-18ac850e2a54
- **UUID (BIOS):** 421aa790-5e6b-a640-e5d1-309471fb4c33
- **Chemin VMX:** `[NFS_PP_01] srv-ise-nac-eval/srv-ise-nac-eval.vmx`
- **OS Invité:** Red Hat Enterprise Linux 8 (64-bit) (ID: rhel8_64Guest)
- **Version VM:** vmx-14
- **VMware Tools:** toolsNotRunning (Version: 11328, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 300.0 | NFS_PP_01 | `[NFS_PP_01] srv-ise-nac-eval/srv-ise-nac-eval.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:87:fe` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |
| Network adapter 2 (4001) | vim.vm.device.VirtualE1000e | `00:50:56:9a:af:bc` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |
| Network adapter 3 (4002) | vim.vm.device.VirtualE1000e | `00:50:56:9a:29:7f` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |
| Network adapter 4 (4003) | vim.vm.device.VirtualE1000e | `00:50:56:9a:b1:e1` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |
| Network adapter 5 (4004) | vim.vm.device.VirtualE1000e | `00:50:56:9a:d8:37` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |
| Network adapter 6 (4005) | vim.vm.device.VirtualE1000e | `00:50:56:9a:fa:28` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: dwh-sql-dev

- **UUID (Instance):** 501a2706-b099-41fb-6509-1e3c91801945
- **UUID (BIOS):** 421a4948-08a8-33e5-ae90-f020272506a0
- **Chemin VMX:** `[DS_PP_REPLI_06] dwh-sql-dev-1/dwh-sql-dev-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] dwh-sql-dev-1/dwh-sql-dev-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1433.6 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] dwh-sql-dev-1/dwh-sql-dev-1_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:35:09` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: cegid-app-dev

- **UUID (Instance):** 501a5aa6-6de1-dd3c-ba26-50c16f19a671
- **UUID (BIOS):** 421a8851-b6d2-e47f-83ef-05b4af58ea95
- **Chemin VMX:** `[DS_PP_REPLI_06] cegid-app-dev/cegid-app-dev.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] cegid-app-dev/cegid-app-dev_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] cegid-app-dev/cegid-app-dev.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:ae:86` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I207R(Talend 7.2.1 NSI REC)

- **UUID (Instance):** 501a6519-5489-fa7f-c3c3-d1e7f9814cf4
- **UUID (BIOS):** 421a0abe-f692-71f9-c5c0-5e53991124e4
- **Chemin VMX:** `[DS_PP_REPLI_10] S00I207R(Talend 7.2.1 NSI REC)/S00I207R(Talend 7.2.1 NSI REC).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_PP_REPLI_10 | `[DS_PP_REPLI_10] S00I207R(Talend 7.2.1 NSI REC)/S00I207R(Talend 7.2.1 NSI REC).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 20.0 | DS_PP_REPLI_10 | `[DS_PP_REPLI_10] S00I207R(Talend 7.2.1 NSI REC)/S00I207R(Talend 7.2.1 NSI REC)_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 50.0 | DS_PP_REPLI_10 | `[DS_PP_REPLI_10] S00I207R(Talend 7.2.1 NSI REC)/S00I207R(Talend 7.2.1 NSI REC)_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:9F:0B` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: cegid-bdd-pp

- **UUID (Instance):** 501a742c-fc12-b931-bea1-9cdb775d284b
- **UUID (BIOS):** 421acd15-6e06-5280-1608-b52786d8fc6f
- **Chemin VMX:** `[DS_PP_REPLI_11] cegid-bdd-pp-2/cegid-bdd-pp-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:58:45 UTC
- **Hôte Actuel:** vm-esx-pp-02.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 4)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-pp-2/cegid-bdd-pp-2_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 210.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-pp-2/cegid-bdd-pp-2.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2003) | 70.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-pp-2/cegid-bdd-pp-2_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:cc:4a` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::930f:6441:ff31:e7f6 (Prefix: 64, State: unknown), 172.16.250.214 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdocmongo-ppa

- **UUID (Instance):** 501a1602-8a5f-10d2-8318-50158207dcb3
- **UUID (BIOS):** 421a3c24-cb5f-5605-d290-d27eabe502e7
- **Chemin VMX:** `[DS_PP_REPLI_07] srv-bdocmongo-ppa/srv-bdocmongo-ppa.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:07:53 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] srv-bdocmongo-ppa/srv-bdocmongo-ppa.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:54:4e` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.90 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:544e (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I608PP

- **UUID (Instance):** 501ae5e6-9b26-b1fd-8f70-5189f3080f36
- **UUID (BIOS):** 421a606e-17e9-91d1-855e-44359be343a6
- **Chemin VMX:** `[DS_PP_REPLI_11] S00I608PP/S00I608PP.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-18 21:32:46 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I608PP/S00I608PP_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ed:18` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.171 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ed18 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I131R(SMTB)

- **UUID (Instance):** 501b07c7-e553-e563-315c-9ccdecbc720e
- **UUID (BIOS):** 421b16cf-b4aa-b9f4-e5f3-4b8f214ad1f3
- **Chemin VMX:** `[DS_PP_REPLI_06] S00I131R(SMTB)/S00I131R(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10252, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-11 16:00:36 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] S00I131R(SMTB)/S00I131R(SMTB).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9b:00:50` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.156 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdocmongo-pp1

- **UUID (Instance):** 501a8a8b-0182-4a28-2c98-2d125739dc17
- **UUID (BIOS):** 421aa634-8ed8-824c-cb48-005251383f6e
- **Chemin VMX:** `[DS_PP_REPLI_07] srv-bdocmongo-pp1/srv-bdocmongo-pp1.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:32:43 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] srv-bdocmongo-pp1/srv-bdocmongo-pp1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:47:e5` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.88 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:47e5 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bigmaxmongo-pp2

- **UUID (Instance):** 501a4c86-521b-4b45-7153-e27aa444fcd2
- **UUID (BIOS):** 421af06a-01ce-5a14-1a9f-154eb9a44acc
- **Chemin VMX:** `[DS_PP_REPLI_08] srv-bigmaxmongo-pp2/srv-bigmaxmongo-pp2.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:37:30 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] srv-bigmaxmongo-pp2/srv-bigmaxmongo-pp2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:37:a7` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.76 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:37a7 (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocWeb-pre-1

- **UUID (Instance):** 501acf69-68a4-4a96-c317-332ac310bc9c
- **UUID (BIOS):** 564d63f4-4d1c-1568-bf75-587b0c42fbb7
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocWeb-pre-1/BdocWeb-pre-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:52:10 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocWeb-pre-1/BdocWeb-pre-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocWeb-pre-1/BdocWeb-pre-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:92:36` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::f0b7:7f4a:ac27:8cca (Prefix: 64, State: unknown), 172.16.250.187 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I131I

- **UUID (Instance):** 501eb255-335f-a386-6a90-8089d707231a
- **UUID (BIOS):** 421e0c88-dc17-b9f3-2bd6-970c6becbdcc
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I131I/S00I131I.vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10252, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-11 13:24:15 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I131I/S00I131I-000001.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9E:17:3A` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: BdocWeb-pre-2

- **UUID (Instance):** 501afcc5-93e3-ecdf-b417-2516d5fc897f
- **UUID (BIOS):** 564d8064-a657-70f7-abb6-89e71fad3554
- **Chemin VMX:** `[DS_PP_REPLI_08] BdocWeb-pre-2/BdocWeb-pre-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:48:01 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] BdocWeb-pre-2/BdocWeb-pre-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] BdocWeb-pre-2/BdocWeb-pre-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:58:80` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::113c:e844:82a1:92f (Prefix: 64, State: unknown), 172.16.250.188 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I97PP

- **UUID (Instance):** 501a1f38-662c-12bb-5b3a-c8489a3fa278
- **UUID (BIOS):** 421a823e-1a1a-9ed2-4c38-b95bd91a2dc3
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I97PP/S00I97PP.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-08
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 16:31:24 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I97PP/S00I97PP.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:60:b5` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.58 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:60b5 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-postfix-pp

- **UUID (Instance):** 501af8cf-f706-6c90-cc1b-67310c428237
- **UUID (BIOS):** 421a9f80-ccb9-83a9-7acc-fa23c6caadc7
- **Chemin VMX:** `[DS_PP_REPLI_05] srv-postfix-pp/srv-postfix-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:19:30 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_05 | `[DS_PP_REPLI_05] srv-postfix-pp/srv-postfix-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:4f:0e` | DVPortGroup: dvportgroup-71 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.1.42 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:4f0e (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocInter-pre-2

- **UUID (Instance):** 501a231c-53dd-ec14-9da4-ed314bc00e42
- **UUID (BIOS):** 421a0226-f2af-ee43-9cc8-09f7d4aa59d3
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocInter-pre-2/BdocInter-pre-2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:51:13 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocInter-pre-2/BdocInter-pre-2.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocInter-pre-2/BdocInter-pre-2_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:6c:b4` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.186 (Prefix: 24, State: preferred) |

---

### 5.x VM: PSQL_BIGMAX_PP

- **UUID (Instance):** 501a9e63-376f-fa9e-883c-98722d07f4fc
- **UUID (BIOS):** 421a4b4c-130a-2928-724f-42859e193b5e
- **Chemin VMX:** `[DS_PP_REPLI_11] PSQL_BIGMAX_PP/PSQL_BIGMAX_PP.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:34 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_BIGMAX_PP/PSQL_BIGMAX_PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_BIGMAX_PP/PSQL_BIGMAX_PP_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] PSQL_BIGMAX_PP/PSQL_BIGMAX_PP_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:A1:8C` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: srv-bdoc-mysql-01-pre

- **UUID (Instance):** 501a1971-3baf-41d9-3081-f41346282cb0
- **UUID (BIOS):** 421af1ea-be11-5ac3-bb9d-6085571ad255
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-bdoc-mysql-01-pre/srv-bdoc-mysql-01-pre.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:07:58 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-bdoc-mysql-01-pre/srv-bdoc-mysql-01-pre.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:07:f2` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.110 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7f2 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I408PP (bcafr-lea-expertise.fr)

- **UUID (Instance):** 501ac391-1d9f-0da9-7679-0323fc06d68f
- **UUID (BIOS):** 564dd23c-dff1-44d8-8071-c20f8372260a
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I408PP (bcafr-lea-expertise.fr)/S00I408PP (bcafr-lea-expertise.fr).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-07 17:14:51 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I408PP (bcafr-lea-expertise.fr)/S00I408PP (bcafr-lea-expertise.fr).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I408PP (bcafr-lea-expertise.fr)/S00I408PP (bcafr-lea-expertise.fr)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:7d:a7` | DVPortGroup: dvportgroup-71 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.1.43 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7da7 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bigmaxmongo-ppa

- **UUID (Instance):** 501ab6c0-7cac-a9cf-9b31-980694314b20
- **UUID (BIOS):** 421ace90-6462-736f-ed96-12de66f00e49
- **Chemin VMX:** `[DS_PP_REPLI_03] srv-bigmaxmongo-ppa/srv-bigmaxmongo-ppa.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:14:35 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-bigmaxmongo-ppa/srv-bigmaxmongo-ppa.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:90:d6` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.78 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:90d6 (Prefix: 64, State: unknown) |

---

### 5.x VM: P00O24

- **UUID (Instance):** 50261692-7913-832a-11e1-45f99d4c076d
- **UUID (BIOS):** 4226268c-b299-6cf8-697a-3129b27cde2e
- **Chemin VMX:** `[DS_PP_REPLI_02] P00O24/P00O24.vmx`
- **OS Invité:** Microsoft Windows XP Professional (32-bit) (ID: winXPProGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10252, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:04:42 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] P00O24/P00O24.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:a6:51:96` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.210.183 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I210P (JON VAL REC)

- **UUID (Instance):** 501edc8f-607e-00a9-fafc-6b85efc5f0c1
- **UUID (BIOS):** 564da3b1-f968-4c33-bfbe-218016258dd1
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I210P (JON VAL REC)/S00I210P (JON VAL REC).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 14:25:45 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I210P (JON VAL REC)/S00I210P (JON VAL REC).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9e:90:8d` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.57 (Prefix: 24, State: preferred), fe80::250:56ff:fe9e:908d (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I230PP

- **UUID (Instance):** 501ae158-7402-d49b-ca3c-851c5d77379f
- **UUID (BIOS):** 421a66af-128b-b672-5b10-b1ec4f87d2c3
- **Chemin VMX:** `[DS_PP_REPLI_04] S00I230PP/S00I230PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:37:17 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I230PP/S00I230PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I230PP/S00I230PP_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:d8:d3` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: S00I93D (SRVPJ-PP+FTP public+DNS)

- **UUID (Instance):** 501b6367-1841-2633-a59d-7c73b11cf837
- **UUID (BIOS):** 421b9174-3103-17dd-daa5-921af2f48bd6
- **Chemin VMX:** `[DS_PP_REPLI_02] S00I93D (SRVPJ-PP+FTP public+DNS)/S00I93D (SRVPJ-PP+FTP public+DNS).vmx`
- **OS Invité:** Red Hat Enterprise Linux 5 (64-bit) (ID: rhel5_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 10358, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-09-13 08:43:44 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 3940 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 39400 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] S00I93D (SRVPJ-PP+FTP public+DNS)/S00I93D (SRVPJ-PP+FTP public+DNS).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:a6:2c:18` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | 172.16.250.134 (Prefix: 16, State: preferred) |

---

### 5.x VM: srv-talend-jobserveur-02-pp

- **UUID (Instance):** 501aa734-d576-309e-03fe-fef997891676
- **UUID (BIOS):** 421a15b4-bb6d-6a2c-f526-dd4fd8aa287e
- **Chemin VMX:** `[DS_PP_REPLI_03] srv-talend-jobserveur-02-pp/srv-talend-jobserveur-02-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-25 06:16:11 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-talend-jobserveur-02-pp/srv-talend-jobserveur-02-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b4:60` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.228 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:b460 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-manager-02-pp

- **UUID (Instance):** 501a2ad4-8b67-5840-2b8f-9276815af5bb
- **UUID (BIOS):** 421a3130-60f7-be1f-4a2d-7b9a8a4ac3c3
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-docker-manager-02-pp/srv-docker-manager-02-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-08 14:43:22 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 122880 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1228800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-docker-manager-02-pp/srv-docker-manager-02-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:b2:97` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.44 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:b297 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-worker05

- **UUID (Instance):** 501a5971-be47-b5b9-2802-54a1138abcf9
- **UUID (BIOS):** 421a082a-89bb-41a7-c096-ab02bdce9b8e
- **Chemin VMX:** `[DS_PP_REPLI_01] k8s-rke2-preprod-worker05/k8s-rke2-preprod-worker05.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:19:28 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] k8s-rke2-preprod-worker05/k8s-rke2-preprod-worker05.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:55:85` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.127 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:5585 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-worker03

- **UUID (Instance):** 501af348-dc87-6f9c-a49d-640f5f1f4c46
- **UUID (BIOS):** 421a3ba6-6684-2673-1ca2-e6b427b61148
- **Chemin VMX:** `[DS_PP_REPLI_05] k8s-rke2-preprod-worker03/k8s-rke2-preprod-worker03.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:20:35 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_05 | `[DS_PP_REPLI_05] k8s-rke2-preprod-worker03/k8s-rke2-preprod-worker03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1b:cc` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.125 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1bcc (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker07

- **UUID (Instance):** 501ae9bb-2a90-30c5-e30b-e177ca67802f
- **UUID (BIOS):** 564d829a-3cfc-2aa5-0e0e-9f61b0a7b1ea
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker07/k8s_preprod_worker07.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:26 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker07/k8s_preprod_worker07.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:37:c9` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.129 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:37c9 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I196PP(BCAPRO_PP et BCASIV_PP ASE157)

- **UUID (Instance):** 501a8393-5eca-8553-d831-9a372f28650a
- **UUID (BIOS):** 421acdf2-a60e-c3e4-b39c-a9b83dd2760f
- **Chemin VMX:** `[DS_PP_REPLI_04] S00I196PP_ASE157/S00I196PP_ASE157.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-08
- **VMware Tools:** toolsOld (Version: 10360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-06-24 07:31:48 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 18 (Cœurs/Socket: 1)
- **RAM:** 65536 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 18000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 655360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I196PP_ASE157/S00I196PP_ASE157.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 70.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I196PP_ASE157/S00I196PP_ASE157_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 740.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I196PP_ASE157/S00I196PP_ASE157_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:05:db` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.67 (Prefix: 16, State: preferred), fe80::250:56ff:fe9a:5db (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I140PP

- **UUID (Instance):** 501a4033-781a-ffb9-c84f-ba9052233437
- **UUID (BIOS):** 421abffc-ec07-4aeb-885b-1e74935c5208
- **Chemin VMX:** `[DS_PP_REPLI_07] S00I140PP/S00I140PP.vmx`
- **OS Invité:** Red Hat Enterprise Linux 7 (64-bit) (ID: rhel7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11269, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-08 16:04:20 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 51.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] S00I140PP/S00I140PP.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:03:29` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: HPE-CloudPhysics

- **UUID (Instance):** 501ad947-0572-9dd7-40ab-fc63e9b399b4
- **UUID (BIOS):** 421aa8a6-3192-6d3b-278b-b8c5fd17621d
- **Chemin VMX:** `[DS_PP_REPLI_11] HPE-CloudPhysics/HPE-CloudPhysics.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-07
- **VMware Tools:** toolsNotRunning (Version: 2147483647, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 4.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] HPE-CloudPhysics/HPE-CloudPhysics.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 8.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] HPE-CloudPhysics/HPE-CloudPhysics_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:43:a5` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: k8s_preprod_worker04

- **UUID (Instance):** 501a3c5e-0efc-7ac4-0d3d-76ffd0135a2f
- **UUID (BIOS):** 421a6a02-6997-ad03-8d20-4481e93d9334
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker04/k8s_preprod_worker04.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:21:36 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker04/k8s_preprod_worker04.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:71:97` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.126 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7197 (Prefix: 64, State: unknown) |

---

### 5.x VM: vCLS-38039e46-6500-4cb8-8403-1c473c80e0da

- **UUID (Instance):** 501ab91e-b3d5-4d6d-e955-81b3f113e4d2
- **UUID (BIOS):** 421a704c-d83a-dad6-a9dd-73610da4ec5b
- **Chemin VMX:** `[NFS_PP_01] vCLS-38039e46-6500-4cb8-8403-1c473c80e0da/vCLS-38039e46-6500-4cb8-8403-1c473c80e0da.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-06 12:28:27 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | NFS_PP_01 | `[NFS_PP_01] vCLS-38039e46-6500-4cb8-8403-1c473c80e0da/vCLS-38039e46-6500-4cb8-8403-1c473c80e0da.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: srv-docker-manager-03-pp

- **UUID (Instance):** 501a628c-92f6-85c0-fbc9-8bd66898b406
- **UUID (BIOS):** 421a7e40-5754-d0a6-e594-36c2b60a3587
- **Chemin VMX:** `[DS_PP_REPLI_11] srv-docker-manager-03-pp/srv-docker-manager-03-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-08 14:43:21 UTC
- **Hôte Actuel:** vm-esx-pp-04.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 122880 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1228800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] srv-docker-manager-03-pp/srv-docker-manager-03-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:d4:00` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.45 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:d400 (Prefix: 64, State: unknown) |

---

### 5.x VM: dwh-sql-pp

- **UUID (Instance):** 501ade54-effe-d4b7-e165-fdba0e1c0eec
- **UUID (BIOS):** 421abc2f-053d-e29b-c8f9-cad01259b3c1
- **Chemin VMX:** `[DS_PP_REPLI_09] dwh-sql-pp/dwh-sql-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:58:25 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 131072 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1310720 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] dwh-sql-pp/dwh-sql-pp.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2003) | 1536.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] dwh-sql-pp/dwh-sql-pp_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:5b:c1` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::7497:7489:22d4:f105 (Prefix: 64, State: unknown), 172.16.250.225 (Prefix: 24, State: preferred) |

---

### 5.x VM: k8s-rke2-preprod-worker07

- **UUID (Instance):** 501a9476-78ef-19ba-81b4-1e96193197be
- **UUID (BIOS):** 421a9682-21d9-3da1-1eb0-5e35cdcf7c2b
- **Chemin VMX:** `[DS_PP_REPLI_01] k8s-rke2-preprod-worker07/k8s-rke2-preprod-worker07.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:15:38 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] k8s-rke2-preprod-worker07/k8s-rke2-preprod-worker07.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bd:74` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.129 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bd74 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-worker04

- **UUID (Instance):** 501a3de2-cd8e-7a3d-1ce0-f1aacd44a8a4
- **UUID (BIOS):** 421aa2d3-8e8b-0121-1f58-7ff4e9863759
- **Chemin VMX:** `[DS_PP_REPLI_01] k8s-rke2-preprod-worker04/k8s-rke2-preprod-worker04.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:06:11 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] k8s-rke2-preprod-worker04/k8s-rke2-preprod-worker04.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:7e:ed` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.126 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:7eed (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-manager-01-pp

- **UUID (Instance):** 501a160d-f117-2b33-afe1-9ed013e5e232
- **UUID (BIOS):** 421a167e-273e-f0ec-94b7-4fef822b6f0e
- **Chemin VMX:** `[DS_PP_REPLI_10] srv-docker-manager-01-pp/srv-docker-manager-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:51:16 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 122880 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1228800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_10 | `[DS_PP_REPLI_10] srv-docker-manager-01-pp/srv-docker-manager-01-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:2b:55` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.42 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:2b55 (Prefix: 64, State: unknown) |

---

### 5.x VM: SRV-IHM-PP-01

- **UUID (Instance):** 501a3a05-f01c-3f61-5afa-a94a960d807f
- **UUID (BIOS):** 421adc72-66fe-6014-4ba8-be80e545a2d7
- **Chemin VMX:** `[DS_PP_REPLI_11] SRV-IHM-PP-01/SRV-IHM-PP-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-IHM-PP-01/SRV-IHM-PP-01.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] SRV-IHM-PP-01/SRV-IHM-PP-01_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:4d:28` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: k8s-rke2-preprod-worker02

- **UUID (Instance):** 501ae974-445f-2c3f-ba87-816d8c616c65
- **UUID (BIOS):** 421a70c5-a73f-9fda-2377-c8904d47bae3
- **Chemin VMX:** `[DS_PP_REPLI_05] k8s-rke2-preprod-worker02/k8s-rke2-preprod-worker02.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:50:21 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_05 | `[DS_PP_REPLI_05] k8s-rke2-preprod-worker02/k8s-rke2-preprod-worker02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:60:51` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.124 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6051 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I201PP (JBOSS EAP 5.2 V3 PREPROD)

- **UUID (Instance):** 501ab12a-a586-3939-8856-220c2218f180
- **UUID (BIOS):** 564d6f9e-75bf-dc7a-f499-359e1aa48eca
- **Chemin VMX:** `[DS_PP_REPLI_11] S00I201PP (JBOSS EAP 5.2 V3 PREPROD)/S00I201PP (JBOSS EAP 5.2 V3 PREPROD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:27 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 14336 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 143360 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I201PP (JBOSS EAP 5.2 V3 PREPROD)/S00I201PP (JBOSS EAP 5.2 V3 PREPROD).vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 10.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] S00I201PP (JBOSS EAP 5.2 V3 PREPROD)/S00I201PP (JBOSS EAP 5.2 V3 PREPROD)_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:4E:62` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: AD-PRA

- **UUID (Instance):** 501adf7d-a8c0-0331-c8ec-1b9193e31266
- **UUID (BIOS):** 421a5e4f-0517-3d7a-9bc7-24aad5cf7388
- **Chemin VMX:** `[NFS_PP_01] AD-PRA/AD-PRA.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12389, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | NFS_PP_01 | `[NFS_PP_01] AD-PRA/AD-PRA.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | NFS_PP_01 | `[NFS_PP_01] AD-PRA/AD-PRA_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:95:61` | VM_Local | False | N/A |

---

### 5.x VM: vCLS-2dd1d3ea-7dd0-4359-bdf4-c79cb92e64ac

- **UUID (Instance):** 501ab019-293e-8795-019f-6b7312c03979
- **UUID (BIOS):** 421a9f36-0846-b2f4-4859-6db195fc3bd7
- **Chemin VMX:** `[NFS_PP_01] vCLS-2dd1d3ea-7dd0-4359-bdf4-c79cb92e64ac/vCLS-2dd1d3ea-7dd0-4359-bdf4-c79cb92e64ac.vmx`
- **OS Invité:** Other 3.x or later Linux (64-bit) (ID: other3xLinux64Guest)
- **Version VM:** vmx-11
- **VMware Tools:** toolsOk (Version: 12352, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-06 11:31:47 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 128 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1280 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 2.0 | NFS_PP_01 | `[NFS_PP_01] vCLS-2dd1d3ea-7dd0-4359-bdf4-c79cb92e64ac/vCLS-2dd1d3ea-7dd0-4359-bdf4-c79cb92e64ac.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

Aucun adaptateur réseau.

---

### 5.x VM: k8s_preprod_worker13

- **UUID (Instance):** 501ab453-4cef-8303-877e-4ed1393b15a4
- **UUID (BIOS):** 564da865-1598-a313-5f97-cefbaa8a501c
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker13/k8s_preprod_worker13.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-04 15:09:47 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker13/k8s_preprod_worker13.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bc:ad` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.135 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bcad (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker09

- **UUID (Instance):** 501a06c6-d7f0-bed9-ca13-aa9f7c40c171
- **UUID (BIOS):** 421aca4b-fa9f-0275-2912-7db524d770b9
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker09/k8s_preprod_worker09.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-11-04 15:09:47 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker09/k8s_preprod_worker09.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f2:c0` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.131 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f2c0 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker06

- **UUID (Instance):** 501afc7e-3f74-b854-b433-2c3fc8135a1c
- **UUID (BIOS):** 421a553c-ad6b-4639-5253-38c874012d73
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker06/k8s_preprod_worker06.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:27 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker06/k8s_preprod_worker06.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:47:9f` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.128 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:479f (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-docker-worker-02-pp

- **UUID (Instance):** 501ac0a6-432b-d776-86bd-1716f1bd5677
- **UUID (BIOS):** 421aa711-ecc6-4086-71db-8be03805bf3d
- **Chemin VMX:** `[DS_PP_REPLI_03] srv-docker-worker-02-pp/srv-docker-worker-02-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-08 14:43:21 UTC
- **Hôte Actuel:** vm-esx-pp-01.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 122880 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1228800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 280.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-docker-worker-02-pp/srv-docker-worker-02-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e3:70` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.49 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e370 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I413PP (NOUVEL INTRANET V4)

- **UUID (Instance):** 501ab010-488d-5b71-cc75-67691a88f8fc
- **UUID (BIOS):** 564d9050-9314-0cd2-d964-4f97531abce0
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I413PP (NOUVEL INTRANET V4)/S00I413PP (NOUVEL INTRANET V4).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 09:56:07 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I413PP (NOUVEL INTRANET V4)/S00I413PP (NOUVEL INTRANET V4).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:c8:5e` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.17 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:c85e (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-ead-pre-01

- **UUID (Instance):** 501ae6eb-ed46-408d-9558-bc069913c43b
- **UUID (BIOS):** 421a44cc-563a-df97-c074-ecb12307f06d
- **Chemin VMX:** `[DS_PP_REPLI_03] srv-ead-pre-01/srv-ead-pre-01.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:55:22 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-ead-pre-01/srv-ead-pre-01.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] srv-ead-pre-01/srv-ead-pre-01_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a3:db` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::1b7a:b81:c230:965a (Prefix: 64, State: unknown), 172.16.250.22 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdocmongo-pp2

- **UUID (Instance):** 501a7d52-2c9e-1e0e-ac0a-a81cd3bd428d
- **UUID (BIOS):** 421a76a8-2c9b-7f26-b42d-c8c69897a5a5
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-bdocmongo-pp2/srv-bdocmongo-pp2.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:13:47 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-bdocmongo-pp2/srv-bdocmongo-pp2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:a1:15` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.89 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:a115 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_master01

- **UUID (Instance):** 501a0eb9-aa7e-2342-b89d-1634ce421085
- **UUID (BIOS):** 564dbcf7-1be9-f5ed-834f-d099abc0cf10
- **Chemin VMX:** `[DS_PP_REPLI_01] k8s_preprod_master01/k8s_preprod_master01.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:35:45 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] k8s_preprod_master01/k8s_preprod_master01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bc:19` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.120 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bc19 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-metier-pre1

- **UUID (Instance):** 501a8b05-e9b5-5516-d3be-7ae76f644ba4
- **UUID (BIOS):** 421a0474-0485-9242-944f-1faa23504f45
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-metier-pre1/srv-metier-pre1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:46:23 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-metier-pre1/srv-metier-pre1.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-metier-pre1/srv-metier-pre1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:04:e0` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::e12a:4411:8388:d6d1 (Prefix: 64, State: unknown), 172.16.250.249 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s_preprod_master03

- **UUID (Instance):** 501ace3f-5448-6d56-1abe-49bf378f397a
- **UUID (BIOS):** 421a59d2-0a4c-6c26-0bbd-49f4a15fad24
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_master03/k8s_preprod_master03.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-19 08:03:51 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_master03/k8s_preprod_master03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:68:03` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.122 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6803 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-master02

- **UUID (Instance):** 501aa58d-2b7f-19f1-795c-935614a92218
- **UUID (BIOS):** 421acdc9-db9e-96b2-efee-8ecf6793f1fc
- **Chemin VMX:** `[DS_PP_REPLI_03] k8s-rke2-preprod-master02/k8s-rke2-preprod-master02.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:15:10 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] k8s-rke2-preprod-master02/k8s-rke2-preprod-master02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:0f:33` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.121 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f33 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-ansible-pro

- **UUID (Instance):** 501a6e49-aceb-678e-0524-fc7e38ec0766
- **UUID (BIOS):** 421afca2-057c-a479-9672-75f9c4e4cbbc
- **Chemin VMX:** `[DS_PP_REPLI_11] srv-ansible-pro/srv-ansible-pro.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-20 11:12:59 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] srv-ansible-pro/srv-ansible-pro.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1c:73` | DVPortGroup: dvportgroup-178069 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.80.32 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:1c73 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I260PP

- **UUID (Instance):** 501aed6c-9960-ce0d-82fe-5f541241eb71
- **UUID (BIOS):** 564dcafb-92b1-82f0-fe8b-da249464a156
- **Chemin VMX:** `[DS_PP_REPLI_09] S00I260PP/S00I260PP.vmx`
- **OS Invité:** Microsoft Windows Server 2012 (64-bit) (ID: windows8Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:22:58 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] S00I260PP/S00I260PP.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9A:68:AD` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: S00I130R(SMTB)

- **UUID (Instance):** 501b8e05-5b30-6d8f-1fef-2e07dfca6ef2
- **UUID (BIOS):** 421b10af-f56c-b442-8ac2-54372858d690
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I130R(SMTB)/S00I130R(SMTB).vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-02-11 16:00:28 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I130R(SMTB)/S00I130R(SMTB)-000001.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9b:00:4e` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: k8s_install_bastion

- **UUID (Instance):** 501a126d-10e5-ca33-d3ff-05b625da6a04
- **UUID (BIOS):** 421a1652-9a16-6671-4693-c4d8b6dd8807
- **Chemin VMX:** `[DS_PP_REPLI_06] k8s_install_bastion/k8s_install_bastion.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11269, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:29 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 32.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] k8s_install_bastion/k8s_install_bastion.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:65:11` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.130 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:6511 (Prefix: 64, State: unknown) |

---

### 5.x VM: cegid-trt-pp

- **UUID (Instance):** 501a114f-df07-728c-0e04-ef0b1de1fba4
- **UUID (BIOS):** 421adca8-abe6-24a5-c894-4e1a9eadf396
- **Chemin VMX:** `[DS_PP_REPLI_03] cegid-trt-pp/cegid-trt-pp.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-10 00:17:26 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 4)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] cegid-trt-pp/cegid-trt-pp_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] cegid-trt-pp/cegid-trt-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:14:f5` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::80f5:1e1d:c3a8:3e8f (Prefix: 64, State: unknown), 172.16.250.215 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-bdoc-mysql-02-pre

- **UUID (Instance):** 501a6ded-4c57-dc27-51e7-f822ce94bfa6
- **UUID (BIOS):** 421ac083-2b90-f0ec-0407-85be411d5b84
- **Chemin VMX:** `[DS_PP_REPLI_06] srv-bdoc-mysql-02-pre/srv-bdoc-mysql-02-pre.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:07:59 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] srv-bdoc-mysql-02-pre/srv-bdoc-mysql-02-pre.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e7:ab` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.111 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e7ab (Prefix: 64, State: unknown) |

---

### 5.x VM: BdocCore-pre-1

- **UUID (Instance):** 501a01c6-aa8f-4c8e-b6bb-efd9611a2dfb
- **UUID (BIOS):** 421ae19d-690a-f10a-a47e-2ac64ca1a822
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocCore-pre-1/BdocCore-pre-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 12:19:09 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocCore-pre-1/BdocCore-pre-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocCore-pre-1/BdocCore-pre-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:82:84` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: BdocAgent-pre-1

- **UUID (Instance):** 501a1f45-dc3d-97a9-78bd-28f9070c633f
- **UUID (BIOS):** 564d37aa-8bb1-87a6-0ec4-263483d68254
- **Chemin VMX:** `[DS_PP_REPLI_07] BdocAgent-pre-1/BdocAgent-pre-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 12:19:36 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocAgent-pre-1/BdocAgent-pre-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] BdocAgent-pre-1/BdocAgent-pre-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:47:cb` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::fbc4:8f3a:3ed0:aa21 (Prefix: 64, State: unknown), 172.16.250.191 (Prefix: 16, State: preferred) |

---

### 5.x VM: k8s-rke2-preprod-master03

- **UUID (Instance):** 501a599a-1278-1173-0211-e30b76ed628e
- **UUID (BIOS):** 421a033e-3e54-d420-098e-b290dbc8e206
- **Chemin VMX:** `[DS_PP_REPLI_01] k8s-rke2-preprod-master03/k8s-rke2-preprod-master03.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:21:24 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] k8s-rke2-preprod-master03/k8s-rke2-preprod-master03.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:40:df` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.122 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:40df (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-mongo-pp-2

- **UUID (Instance):** 501a31bd-5d27-92fa-5064-ab0e0f59bc22
- **UUID (BIOS):** 421acdc9-8755-f75f-1559-25a6aac46999
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-mongo-pp/srv-mongo-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:07:57 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-mongo-pp/srv-mongo-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:5c:c2` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.93 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:5cc2 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-postgres-01-pp

- **UUID (Instance):** 501a3ee8-6112-ef9b-5742-e807f876b6f4
- **UUID (BIOS):** 421abdc2-6d16-729a-2ab9-0a75b3e23fe3
- **Chemin VMX:** `[DS_PP_REPLI_05] srv-postgres-01-pp/srv-postgres-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:21:31 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 6 (Cœurs/Socket: 2)
- **RAM:** 6144 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 6000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 61440 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 370.0 | DS_PP_REPLI_05 | `[DS_PP_REPLI_05] srv-postgres-01-pp/srv-postgres-01-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:0a:f4` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.229 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:af4 (Prefix: 64, State: unknown) |

---

### 5.x VM: S00I220PP

- **UUID (Instance):** 501a9fad-2ce8-8360-0d18-a85d497edd5c
- **UUID (BIOS):** 421aecf5-8ff4-8992-c450-e45eefd458c9
- **Chemin VMX:** `[DS_PP_REPLI_03] S00I220PP/S00I220PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-12 01:35:45 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 40.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] S00I220PP/S00I220PP.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:1e:72` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::b6b2:6f70:70fc:53c1 (Prefix: 64, State: unknown), 172.16.250.20 (Prefix: 24, State: preferred) |

---

### 5.x VM: BdocInter-pre-1

- **UUID (Instance):** 501a5590-799d-a9a4-57e8-0375ca22af70
- **UUID (BIOS):** 421a5d48-e0b3-9d43-7cfe-b4514bdb66c7
- **Chemin VMX:** `[DS_PP_REPLI_08] BdocInter-pre-1/BdocInter-pre-1.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:51:20 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] BdocInter-pre-1/BdocInter-pre-1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] BdocInter-pre-1/BdocInter-pre-1_1.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9A:84:F7` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: srv-rabbitmq-pp

- **UUID (Instance):** 501aa561-fc52-9e1b-9746-8b2ecbcb7308
- **UUID (BIOS):** 421af7b2-d95a-d26c-353b-5cfa3e8cc582
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-rabbitmq-pp/srv-rabbitmq-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-30 15:25:17 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-rabbitmq-pp/srv-rabbitmq-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:ee:7a` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.50 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:ee7a (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-talend-tac-01-pp

- **UUID (Instance):** 501abb51-9d82-1c9c-3a36-72c1f42dd894
- **UUID (BIOS):** 421a8fce-af4d-4dd2-6f96-d8877b4d222d
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-talend-tac-01-pp/srv-talend-tac-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-25 06:17:09 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 70.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-talend-tac-01-pp/srv-talend-tac-01-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f0:4c` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.207 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f04c (Prefix: 64, State: unknown) |

---

### 5.x VM: PSQL_BIGMAX_PP_SEC

- **UUID (Instance):** 501ac2a3-8ada-88b8-1088-11a97f9738b7
- **UUID (BIOS):** 421a5514-2b8c-9467-622f-547bf8805476
- **Chemin VMX:** `[DS_PP_REPLI_08] PSQL_BIGMAX_PP_SEC/PSQL_BIGMAX_PP_SEC.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:28:35 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] PSQL_BIGMAX_PP_SEC/PSQL_BIGMAX_PP_SEC.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 40.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] PSQL_BIGMAX_PP_SEC/PSQL_BIGMAX_PP_SEC_1.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] PSQL_BIGMAX_PP_SEC/PSQL_BIGMAX_PP_SEC_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9a:8f:32` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.99 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8f32 (Prefix: 64, State: unknown) |

---

### 5.x VM: dwh-sql-rec-mgr

- **UUID (Instance):** 501ad05f-6b20-c4cd-85b2-1f49bc484abd
- **UUID (BIOS):** 421a436b-bde4-3580-c59e-c1b141e349d4
- **Chemin VMX:** `[DS_PP_REPLI_01] dwh-sql-rec/dwh-sql-rec.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 4)
- **RAM:** 131072 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 1310720 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] dwh-sql-rec/dwh-sql-rec_3-000001.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 1433.6 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] dwh-sql-rec/dwh-sql-rec_1-000001.vmdk` | persistent | False | -1 IOPS |
| Hard disk 3 (2002) | 550.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] dwh-sql-rec/dwh-sql-rec_2-000001.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:52:90` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I105PP

- **UUID (Instance):** 501aaa48-3ef1-984a-4bed-a28b212ee900
- **UUID (BIOS):** 421a0a57-5d94-f9cb-14a8-ff16a50e06c5
- **Chemin VMX:** `[DS_PP_REPLI_04] S00I105PP/S00I105PP.vmx`
- **OS Invité:** Debian GNU/Linux 10 (64-bit) (ID: debian10_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 11360, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 18:02:05 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 71680 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 716800 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I105PP/S00I105PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 50.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] S00I105PP/S00I105PP_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:3f:55` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.96 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:3f55 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-talend-jobserveur-01-pp

- **UUID (Instance):** 501a7acb-6ca0-e1c1-cc45-84ddfd57e1a8
- **UUID (BIOS):** 421abb97-59fa-9362-0d85-0ff70c37c21a
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-talend-jobserveur-01-pp/srv-talend-jobserveur-01-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-25 06:15:39 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 32768 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 327680 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 80.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-talend-jobserveur-01-pp/srv-talend-jobserveur-01-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:88:72` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.227 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8872 (Prefix: 64, State: unknown) |

---

### 5.x VM: srv-bdoc-mysql-03-pre

- **UUID (Instance):** 501a1363-820d-3b88-d8df-b6e7e51f6eeb
- **UUID (BIOS):** 421a3771-e6be-dee6-15fa-e46bc46212dd
- **Chemin VMX:** `[DS_PP_REPLI_02] srv-bdoc-mysql-03-pre/srv-bdoc-mysql-03-pre.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:15:59 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] srv-bdoc-mysql-03-pre/srv-bdoc-mysql-03-pre.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:bf:26` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.112 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:bf26 (Prefix: 64, State: unknown) |

---

### 5.x VM: IES-P-BI-PP

- **UUID (Instance):** 501a96d2-2363-43f5-39ec-1061433ba148
- **UUID (BIOS):** 564d87b0-d5b8-1426-4209-4c0fcba7a388
- **Chemin VMX:** `[DS_PP_REPLI_09] IES-P-BI-PP/IES-P-BI-PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:51:17 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 170.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] IES-P-BI-PP/IES-P-BI-PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 250.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] IES-P-BI-PP/IES-P-BI-PP_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:7c:a0` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::dd4d:411:6cd:2f8d (Prefix: 64, State: unknown), 172.16.250.60 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I130PP

- **UUID (Instance):** 501a2628-b8ba-c0de-cd19-4beb5f02cdf7
- **UUID (BIOS):** 421ad168-a9b7-39e3-e3f8-d1c705f36209
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I130PP/S00I130PP.vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOld (Version: 9356, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 14:28:24 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 65.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I130PP/S00I130PP.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9a:ff:ca` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.150 (Prefix: 24, State: preferred) |

---

### 5.x VM: IES-SSAS-PP

- **UUID (Instance):** 501a37a3-a585-c0d0-0268-e8bb29d80069
- **UUID (BIOS):** 421a970b-5843-417e-4e8b-0031ea253c17
- **Chemin VMX:** `[DS_PP_REPLI_09] IES-SSAS-PP/IES-SSAS-PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:47:58 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] IES-SSAS-PP/IES-SSAS-PP.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:82:1d` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::938:cb40:b03e:a5d8 (Prefix: 64, State: unknown), 172.16.250.62 (Prefix: 24, State: preferred) |

---

### 5.x VM: S00I130I

- **UUID (Instance):** 501e97e6-2145-ab93-1547-f235ad9ba73d
- **UUID (BIOS):** 421e006f-ad5e-8603-8c61-19053dbda78f
- **Chemin VMX:** `[DS_PP_REPLI_01] S00I130I/S00I130I.vmx`
- **OS Invité:** Microsoft Windows Server 2003 Standard (32-bit) (ID: winNetStandardGuest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 1 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 1000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] S00I130I/S00I130I-000002.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualPCNet32 | `00:50:56:9E:AD:C7` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: S00I401PP (JBOSS EAP 7 V4 PREPROD)

- **UUID (Instance):** 501acb47-66b5-666d-358a-ed493ecdc574
- **UUID (BIOS):** 564d9e01-dda9-35bb-6415-4e68660dfd91
- **Chemin VMX:** `[DS_PP_REPLI_09] S00I401PP (JBOSS EAP 7 V4 PREPROD)/S00I401PP (JBOSS EAP 7 V4 PREPROD).vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:28:35 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 10240 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 102400 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] S00I401PP (JBOSS EAP 7 V4 PREPROD)/S00I401PP (JBOSS EAP 7 V4 PREPROD).vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000 | `00:50:56:9A:77:C4` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | N/A |

---

### 5.x VM: srv-automator-core-pp

- **UUID (Instance):** 501a16a9-4e9e-865b-58f3-5b07f947c7e9
- **UUID (BIOS):** 421aa3c1-6be8-46f5-53f3-447d496be355
- **Chemin VMX:** `[DS_PP_REPLI_01] srv-automator-core-pp/srv-automator-core-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:11:33 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_01 | `[DS_PP_REPLI_01] srv-automator-core-pp/srv-automator-core-pp.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:8b:9c` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.122 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8b9c (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker08

- **UUID (Instance):** 501a4a4e-2933-bb1a-dad2-874f48652d39
- **UUID (BIOS):** 564d2e17-0a42-e737-1dc8-20fb33b1c90a
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker08/k8s_preprod_worker08.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-10-08 17:31:40 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker08/k8s_preprod_worker08.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:8d:17` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.130 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:8d17 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker02

- **UUID (Instance):** 501a30b7-2651-e52b-364b-f50af4be059b
- **UUID (BIOS):** 564d30a1-fe75-386a-7c9f-05aaaf6199b7
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker02/k8s_preprod_worker02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:16:30 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker02/k8s_preprod_worker02.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2001) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker02/k8s_preprod_worker02_1.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:37:1b` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.124 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:371b (Prefix: 64, State: unknown) |

---

### 5.x VM: AD-ASSMT

- **UUID (Instance):** 501a5e03-3d69-5029-50c1-6d55e33a70c7
- **UUID (BIOS):** 421a9b33-01b9-e3a9-31cc-617b5ebf07dc
- **Chemin VMX:** `[NFS_PP_01] AD-ASSMT/AD-ASSMT.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 11333, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 2048 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 20480 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | NFS_PP_01 | `[NFS_PP_01] AD-ASSMT/AD-ASSMT.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:48:98` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: PSQL_VAL_REC

- **UUID (Instance):** 501ebb75-9cf8-6778-5d09-1fd478de5057
- **UUID (BIOS):** 421e7f76-21a7-8f1c-2e22-d46822b31b14
- **Chemin VMX:** `[DS_PP_REPLI_09] PSQL_VAL_REC/PSQL_VAL_REC.vmx`
- **OS Invité:** Red Hat Enterprise Linux 6 (64-bit) (ID: rhel6_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 10362, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 200.0 | DS_PP_REPLI_09 | `[DS_PP_REPLI_09] PSQL_VAL_REC/PSQL_VAL_REC.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9e:dd:8d` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: k8s_preprod_master02

- **UUID (Instance):** 501ac7f6-9fe3-eeae-79ed-0743a71e64db
- **UUID (BIOS):** 564d2524-8c13-dc84-6ee0-04b8ca46e223
- **Chemin VMX:** `[DS_PP_REPLI_07] k8s_preprod_master02/k8s_preprod_master02.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:31:01 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 2)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_07 | `[DS_PP_REPLI_07] k8s_preprod_master02/k8s_preprod_master02.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:f6:d4` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.121 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:f6d4 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-worker06

- **UUID (Instance):** 501aeed3-afa9-928d-9a5a-8d4cab2663c1
- **UUID (BIOS):** 421a9dc3-9211-e0c1-c1b6-04f7740f40f0
- **Chemin VMX:** `[DS_PP_REPLI_03] k8s-rke2-preprod-worker06/k8s-rke2-preprod-worker06.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:08:29 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_03 | `[DS_PP_REPLI_03] k8s-rke2-preprod-worker06/k8s-rke2-preprod-worker06.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:e0:2f` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.128 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:e02f (Prefix: 64, State: unknown) |

---

### 5.x VM: AD-PRA2

- **UUID (Instance):** 501abac1-bb54-4b63-557c-b9daffceaff2
- **UUID (BIOS):** 421a154a-4d16-f2f1-6dac-611e8c5c8811
- **Chemin VMX:** `[NFS_PP_01] AD-PRA2/AD-PRA2.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotRunning (Version: 12294, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | NFS_PP_01 | `[NFS_PP_01] AD-PRA2/AD-PRA2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:c5:ef` | VM_Local | False | N/A |

---

### 5.x VM: cegid-bdd-dev

- **UUID (Instance):** 501a4528-9300-1d6a-b743-ae260ace2bfc
- **UUID (BIOS):** 421a6252-be9b-6553-0c8b-2155857f6d0a
- **Chemin VMX:** `[DS_PP_REPLI_11] cegid-bdd-dev_1/cegid-bdd-dev.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsNotInstalled (Version: 0, Exécution: guestToolsNotRunning)
- **État d'alimentation:** poweredOff
- **Heure de démarrage:** 1-01-01 00:00:00 
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 12288 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 122880 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 60.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-dev_1/cegid-bdd-dev_3.vmdk` | persistent | True | -1 IOPS |
| Hard disk 2 (2001) | 210.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-dev_1/cegid-bdd-dev.vmdk` | persistent | True | -1 IOPS |
| Hard disk 3 (2003) | 70.0 | DS_PP_REPLI_11 | `[DS_PP_REPLI_11] cegid-bdd-dev_1/cegid-bdd-dev_2.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualE1000e | `00:50:56:9a:5b:f2` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | False | N/A |

---

### 5.x VM: k8s_preprod_worker10

- **UUID (Instance):** 501a6562-fd4e-449a-ebd7-73fa741e8695
- **UUID (BIOS):** 564d466d-4c81-b28c-239d-8b730fb257b5
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker10/k8s_preprod_worker10.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:27:32 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 8000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 491520 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker10/k8s_preprod_worker10.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:dc:a0` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.132 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:dca0 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s-rke2-preprod-master01

- **UUID (Instance):** 501aeb95-d571-0400-0f08-8f8f4b5ca787
- **UUID (BIOS):** 421a480b-0f63-c927-9506-a0646535b702
- **Chemin VMX:** `[DS_PP_REPLI_02] k8s-rke2-preprod-master01/k8s-rke2-preprod-master01.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-03-13 15:27:19 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 4 (Cœurs/Socket: 1)
- **RAM:** 8192 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 4000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 81920 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_02 | `[DS_PP_REPLI_02] k8s-rke2-preprod-master01/k8s-rke2-preprod-master01.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:04:0e` | DVPortGroup: dvportgroup-178068 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.70.120 (Prefix: 24, State: preferred), 192.168.70.12 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:40e (Prefix: 64, State: unknown) |

---

### 5.x VM: IES-SQL-BI-PP

- **UUID (Instance):** 501a7c9f-6aa9-2f05-db6e-bef63cb712dd
- **UUID (BIOS):** 421a6258-bf2b-902c-35a7-0a7c6cba061b
- **Chemin VMX:** `[DS_PP_REPLI_06] IES-SQL-BI-PP/IES-SQL-BI-PP.vmx`
- **OS Invité:** Microsoft Windows Server 2016 or later (64-bit) (ID: windows9Server64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12389, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-04-09 23:48:54 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 2)
- **RAM:** 16384 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 163840 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 420.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] IES-SQL-BI-PP/IES-SQL-BI-PP.vmdk` | persistent | False | -1 IOPS |
| Hard disk 2 (2002) | 40.0 | DS_PP_REPLI_06 | `[DS_PP_REPLI_06] IES-SQL-BI-PP/IES-SQL-BI-PP_2.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:86:df` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | fe80::a5df:461b:b476:fe8e (Prefix: 64, State: unknown), 172.16.250.61 (Prefix: 24, State: preferred) |

---

### 5.x VM: srv-autom-pp

- **UUID (Instance):** 501a4e45-5790-43e4-e521-e9e328f22b81
- **UUID (BIOS):** 421a6b3c-c776-35d2-66b0-d3308d878b4d
- **Chemin VMX:** `[DS_PP_REPLI_04] srv-autom-pp/srv-autom-pp.vmx`
- **OS Invité:** Ubuntu Linux (64-bit) (ID: ubuntu64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 12421, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2025-01-19 12:22:46 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 2 (Cœurs/Socket: 1)
- **RAM:** 4096 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 50.0 | DS_PP_REPLI_04 | `[DS_PP_REPLI_04] srv-autom-pp/srv-autom-pp.vmdk` | persistent | True | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:4f:a3` | DVPortGroup: dvportgroup-72 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 172.16.250.195 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:4fa3 (Prefix: 64, State: unknown) |

---

### 5.x VM: k8s_preprod_worker05

- **UUID (Instance):** 501ab90b-1e76-1b13-4b2f-afad1f5c66db
- **UUID (BIOS):** 421a6747-edd7-1dd7-42eb-ac2b46462094
- **Chemin VMX:** `[DS_PP_REPLI_08] k8s_preprod_worker05/k8s_preprod_worker05.vmx`
- **OS Invité:** CentOS 7 (64-bit) (ID: centos7_64Guest)
- **Version VM:** vmx-15
- **VMware Tools:** toolsOk (Version: 10362, Exécution: guestToolsRunning)
- **État d'alimentation:** poweredOn
- **Heure de démarrage:** 2024-04-26 16:28:35 UTC
- **Hôte Actuel:** vm-esx-pp-03.bcaexpertise.org
- **vCPUs:** 8 (Cœurs/Socket: 1)
- **RAM:** 49152 MB
  - Réservation CPU: 0 MHz, Limite CPU: -1 MHz, Partages CPU: 2000 (normal)
  - Réservation Mém.: 0 MB, Limite Mém.: -1 MB, Partages Mém.: 40960 (normal)


#### Disques Virtuels

| Label (Clé) | Capacité (GB) | Datastore | Chemin VMDK | Mode | Thin Prov. | SIOC Limit |
|---|---|---|---|---|---|---|
| Hard disk 1 (2000) | 100.0 | DS_PP_REPLI_08 | `[DS_PP_REPLI_08] k8s_preprod_worker05/k8s_preprod_worker05.vmdk` | persistent | False | -1 IOPS |


#### Adaptateurs Réseau Virtuels

| Label (Clé) | Type | MAC | Réseau | Connecté | IPs Invité |
|---|---|---|---|---|---|
| Network adapter 1 (4000) | vim.vm.device.VirtualVmxnet3 | `00:50:56:9a:79:e5` | DVPortGroup: dvportgroup-106 (DVS: 50 1a 5e d8 ec 49 9c 61-ec 6c e3 9f 94 d4 a2 49) | True | 192.168.2.127 (Prefix: 24, State: preferred), fe80::250:56ff:fe9a:79e5 (Prefix: 64, State: unknown) |

---
