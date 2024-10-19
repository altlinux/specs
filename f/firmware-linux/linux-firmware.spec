Name: firmware-linux
Version: 20241018
Release: alt1

Summary: Firmware files used by the Linux kernel
License: GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
Provides: linux-firmware

BuildRequires: hardlink
BuildRequires: python3
Requires: udev
AutoReqProv: no

%add_verify_elf_skiplist /lib/firmware/*

%description
Kernel-firmware includes firmware files
required for some devices to operate.

%package netronome
Group: System/Kernel and hardware
Summary: firmware for Agilio SmartNICs

%description netronome
firmware for Agilio SmartNICs

%package liquidio
Group: System/Kernel and hardware
Summary: firmware for LiquidIO Smart NICs

%description liquidio
firmware for LiquidIO II Smart NICs

%package qcom
Group: System/Kernel and hardware
Summary: firmware for Qualcomm platforms

%description qcom
firmware for Qualcomm platforms (most of it)

%package mrvl
Group: System/Kernel and hardware
Summary: firmware for Marvell Prestera

%description mrvl
firmware for Marvell Prestera switchdev

%package mellanox
Group: System/Kernel and hardware
Summary: firmware for Mellanox Spectrum

%description mellanox
firmware for Mellanox Spectrum switchdev

%prep
%setup -n %name-%version
%patch -p1

%install
DESTDIR=%buildroot FIRMWAREDIR=lib/firmware make install
hardlink -cv %buildroot/lib/firmware

## *TODO* check these too
rm -rf %buildroot/lib/firmware{ess,korg,sb16,yamaha}

%files
%doc WHENCE LICEN?E.*
/lib/firmware/*
%exclude /lib/firmware/netronome
%exclude /lib/firmware/liquidio
%exclude /lib/firmware/qcom/*/
%exclude /lib/firmware/mrvl/*/
%exclude /lib/firmware/mellanox

%files netronome
/lib/firmware/netronome

%files liquidio
/lib/firmware/liquidio

%files qcom
/lib/firmware/qcom/*/

%files mrvl
/lib/firmware/mrvl/*/

%files mellanox
/lib/firmware/mellanox

%changelog
* Sat Oct 19 2024 Anton Midyukov <antohami@altlinux.org> 20241018-alt1
- configuration changes:
  + update.sh: do not git fetch tag from upstream/main
- upstream changes (GIT 41a6688a):
  + check_whence.py: skip some validation if git ls-files fails (thx Emil Velikov)
  + qcom: Add Audio firmware for X1E80100 CRD/QCPs (thx Sibi Sankar)
  + amdgpu: DMCUB updates forvarious AMDGPU ASICs (thx Wayne Lin)
  + brcm: replace NVRAM for Jetson TX1 (thx Tomasz Maciej Nowak)
  + rtlwifi: Update firmware for RTL8192FU to v7.3 (thx Zenm Chen)
  + make: separate installation and de-duplication targets (thx Emil Velikov)
  + check_whence.py: check the permissions (thx Emil Velikov)
  + configure: remove unused file (thx Emil Velikov)
  + rtl_nic: add firmware rtl8125d-1 (thx ChunHao Lin)
  + iwlwifi: add gl/Bz FW for core91-69 release (thx Miri Korenblit)
  + iwlwifi: update ty/So/Ma firmwares for core91-69 release (thx Miri Korenblit)
  + iwlwifi: update cc/Qu/QuZ firmwares for core91-69 release (thx Miri Korenblit)
  + cirrus: cs35l56: Add firmware for Cirrus CS35L56 for a Lenovo
    Laptop (thx Simon Trimmer)
  + cirrus: cs35l56: Add firmware for Cirrus CS35L56 for some
    ASUS laptops (thx Simon Trimmer)
  + cirrus: cs35l56: Add firmware for Cirrus Amps for some HP laptops (thx Simon Trimmer)
  + update firmware for en8811h 2.5G ethernet phy (thx Lucien.Jheng)
  + mtk_wed: add firmware for mt7988 Wireless Ethernet Dispatcher (thx Shayne Chen)
  + ath12k: WCN7850 hw2.0: update board-2.bin (thx Jeff Johnson)
  + ath12k: QCN9274 hw2.0: add to
    WLAN.WBE.1.3.1-00162-QCAHKSWPL_SILICONZ-1 (thx Jeff Johnson)
  + ath12k: QCN9274 hw2.0: add board-2.bin (thx Jeff Johnson)
  + copy-firmware.sh: rename variables in symlink hanlding (thx Emil Velikov)
  + copy-firmware.sh: remove no longer reachable test -L (thx Emil Velikov)
  + copy-firmware.sh: remove no longer reachable test -f (thx Emil Velikov)
  + copy-firmware.sh: call ./check_whence.py before parsing the file (thx Emil Velikov)
  + copy-firmware.sh: warn if the destination folder is not empty (thx Emil Velikov)
  + copy-firmware.sh: add err() helper (thx Emil Velikov)
  + copy-firmware.sh: fix indentation (thx Emil Velikov)
  + copy-firmware.sh: reset and consistently handle destdir (thx Emil Velikov)
  + Revert "copy-firmware: Support additional compressor options" (thx Emil Velikov)
  + copy-firmware.sh: flesh out and fix dedup-firmware.sh (thx Emil Velikov)
  + editorconfig: add initial config file (thx Emil Velikov)
  + check_whence.py: annotate replacement strings as raw (thx Emil Velikov)
  + check_whence.py: LC_ALL=C sort -u the filelist (thx Emil Velikov)
  + check_whence.py: ban link-to-a-link (thx Emil Velikov)
  + check_whence.py: use consistent naming (thx Emil Velikov)
  + tas2781: Upload dsp firmware for ASUS laptop 1EB30 & 1EB31 (thx Shenghao Ding)
  + rtlwifi: Add firmware v39.0 for RTL8192DU (thx Bitterblue Smith)
  + Revert "ath12k: WCN7850 hw2.0: update board-2.bin" (thx Mario Limonciello)
  + QCA: Add Bluetooth firmwares for WCN785x with UART transport (thx Zijun Hu)
  + amdgpu: DMCUB DCN35 update (thx Rodrigo Siqueira)
  + brcm: Add BCM4354 NVRAM for Jetson TX1 (thx Peter Robinson)
  + brcm: Link FriendlyElec NanoPi M4 to AP6356S nvram (thx Peter Robinson)
  + add firmware for MediaTek Bluetooth chip (MT7920) (thx Chris Lu)
  + add firmware for MT7920 (thx Deren Wu)
  + amdgpu: update raven firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.3 firmware (thx Alex Deucher)
  + amdgpu: update VCN 3.1.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.5 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update vega12 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.4 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.2 firmware (thx Alex Deucher)
  + amdgpu: update vega10 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware (thx Alex Deucher)
  + amdgpu: update picasso firmware (thx Alex Deucher)
  + amdgpu: update beige goby firmware (thx Alex Deucher)
  + amdgpu: update vangogh firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware (thx Alex Deucher)
  + amdgpu: update navy flounder firmware (thx Alex Deucher)
  + amdgpu: update green sardine firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.4 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.1 firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.6 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.1 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.1 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.5 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.0 firmware (thx Alex Deucher)
  + amdgpu: update navi14 firmware (thx Alex Deucher)
  + amdgpu: update renoir firmware (thx Alex Deucher)
  + amdgpu: update navi12 firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 4.4.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update GC 9.4.3 firmware (thx Alex Deucher)
  + amdgpu: update yellow carp firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.4 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.2 firmware (thx Alex Deucher)
  + amdgpu: update navi10 firmware (thx Alex Deucher)
  + amdgpu: update aldebaran firmware (thx Alex Deucher)
  + qcom: update gpu firmwares for qcm6490 chipset (thx Akhil P Oommen)
  + mt76: mt7996: add firmware files for mt7992 chipset (thx Shayne Chen)
  + mt76: mt7996: add firmware files for mt7996 chipset variants (thx Shayne Chen)
  + qcom: add gpu firmwares for sa8775p chipset (thx Akhil P Oommen)
  + amdgpu: update DMCUB to v0.0.233.0 DCN351 (thx Alex Hung)
  + rtw89: 8922a: add fw format-2 v0.35.42.1 (thx Chin-Yen Lee)
  + copy-firmware: Handle links to uncompressed files (thx Juerg Haefliger)
  + WHENCE: Fix battmgr.jsn entry type (thx Juerg Haefliger)
  + amdgpu: Add VPE 6.1.3 microcode (thx Mario Limonciello)
  + amdgpu: add SDMA 6.1.2 microcode (thx Mario Limonciello)
  + amdgpu: Add support for PSP 14.0.4 (thx Mario Limonciello)
  + amdgpu: add GC 11.5.2 microcode (thx Mario Limonciello)
  + qcom: qcm6490: add ADSP and CDSP firmware (thx Dmitry Baryshkov)
  + Update firmware file for Intel Bluetooth Magnetor core (thx Kiran K)
  + Update firmware file for Intel BlazarU core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Solar core (thx Kiran K)
  + rtl_bt: Update RTL8852B BT USB FW to 0x0447_9301 (thx Hilda Wu)
  + realtek: rt1320: Add patch firmware of MCU (thx Shuming Fan)
  + i915: Update MTL DMC v2.23 (thx Dnyaneshwar Bhadane)
  + cirrus: cs35l56: Add firmware for Cirrus CS35L54 for some
    HP laptops (thx Simon Trimmer)
  + amdgpu: Revert sienna cichlid dmcub firmware update (thx Mario Limonciello)
  + iwlwifi: add Bz FW for core89-58 release (thx Miri Korenblit)
  + rtl_nic: add firmware rtl8126a-3 (thx ChunHao Lin)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris Lu)
  + amdgpu: update DMCUB to v0.0.232.0 for DCN314 and DCN351 (thx Hamza Mahfooz)
  + qcom: vpu: restore compatibility with kernels before 6.6 (thx Dmitry Baryshkov)
  + amdgpu: DMCUB updates forvarious AMDGPU ASICs (thx Zaeem Mohamed)
  + rtw89: 8922a: add fw format-1 v0.35.41.0 (thx Chin-Yen Lee)
  + update firmware for MT7925 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7925) (thx Chris Lu)
  + rtl_bt: Add firmware and config files for RTL8922A (thx Max Chou)
  + rtl_bt: Add firmware file for the the RTL8723CS Bluetooth part (thx Peter Robinson)
  + rtl_bt: de-dupe identical config.bin files (thx Peter Robinson)
  + Update AMD SEV firmware (thx John Allen)
  + update firmware for MT7996 (thx Shayne Chen)
  + Revert "i915: Update MTL DMC v2.22" (thx Gustavo Sousa)
  + ath12k: WCN7850 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.41 (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: QCA2066 hw2.1: add to
    WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.3 (thx Kalle Valo)
  + ath11k: QCA2066 hw2.1: add board-2.bin (thx Kalle Valo)
  + ath11k: IPQ5018 hw1.0: update to
    WLAN.HK.2.6.0.1-01291-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + qcom: vpu: add video firmware for sa8775p (thx Dikshita Agarwal)
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Tom Chung)
  + qcom: update path for video firmware for vpu-1/2/3.0 (thx Dikshita Agarwal)
  + QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00642 (thx Zijun Hu)
  + rtw89: 8852c: add fw format-1 v0.27.97.0 (thx Chin-Yen Lee)
  + rtw89: 8852bt: add firmware 0.29.91.0 (thx Ping-Ke Shih)
  + amdgpu: Update ISP FW for isp v4.1.1 (thx Pratap Nirujogi)
  + mediatek: Update mt8195 SOF firmware (thx Xiangzhi Tang)
  + amdgpu: DMCUB updates for DCN314 (thx Wayne Lin)
  + xe: First GuC release v70.29.2 for BMG (thx Julia Filipchuk)
  + xe: Add GuC v70.29.2 for LNL (thx Julia Filipchuk)
  + i915: Add GuC v70.29.2 for ADL-P, DG1, DG2, MTL, and TGL (thx Julia Filipchuk)
  + i915: Update MTL DMC v2.22 (thx Dnyaneshwar Bhadane)
  + i915: update MTL GSC to v102.0.10.1878 (thx Daniele Ceraolo Spurio)
  + xe: Add BMG HuC 8.2.10 (thx Daniele Ceraolo Spurio)
  + xe: Add GSC 104.0.0.1161 for LNL (thx Daniele Ceraolo Spurio)
  + xe: Add LNL HuC 9.4.13 (thx Daniele Ceraolo Spurio)
  + i915: update DG2 HuC to v7.10.16 (thx Daniele Ceraolo Spurio)
  + amdgpu: Update ISP FW for isp v4.1.1 (thx Pratap Nirujogi)
  + amdgpu: add new ISP 4.1.1 firmware (thx Pratap Nirujogi)
  + QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00641 (thx Zijun Hu)
  + amdgpu: update DMCUB to v0.0.227.0 for DCN35 and DCN351 (thx Rodrigo Siqueira)
  + Revert "iwlwifi: update ty/So/Ma firmwares for core89-58 release" (thx Miri Korenblit)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris Lu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris Lu)
  + iwlwifi: add gl FW for core89-58 release (thx Miri Korenblit)
  + iwlwifi: update ty/So/Ma firmwares for core89-58 release (thx Miri Korenblit)
  + iwlwifi: update cc/Qu/QuZ firmwares for core89-58 release (thx Miri Korenblit)
  + mediatek: Update mt8195 SOF firmware and sof-tplg (thx Xiangzhi Tang)
  + ASoC: tas2781: fix the license issue for tas781 firmware (thx Shenghao Ding)
  + rtl_bt: Update RTL8852B BT USB FW to 0x048F_4008 (thx Hilda Wu)
  + .gitignore: Ignore intermediate files (thx WangYuli)
  + i915: Update Xe2LPD DMC to v2.21 (thx Dnyaneshwar Bhadane)
  + qcom: move signed x1e80100 signed firmware to the SoC subdir (thx Dmitry Baryshkov)
  + qcom: add video firmware file for vpu-3.0 (thx Dikshita Agarwal)
  + amdgpu: update DMCUB to v0.0.225.0 for Various AMDGPU Asics (thx Fangzhi Zuo)
  + qcom: add gpu firmwares for x1e80100 chipset (thx Akhil P Oommen)
  + add firmware for qat_402xx devices (thx Giovanni Cabiddu)
  + amdgpu: update raven firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.3 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.3 firmware (thx Alex Deucher)
  + amdgpu: update vega20 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.5 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update vega12 firmware (thx Alex Deucher)
  + amdgpu: update vega10 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware (thx Alex Deucher)
  + amdgpu: update picasso firmware (thx Alex Deucher)
  + amdgpu: update beige goby firmware (thx Alex Deucher)
  + amdgpu: update vangogh firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware (thx Alex Deucher)
  + amdgpu: update navy flounder firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.11 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.4 firmware (thx Alex Deucher)
  + amdgpu: update green sardine firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.2 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.1 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.4 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.1 firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware (thx Alex Deucher)
  + amdgpu: update VPE 6.1.1 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.6 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.1.1 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.1 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.1 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.5 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.1.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.0 firmware (thx Alex Deucher)
  + amdgpu: update navi14 firmware (thx Alex Deucher)
  + amdgpu: update renoir firmware (thx Alex Deucher)
  + amdgpu: update navi12 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update GC 9.4.3 firmware (thx Alex Deucher)
  + amdgpu: update yellow carp firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.4 firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.2 firmware (thx Alex Deucher)
  + amdgpu: update navi10 firmware (thx Alex Deucher)
  + amdgpu: update raven2 firmware (thx Alex Deucher)
  + amdgpu: update aldebaran firmware (thx Alex Deucher)
  + Update AMD cpu microcode (thx John Allen)
  + intel: avs: Add topology file for I2S Analog Devices 4567 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Nuvoton 8825 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Maxim 98927 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Maxim 98373 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Maxim 98357a (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Dialog 7219 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 5663 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 5640 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 5514 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 298 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 286 (thx Cezary Rojewski)
  + intel: avs: Add topology file for I2S Realtek 274 (thx Cezary Rojewski)
  + intel: avs: Add topology file for Digital Microphone Array (thx Cezary Rojewski)
  + intel: avs: Add topology file for HDMI codecs (thx Cezary Rojewski)
  + intel: avs: Add topology file for HDAudio codecs (thx Cezary Rojewski)
  + intel: avs: Update AudioDSP base firmware for APL-based platforms (thx Cezary Rojewski)
  + Add ISH firmware file for Intel Lunar Lake platform (thx Zhang Lixu)
  + amdgpu: update DMCUB to v0.0.224.0 for Various AMDGPU Asics (thx Fangzhi Zuo)
  + cirrus: cs35l41: Update various firmware for ASUS laptops
    using CS35L41 (thx Stefan Binding)
  + amdgpu: Update ISP FW for isp v4.1.1 (thx Pratap Nirujogi)
  + mediatek: Update MT8173 VPU firmware to v1.2.0 (thx Irui Wang)
  + qcom: Add AIC100 firmware files (thx Jeffrey Hugo)
  + amlogic: Update bluetooth firmware binary (thx Yang Li)
  + Update firmware file for Intel BlazarU core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Magnetor core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Solar core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Pulsar core (thx Kiran K)
  + rtl_bt: Update RTL8822C BT UART firmware to 0xB5D6_6DCB (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT USB firmware to 0xAED6_6DCB (thx Hilda Wu)
  + amdgpu: update DMCUB to v0.0.222.0 for DCN314 (thx Hamza Mahfooz)
  + iwlwifi: add ty/So/Ma firmwares for core88-87 release (thx Miri Korenblit)
  + iwlwifi: update cc/Qu/QuZ firmwares for core88-87 release (thx Miri Korenblit)
  + add new cc33xx firmware for cc33xx chips (thx Sabeeh Khan)
  + cirrus: cs35l56: Update firmware for Cirrus CS35L56 for ASUS
    UM5606 laptop (thx Simon Trimmer)

* Thu Jun 13 2024 Cronbuild Service <cronbuild@altlinux.org> 20240612-alt1
- upstream changes (GIT 776320a9):
  + cirrus: cs35l56: Update firmware for Cirrus CS35L56 for various
    ASUS laptops (thx Simon Trimmer)
  + Add firmware for Lenovo Thinkbooks (thx Stefan Binding)

* Wed Jun 05 2024 Cronbuild Service <cronbuild@altlinux.org> 20240604-alt1
- upstream changes (GIT 22643bb4):
  + amdgpu: update yellow carp firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.4 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.2 firmware (thx Alex Deucher)
  + amdgpu: update navi10 firmware (thx Alex Deucher)
  + amdgpu: update raven2 firmware (thx Alex Deucher)
  + amdgpu: update raven firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.3 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.3 firmware (thx Alex Deucher)
  + amdgpu: update VCN 3.1.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.5 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update vega20 firmware (thx Alex Deucher)
  + amdgpu: update vega12 firmware (thx Alex Deucher)
  + amdgpu: update vega10 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: update smu 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware (thx Alex Deucher)
  + amdgpu: update picasso firmware (thx Alex Deucher)
  + amdgpu: update beige goby firmware (thx Alex Deucher)
  + amdgpu: update vangogh firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware (thx Alex Deucher)
  + amdgpu: update green sardine firmware (thx Alex Deucher)
  + amdgpu: update navy flounder firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.11 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.4 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.2 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.1 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.4 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.1 firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.5 firmware (thx Alex Deucher)
  + amdgpu: update PSP 14.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.5.0 firmware (thx Alex Deucher)
  + amdgpu: update navi14 firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update GC 9.4.3 firmware (thx Alex Deucher)
  + amdgpu: update renoir firmware (thx Alex Deucher)
  + amdgpu: update navi12 firmware (thx Alex Deucher)
  + amdgpu: update aldebaran firmware (thx Alex Deucher)
  + amdgpu: add support for PSP 14.0.1 (thx Mario Limonciello)
  + amdgpu: add support for VPE 6.1.1 (thx Mario Limonciello)
  + amdgpu: add support for VCN 4.0.6 (thx Mario Limonciello)
  + amdgpu: add support for SDMA 6.1.1 (thx Mario Limonciello)
  + amdgpu: add support for GC 11.5.1 (thx Mario Limonciello)
  + amdgpu: Add support for DCN 3.5.1 (thx Mario Limonciello)
  + cnm: update chips&media wave521c firmware. (thx Nas Chung)
  + Add ordinary firmware for RTL8821AU device (thx Larry Finger)

* Mon May 27 2024 Cronbuild Service <cronbuild@altlinux.org> 20240519-alt1
- upstream changes (GIT ec8627ef):
  + amdgpu: add new ISP 4.1.1 firmware (thx Pratap Nirujogi)

* Sun May 12 2024 Cronbuild Service <cronbuild@altlinux.org> 20240510-alt1
- upstream changes (GIT b9d2bf23):
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Alex Hung)
  + Amphion: Update vpu firmware (thx Ming Qian)
  + Update firmware file for Intel BlazarU core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Magnetor core (thx Kiran K)
  + Update firmware file for Intel Bluetooth Solar core (thx Kiran K)
  + i915: Add BMG DMC v2.06 (thx Gustavo Sousa)
  + Add CS35L41 HDA Firmware for Asus HN7306 (thx Stefan Binding)
  + Update firmware tuning for HP Consumer Laptop (thx Stefan Binding)
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Tom Chung)
  + rtl_bt: Update RTL8822C BT UART firmware to 0x0FD6_407B (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT USB firmware to 0x0ED6_407B (thx Hilda Wu)
  + cirrus: cs35l56: Add firmware for Cirrus CS35L56 for various
    ASUS laptops (thx Simon Trimmer)
  + Add firmware and tuning for Lenovo Y770S (thx Stefan Binding)

* Mon Apr 29 2024 Cronbuild Service <cronbuild@altlinux.org> 20240426-alt1
- upstream changes (GIT fc21f475):
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Wayne Lin)
  + Add firmware for Cirrus CS35L56 for various HP laptops (thx Simon Trimmer)
  + i915: Update Xe2LPD DMC to v2.20 (thx Dnyaneshwar Bhadane)
  + Remove Calibration Firmware and Tuning for CS35L41 (thx Stefan Binding)
  + Add firmware for Lenovo Thinkbook 13X (thx Stefan Binding)
  + ASoC: tas2781: Add dsp firmware for Thinkpad ICE-1 laptop (thx Shenghao Ding)
  + amdgpu: add DMCUB 3.5 firmware (thx Alex Deucher)
  + amdgpu: add VPE 6.1.0 firmware (thx Alex Deucher)
  + amdgpu: add VCN 4.0.5 firmware (thx Alex Deucher)
  + amdgpu: add UMSCH 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: add SDMA 6.1.0 firmware (thx Alex Deucher)
  + amdgpu: add PSP 14.0.0  firmware (thx Alex Deucher)
  + amdgpu: add GC 11.5.0 firmware (thx Alex Deucher)
  + amdgpu: update license date (thx Alex Deucher)
  + Montage: update firmware for Mont-TSSE (thx Carrie.Cai)

* Fri Apr 19 2024 Cronbuild Service <cronbuild@altlinux.org> 20240419-alt1
- upstream changes (GIT 055dfa8e):
  + Add tuning parameter configs for CS35L41 Firmware (thx Stefan Binding)
  + Fix firmware names for Laptop SSID 104316a3 (thx Stefan Binding)
  + Add CS35L41 HDA Firmware for Lenovo Legion Slim 7 16ARHA7 (thx Stefan Binding)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris Lu)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + iwlwifi: add gl FW for core87-44 release (thx Miri Korenblit)
  + iwlwifi: add ty/So/Ma firmwares for core87-44 release (thx Miri Korenblit)
  + iwlwifi: update cc/Qu/QuZ firmwares for core87-44 release (thx Miri Korenblit)
  + nvidia: Update Tegra210 XUSB firmware to v50.29 (thx JC Kuo)
  + amdgpu: update beige goby firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.11 firmware (thx Alex Deucher)
  + amdgpu: update gc 11.0.4 firmware (thx Alex Deucher)
  + amdgpu: update navy flounder firmware (thx Alex Deucher)
  + amdgpu: update renoir firmware (thx Alex Deucher)
  + amdgpu: update vcn 4.0.2 firmware (thx Alex Deucher)
  + amdgpu: update sdma 6.0.1 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.4 firmware (thx Alex Deucher)
  + amdgpu: update gc 11.0.1 firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware (thx Alex Deucher)
  + amdgpu: update vega20 firmware (thx Alex Deucher)
  + amdgpu: update yellow carp firmware (thx Alex Deucher)
  + amdgpu: update green sardine firmware (thx Alex Deucher)
  + amdgpu: update vega12 firmware (thx Alex Deucher)
  + amdgpu: update raven2 firmware (thx Alex Deucher)
  + amdgpu: update vcn 4.0.4 firmware (thx Alex Deucher)
  + amdgpu: update smu 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update sdma 6.0.2 firmware (thx Alex Deucher)
  + amdgpu: update ipsp 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update gc 11.0.2 firmware (thx Alex Deucher)
  + amdgpu: update vega10 firmware (thx Alex Deucher)
  + amdgpu: update raven firmware (thx Alex Deucher)
  + amdgpu: update navi14 firmware (thx Alex Deucher)
  + amdgpu: update smu 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update sdma 6.0.3 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update gc 11.0.3 firmware (thx Alex Deucher)
  + amdgpu: update vcn 3.1.2 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.5 firmware (thx Alex Deucher)
  + amdgpu: update gc 10.3.6 firmware (thx Alex Deucher)
  + amdgpu: update navi12 firmware (thx Alex Deucher)
  + amdgpu: update arcturus firmware (thx Alex Deucher)
  + amdgpu: update vangogh firmware (thx Alex Deucher)
  + amdgpu: update navi10 firmware (thx Alex Deucher)
  + amdgpu: update vcn 4.0.3 firmware (thx Alex Deucher)
  + amdgpu: update smu 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: update gc 9.4.3 firmware (thx Alex Deucher)
  + amdgpu: update vcn 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: update smu 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update sdma 6.0.0 firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update gc 11.0.0 firmware (thx Alex Deucher)
  + amdgpu: update  firmware (thx Alex Deucher)
  + amdgpu: update aldebaran firmware (thx Alex Deucher)
  + amdgpu: update psp 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update gc 10.3.7 firmware (thx Alex Deucher)
  + mediatek: Update MT8173 VPU firmware to v1.1.9 (thx Irui Wang)
  + ath10k: WCN3990: hw1.0: add qcm2290 firmware API file (thx Dmitry Baryshkov)
  + ath10k: WCN3990: hw1.0: move firmware back from qcom/ location (thx Dmitry Baryshkov)

* Mon Apr 08 2024 Cronbuild Service <cronbuild@altlinux.org> 20240405-alt1
- upstream changes (GIT 2180c887):
  + i915: Add DG2 HuC 7.10.15 (thx Daniele Ceraolo Spurio)
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Tom Chung)
  + update firmware for en8811h 2.5G ethernet phy (thx SkyLake.Huang)

* Tue Mar 26 2024 Cronbuild Service <cronbuild@altlinux.org> 20240322-alt1
- upstream changes (GIT e068ccf0):
  + mekdiatek: Update mt8186 SOF firmware to v2.0.1 (thx Hailong Fan)
  + Add firmware for Cirrus CS35L56 for Dell laptops (thx Simon Trimmer)
  + Montage: update firmware for Mont-TSSE (thx Carrie.Cai)
  + WHENCE: Link the Raspberry Pi CM4 and 5B to the 4B (thx Peter Robinson)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth BE200 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX210 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Wayne Lin)
  + mediatek: Update MT8173 VPU firmware to v1.1.8 (thx Irui Wang)
  + imx: sdma: update firmware to v3.6/v4.6 (thx Joy Zou)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris Lu)
  + iwlwifi: update 9000-family firmwares to core85-89 (thx Miri Korenblit)
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9D6_17DA (thx Hilda Wu)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris Lu)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + Add CS35L41 HDA Firmware for Lenovo Thinkbook 16P Laptops (thx Stefan Binding)
  + amdgpu: Update VCN firmware binaries (thx Mario Limonciello)
  + Intel IPU2: Add firmware files (thx Sakari Ailus)
  + brcm: Add nvram for the Acer Iconia One 7 B1-750 tablet (thx Hans de Goede)
  + i915: Add Xe2LPD DMC v2.18 (thx Gustavo Sousa)
  + i915: Update MTL DMC v2.21 (thx Gustavo Sousa)

* Tue Feb 20 2024 Cronbuild Service <cronbuild@altlinux.org> 20240220-alt1
- upstream changes (GIT 97b693d2):
  + update firmware for en8811h 2.5G ethernet phy (thx Lucien Jheng)
  + add firmware for MT7996 (thx Shayne Chen)
  + xe: First GuC release for LNL and Xe (thx John Harrison)
  + i915: Add GuC v70.20.0 for ADL-P, DG1, DG2, MTL and TGL (thx John Harrison)
  + Add CS35L41 firmware for Lenovo Legion 7i gen7 laptop (16IAX7) (thx Stefan Binding)
  + brcm: Add nvram for the Asus Memo Pad 7 ME176C tablet (thx Hans de Goede)
  + ice: update ice DDP package to 1.3.36.0 (thx Przemek Kitszel)
  + Intel IPU3 ImgU: Move firmware file under intel/ipu (thx Sakari Ailus)
  + Intel IPU6: Move firmware binaries under ipu/ (thx Sakari Ailus)
  + check_whence: Add a check for duplicate link entries (thx Juerg Haefliger)
  + WHENCE: Clean up section separators (thx Juerg Haefliger)
  + Add CS35L41 firmware for additional ASUS Zenbook 2023 models (thx Stefan Binding)

* Tue Feb 13 2024 Cronbuild Service <cronbuild@altlinux.org> 20240208-alt1
- upstream changes (GIT fbef4d38):
  + panthor: Add initial firmware for Gen10 Arm Mali GPUs (thx Liviu Dudau)
  + amdgpu: DMCUB Updates for DCN321: 7.0.38.0 (thx Aurabindo Pillai)
  + amdgpu: DMCUB updates for Yellow Carp: 4.0.68.0 (thx Aurabindo Pillai)
  + Montage: add firmware for Mont-TSSE (thx Carrie.Cai)

* Tue Feb 06 2024 Cronbuild Service <cronbuild@altlinux.org> 20240203-alt1
- upstream changes (GIT b4b04a5c):
  + amdgpu: update DMCUB to v0.0.203.0 for DCN314 and DCN32 (thx Hamza Mahfooz)
  + wilc1000: update WILC1000 firmware to v16.1.2 (thx Ajay Singh)
  + rtl_nic: add firmware for RTL8126A (thx Heiner Kallweit)
  + intel: Add IPU6 firmware binaries (thx Bingbu Cao)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.37 (thx Kalle Valo)
  + qcom: Add Audio firmware for SM8550 HDK (thx Neil Armstrong)
  + Revert "amdgpu: DMCUB updates for various AMDGPU ASICs" (thx Mario Limonciello)
  + amdgpu: update SMU 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware (thx Alex Deucher)
  + brcm: Add brcmfmac43430-sdio.xxx.txt nvram for the Chuwi Hi8
    (CWI509) tablet (thx Hans de Goede)
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Tom Chung)
  + qcom: Add Audio firmware for SM8650 MTP (thx Neil Armstrong)
  + Add firmware for Cirrus CS35L41 on HP Consumer Laptops (thx Stefan Binding)
  + Intel Bluetooth: Make spacing consistent with rest of WHENCE (thx Diederik de Haas)
  + amdgpu: update raven2 firmware (thx Alex Deucher)
  + amdgpu: update raven firmware (thx Alex Deucher)
  + amdgpu: update SDMA 5.2.7 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update VCN 3.1.2 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 5.2.6 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.5 firmware (thx Alex Deucher)
  + amdgpu: update GC 10.3.6 firmware (thx Alex Deucher)
  + amdgpu: add GC 11.0.1 rlc_1 firmware (thx Alex Deucher)
  + amdgpu: update vega20 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware (thx Alex Deucher)
  + amdgpu: update vega12 firmware (thx Alex Deucher)
  + amdgpu: update vega10 firmware (thx Alex Deucher)
  + amdgpu: update beige goby firmware (thx Alex Deucher)
  + amdgpu: update picasso firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware (thx Alex Deucher)
  + amdgpu: update vangogh firmware (thx Alex Deucher)
  + amdgpu: update navy flounder firmware (thx Alex Deucher)
  + amdgpu: update green sardine firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.11 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.4 firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.2 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.4 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.1 firmware (thx Alex Deucher)
  + amdgpu: update arcturus firmware (thx Alex Deucher)
  + amdgpu: update navi14 firmware (thx Alex Deucher)
  + amdgpu: add VCN 4.0.3 firmware (thx Alex Deucher)
  + amdgpu: add SDMA 4.4.2 firmware (thx Alex Deucher)
  + amdgpu: add SMU 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: add PSP 13.0.6 firmware (thx Alex Deucher)
  + amdgpu: Add GC 9.4.3 firmware (thx Alex Deucher)
  + amdgpu: update renoir firmware (thx Alex Deucher)
  + amdgpu: update VCN 4.0.4 firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.7 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.2 firmware (thx Alex Deucher)
  + amdgpu: update navi12 firmware (thx Alex Deucher)
  + amdgpu: update yellow carp firmware (thx Alex Deucher)
  + amdgpu: update SMU 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.3 firmware (thx Alex Deucher)
  + amdgpu: update PSP 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: update GC 11.0.3 firmware (thx Alex Deucher)
  + amdgpu: update navi10 firmware (thx Alex Deucher)
  + amdgpu: update aldebaran firmware (thx Alex Deucher)
  + Update AMD cpu microcode (thx John Allen)
  + RTL8192E: Remove old realtek WiFi firmware (thx Peter Robinson)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX101 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX203 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX203 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX211 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX211 (thx Lokendra Singh)
  + amdgpu: DMCUB updates for DCN314 (thx Alex Hung)

* Sun Jan 14 2024 Cronbuild Service <cronbuild@altlinux.org> 20240111-alt1
- upstream changes (GIT b3132c18):
  + qcom: Update the firmware for Adreno a630 family of GPUs (thx Akhil P Oommen)
  + cirrus: Add CS35L41 firmware for Legion Slim 7 Gen 8 laptops (thx Vitaly Rodionov)
  + Add firmware for Cirrus CS35L41 for various Dell laptops (thx Stefan Binding)
  + update firmware for qat_4xxx devices (thx Adam Guerin)
  + update firmware for w1u_uart (thx Yang Li)
  + amdgpu: DMCUB updates for DCN314 (thx Rodrigo Siqueira)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX211 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX101 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX203 (thx Lokendra Singh)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX210 (thx Lokendra Singh)

* Fri Jan 05 2024 Cronbuild Service <cronbuild@altlinux.org> 20240105-alt1
- upstream changes (GIT c82c9486):
  + amlogic/bluetooth: add firmware bin of W1 serial soc(w1u_uart) (thx yang.li)
  + add firmware for mediatek bluetooth chip (MT7925) (thx Peter Tsao)
  + add firmware for MT7925 (thx Deren Wu)
  + ASoC: tas2563: Add dsp firmware for laptops or other mobile
    devices (thx Shenghao Ding)
  + rtl_bt: Add firmware and config files for RTL8852BT/RTL8852BE-VT (thx Max Chou)
  + ASoC: tas2781: Add dsp firmware for different laptops (thx Shenghao Ding)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.36 (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: WCN6750 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath11k: IPQ8074 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: WCN3990 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00309- (thx Kalle Valo)
  + ath12k: add new driver and firmware for WCN7850 (thx Kalle Valo)
  + iwlwifi: update gl FW for core80-165 release (thx Miri Korenblit)
  + intel: vsc: Add firmware for Visual Sensing Controller (thx Sakari Ailus)
  + cirrus: Add CS35L41 firmware and tunings for ASUS Zenbook
    2023 Models (thx Stefan Binding)
  + cirrus: Add CS35L41 firmware and tunings for ASUS Zenbook
    2022 Models (thx Stefan Binding)
  + QCA: Add bluetooth firmware nvm files for QCA2066 (thx Zijun Hu)
  + QCA: Update Bluetooth QCA2066 firmware to 2.1.0-00629 (thx Zijun Hu)

* Fri Dec 22 2023 Cronbuild Service <cronbuild@altlinux.org> 20231215-alt1
- upstream changes (GIT c156e6be):
  + amdgpu: DMCUB updates for various AMDGPU ASICs (thx Wayne Lin)
  + qcom: Add Audio firmware for SM8650 QRD (thx Neil Armstrong)
  + qcom: Add Audio firmware for SM8550 QRD (thx Neil Armstrong)

* Thu Dec 14 2023 Cronbuild Service <cronbuild@altlinux.org> 20231212-alt1
- upstream changes (GIT c52dc252):
  + wfx: update to firmware 3.17 (thx J?r?me Pouiller)
  + wfx: fix broken firmware (thx J?r?me Pouiller)

* Thu Dec 07 2023 Cronbuild Service <cronbuild@altlinux.org> 20231205-alt1
- upstream changes (GIT c004dbee):
  + Update AMD cpu microcode (thx John Allen)

* Wed Dec 06 2023 Michael Shigorin <mike@altlinux.org> 20231204-alt2
- split off qcom, mrvl, mellanox subpackages:
  these hold huge firmwares for rare SoCs (e.g. robotics, 100GE switches)
- minor spec cleanup (see also ALT#46206)

* Mon Dec 04 2023 Cronbuild Service <cronbuild@altlinux.org> 20231204-alt1
- upstream changes (GIT b9d971b9):
  + cxgb4: Update firmware to revision 1.27.5.0 (thx Rahul Lakkireddy)
  + add firmware for en8811h 2.5G ethernet phy (thx SkyLake.Huang)
  + s5p-mfc: Add MFC v12 Firmware (thx Aakarsh Jain)

* Tue Nov 28 2023 Anton Midyukov <antohami@altlinux.org> 20231128-alt1
- configuration changes:
  + Revert "copy-firmware.sh: do'nt require rdfind";
  + spec: make install-nodedup
- upstream changes (GIT 5aadb590):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDFC8_145F (thx Hilda Wu)
  + ice: update ice DDP wireless_edge package to 1.3.13.0 (thx Przemek Kitszel)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris Lu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris Lu)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + Makefile, copy-firmware: Use portable "command -v" to detect
    installed programs (thx Eli Schwartz)
  + amdgpu: update DMCUB firmware to 0.0.194.0 for DCN321 and DCN32 (thx Tom Chung)
  + powervr: add firmware for Imagination Technologies AXE-1-16M GPU (thx Frank Binns)
  + ice: update ice DDP comms package to 1.3.45.0 (thx Przemek Kitszel)
  + ice: update ice DDP package to 1.3.35.0 (thx Przemek Kitszel)
  + mediatek: Remove an unused packed library (thx Jason Chen)

* Tue Nov 21 2023 Cronbuild Service <cronbuild@altlinux.org> 20231120-alt1
- upstream changes (GIT 9552083a):
  + mediatek: Sync shared memory structure changes (thx Jason Chen)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth BE200 (thx Kiran K)
  + i915: Update MTL DMC to v2.19 (thx Gustavo Sousa)
  + iwlwifi: fix for the new FWs from core83-55 release (thx Gregory Greenman)

* Thu Nov 16 2023 Anton Midyukov <antohami@altlinux.org> 20231115-alt2
- copy-firmware.sh: do'nt require rdfind

* Wed Nov 15 2023 Anton Midyukov <antohami@altlinux.org> 20231115-alt1
- upstream changes (GIT 124b6639):
  + iwlwifi: add new FWs from core83-55 release (thx Gregory Greenman)
  + iwlwifi: update cc/Qu/QuZ firmwares for core83-55 release (thx Gregory Greenman)
  + add firmware for mt7988 internal 2.5G ethernet phy (thx SkyLake.Huang)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Magnetor Intel
    Bluetooth AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX101 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for SolarF Intel Bluetooth
    AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Solar Intel Bluetooth
    AX210 (thx Kiran K)

* Thu Nov 02 2023 Cronbuild Service <cronbuild@altlinux.org> 20231030-alt1
- upstream changes (GIT 2b304bfe):
  + Intel Bluetooth: Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth
    Magnetor AX101 (thx Kiran K)

* Fri Oct 27 2023 Cronbuild Service <cronbuild@altlinux.org> 20231026-alt1
- upstream changes (GIT 2ceaa29d):
  + Intel Bluetooth: Update firmware file for Intel Bluetooth AX203 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth
    Magnetor AX201 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth
    Magnetor AX211 (thx Kiran K)
  + Intel Bluetooth: Update firmware file for Intel Bluetooth BE200 (thx Kiran K)
  + rtl_nic: update firmware of RTL8156B (thx Hayes Wang)

* Thu Oct 19 2023 Cronbuild Service <cronbuild@altlinux.org> 20231019-alt1
- upstream changes (GIT d983107a):
  + Update AMD cpu microcode (thx John Allen)
  + amdgpu: update SMU 13.0.0 firmware (thx Alex Deucher)
  + add Amlogic bluetooth firmware (thx yang.li)
  + i915: Add GuC v70.13.1 for DG2, TGL, ADL-P and MTL (thx John Harrison)
  + iwlwifi: add a missing FW from core80-39 release (thx Gregory Greenman)

* Fri Oct 13 2023 Cronbuild Service <cronbuild@altlinux.org> 20231006-alt1
- upstream changes (GIT 7727f7e3):
  + WHENCE: add symlink for BananaPi M64 (thx Peter Robinson)

* Fri Oct 06 2023 Cronbuild Service <cronbuild@altlinux.org> 20231004-alt1
- upstream changes (GIT 5105ff4b):
  + Add firmware file for Intel Bluetooth AX211 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX201 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX211 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX210 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth 9560 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth 9260 (thx Lokendra Singh)
  + i915: Update MTL DMC to v2.17 (thx Gustavo Sousa)
  + iwlwifi: add FWs for new GL and MA device types with multiple
    RF modules (thx Gregory Greenman)

* Thu Sep 28 2023 Cronbuild Service <cronbuild@altlinux.org> 20230926-alt1
- upstream changes (GIT 8b855f37):
  + amd_pmf: Add initial PMF TA for Smart PC Solution Builder (thx Shyam Sundar S K)
  + Update FW files for MRVL PCIE 8997 chipsets (thx Neeraj Kale)
  + rtl_bt: Update RTL8851B BT USB firmware to 0x048A_D230 (thx Max Chou)
  + iwlwifi: add new FWs from core81-65 release (thx Gregory Greenman)
  + iwlwifi: update cc/Qu/QuZ firmwares for core81-65 release (thx Gregory Greenman)

* Fri Sep 22 2023 Cronbuild Service <cronbuild@altlinux.org> 20230918-alt1
- upstream changes (GIT 3672ccab):
  + amd-ucode: Add note on fam19h warnings (thx Sandipan Das)
  + i915: update MTL HuC to version 8.5.4 (thx Daniele Ceraolo Spurio)
  + amdgpu: update DMCUB to 0.0.183.0 for various AMDGPU ASICs (thx Stylon Wang)

* Thu Sep 07 2023 Cronbuild Service <cronbuild@altlinux.org> 20230907-alt1
- upstream changes (GIT dfa11466):
  + add link to sc8280xp audioreach firmware (thx Srinivas Kandagatla)
  + qcom: sm8250: add RB5 sensors DSP firmware (thx Dmitry Baryshkov)
  + qcom: Update vpu-1.0 firmware (thx Dmitry Baryshkov)
  + qcom: sm8250: update DSP firmware (thx Dmitry Baryshkov)
  + qcom: add firmware for the onboard WiFi on qcm2290 / qrb4210 (thx Dmitry Baryshkov)
  + qcom: add venus firmware files for v6.0 (thx Dmitry Baryshkov)
  + qcom: add firmware for QRB4210 platforms (thx Dmitry Baryshkov)
  + qcom: add firmware for QCM2290 platforms (thx Dmitry Baryshkov)
  + qcom: add GPU firmware for QCM2290 / QRB2210 (thx Dmitry Baryshkov)
  + ath10k/WCN3990: move wlanmdsp to qcom/sdm845 (thx Dmitry Baryshkov)
  + WHENCE: Don't compress qcom json files (thx Juerg Haefliger)
  + WHENCE: amd-ucode: Use new RawFile keyword (thx Juerg Haefliger)
  + check_whence: Recognize RawFile keyword (thx Juerg Haefliger)

* Fri Sep 01 2023 Cronbuild Service <cronbuild@altlinux.org> 20230831-alt1
- upstream changes (GIT 6c097314):
  + check_whence: reformat using python black (thx Mario Limonciello)
  + i915: Update MTL DMC to v2.16 (thx Gustavo Sousa)
  + copy-firmware: Introduce 'RawFile' keyword (thx Juerg Haefliger)
  + copy-firmware: Support additional compressor options (thx Juerg Haefliger)
  + Update firmware file for Intel Bluetooth AX203 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX211 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX210 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX200 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX201 (thx Lokendra Singh)
  + update firmware for qat_4xxx devices (thx Adam Guerin)
  + Update AMD SEV firmware (thx John Allen)
  + amdgpu: update DMCUB to 0.0.181.0 for various AMDGPU ASICs (thx Hamza Mahfooz)
  + rtw89: 8852b: update fw to v0.29.29.3 (thx Chin-Yen Lee)
  + rtw89: 8851b: update fw to v0.29.41.2 (thx Chin-Yen Lee)
  + i915: add GSC 102.0.0.1655 for MTL (thx Daniele Ceraolo Spurio)
  + amdgpu: DMCUB updates for various AMDGPU asics (thx Wayne Lin)

* Tue Aug 15 2023 Anton Midyukov <antohami@altlinux.org> 20230814-alt1
- upstream changes (GIT 0e048b06):
  + amdgpu: DMCUB updates for various AMDGPU asics (thx Stylon Wang)
  + Revert "amdgpu: partially revert firmware for GC 11.0.0 and
    GC 11.0.2" (thx Mario Limonciello)

* Thu Aug 10 2023 Anton Midyukov <antohami@altlinux.org> 20230809-alt1
- configuration changes:
  + update.sh: fix check_link
- upstream changes (GIT 789aa815):
  + amdgpu: partially revert firmware for GC 11.0.0 and GC 11.0.2 (thx Mario Limonciello)
  + Update AMD cpu microcode (thx John Allen)
  + rtl_bt: Add firmware v2 file for RTL8852C (thx Hilda Wu)
  + Revert "rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225" (thx Hilda Wu)
  + amdgpu: DMCUB updates for various AMDGPU asics (thx Tom Chung)
  + cxgb4: Update firmware to revision 1.27.4.0 (thx Rahul Lakkireddy)

* Mon Jul 24 2023 Cronbuild Service <cronbuild@altlinux.org> 20230714-alt1
- upstream changes (GIT 59fbffa9):
  + amdgpu: update VCN 4.0.0 firmware (thx Alex Deucher)
  + amdgpu: add initial SMU 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: add initial SDMA 6.0.3 firmware (thx Alex Deucher)
  + amdgpu: add initial PSP 13.0.10 firmware (thx Alex Deucher)
  + amdgpu: add initial GC 11.0.3 firmware (thx Alex Deucher)
  + Update AMD fam17h cpu microcode (thx John Allen)
  + Update AMD cpu microcode (thx John Allen)
  + amdgpu: update green sardine VCN firmware (thx Alex Deucher)
  + amdgpu: update renoir VCN firmware (thx Alex Deucher)
  + amdgpu: update raven VCN firmware (thx Alex Deucher)
  + amdgpu: update raven2 VCN firmware (thx Alex Deucher)
  + amdgpu: update Picasso VCN firmware (thx Alex Deucher)
  + amdgpu: update DMCUB to v0.0.175.0 for various AMDGPU ASICs (thx Alan Liu)
  + wfx: update to firmware 3.16.1 (thx J?r?me Pouiller)
  + mediatek: Update mt8195 SCP firmware to support 10bit mode (thx Yunfei Dong)
  + i915: update DG2 GuC to v70.8.0 (thx Daniele Ceraolo Spurio)
  + i915: update to GuC 70.8.0 and HuC 8.5.1 for MTL (thx Daniele Ceraolo Spurio)
  + cirrus: Add CS35L41 firmware for ASUS ROG 2023 Models (thx Stefan Binding)

* Tue Jul 11 2023 Cronbuild Service <cronbuild@altlinux.org> 20230705-alt1
- upstream changes (GIT d3f66064):
  + Partially revert "amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5" (thx Hamza Mahfooz)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris Lu)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + Update firmware file for Intel Bluetooth AX203 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX211 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX210 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX200 (thx Lokendra Singh)
  + Update firmware file for Intel Bluetooth AX201 (thx Lokendra Singh)
  + check_whence: Check link targets are valid (thx Adam Sampson)
  + iwlwifi: add new FWs from core80-39 release (thx Gregory Greenman)
  + iwlwifi: update cc/Qu/QuZ firmwares for core80-39 release (thx Gregory Greenman)
  + qcom: Add Audio firmware for SC8280XP X13s (thx Srinivas Kandagatla)
  + Makefile, copy-firmware: support xz/zstd compressed firmware (thx Emil Velikov)
  + copy-firmware: silence the last shellcheck warnings (thx Emil Velikov)
  + copy-firmware: drop obsolete backticks, quote (thx Emil Velikov)
  + copy-firmware: tweak sed invocation (thx Emil Velikov)
  + copy-firmware: quote deskdir and dirname (thx Emil Velikov)
  + check_whence: error if symlinks are in-tree (thx Emil Velikov)
  + check_whence: error if File: is actually a link (thx Emil Velikov)
  + check_whence: strip quotation marks (thx Emil Velikov)
  + wilc1000: update WILC1000 firmware to v16.0 (thx Ajay Singh)
  + ice: update ice DDP wireless_edge package to 1.3.10.0 (thx Shekhar Deb)
  + amdgpu: DMCUB updates for DCN 3.1.4 and 3.1.5 (thx Rodrigo Siqueira)
  + amdgpu: update DMCUB to v0.0.172.0 for various AMDGPU ASICs (thx Hamza Mahfooz)
  + qcom: Update the microcode files for Adreno a630 GPUs. (thx Dmitry Baryshkov)
  + qcom: sdm845: rename the modem firmware (thx Dmitry Baryshkov)
  + qcom: sdm845: update remoteproc firmware (thx Dmitry Baryshkov)

* Mon Jun 12 2023 Cronbuild Service <cronbuild@altlinux.org> 20230607-alt1
- upstream changes (GIT 1cd1c871):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDAC7_480D (thx Hilda Wu)
  + rtl_bt: Update RTL8852C BT USB firmware to 0x040D_7225 (thx Hilda Wu)
  + amdgpu: DMCUB updates for various AMDGPU asics (thx Stylon Wang)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris.Lu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris.Lu)
  + i915: Add HuC v8.5.0 for MTL (thx Daniele Ceraolo Spurio)
  + mediatek: Update mt8195 SCP firmware to support hevc (thx Yunfei Dong)

* Tue Jun 06 2023 Cronbuild Service <cronbuild@altlinux.org> 20230531-alt1
- upstream changes (GIT fc90c59b):
  + qcom: apq8016: add Dragonboard 410c WiFi and modem firmware (thx Dmitry Baryshkov)
  + cirrus: Add firmware for new Asus ROG Laptops (thx Stefan Binding)

* Tue May 30 2023 Cronbuild Service <cronbuild@altlinux.org> 20230523-alt1
- upstream changes (GIT d11ae984):
  + brcm: Add symlinks from Pine64 devices to AW-CM256SM.txt (thx Diederik de Haas)
  + amdgpu: Update GC 11.0.1 and 11.0.4 (thx Mario Limonciello)
  + rtw89: 8851b: add firmware v0.29.41.0 (thx Ping-Ke Shih)
  + amdgpu: update yellow carp firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update navi14 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update navi12 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update vega20 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update vega12 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update navi10 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update vega10 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update PSP 13.0.11 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 11.0.4 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update SDMA 6.0.1 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update PSP 13.0.4 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 11.0.1 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update 13.0.8 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 10.3.7 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update vangogh firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update VCN 4.0.4 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update SMU 13.0.7 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update PSP 13.0.7 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 11.0.2 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update renoir firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update VCN 4.0.0 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update SMU 13.0.0 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update PSP 13.0.0 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 11.0.0 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update green sardine firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update beige goby firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update arcturus firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update vcn 3.1.2 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update psp 13.0.5 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update GC 10.3.6 firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update navy flounder firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: update aldebaran firmware for amd.5.5 release (thx Alex Deucher)
  + amdgpu: DMCUB updates for various AMDGPU asics (thx Aurabindo Pillai)
  + ice: update ice DDP comms package to 1.3.40.0 (thx Shekhar Deb)

* Mon May 22 2023 Cronbuild Service <cronbuild@altlinux.org> 20230517-alt1
- upstream changes (GIT 601c1813):
  + rtlwifi: Add firmware v6.0 for RTL8192FU (thx Bitterblue Smith)
  + rtlwifi: Update firmware for RTL8188EU to v28.0 (thx Bitterblue Smith)

* Tue May 16 2023 Cronbuild Service <cronbuild@altlinux.org> 20230515-alt1
- upstream changes (GIT 51290942):
  + cirrus: Add firmware and tuning files for HP G10 series laptops (thx Vitaly Rodionov)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris.Lu)
  + WHENCE: Cleanup Realtek BT firmware provenance (thx Juerg Haefliger)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + cnm: update chips&media wave521c firmware. (thx Nas Chung)
  + cirrus: Add firmware and tuning files for Lenovo ThinkPad P1
    Gen 6 (thx Vitaly Rodionov)
  + check_whence: error on directory listed as File (thx Emil Velikov)
  + check_whence: error on duplicate file entries (thx Emil Velikov)
  + WHENCE: comment out duplicate MediaTek firmware (thx Emil Velikov)
  + i915: Add GuC v70.6.6 for MTL (thx John Harrison)

* Thu May 04 2023 Cronbuild Service <cronbuild@altlinux.org> 20230502-alt1
- upstream changes (GIT 312c61f5):
  + amdgpu: update DCN 3.1.6 DMCUB firmware (thx Alex Deucher)
  + rtl_bt: Update RTL8852B BT USB firmware to 0xDBC6_B20F (thx Hilda Wu)
  + rtl_bt: Update RTL8761B BT USB firmware to 0xDFC6_D922 (thx Hilda Wu)
  + rtl_bt: Update RTL8761B BT UART firmware to 0x9DC6_D922 (thx Hilda Wu)
  + rtl_nic: update firmware of USB devices (thx Hayes Wang)
  + Update firmware file for Intel Bluetooth AX200 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX201 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX203 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX211 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX210 (thx Aniket Sahu)
  + update firmware for MT7981 (thx Shayne Chen)
  + qca: Update firmware files for BT chip WCN6750 (thx sampnimm)

* Wed Apr 19 2023 Cronbuild Service <cronbuild@altlinux.org> 20230418-alt1
- upstream changes (GIT 8451c2b1):
  + mt76xx: Move the old Mediatek WiFi firmware to mediatek (thx Peter Robinson)
  + rtl_bt: Add firmware and config files for RTL8851B (thx Max Chou)
  + Update AMD cpu microcode (thx John Allen)
  + add firmware for MT7981 (thx Shayne Chen)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Sean Wang)
  + update qat firmware (thx Adam Guerin)
  + Add firmware for Cirrus CS35L41 on Lenovo Laptops (thx Stefan Binding)

* Thu Apr 13 2023 Cronbuild Service <cronbuild@altlinux.org> 20230406-alt1
- upstream changes (GIT 86da2ac9):
  + update firmware for MT7916 (thx Shayne Chen)
  + rtw89: 8852b: update format-1 fw to v0.29.29.1 (thx Ping-Ke Shih)
  + rtw89: 8852c: update fw to v0.27.56.13 (thx Chin-Yen Lee)
  + ath11k: WCN6855 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: WCN6750 hw1.0: update to
    WLAN.MSL.1.0.1-01160-QCAMSLSWPLZ-1 (thx Kalle Valo)
  + ath11k: QCN9074 hw1.0: update to
    WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ8074 hw2.0: update to
    WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ8074 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: IPQ6018 hw1.0: update to
    WLAN.HK.2.7.0.1-01744-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ6018 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA99X0 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)

* Thu Apr 06 2023 Cronbuild Service <cronbuild@altlinux.org> 20230403-alt1
- upstream changes (GIT 2e92a49f):
  + nvidia: update Tu10x and Tu11x signed firmware to support newer
    Turing HW (thx Gourav Samaiya)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Sean Wang)
  + Amphion: Update vpu firmware (thx Ming Qian)
  + iwlwifi: add new FWs from core78-32 release (thx Gregory Greenman)
  + iwlwifi: update 9000-family firmwares to core78-32 (thx Gregory Greenman)
  + amdgpu: Update SDMA 6.0.1 firmware (thx Mario Limonciello)
  + amdgpu: Add PSP 13.0.11 firmware (thx Mario Limonciello)
  + amdgpu: Update PSP 13.0.4 firmware (thx Mario Limonciello)
  + amdgpu: Update GC 11.0.1 firmware (thx Mario Limonciello)
  + amdgpu: Update DCN 3.1.4 firmware (thx Mario Limonciello)
  + amdgpu: Add GC 11.0.4 firmware (thx Mario Limonciello)
  + rtw88: 8822c: Update normal firmware to v9.9.15 (thx Po-Hao Huang)

* Wed Mar 22 2023 Cronbuild Service <cronbuild@altlinux.org> 20230320-alt1
- upstream changes (GIT bcdcfbcf):
  + Update firmware file for Intel Bluetooth AX101 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth 9462 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth 9560 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX203 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX211 (thx Aniket Sahu)
  + Update firmware file for Intel Bluetooth AX210 (thx Aniket Sahu)
  + add firmware files for NXP BT chipsets (thx Neeraj Kale)
  + rtw89: 8852b: update format-1 fw to v0.29.29.0 (thx Ping-Ke Shih)
  + rtw89: 8852b: add format-1 fw v0.29.26.0 (thx Ping-Ke Shih)
  + rtw89: 8852b: rollback firmware to v0.27.32.1 (thx Ping-Ke Shih)
  + i915: Update MTL DMC to v2.12 (thx Gustavo Sousa)
  + i915: Update ADLP DMC to v2.19 (thx Gustavo Sousa)
  + mediatek: Update mt8192/mt8195 SCP firmware to support MM21
    and MT21 (thx Tinghan Shen)

* Thu Mar 16 2023 Cronbuild Service <cronbuild@altlinux.org> 20230313-alt1
- upstream changes (GIT c761dbe8):
  + iwlwifi: update core69 and core72 firmwares for So device (thx Gregory Greenman)
  + qat: update licence text (thx Fiona Trahe)
  + rtl_bt: Update RTL8822C BT USB firmware to 0x0CC6_D2E3 (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT UART firmware to 0x05C6_D2E3 (thx Hilda Wu)

* Wed Mar 08 2023 Cronbuild Service <cronbuild@altlinux.org> 20230301-alt1
- upstream changes (GIT 5adebcfa):
  + WHENCE: remove duplicate File entries (thx Emil Velikov)
  + WHENCE: remove trailing white space (thx Emil Velikov)
  + add fw for qat_4xxx (thx Adam Guerin)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Jing Cai)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + iwlwifi: update core69 and core72 firmwares for Ty device (thx Gregory Greenman)
  + rtlwifi: Add firmware v16.0 for RTL8710BU aka RTL8188GU (thx Bitterblue Smith)
  + brcm: Add nvram for the Lenovo Yoga Book X90F / X90L convertible (thx Hans de Goede)
  + brcm: Fix Xiaomi Inc Mipad2 nvram/.txt file macaddr (thx Hans de Goede)
  + brcm: Add nvram for the Advantech MICA-071 tablet (thx Hans de Goede)

* Wed Mar 01 2023 Cronbuild Service <cronbuild@altlinux.org> 20230227-alt1
- upstream changes (GIT 60971a64):
  + rtl_bt: Update RTL8852C BT USB firmware to 0xD7B8_FABF (thx Hilda Wu)
  + rtl_bt: Add firmware and config files for RTL8821CS (thx Max Chou)
  + rtw89: 8852b: update fw to v0.29.29.0 (thx Ping-Ke Shih)
  + rtw89: 8852b: update fw to v0.29.26.0 (thx Ping-Ke Shih)
  + liquidio: remove lio_23xx_vsw.bin (thx Chickles, Derek)

* Wed Feb 15 2023 Cronbuild Service <cronbuild@altlinux.org> 20230215-alt1
- upstream changes (GIT 83f1d778):
  + intel: avs: Add AudioDSP base firmware for CNL-based platforms (thx Cezary Rojewski)
  + intel: avs: Add AudioDSP base firmware for APL-based platforms (thx Cezary Rojewski)
  + intel: avs: Add AudioDSP base firmware for SKL-based platforms (thx Cezary Rojewski)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.23 (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: WCN6750 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath11k: IPQ5018 hw1.0: add to
    WLAN.HK.2.6.0.1-00861-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ5018 hw1.0: add board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-sdio-6.bin to version
    WLAN.RMH.4.4.1-00174 (thx Kalle Valo)
  + ath10k: WCN3990 hw1.0: update board-2.bin (thx Kalle Valo)
  + cnm: update chips&media wave521c firmware. (thx Nas Chung)
  + amdgpu: Update GC 11.0.1 firmware (thx Mario Limonciello)
  + intel: catpt: Add AudioDSP base firmware for BDW platforms (thx Cezary Rojewski)
  + Update AMD cpu microcode (thx John Allen)
  + brcm: revert firmware files for Cypress devices (thx Arend van Spriel)
  + brcm: restore previous firmware file for BCM4329 device (thx Arend van Spriel)
  + rtw88: 8822c: Update normal firmware to v9.9.14 (thx Chin-Yen Lee)
  + i915: Add DMC v2.11 for MTL (thx Gustavo Sousa)
  + Add firmware for Cirrus CS35L41 on UM3402 ASUS Laptop (thx Stefan Binding)
  + Add missing tuning files for HP Laptops using Cirrus Amps (thx Stefan Binding)
  + i915: Add DMC v2.18 for ADLP (thx Gustavo Sousa)

* Wed Jan 25 2023 Cronbuild Service <cronbuild@altlinux.org> 20230124-alt1
- upstream changes (GIT 5c11a374):
  + amdgpu: Add VCN 4.0.2 firmware (thx Mario Limonciello)
  + amdgpu: Add PSP 13.0.4 firmware (thx Mario Limonciello)
  + amdgpu: Add SDMA 6.0.1 fimware (thx Mario Limonciello)
  + amdgpu: Add GC 11.0.1 firmware (thx Mario Limonciello)
  + amdgpu: Add DCN 3.1.4 firmware (thx Mario Limonciello)
  + iwlwifi: remove old intermediate 5.15+ firmwares (thx Peter Robinson)
  + iwlwifi: remove 5.10 and 5.15 intermediate old firmwares (thx Peter Robinson)
  + iwlwifi: remove 5.4 and 5.10 intermediate old firmwares (thx Peter Robinson)
  + iwlwifi: remove 4.19 and 5.4 intermediate old firmwares (thx Peter Robinson)
  + iwlwifi: remove old unsupported older than 4.14 LTS (thx Peter Robinson)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris.Lu)
  + amdgpu: update vangogh firmware (thx Alex Deucher)

* Wed Jan 18 2023 Cronbuild Service <cronbuild@altlinux.org> 20230117-alt1
- upstream changes (GIT 7e4f0eda):
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + brcm: add configuration files for CyberTan WC121 (thx Andreas Kemnade)
  + qcom: add firmware files for Adreno A200 (thx Dmitry Baryshkov)
  + rtw89: 8852c: update fw to v0.27.56.10 (thx Ping-Ke Shih)
  +  QCA: Add Bluetooth firmware for QCA2066 (thx Tim Jiang)

* Thu Jan 12 2023 Cronbuild Service <cronbuild@altlinux.org> 20230110-alt1
- upstream changes (GIT a1ad1d5b):
  + amdgpu: add VCN4.0.4 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: add SMU13.0.7 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: add SDMA6.0.2 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: add PSP13.0.7 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: add GC11.0.2 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: add DCN3.2.1 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: update VCN4.0.0 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: update SMU13.0.0 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: update SDMA6.0.0 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: update PSP13.0.0 firmware from amd-5.4 (thx Alex Deucher)
  + amdgpu: update GC11.0.0 firmware from amd-5.4 (thx Alex Deucher)
  + iwlwifi: add new FWs from core76-35 release (thx Gregory Greenman)
  + iwlwifi: update cc/Qu/QuZ firmwares for core76-35 release (thx Gregory Greenman)
  + iwlwifi: add new FWs from core75-47 release (thx Gregory Greenman)
  + iwlwifi: update 9000-family firmwares to core75-47 (thx Gregory Greenman)
  + amdgpu: update renoir DMCUB firmware (thx Alex Deucher)
  + amdgpu: Update renoir PSP firmware (thx Alex Deucher)
  + amdgpu: update copyright date for LICENSE.amdgpu (thx Alex Deucher)

* Wed Jan 04 2023 Cronbuild Service <cronbuild@altlinux.org> 20230104-alt1
- upstream changes (GIT 4ee20147):
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Chris.Lu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Chris.Lu)
  + cxgb4: Update firmware to revision 1.27.1.0 (thx Rahul Lakkireddy)
  + qca: Update firmware files for BT chip WCN6750 (thx sampnimm)

* Thu Dec 22 2022 Cronbuild Service <cronbuild@altlinux.org> 20221216-alt1
- upstream changes (GIT 52261d03):
  + rtw89: 8852c: update fw to v0.27.56.9 (thx Chin-Yen Lee)
  + rtw89: 8852c: update fw to v0.27.56.8 (thx Ping-Ke Shih)

* Wed Dec 14 2022 Cronbuild Service <cronbuild@altlinux.org> 20221213-alt1
- upstream changes (GIT f3c283e1):
  + amdgpu: updated navi10 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated yellow carp firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated raven2 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated raven firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated PSP 13.0.8 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated GC 10.3.7 RLC firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated vega20 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated PSP 13.0.5 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: add VCN 4.0.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: add SMU 13.0.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: Add SDMA 6.0.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: add PSP 13.0.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: add GC 11.0.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: add DCN 3.2.0 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated vega10 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated beige goby firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated dimgrey cavefish firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated vangogh firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated picasso firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated navy flounder firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated green sardine firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated sienna cichlid firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated arcture firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated navi14 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated renoir firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated navi12 firmware for amd-5.4 (thx Alex Deucher)
  + amdgpu: updated aldebaran firmware for amd-5.4 (thx Alex Deucher)
  + sr150 : Add NXP SR150 UWB firmware (thx Manjunatha Venkatesh)
  + brcm: add/update firmware files for brcmfmac driver (thx Arend van Spriel)

* Wed Dec 07 2022 Cronbuild Service <cronbuild@altlinux.org> 20221202-alt1
- upstream changes (GIT 16c9630e):
  + rtl_bt: Update RTL8821C BT(USB I/F) FW to 0x75b8_f098 (thx Max Chou)

* Thu Dec 01 2022 Cronbuild Service <cronbuild@altlinux.org> 20221129-alt1
- upstream changes (GIT 80ed874a):
  + amdgpu: update sdma_5.2.7 firmware (thx Alex Deucher)
  + QCA: Add Bluetooth firmware for WCN785x This commit will add
    required Bluetooth firmware files for QCA WCN785x. The image
    version is 2.0.0-00515. (thx Rocky Liao)

* Wed Nov 23 2022 Cronbuild Service <cronbuild@altlinux.org> 20221123-alt1
- upstream changes (GIT cdf9499c):
  + update firmware for MT7916 (thx Shayne Chen)
  + update firmware for MT7915 (thx Shayne Chen)
  + amdgpu: update green sardine DMCUB firmware (thx Alex Deucher)
  + i915: Add DMC v2.10 for MTL (thx Madhumitha Tolakanahalli Pradeep)

* Wed Nov 16 2022 Cronbuild Service <cronbuild@altlinux.org> 20221110-alt1
- upstream changes (GIT daff4049):
  + update firmware for MT7986 (thx Shayne Chen)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Sean Wang)
  + update firmware for MT7921 WiFi device (thx Deren Wu)

* Thu Nov 10 2022 Cronbuild Service <cronbuild@altlinux.org> 20221109-alt1
- upstream changes (GIT 60310c2d):
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + amdgpu: update DMCUB firmware for DCN 3.1.6 (thx Alex Deucher)
  + rtl_bt: Update RTL8822C BT UART firmware to 0xFFB8_ABD6 (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT USB firmware to 0xFFB8_ABD3 (thx Hilda Wu)
  + WHENCE: mrvl: prestera: Add WHENCE entries for newly updated
    4.1 FW images (thx Oleksandr Mazur)
  + mrvl: prestera: Update Marvell Prestera Switchdev FW to v4.1 (thx Oleksandr Mazur)
  + iwlwifi: add new FWs from core74_pv-60 release (thx Gregory Greenman)
  + qcom: drop split a530_zap firmware file (thx Dmitry Baryshkov)
  + qcom/vpu-1.0: drop split firmware in favour of the mbn file (thx Dmitry Baryshkov)
  + qcom/venus-4.2: drop split firmware in favour of the mbn file (thx Dmitry Baryshkov)
  + qcom/venus-4.2: replace split firmware with the mbn file (thx Dmitry Baryshkov)
  + qcom/venus-1.8: replace split firmware with the mbn file (thx Dmitry Baryshkov)

* Wed Nov 02 2022 Cronbuild Service <cronbuild@altlinux.org> 20221031-alt1
- upstream changes (GIT 8bb75626):
  + Add firmware for Cirrus CS35L41 on new ASUS Laptop (thx Stefan Binding)
  + iwlwifi: add new PNVM binaries from core74-44 release (thx Gregory Greenman)
  + iwlwifi: add new FWs from core69-81 release (thx Gregory Greenman)
  + qcom: update venus firmware files for VPU-2.0 (thx Nathan Hebert)
  + qcom: remove split SC7280 venus firmware images (thx Nathan Hebert)
  + qcom: update venus firmware file for v5.4 (thx Nathan Hebert)
  + qcom: replace split SC7180 venus firmware images with symlink (thx Nathan Hebert)

* Wed Oct 26 2022 Cronbuild Service <cronbuild@altlinux.org> 20221024-alt1
- upstream changes (GIT 0cac82d3):
  + rtw89: 8852b: update fw to v0.27.32.1 (thx Ping-Ke Shih)
  + rtlwifi: update firmware for rtl8192eu to v35.7 (thx James Hilliard)
  + rtlwifi: Add firmware v4.0 for RTL8188FU (thx Bitterblue Smith)
  + i915: Add HuC 7.10.3 for DG2 (thx Daniele Ceraolo Spurio)

* Thu Oct 20 2022 Cronbuild Service <cronbuild@altlinux.org> 20221017-alt1
- upstream changes (GIT 48407ffd):
  + cnm: update chips&media wave521c firmware. (thx Nas Chung)
  + brcm: add symlink for Pi Zero 2 W NVRAM file (thx Peter Robinson)
  + rtw89: 8852b: add initial fw v0.27.32.0 (thx Ping-Ke Shih)
  + iwlwifi: add new FWs from core72-129 release (thx Gregory Greenman)
  + iwlwifi: update 9000-family firmwares to core72-129 (thx Gregory Greenman)

* Wed Oct 12 2022 Cronbuild Service <cronbuild@altlinux.org> 20221012-alt1
- upstream changes (GIT 8b07c1fb):
  + rtl_bt: Update RTL8852C BT USB firmware to 0xD5B8_A40A (thx Hilda Wu)
  + amdgpu: update GC 10.3.6 RLC firmware (thx Alex Deucher)
  + amdgpu: update GC 10.3.7 RLC firmware (thx Alex Deucher)
  + amdgpu: update Yellow Carp RLC firmware (thx Alex Deucher)
  + amdgpu: update Beige Goby RLC firmware (thx Alex Deucher)
  + amdgpu: update Dimgrey Cavefish RLC firmware (thx Alex Deucher)
  + amdgpu: update Navy Flounder RLC firmware (thx Alex Deucher)
  + amdgpu: update Sienna Cichlid RLC firmware (thx Alex Deucher)
  + mediatek: Update mt8195 SOF firmware to v0.4.1 (thx Tinghan Shen)
  + qcom: add squashed version of a530 zap shader (thx Dmitry Baryshkov)
  + rtw89: 8852c: update fw to v0.27.56.1 (thx Chin-Yen Lee)
  + rtw89: 8852c: update fw to v0.27.56.0 (thx Chin-Yen Lee)
  + mediatek: Update mt8186 SCP firmware (thx Allen-KH Cheng)

* Wed Oct 05 2022 Cronbuild Service <cronbuild@altlinux.org> 20220930-alt1
- upstream changes (GIT fdf1a652):
  + Update AMD cpu microcode (thx John Allen)

* Thu Sep 29 2022 Cronbuild Service <cronbuild@altlinux.org> 20220928-alt1
- upstream changes (GIT 8d198465):
  + mediatek: mt8195: Update scp.img to v2.0.11956 (thx Tinghan Shen)

* Wed Sep 28 2022 Anton Midyukov <antohami@altlinux.org> 20220927-alt1
- upstream changes (GIT 0958301b):
  + mediatek: Add new mt8195 SOF firmware (thx Tinghan Shen)
  + mediatek: Update mt8186 SOF firmware to v0.2.1 (thx Tinghan Shen)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Sean Wang)
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9B8_8207 (thx Hilda Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Sean Wang)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + cxgb4: Update firmware to revision 1.27.0.0 (thx Rahul Lakkireddy)
  + i915: Add versionless HuC files for current platforms (thx John Harrison)
  + i915: Add GuC v70.5.1 for DG1, DG2, TGL and ADL-P (thx John Harrison)

* Wed Sep 28 2022 Anton Midyukov <antohami@altlinux.org> 20220912-alt3
- .gear/update.sh: git diff WHENCE only

* Fri Sep 23 2022 Anton Midyukov <antohami@altlinux.org> 20220912-alt2
- .gear/update.sh: check symlink -> dir, dir -> symlink, when updating
- cronbuild-options: add antohami@ to cronbuild_cc

* Wed Sep 14 2022 Cronbuild Service <cronbuild@altlinux.org> 20220912-alt1
- upstream changes (GIT f09bebf):
  + amdgpu: update yellow carp DMCUB firmware (thx Mario Limonciello)
  + amdgpu: add firmware for VCN 3.1.2 IP block (thx Mario Limonciello)
  + amdgpu: add firmware for SDMA 5.2.6 IP block (thx Mario Limonciello)
  + amdgpu: add firmware for PSP 13.0.5 IP block (thx Mario Limonciello)
  + amdgpu: add firmware for GC 10.3.6 IP block (thx Mario Limonciello)
  + amdgpu: add firmware for DCN 3.1.5 IP block (thx Mario Limonciello)
  + qcom: rename Lenovo ThinkPad X13s firmware paths (thx Dmitry Baryshkov)
  + rtw89: 8852c: update fw to v0.27.42.0 (thx Ping-Ke Shih)
  + rtw89: 8852c: update fw to v0.27.36.0 (thx Po-Hao Huang)

* Wed Sep 07 2022 Cronbuild Service <cronbuild@altlinux.org> 20220902-alt1
- upstream changes (GIT 2f2f018):
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.3146 (thx Petr Machata)
  + amdgpu: update beige goby VCN firmware (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish VCN firmware (thx Alex Deucher)
  + amdgpu: update navy flounder VCN firmware (thx Alex Deucher)
  + amdgpu: update sienna cichlid VCN firmware (thx Alex Deucher)

* Wed Aug 31 2022 Cronbuild Service <cronbuild@altlinux.org> 20220817-alt1
- upstream changes (GIT d3c9228):
  + rtl_bt: Update RTL8852C BT USB firmware to 0xDFB8_5A33 (thx Hilda Wu)
  + mediatek: reference the LICENCE file for MediaTek firmwares (thx Tinghan Shen)

* Tue Aug 16 2022 Cronbuild Service <cronbuild@altlinux.org> 20220815-alt1
- upstream changes (GIT 8413c63):
  + mediatek: Add new mt8186 SOF firmware (thx Tinghan Shen)
  + ice: Update package to 1.3.30.0 (thx Tony Nguyen)
  + QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00438 (thx Tim Jiang)
  + brcm: Add nvram for Lenovo Yoga Tablet 2 830F/L and 1050F/L
    tablets (thx Hans de Goede)
  + brcm: Add nvram for the Xiaomi Mi Pad 2 tablet (thx Hans de Goede)
  + brcm: Add nvram for the Asus TF103C tablet (thx Hans de Goede)
  + qca: Update firmware files for BT chip WCN6750.      This commit
    will update required firmware files for WCN6750. (thx Suraj Magar)

* Wed Aug 10 2022 Cronbuild Service <cronbuild@altlinux.org> 20220805-alt1
- upstream changes (GIT e6857b6):
  + amdgpu: Update Yellow Carp VCN firmware (thx Mario Limonciello)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.3020 (thx Petr Machata)
  + Add firmware for Cirrus CS35L41 (thx Vitaly Rodionov)
  + i915: Add GuC v70.4.1 for DG2 (thx John Harrison)
  + i915: Add DMC v2.07 for DG2 (thx Anusha Srivatsa)

* Tue Jul 26 2022 Cronbuild Service <cronbuild@altlinux.org> 20220722-alt1
- upstream changes (GIT 150864a):
  + amdgpu partially revert "amdgpu: update beige goby to release
    22.20" (thx Alex Deucher)
  + mediatek: Update mt8183/mt8192/mt8195 SCP firmware (thx Tinghan Shen)

* Tue Jul 19 2022 Cronbuild Service <cronbuild@altlinux.org> 20220718-alt1
- upstream changes (GIT 4421586):
  + amdgpu: update renoir to release 22.20 (thx Alex Deucher)
  + amdgpu: update beige goby to release 22.20 (thx Alex Deucher)
  + amdgpu: update yellow carp to release 22.20 (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish to release 22.20 (thx Alex Deucher)
  + amdgpu: update vega20 to release 22.20 (thx Alex Deucher)
  + amdgpu: update vega12 to release 22.20 (thx Alex Deucher)
  + amdgpu: update raven to release 22.20 (thx Alex Deucher)
  + amdgpu: update navy flounder to release 22.20 (thx Alex Deucher)
  + amdgpu: update vega10 to release 22.20 (thx Alex Deucher)
  + amdgpu: update sienna cichlid to release 22.20 (thx Alex Deucher)
  + amdgpu: update navi14 to release 22.20 (thx Alex Deucher)
  + amdgpu: update green sardine to release 22.20 (thx Alex Deucher)
  + amdgpu: update vangogh to release 22.20 (thx Alex Deucher)
  + amdgpu: update navi12 to release 22.20 (thx Alex Deucher)
  + amdgpu: update navi10 to release 22.20 (thx Alex Deucher)
  + amdgpu: update picasso to release 22.20 (thx Alex Deucher)
  + amdgpu: update aldebaran to release 22.20 (thx Alex Deucher)
  + amdgpu: update psp 13.0.8 TA firmware (thx Alex Deucher)
  + WHENCE: Fix the dangling symlinks fix (thx Peter Robinson)
  + amdgpu: update DMCUB firmware for DCN 3.1.6 (thx Alex Deucher)

* Wed Jul 13 2022 Cronbuild Service <cronbuild@altlinux.org> 20220708-alt1
- upstream changes (GIT dfa2931):
  + WHENCE: Correct dangling symlinks (thx Mario Limonciello)

* Tue Jul 05 2022 Cronbuild Service <cronbuild@altlinux.org> 20220704-alt1
- upstream changes (GIT f5f02da):
  + bnx2: Drop unsupported Broadcom NetXtremeII firmware (thx Peter Robinson)
  + bnx2: drop unsupported firmwares (thx Peter Robinson)
  + bnx2: sort firmware names in filesystem order (thx Peter Robinson)
  + brocade: drop old unsupported firmware revs (thx Peter Robinson)
  + amdgpu: update yellow carp DMCUB firmware (thx Mario Limonciello)
  + update firmware for MT7622 WiFi device (thx Ryder Lee)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Sean Wang)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + mediatek: Add SCP firmware for MT8186 (thx Allen-kh Cheng)
  + rtw88: 8822c: Update normal firmware to v9.9.13 (thx Po-Hao Huang)
  + rtw88: 8822c: Update normal firmware to v9.9.12 (thx Po-Hao Huang)
  + amdgpu: update Yellow Carp VCN firmware (thx Alex Deucher)

* Wed Jun 22 2022 Cronbuild Service <cronbuild@altlinux.org> 20220621-alt1
- upstream changes (GIT fc8557e):
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Sean Wang)
  + qed: update 8.59.1.0 firmware (thx Manish Chopra)
  +     qca: Update firmware files for BT chip WCN6750. (thx Suraj Magar)
  + QCA: Update Bluetooth WCN685x 2.1 firmware to 2.1.0-00409 (thx Zijun Hu)

* Tue Jun 14 2022 Cronbuild Service <cronbuild@altlinux.org> 20220610-alt1
- upstream changes (GIT 7b71b75):
  + WHENCE: add symlinks for StarFive based boards (thx Dimitri John Ledkov)
  + wilc1000: update WILC1000 firmware to v15.6 (thx Ajay Singh)
  + brcm: Add NVRAM file 43455 based Wifi/BT module as used on the
    Quartz64 Model B from Pine64. This file is based on the existing
    "brcm/brcmfmac43455-sdio.raspberrypi,4-model-b.txt" NVRAM file. (thx Dan Johansen)
  + iwlwifi: add new FWs from core70-87 release (thx Gregory Greenman)
  + iwlwifi: update 9000-family firmwares to core70-87 (thx Gregory Greenman)

* Tue Jun 07 2022 Cronbuild Service <cronbuild@altlinux.org> 20220607-alt1
- upstream changes (GIT 02c6986):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDFB8_0634 (thx Hilda Wu)
  + Makefile: replace mkdir by install (thx Konrad Weihmann)
  + iwlwifi: remove old unsupported 3160/7260/7265/8000/8265 firmware (thx Peter Robinson)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.9 (thx Kalle Valo)
  + WHENCE: ath11k: move regdb.bin before board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00157 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00157 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: WCN3990 hw1.0: add board-2.bin (thx Kalle Valo)

* Tue May 17 2022 Cronbuild Service <cronbuild@altlinux.org> 20220512-alt1
- upstream changes (GIT 251d290):
  + amdgpu: update beige goby firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update vega20 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update yellow carp firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update navy flounder firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update raven firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update green sardine firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update PCO firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update vangogh firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update navi12 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 22.10 (thx Alex Deucher)
  + amdgpu: update aldebaran firmware for 22.10 (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + mediatek: Update mt8192 SCP firmware (thx Tinghan Shen)

* Mon May 09 2022 Cronbuild Service <cronbuild@altlinux.org> 20220509-alt1
- upstream changes (GIT b19cbdc):
  + mediatek: Update mt8183 SCP firmware (thx Tinghan Shen)
  + ice: Update package to 1.3.28.0 (thx Tony Nguyen)

* Mon May 02 2022 Cronbuild Service <cronbuild@altlinux.org> 20220502-alt1
- upstream changes (GIT c3624eb):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDBB7_C1D9 (thx Hilda Wu)
  + amdgpu: update psp_13_0_8 firmware (thx Alex Deucher)
  + amdgpu: update gc_10_3_7_rlc firmware (thx Alex Deucher)
  + amdgpu: update dcn_3_1_6_dmcub firmware (thx Alex Deucher)
  + ath11k: QCA6390 hw2.0: update to
    WLAN.HST.1.0.1-05266-QCAHSTSWPLZ_V2_TO_X86-1 (thx Kalle Valo)
  + qcom: add firmware files for Adreno a420 & related generations (thx Dmitry Baryshkov)
  + qcom: add firmware files for Adreno a330 (thx Dmitry Baryshkov)
  + qcom: add firmware files for Adreno a220 (thx Dmitry Baryshkov)
  + i915: Add GuC v70.1.2 for DG2 (thx John Harrison)
  + rtw89: 8852c: add new firmware v0.27.20.0 for RTL8852C (thx Ping-Ke Shih)
  + ath10k: QCA9984 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00156 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00156 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00288-QCARMSWPZ-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA99X0 hw2.0: add board-2.bin (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: update to
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3.6510.7 (thx Kalle Valo)
  + ath11k: WCN6750 hw1.0: add to WLAN.MSL.1.0.1-00887-QCAMSLSWPLZ-1 (thx Kalle Valo)
  + ath11k: WCN6750 hw1.0: add board-2.bin (thx Kalle Valo)
  + ath11k: QCN9074 hw1.0: add to
    WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: QCN9074 hw1.0: add board-2.bin (thx Kalle Valo)
  + ath11k: QCA6390 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: IPQ8074 hw2.0: update to
    WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ8074 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath11k: IPQ6018 hw1.0: update to
    WLAN.HK.2.5.0.1-01208-QCAHKSWPL_SILICONZ-1 (thx Kalle Valo)
  + ath11k: IPQ6018 hw1.0: update board-2.bin (thx Kalle Valo)

* Tue Apr 26 2022 Cronbuild Service <cronbuild@altlinux.org> 20220422-alt1
- upstream changes (GIT ac21ab5):
  + Mellanox: Add lc_ini_bundle for xx.2010.1006 (thx Petr Machata)
  + Mellanox: xx.2010.1502: Distribute non-xz-compressed
    lc_ini_bundle (thx Petr Machata)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.1502 (thx Petr Machata)
  + amdgpu: update yellow carp DMCUB firmware (thx Alex Deucher)
  + update firmware for mediatek bluetooth chip (MT7922) (thx Sean Wang)
  + update firmware for MT7922 WiFi device (thx Deren Wu)
  + mediatek: Add mt8195 SCP firmware (thx Tinghan Shen)
  + qcom: apq8096: add modem firmware (thx Dmitry Baryshkov)
  + qcom: apq8096: add aDSP firmware (thx Dmitry Baryshkov)
  + rtl_bt: Add firmware and config files for RTL8852C (thx Max Chou)

* Wed Apr 13 2022 Cronbuild Service <cronbuild@altlinux.org> 20220411-alt1
- upstream changes (GIT f219d61):
  + mediatek: Add mt8192 SCP firmware (thx Yunfei Dong)
  + Update AMD cpu microcode (thx John Allen)
  + nvidia: add GA102/GA103/GA104/GA106/GA107 signed firmware (thx Gourav Samaiya)
  + brcm: rename Rock960 NVRAM to AP6356S and link devices to it (thx Peter Robinson)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + amdgpu: update green sardine VCN firmware (thx Alex Deucher)
  + amdgpu: update renoir VCN firmware (thx Alex Deucher)
  + amdgpu: update navi14 VCN firmware (thx Alex Deucher)
  + amdgpu: update navi12 VCN firmware (thx Alex Deucher)
  + amdgpu: update navi10 VCN firmware (thx Alex Deucher)
  + update firmware for MT7921 WiFi device (thx Sean Wang)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Sean Wang)
  + rtw88: 8821c: Update normal firmware to v24.11.00 (thx Chin-Yen Lee)
  + ice: Add wireless edge file for Intel E800 series driver (thx Guruprasad Rao)
  + ice: update ice DDP comms package to 1.3.31.0 (thx Arjun Anantharam)

* Wed Mar 23 2022 Cronbuild Service <cronbuild@altlinux.org> 20220315-alt1
- upstream changes (GIT 681281e):
  + amdgpu: update PSP 13.0.8 firmware (thx Alex Deucher)
  + amdgpu: update GC 10.3.7 firmware (thx Alex Deucher)
  + rtl_bt: Add firmware and config files for RTL8852B (thx Max Chou)

* Tue Mar 15 2022 Cronbuild Service <cronbuild@altlinux.org> 20220309-alt1
- upstream changes (GIT cd01f85):
  + iwlwifi: add new FWs from core68-60 release (thx Luca Coelho)
  + ath11k: add links for WCN6855 hw2.1 (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: add
    WLAN.HSP.1.1-03125-QCAHSPSWPL_V1_V2_SILICONZ_LITE-3 (thx Kalle Valo)
  + ath11k: WCN6855 hw2.0: add board-2.bin and regdb.bin (thx Kalle Valo)
  + ath10k/ath11k: mark notice.txt as "File:" (thx Kalle Valo)

* Tue Mar 08 2022 Cronbuild Service <cronbuild@altlinux.org> 20220303-alt1
- upstream changes (GIT f011ccb):
  + add firmware for MT7986 (thx Shayne Chen)
  + amdgpu: add firmware for SDMA 5.2.7 IP block (thx Alex Deucher)
  + amdgpu: add firmware for PSP 13.0.8 IP block (thx Alex Deucher)
  + amdgpu: add firmware for DCN 3.1.6 IP block (thx Alex Deucher)
  + amdgpu: add firmware for GC 10.3.7 IP block (thx Alex Deucher)
  + rtw89: 8852a: update fw to v0.13.36.0 (thx Zong-Zhe Yang)

* Wed Mar 02 2022 Cronbuild Service <cronbuild@altlinux.org> 20220225-alt1
- upstream changes (GIT ee0667a):
  + amdgpu: update raven2 VCN firmware (thx Alex Deucher)
  + amdgpu: update raven VCN firmware (thx Alex Deucher)
  + amdgpu: update picasso VCN firmware (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update AMD SEV firmware (thx John Allen)
  + rtw89: 8852a: update fw to v0.13.35.0 (thx Chin-Yen Lee)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.1406 (thx Petr Machata)
  + wfx: update to firmware 3.14 (thx J?r?me Pouiller)
  + wfx: add antenna configuration files (thx J?r?me Pouiller)
  + wfx: rename silabs/ into wfx/ (thx J?r?me Pouiller)
  + update firmware for mediatek bluetooth chip(MT7921) (thx Mark Chen)
  + Update firmware patch for Intel Bluetooth 8260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 8265 (thx Kiran K)
  + Intel BT 7265: Fix Security Issues (thx Kiran K)

* Tue Feb 22 2022 Cronbuild Service <cronbuild@altlinux.org> 20220218-alt1
- upstream changes (GIT c53073d):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDFB7_6D7A (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT USB firmware to 0x19B7_6D7D (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT UART firmware to 0x15B7_6D7D (thx Hilda Wu)
  + amdgpu: Update yellow carp firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update vega20 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update vega12 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update vega10 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update vangogh firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update renoir firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update raven2 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update raven firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update picasso firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update beige goby firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update dimgrey cavefish firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update navy flounder firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update sienna cichlid firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update navi14 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update navi12 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update navi10 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update cyan skillfish2 firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update green sardine firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Update arcturus firmware from 21.50 (thx Alex Deucher)
  + amdgpu: Add aldebaran firmware from 21.50 (thx Alex Deucher)
  + LICENSE.amdgpu: update copyright date (thx Alex Deucher)
  + Update AMD cpu microcode (thx John Allen)
  + update firmware for MT7921 WiFi device (thx Deren Wu)

* Tue Feb 15 2022 Cronbuild Service <cronbuild@altlinux.org> 20220126-alt1
- upstream changes (GIT 6342082):
  + Amphion: Add VPU firmwares for NXP i.MX8Q SoCs (thx Ming Qian)
  + i915: Add DMC firmware v2.16 for ADL-P (thx Madhumitha Tolakanahalli Pradeep)

* Tue Jan 25 2022 Cronbuild Service <cronbuild@altlinux.org> 20220124-alt1
- upstream changes (GIT eb8ea1b):
  + mediatek: Update MT8173 VPU firmware to v1.1.7 (thx Irui Wang)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)

* Tue Jan 18 2022 Cronbuild Service <cronbuild@altlinux.org> 20220114-alt1
- upstream changes (GIT 1e744b8):
  + update firmware for mediatek bluetooth chip(MT7921) (thx Mark Chen)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.1232 (thx Petr Machata)
  + add marvell CPT firmware images (thx DhanaSaravanan)

* Tue Jan 18 2022 Igor Vlasenko <viy@altlinux.org> 20220111-alt2
- NMU for cronbuild: verbose update for better debugging

* Tue Jan 18 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 20220111-alt1
- upstream changes (GIT 13dca28):
  + update firmware for MT7915 (thx Shayne Chen)
  + iwlwifi: add new FWs from core63-136 release (thx Luca Coelho)
  + iwlwifi: add new FWs from core66-88 release (thx Luca Coelho)
  + iwlwifi: update 9000-family firmwares to core66-88 (thx Luca Coelho)
  + add firmware for MT7916 (thx Shayne Chen)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + WHENCE: add missing symlink for NanoPi R1 (thx Vijai Kumar K)
  + amdgpu: update yellow carp dmcub firmware (thx Mario Limonciello)
  + cxgb4: Update firmware to revision 1.26.6.0 (thx Rahul Lakkireddy)
  + cnm: add chips&media wave521c firmware. (thx Nas Chung)
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + update firmware for mediatek bluetooth chip (MT7921) (thx Mark Chen)
  + rtw88: 8822c: Update normal firmware to v9.9.11 (thx Po-Hao Huang)
  + QCA: Update Bluetooth WCN685x firmware to 2.1.0-00298 (thx Zijun Hu)
- Updated upstream branch name (master -> main) to fix cronbuild updates.

* Wed Dec 22 2021 Cronbuild Service <cronbuild@altlinux.org> 20211216-alt1
- upstream changes (GIT f682ecb):
  + amdgpu: update green sardine PSP firmware (thx Alex Deucher)
  + bnx2x: Add FW 7.13.21.0 (thx Manish Chopra)
  + update frimware for mediatek bluetooth chip (MT7921) (thx Mark Chen)
  + wilc1000: update WILC1000 firmware to v15.4.1 (thx Ajay Singh)
  + rtl_bt: Update RTL8761B BT UART firmware to 0x0CA9_8A6B (thx Hilda Wu)
  + rtl_bt: Update RTL8761B BT USB firmware to 0x09A9_8A6B (thx Hilda Wu)
  + cxgb4: Update firmware to revision 1.26.4.0 (thx Rahul Lakkireddy)
  + rtw89: 8852a: update fw to v0.13.33.0 (thx Ping-Ke Shih)
  + i915: Add DMC firmware v2.14 for ADL-P (thx Madhumitha Tolakanahalli Pradeep)

* Thu Nov 25 2021 Cronbuild Service <cronbuild@altlinux.org> 20211123-alt1
- upstream changes (GIT b0e898f):
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + amdgpu: update yellow carp dmcub firmware (thx Alex Deucher)
  + amdgpu: update vangogh DMCUB firmware (thx Alex Deucher)
  + mrvl: prestera: Update Marvell Prestera Switchdev v4.0 (thx Volodymyr Mytnyk)
  + QCA: Add Bluetooth firmware for WCN685x (thx Tim Jiang)

* Wed Nov 17 2021 Cronbuild Service <cronbuild@altlinux.org> 20211115-alt1
- upstream changes (GIT f5d5195):
  + Update AMD cpu microcode (thx John Allen)
  + amdgpu: update raven2 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update navi14 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update raven firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update navi12 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update navi10 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update vega20 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update picasso firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update vangogh firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update beige goby firmware from 21.40 (thx Alex Deucher)
  + amdgpu: add cyan skillfish firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update green sardine firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update navy flounder firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update renoir firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update arcturus firmware from 21.40 (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware from 21.40 (thx Alex Deucher)

* Thu Nov 04 2021 Cronbuild Service <cronbuild@altlinux.org> 20211102-alt1
- upstream changes (GIT c9e68c4):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xDBA9_6937 (thx Hilda Wu)
  + iwlwifi: add new FWs from core64-96 release (thx Luca Coelho)
  + iwlwifi: update 9000-family firmwares to core64-96 (thx Luca Coelho)
  + amdgpu: update VCN firmware for green sardine (thx Alex Deucher)
  + update frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + Update AMD cpu microcode (thx John Allen)
  + QCA: Update Bluetooth firmware for WCN685x (thx Rocky Liao)

* Wed Nov 03 2021 L.A. Kostis <lakostis@altlinux.ru> 20211025-alt1.1
- gears/update: fix git pull command (use fast-forward stategy).

* Tue Oct 26 2021 Cronbuild Service <cronbuild@altlinux.org> 20211025-alt1
- upstream changes (GIT fc14618):
  + bnx2x: Add FW 7.13.20.0 (thx Manish Chopra)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2010.1006 (thx Petr Machata)
  + Update NXP Management Complex firmware to version 10.28.1 (thx Florinel Iordache)

* Mon Oct 18 2021 Cronbuild Service <cronbuild@altlinux.org> 20211018-alt1
- upstream changes (GIT d34196f):
  + update firmware for MT7921 WiFi device (thx Deren Wu)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)

* Tue Oct 05 2021 Cronbuild Service <cronbuild@altlinux.org> 20210926-alt1
- upstream changes (GIT 7a30050):
  + brcm: Add 43455 based AP6255 NVRAM for the ACEPC T8 Mini PC (thx Hans de Goede)
  + Update firmware file for Intel Bluetooth 9462 (thx Kiran K)
  + amdgpu: update VCN firmware for dimgrey cavefish (thx Alex Deucher)
  + amdgpu: update VCN firmware for navy flounder (thx Alex Deucher)
  + amdgpu: update VCN firmware for sienna cichlid (thx Alex Deucher)
  + amdgpu: update VCN firmware for vangogh (thx Alex Deucher)
  + amdgpu: update VCN firmware for renoir (thx Alex Deucher)
  + amdgpu: update VCN firmware for picasso (thx Alex Deucher)
  + amdgpu: update VCN firmware for raven2 (thx Alex Deucher)
  + amdgpu: update VCN firmware for raven (thx Alex Deucher)
  + amdgpu: Add initial firmware for Beige Goby (thx Alex Deucher)
  + cxgb4: Update firmware to revision 1.26.2.0 (thx Rahul Lakkireddy)

* Mon Sep 27 2021 Cronbuild Service <cronbuild@altlinux.org> 20210923-alt1
- upstream changes (GIT 0268c1b):
  + update frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)

* Tue Sep 21 2021 Cronbuild Service <cronbuild@altlinux.org> 20210916-alt1
- upstream changes (GIT d526e04):
  + qed: Add firmware 8.59.1.0 (thx Prabhakar Kushwaha)
  + Update firmware file for Intel Bluetooth AX211 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 8265 (thx Kiran K)
  + iwlwifi: add FWs for new So device types with multiple RF modules (thx Luca Coelho)
  + amdgpu: add initial firmware for Yellow Carp (thx Alex Deucher)

* Tue Sep 14 2021 Cronbuild Service <cronbuild@altlinux.org> 20210913-alt1
- upstream changes (GIT 090a34d):
  + add frimware for mediatek bluetooth chip (MT7922) (thx mark-yw.chen)
  + Update AMD SEV firmware (thx John Allen)

* Mon Sep 06 2021 Cronbuild Service <cronbuild@altlinux.org> 20210903-alt1
- upstream changes (GIT 2984e26):
  + Revert "iwlwifi: add FW for new So/Gf device type" (thx Luca Coelho)
  + update frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9A9_1D69 (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT UART firmware to 0x05A9_1A4A (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT USB firmware to 0x09A9_1A4A (thx Hilda Wu)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.3326 (thx Petr Machata)
  + iwlwifi: add FW for new So/Gf device type (thx Luca Coelho)

* Mon Aug 30 2021 Cronbuild Service <cronbuild@altlinux.org> 20210820-alt1
- upstream changes (GIT 2e271f2):
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9A9_127B (thx Hilda Wu)
  + rtl_nic: update firmware of RTL8153C (thx Hayes Wang)
  + ice: update package file to 1.3.26.0 (thx Tony Nguyen)

* Mon Aug 16 2021 Cronbuild Service <cronbuild@altlinux.org> 20210812-alt1
- upstream changes (GIT 24c4a85):
  + amdgpu: revert back to older raven2 sdma firmware (thx Alex Deucher)
  + amdgpu: revert back to older raven sdma firmware (thx Alex Deucher)
  + amdgpu: revert back to older picasso sdma firmware (thx Alex Deucher)
  + amdgpu: add initial vangogh support (thx Alex Deucher)
  + amdgpu: update vega20 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update renoir firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update raven2 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update raven firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update polaris12 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update picasso firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update dimgrey cavefish firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update navy flounder firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update navi14 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update navi12 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update navi10 firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update green sardine firmware from 21.30 (thx Alex Deucher)
  + amdgpu: update arcturus firmware from 21.30 (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + update frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + add firmware for MT7922 (thx Deren Wu)
  + QCA : Updated firmware files for WCN3991 (thx smagar)
  + i915: Add v2.03 DMC for RKL (thx Anusha Srivatsa)
  + i915: Add v2.12 DMC for TGL (thx Anusha Srivatsa)
  + qca: Add firmware files for BT chip WCN6750. (thx smagar)

* Mon Jul 19 2021 Cronbuild Service <cronbuild@altlinux.org> 20210719-alt1
- upstream changes (GIT 168452e):
  + iwlwifi: add ty firmware from Core63-43 (thx Johannes Berg)
  + update NXP 8897/8997 firmware images (thx Sharvari Harisangam)
  + rtlwifi: de-dupe rtl8723b WiFi firmware (thx Peter Robinson)
  + rtlwifi: de-dupe rtl8192e WiFi firmware (thx Peter Robinson)
  + update frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + cxgb4: Update firmware to revision 1.26.0.0 (thx Raju Rangoju)
  + firmware/i915/guc: Add HuC v7.9.3 for TGL & DG1 (thx John Harrison)
  + firmware/i915/guc: Add GuC v62.0.3 for ADL-P (thx John Harrison)
  + firmware/i915/guc: Add GuC v62.0.0 for all platforms (thx John Harrison)

* Mon Jul 05 2021 Cronbuild Service <cronbuild@altlinux.org> 20210628-alt1
- upstream changes (GIT d79c267):
  + amdgpu: update vcn firmware for green sardine for 21.20 (thx Alex Deucher)
  + amdgpu: update vcn firmware for renoir for 21.20 (thx Alex Deucher)
  + amdgpu: update vcn firmware for navi14 for 21.20 (thx Alex Deucher)
  + amdgpu: update vcn firmware for navi12 for 21.20 (thx Alex Deucher)
  + amdgpu: update vcn firmware for navi10 for 21.20 (thx Alex Deucher)
  + amdgpu: add initial dimgrey cavefish firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update vega20 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update Picasso firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update navi14 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update green sardine firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update navi12 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update renoir firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update navi10 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update raven2 firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update arcturus firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update raven firmware from 21.20 (thx Alex Deucher)
  + amdgpu: update navy flounder firmware from 21.20 (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9A8_A0CD (thx Hilda Wu)
  + update firmware for MT7921 WiFi device to 20210612122753 (thx Sean Wang)
  + rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x05A8_C6B4 (thx Hilda Wu)
  + QCA: Update Bluetooth firmware for QCA6174 (thx Rocky Liao)

* Mon Jun 14 2021 Cronbuild Service <cronbuild@altlinux.org> 20210608-alt1
- upstream changes (GIT 0f66b74):
  + cypress: update firmware for cyw54591 pcie (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw4373 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw43570 pcie (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw4356 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw4354 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw43455 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw43430 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw43340 sdio (thx Chi-Hsien Lin)
  + cypress: update firmware for cyw43012 sdio (thx Chi-Hsien Lin)
  + rtl_bt: Add rtl8761bu firmware (thx Joakim Tjernlund)
  + rtl_bt: Add rtl8761b firmware (thx Joakim Tjernlund)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.2946 (thx Petr Machata)
  + mediatek: update MT7915 firmware to 20201105 (thx Ryder Lee)
  + rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x05A8_A0CB (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x09A8_A0CB (thx Hilda Wu)
  + update firmware for MT7921 WiFi device (thx Sean Wang)
  + QCA: Add Bluetooth firmware for WCN685x (thx Rocky Liao)
  + QCA: Update Bluetooth firmware for QCA6174 (thx Rocky Liao)
  + QCA: Update Bluetooth firmware for QCA6390 (thx Rocky Liao)
  + cxgb4: Update firmware to revision 1.25.6.0 (thx Raju Rangoju)

* Mon May 24 2021 Cronbuild Service <cronbuild@altlinux.org> 20210518-alt1
- upstream changes (GIT f846292):
  + nvidia: fix symlinks for tu104/tu106 acr unload firmware (thx Ben Skeggs)
  + rtw88: 8822c: Update normal firmware to v9.9.10 (thx Chin-Yen Lee)

* Mon May 17 2021 Cronbuild Service <cronbuild@altlinux.org> 20210512-alt1
- upstream changes (GIT 55d9649):
  + iwlwifi: update 8000 family firmwares (thx Luca Coelho)
  + iwlwifi: update 9000-family firmwares to core60-51 (thx Luca Coelho)
  + iwlwifi: add new FWs from core60-51 release (thx Luca Coelho)
  + nvidia: Update Tegra194 XUSB firmware to v60.09 (thx JC Kuo)
  + nvidia: Update Tegra186 XUSB firmware to v55.18 (thx JC Kuo)
  + nvidia: Update Tegra210 XUSB firmware to v50.26 (thx JC Kuo)
  + update firmware for mhdp8546 (thx Parshuram Thombare)
  + i915: Add ADL-P DMC Support (thx Anusha Srivatsa)
  + amdgpu: add new polaris 12 MC firmware (thx Alex Deucher)
  + firmware: nvidia: Add VIC firmware for Tegra194 (thx Mikko Perttunen)
  + qcom: add gpu firmwares for sc7280 (thx Akhil P Oommen)
  + brcm: Add a link to enable khadas VIM2's WiFi (thx Jian-Hong Pan)
  + rtw89: 8852a: update fw to v0.13.8.0 (thx Ping-Ke Shih)
  + rtl_bt: Update RTL8852A BT USB firmware to 0xD9A8_7893 (thx hildawu)
  + qcom: Add venus firmware files for VPU-2.0 (thx smagar)
  + rtw89: 8852a: update fw to v0.13.8.0 (thx Ping-Ke Shih)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Intel BT 7265: Fix Security Issues (thx Kiran K)
  + Update firmware file for Intel Bluetooth 8265 (thx Kiran K)
  + qcom: update venus firmware files for v5.4 (thx smagar)
  + mrvl: prestera: Add Marvell Prestera Switchdev firmware 3.0
    version (thx Vadym Kochan)
  + rtw88: 8822c: Update normal firmware to v9.9.9 (thx Po-Hao Huang)
  + brcm: add missing symlink for Pi Zero W NVRAM file (thx Michel Piquemal)
  + amdgpu: update arcturus firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update navy flounder firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update sienna cichlid firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update vega20 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update picasso firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update navi14 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update green sardine firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update navi12 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update renoir firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update navi10 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update raven2 firmware from 21.10 (thx Alex Deucher)
  + amdgpu: update raven firmware from 21.10 (thx Alex Deucher)
  + rtl_nic: add new firmware for RTL8153 and RTL8156 series (thx Hayes Wang)
  + cxgb4: Update firmware to revision 1.25.4.0 (thx Raju Rangoju)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.2438 (thx Petr Machata)
  + brcm: Link CM4's WiFi firmware with DMI machine name. (thx Jeremy Linton)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + amdgpu: update navi14 smc firmware (thx Alex Deucher)
  + amdgpu: update navi10 SMC firmware (thx Alex Deucher)
  + QCA: Update Bluetooth firmware for QCA6174 (thx Rocky Liao)
  + WHENCE: link to similar config file for rtl8821a support (thx maximilian attems)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.14.A.6 (thx Louis Peens)
  + amdgpu: add arcturus firmware (thx Alex Deucher)

* Sat Apr 24 2021 Anton Midyukov <antohami@altlinux.org> 20210403-alt3
- use Makefile for install (Closes: 39980)

* Thu Apr 22 2021 Dmitry Terekhin <jqt4@altlinux.org> 20210403-alt2
- brcm: Add symlinks for brcm devices

* Mon Apr 05 2021 Cronbuild Service <cronbuild@altlinux.org> 20210403-alt1
- upstream changes (GIT 0dd245d):
  + rtl_bt: Add rtl8723bs_config-OBDA0623.bin symlink (thx Hans de Goede)
  + brcm: Add nvram for the Chuwi Hi8 (CWI509) tablet (thx Hans de Goede)
  + brcm: Add nvram for the Predia Basic tablet (thx Hans de Goede)
  + qcom: sm8250: update remoteproc firmware (thx Dmitry Baryshkov)
  + qcom: update a650 firmware files (thx Dmitry Baryshkov)

* Sun Mar 28 2021 Cronbuild Service <cronbuild@altlinux.org> 20210322-alt1
- upstream changes (GIT 3f026a2):
  + rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x59A_76A3 (thx hildawu)
  + amdgpu: update sienna cichlid firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update vega20 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update picasso firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update navi12 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 20.50 (thx Alex Deucher)
  + amdgpu: update raven firmware for 20.50 (thx Alex Deucher)
  + amdgpu: add initial support for navy flounder (thx Alex Deucher)

* Sun Mar 21 2021 Cronbuild Service <cronbuild@altlinux.org> 20210310-alt1
- upstream changes (GIT 3568f96):
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + rtw88: 8822c: Update normal firmware to v9.9.6 (thx Zong-Zhe Yang)
  + iwlwifi: add new FWs from core59-66 release (thx Luca Coelho)
  + iwlwifi: update 9000-family firmwares (thx Luca Coelho)
  + iwlwifi: update 7265D firmware (thx Luca Coelho)

* Sun Mar 07 2021 Cronbuild Service <cronbuild@altlinux.org> 20210305-alt1
- upstream changes (GIT e425f76):
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.2406 (thx Petr Machata)
  + add frimware for mediatek bluetooth chip (MT7921) (thx mark-yw.chen)
  + rtw89: 8852a: add firmware v0.9.12.2 (thx Ping-Ke Shih)
  + WHENCE: add missing symlink for BananaPi M3 (thx maximilian attems)
  + brcm: Fix Raspberry Pi 4B NVRAM file (thx Matthias Brugger)
  + silabs: add new firmware for WF200 (thx J?r?me Pouiller)

* Sun Feb 14 2021 Cronbuild Service <cronbuild@altlinux.org> 20210211-alt1
- upstream changes (GIT f7915a0):
  + amdgpu: add initial firmware for green sardine (thx Alex Deucher)
  + rtw88: RTL8822C: Update normal firmware to v9.9.5 (thx Zong-Zhe Yang)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.2304 (thx Petr Machata)
  + add firmware for MT7921 (thx Sean Wang)
  + rtw88: RTL8821C: Update firmware to v24.8 (thx Guo-Feng Fan)
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + i915: Add DMC v2.01 for ADL-S (thx Anusha Srivatsa)
  + i915: Add HuC v7.7.1 for DG1 (thx Anusha Srivatsa)
  + i915: Add GuC v49.0.1 for DG1 (thx Anusha Srivatsa)
  + qcom: Add venus firmware files for VPU-1.0 (thx Dmitry Baryshkov)
  + qcom: Add SM8250 Compute DSP firmware (thx Dmitry Baryshkov)
  + qcom: Add SM8250 Audio DSP firmware (thx Dmitry Baryshkov)
  + qcom: add firmware files for Adreno a650 (thx Dmitry Baryshkov)

* Sun Jan 24 2021 Cronbuild Service <cronbuild@altlinux.org> 20210111-alt1
- upstream changes (GIT 0578970):
  + brcm: Link RPi4's WiFi firmware with DMI machine name. (thx Jeremy Linton)

* Mon Jan 11 2021 Cronbuild Service <cronbuild@altlinux.org> 20210108-alt1
- upstream changes (GIT d528862):
  + brcm: Add NVRAM for Vamrs 96boards Rock960 (thx Peter Robinson)
  + brcm: Update Raspberry Pi 3B+/4B NVRAM for downstream changes (thx Peter Robinson)
  + cypress: Fix link direction (thx Jeremy Linton)
  + cypress: Link the new cypress firmware to the old brcm files (thx Peter Robinson)
  + brcm: remove old brcm firmwares that have newer cypress variants (thx Peter Robinson)

* Mon Jan 04 2021 Cronbuild Service <cronbuild@altlinux.org> 20201116-alt1
- upstream changes (GIT f580dc2):
  + rtl_bt: Update RTL8822C BT(UART I/F) FW to 0x059A_25CB (thx Hilda Wu)
  + rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x099a_7253 (thx Max Chou)
  + rtl_bt: Add firmware and config files for RTL8852A BT USB chip (thx Max Chou)
  + rtl_bt: Update RTL8821C BT(USB I/F) FW to 0x829a_7644 (thx Max Chou)

* Mon Dec 21 2020 Cronbuild Service <cronbuild@altlinux.org> 20201216-alt1
- upstream changes (GIT 646f159):
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + add firmware for Lontium LT9611UXC DSI to HDMI bridge (thx Dmitry Baryshkov)
  + mediatek: update MT8173 VPU firmware to v1.1.6 (thx Irui Wang)
  + QCA : Updated firmware files for WCN3991 (thx sampnimm)

* Sun Dec 06 2020 Cronbuild Service <cronbuild@altlinux.org> 20201130-alt1
- upstream changes (GIT 7455a36):
  + Update firmware file for Intel Bluetooth AX210 (thx Kiran K)
  + i915: Add GuC firmware v49.0.1 for all platforms (thx John Harrison)
  + i915: Remove duplicate KBL DMC entry (thx John Harrison)

* Mon Nov 30 2020 Cronbuild Service <cronbuild@altlinux.org> 20201123-alt1
- upstream changes (GIT b362fd4):
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.2018 (thx Petr Machata)

* Sun Nov 22 2020 Cronbuild Service <cronbuild@altlinux.org> 20201120-alt1
- upstream changes (GIT bc9cd0b):
  + Update AMD SEV firmware (thx John Allen)
  + amdgpu: add sienna cichlid firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update vega20 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update navi12 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 20.45 (thx Alex Deucher)
  + amdgpu: update raven firmware for 20.45 (thx Alex Deucher)

* Sun Nov 15 2020 Cronbuild Service <cronbuild@altlinux.org> 20201109-alt1
- upstream changes (GIT 2ea8667):
  + rtlwifi: v88.2 firmware files for RTL8192CU (thx Reto Schneider)
  + rtw88: RTL8822C: Update firmware to v9.9.4 (thx Tzu-En Huang)
  + Revert "rtw88: RTL8822C: Update firmware to v9.9.4" (thx Josh Boyer)
  + vpdma: Move firmware to ti directory (thx Nikhil Devshatwar)
  + amdgpu: update picasso VCN firmware (thx Alex Deucher)
  + amdgpu: update raven2 VCN firmware (thx Alex Deucher)
  + amdgpu: update raven VCN firmware (thx Alex Deucher)
  + rtw88: RTL8822C: Update firmware to v9.9.4 (thx Tzu-En Huang)
  + rtl_bt: Update RTL8822C BT(USB I/F) FW to 0x099A_281A (thx Max Chou)
  + QCA: Update Bluetooth firmware for QCA6390 (thx Rocky Liao)
  + qcom : updated venus firmware files for v5.4 (thx Asit Shah)
  + QCA : Fixed BT SSR due to command timeout / IO fatal error (thx Asit Shah)

* Sun Oct 25 2020 Cronbuild Service <cronbuild@altlinux.org> 20201023-alt1
- upstream changes (GIT dae4b4c):
  + cypress: add Cypress firmware and clm_blob files (thx Chi-Hsien Lin)
  + rtl_bt: Update RTL8821C BT FW to 0xAA6C_A99E (thx Max Chou)
  + ath10k: add SDIO firmware for QCA9377 WiFi (thx Christian Hewitt)
  + ice: update package file to 1.3.16.0 (thx Tony Nguyen)
  + mediatek: separate venc service thread (thx Irui Wang)
  + QCA : Updated firmware file for WCN3991 (thx Asit Shah)
  + iwlwifi: update and add new FWs from core56-54 release (thx Luca Coelho)
  + iwlwifi: update 3168, 7265D, 8000C and 8265 firmwares (thx Luca Coelho)
  + i915: Add DG1 DMC v2.02 (thx Anusha Srivatsa)
  + qcom : updated venus firmware files for v5.4 (thx Asit Shah)

* Sun Oct 11 2020 Cronbuild Service <cronbuild@altlinux.org> 20200929-alt1
- upstream changes (GIT 58d41d0):
  + ice: Add comms package file for Intel E800 series driver (thx Tony Nguyen)
  + copy-firmware: Always write Link: entries (thx Tony Nguyen)
  + amdgpu: update vega20 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update raven firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update picasso firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update navi12 firmware for 20.40 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.40 (thx Alex Deucher)
  + Add new VPDMA firmware 1b8.bin (thx Nikhil Devshatwar)
  + QCA : Updated firmware files for WCN3991 (thx Asit Shah)

* Sun Oct 04 2020 Cronbuild Service <cronbuild@altlinux.org> 20200923-alt1
- upstream changes (GIT b78a66c):
  + Update firmware for Cadence MHDP8546 DP bridge (thx Swapnil Jakhade)
  + Update firmware patch for Intel Bluetooth 7265 (D1) (thx Kiran K)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.1312 (thx Petr Machata)
  + nvidia: move firmware symlinks to WHENCE (thx Peter Robinson)
  + move i915 firmware symlinks to WHENCE (thx Peter Robinson)
  + move iwlwifi-7265D-10.ucode symlink to WHENCE (thx Peter Robinson)
  + Update Marvell Switchdev firmware with ABI changes (thx Vadym Kochan)

* Mon Sep 28 2020 Cronbuild Service <cronbuild@altlinux.org> 20200915-alt1
- upstream changes (GIT 00a84c5):
  + Update AMD SEV firmware (thx John Allen)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.1310 (thx Petr Machata)
  + mediatek: update MT7915 firmware to 20200819 (thx Ryder Lee)
  + brcm: Fix a stale symlink for RPi3 model b+ (thx Takashi Iwai)
  + qcom: Add updated a5xx and a6xx microcode (thx Jordan Crouse)

* Tue Sep 01 2020 Cronbuild Service <cronbuild@altlinux.org> 20200901-alt1
- upstream changes (GIT d5f9eea):
  + wl18xx: update firmware file 8.9.0.0.83 (thx Raz Bouganim)
  + mt7615: update firmware to 20200814 version (thx Shayne Chen)

* Wed Aug 26 2020 Cronbuild Service <cronbuild@altlinux.org> 20200819-alt1
- upstream changes (GIT 74bd44f):
  + amdgpu: add navi12 firmware from 20.30 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.30 (thx Alex Deucher)

* Tue Aug 18 2020 Cronbuild Service <cronbuild@altlinux.org> 20200817-alt1
- upstream changes (GIT 7a30af1):
  + brcm: Add brcmfmac43455-sdio.raspberrypi,3-model-a-plus.txt
    symlink (thx Peter Robinson)
  + rtl_bt: Update RTL8822C BT UART firmware to 0x0599_8A4F (thx Hilda Wu)
  + i915: Add DMC firmware 2.02 for RKL (thx Jos? Roberto de Souza)
  + i915: Add DMC firmware 2.08 for TGL (thx Jos? Roberto de Souza)
  + i915: Add HuC firwmare v7.5.0 for TGL (thx Jos? Roberto de Souza)

* Tue Aug 11 2020 Cronbuild Service <cronbuild@altlinux.org> 20200804-alt1
- upstream changes (GIT c331aa9):
  + amdgpu: update vega20 firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update raven firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update picasso firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 20.30 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.30 (thx Alex Deucher)

* Wed Aug 05 2020 Cronbuild Service <cronbuild@altlinux.org> 20200803-alt1
- upstream changes (GIT 9bc3789):
  + update NXP SDSD-8997 firmware image (thx Ganapathi Bhat)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2008.1036 (thx Petr Machata)

* Tue Jul 21 2020 Cronbuild Service <cronbuild@altlinux.org> 20200720-alt1
- upstream changes (GIT 2b823fc):
  + Update AMD SEV firmware (thx John Allen)
  + rtl_nic: update firmware for RTL8125B (thx Heiner Kallweit)

* Wed Jul 15 2020 Cronbuild Service <cronbuild@altlinux.org> 20200714-alt1
- upstream changes (GIT f39b687):
  + Update firmware file for Intel Bluetooth AX201 (thx Kiran K)
  + Update firmware file for Intel Bluetooth AX200 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9560 (thx Kiran K)
  + Update firmware file for Intel Bluetooth 9260 (thx Kiran K)
  + wilc1000: add wilc1000 v15.4 FW (thx Ajay Singh)
  + QCA: Update Bluetooth firmware for QCA6390 (thx Rocky Liao)

* Tue Jul 07 2020 Cronbuild Service <cronbuild@altlinux.org> 20200702-alt1


* Tue Jun 30 2020 Cronbuild Service <cronbuild@altlinux.org> 20200629-alt1
- upstream changes (GIT 1a0c0c2):
  + amdgpu: add UVD firmware for SI asics (thx Alex Deucher)
  + amdgpu: update renoir firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update picasso firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update raven2 firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update raven firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: add vega20 TA firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update vega20 firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update navi10 firmware from 20.20 release (thx Alex Deucher)
  + amdgpu: update navi14 firmware from 20.20 release (thx Alex Deucher)

* Wed Jun 24 2020 Cronbuild Service <cronbuild@altlinux.org> 20200615-alt1
- upstream changes (GIT 3890db3):
  + rtl_nic: add firmware for RTL8125B (thx Heiner Kallweit)

* Tue Jun 16 2020 Cronbuild Service <cronbuild@altlinux.org> 20200527-alt1
- upstream changes (GIT 887d2a1):
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Mellanox: Add new mlxsw_spectrum firmware xx.2007.1168 (thx Petr Machata)
  + rtw88: RTL8822C: update firmware version to v9.9 (thx Yan-Hsuan Chuang)
  + cxgb4: Update firmware to revision 1.24.17.0 (thx Vishal Kulkarni)
  + mrvl: add firmware for Prestera ASIC devices (thx Vadym Kochan)

* Tue Jun 02 2020 Cronbuild Service <cronbuild@altlinux.org> 20200519-alt1
- upstream changes (GIT 8ba6fa6):
  + iwlwifi: update and add new FWs from core50-70 and core52-81
    releases (thx Luca Coelho)
  + rtw88: RTL8821C: add firmware file v24.5 (thx Yan-Hsuan Chuang)
  + iwlwifi: update FWs to core47-142 release (thx Luca Coelho)
  + iwlwifi: update 8265 FW (thx Luca Coelho)
  + rtw88: update firmware information and README (thx Yan-Hsuan Chuang)
  + add firmware for MT7915E (thx Ryder Lee)
  + QCA: Add Bluetooth firmware for QCA9377 (thx Christian Hewitt)
  + add rebb firmware for mt7663 (thx Lorenzo Bianconi)

* Thu May 28 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 20200422-alt2
- netronome and liquidio moved to subpackages
- hardlinking identical files
- minor spec cleanup

* Sat Apr 25 2020 Cronbuild Service <cronbuild@altlinux.org> 20200422-alt1
- upstream changes (GIT b2cad6a):
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + rtl_bt: Update RTL8822C BT FW to 0x0999_3AA1 (thx Max Chou)
  + cxgb4: Update T6 config file (thx Vishal Kulkarni)

* Fri Apr 17 2020 Cronbuild Service <cronbuild@altlinux.org> 20200416-alt1
- upstream changes (GIT 6314fa0):
  + amdgpu: update vega20 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update vega12 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update vega10 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update renoir firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update raven firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update picasso firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update navi10 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 20.10 (thx Alex Deucher)
  + amdgpu: add navi14 TA firmware from 20.10 (thx Alex Deucher)
  + cxgb4: Update firmware to revision 1.24.14.0 (thx Vishal Kulkarni)
  + add firmware for MT7663 Wifi/BT combo device (thx Sean Wang)
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + qcom: Add SDM845 Adreno ZAP shader firmware (thx Bjorn Andersson)
  + qca: Enable transparent WBS for WCN3991 (thx Balakrishna Godavarthi)
  + QCA: Add Bluetooth firmware for QCA6390 (thx Rocky Liao)

* Fri Mar 20 2020 Cronbuild Service <cronbuild@altlinux.org> 20200320-alt1
- upstream changes (GIT edf390c):
  + mediatek: Add mt8183 SCP firmware (thx Erin Lo)
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + amdgpu: update vega20 firmware from 19.50 (thx Alex Deucher)
  + amdgpu: update vega12 firmware from 19.50 (thx Alex Deucher)
  + amdgpu: update vega10 firmware from 19.50 (thx Alex Deucher)
  + rtl_bt: Add firmware and configuration files for RTL8822C BT
    UART chip (thx Hilda Wu)
  + i915: Add DMC firmware v2.06 for TGL (thx Jos? Roberto de Souza)
  + i915: add HuC firmware v7.0.12 for TGL (thx Daniele Ceraolo Spurio)

* Fri Mar 20 2020 L.A. Kostis <lakostis@altlinux.ru> 20200302-alt1.1
- cronbuild: fix changelog encoding

* Fri Mar 06 2020 Cronbuild Service <cronbuild@altlinux.org> 20200302-alt1
- upstream changes (GIT 0148cfe):
  + check_whence: python3/utf-8 support (thx Brian Norris)
  + Makefile: improve `make check` usefulness (thx Brian Norris)
  + mediatek: Remove in-tree symlinks (thx Josh Boyer)
  + qca: Fix blueooth firmware name for QCA6174 (thx Rocky Liao)
  + mediatek: move MT8173 VPU FW to subfolder (thx gtk_ruiwang)

* Fri Feb 28 2020 Cronbuild Service <cronbuild@altlinux.org> 20200224-alt1
- upstream changes (GIT efcfa03):
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + qca: Add firmware files for BT chip wcn3991. (thx Balakrishna Godavarthi)

* Sat Feb 22 2020 Cronbuild Service <cronbuild@altlinux.org> 20200217-alt1
- upstream changes (GIT 2277987):
  + nvidia: add TU116/117 signed firmware (thx Gourav Samaiya)
  + drm/amdgpu: update to latest 19.50 firmware for raven (thx Alex Deucher)
  + mediatek: update MT8173 VPU firmware to v1.1.4 (thx gtk_ruiwang)

* Fri Feb 07 2020 Cronbuild Service <cronbuild@altlinux.org> 20200207-alt1
- upstream changes (GIT 6f89735):
  + rtl_nic: update firmware for RTL8153A (thx Hayes Wang)
  + rtl_bt: Update RTL8822C BT FW to V0x0998_C2B4 (thx Max Chou)
  + add firmware for MT7622 (thx Ryder Lee)
  + add version 2 for MT7615E (thx Ryder Lee)
  + amdgpu: update to latest navi10 firmware from 19.50 (thx Alex Deucher)
  + Revert "radeon: update oland rlc microcode from amdgpu" (thx Alex Deucher)
  + amlogic: update video decoder firmwares (thx Maxime Jourdan)
  + amdgpu: add renoir firmware for 19.50 (thx Alex Deucher)
  + amdgpu: update raven2 firmware for 19.50 (thx Alex Deucher)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.12.A.13 (thx Louis Peens)
  + qca: update bluetooth firmware for QCA6174 (thx Kalle Valo)

* Fri Jan 24 2020 Cronbuild Service <cronbuild@altlinux.org> 20200121-alt1
- upstream changes (GIT 1eb2408):
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + nvidia: add TU102/TU104/TU106 signed firmware (thx Gourav Samaiya)

* Fri Jan 17 2020 Cronbuild Service <cronbuild@altlinux.org> 20200113-alt1
- upstream changes (GIT 9c340bd):
  + amdgpu: update navi10 firmware for 19.50 (thx Alex Deucher)
  + amdgpu: Add navi10 TA ucode (thx Alex Deucher)
  + mediatek: update MT8173 VPU firmware to v1.1.3 (thx gtk_ruiwang)

* Sat Jan 11 2020 Cronbuild Service <cronbuild@altlinux.org> 20200107-alt1
- upstream changes (GIT 67d4ff5):
  + Mellanox: Add new mlxsw_spectrum firmware xx.2000.2714 (thx Ido Schimmel)
  + radeon: update oland rlc microcode from amdgpu (thx Alex Deucher)
  + amdgpu: update vega20 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update vega12 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update vega10 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update picasso microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update raven2 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update raven microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update navi10 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: update navi14 microcode for 19.50 (thx Alex Deucher)
  + amdgpu: add TA microcode for Raven asics (thx Alex Deucher)
  + qed: Add firmware 8.42.2.0 (thx Michal Kalderon)
  + qcom: Switch SDM845 WLAN firmware (thx Bjorn Andersson)
  + add NXP firmware licence file (thx Ganapathi Bhat)

* Wed Dec 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20191220-alt1
- upstream changes (GIT 6871bff):
  + ath10k: WCN3990 hw1.0: add firmware
    WLAN.HL.2.0-01387-QCAHLSWMTPLZ-1 (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00070 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00047 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00070 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00047 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)

* Wed Dec 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20191218-alt1
- upstream changes (GIT c4586ff):
  + Update AMD cpu microcode (thx John Allen)
  + inside-secure: add new "mini" firmware for the EIP197 driver (thx Pascal van Leeuwen)
  + WHENCE: Add raspberry-pi4 SDIO file (thx Josh Boyer)
  + qcom: update venus firmware files for v5.4 (thx Dikshita Agarwal)
  + cxgb4: Update firmware to revision 1.24.11.0 (thx Vishal Kulkarni)
  + brcm: Add BCM43455 NVRAM for Raspberry Pi 4 B (thx Matthias Brugger)
  + qcom: Add SDM845 Compute DSP firmware (thx Bjorn Andersson)
  + qcom: Add SDM845 Audio DSP firmware (thx Bjorn Andersson)
  + qcom: Add SDM845 modem firmware (thx Bjorn Andersson)

* Thu Nov 21 2019 Cronbuild Service <cronbuild@altlinux.org> 20191115-alt1
- upstream changes (GIT e8a0f4c):
  + rtl_nic: add firmware rtl8168fp-3 (thx Heiner Kallweit)
  + Update NXP Management Complex firmware to version 10.18.0 (thx Cristian Sovaiala)

* Wed Nov 13 2019 Cronbuild Service <cronbuild@altlinux.org> 20191113-alt1
- upstream changes (GIT c62c3c2):
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + amdgpu: update navi14 vcn firmware (thx Alex Deucher)
  + amdgpu: update navi10 vcn firmware (thx Alex Deucher)
  + i915: Add HuC firmware v7.0.3 for TGL (thx Daniele Ceraolo Spurio)
  + i915: Add GuC firmware v35.2.0 for TGL (thx Daniele Ceraolo Spurio)
  + i915: Add HuC firmware v9.0.0 for EHL (thx Daniele Ceraolo Spurio)
  + i915: Add GuC firmware v33.0.4 for EHL (thx Daniele Ceraolo Spurio)

* Wed Nov 06 2019 Cronbuild Service <cronbuild@altlinux.org> 20191104-alt1
- upstream changes (GIT 11bdc57):
  + rtw88: RTL8723D: add firmware file v48 (thx Yan-Hsuan Chuang)

* Thu Oct 31 2019 Cronbuild Service <cronbuild@altlinux.org> 20191028-alt1
- upstream changes (GIT 9e194c7):
  + qed: Add firmware 8.40.33.0 (thx Rasesh Mody)
  + amdgpu: add new navi14 wks gfx firmware for 19.30 (thx Alex Deucher)
  + amdgpu: update navi14 firmware for 19.30 (thx Alex Deucher)
  + amdgpu: update raven firmware for 19.30 (thx Alex Deucher)
  + Add firmware file for Intel Bluetooth AX201 (thx Amit K Bag)

* Wed Oct 23 2019 Cronbuild Service <cronbuild@altlinux.org> 20191023-alt1
- upstream changes (GIT ad7a8b2):
  + Mellanox: Add new mlxsw_spectrum2 firmware 29.2000.2308 (thx Ido Schimmel)
  + Mellanox: Add new mlxsw_spectrum firmware 13.2000.2308 (thx Ido Schimmel)
  + rtl_nic: add firmware files for RTL8153 (thx Hayes Wang)
  + rtl_bt: Update configuration file for BT part of RTL8822CU (thx Max Chou)
  + bnx2x: Add FW 7.13.15.0. (thx Sudarsana Reddy Kalluru)
  + Update AMD cpu microcode (thx Allen, John)

* Wed Oct 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20191010-alt1
- upstream changes (GIT 4c3e853):
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)

* Thu Oct 10 2019 Cronbuild Service <cronbuild@altlinux.org> 20191007-alt1
- upstream changes (GIT aa95e90):
  + amdgpu: add initial navi14 firmware form 19.30 (thx Alex Deucher)
  + rtlwifi: rtl8821ae: Add firmware for the RTL8812AE variant. (thx Larry Finger)
  + ice: Fix up WHENCE entry and symlink (thx Josh Boyer)
  + nvidia: Update Tegra210 XUSB firmware to v50.24 (thx Thierry Reding)
  + nvidia: Add XUSB firmware for Tegra194 (thx Thierry Reding)
  + copy-firmware: Create symlinks from WHENCE file (thx Thierry Reding)

* Wed Oct 02 2019 Cronbuild Service <cronbuild@altlinux.org> 20190925-alt1
- upstream changes (GIT c0590d8):
  + amdgpu: update vega20 ucode for 19.30 (thx Alex Deucher)
  + amdgpu: update vega12 ucode for 19.30 (thx Alex Deucher)
  + amdgpu: update vega10 ucode for 19.30 (thx Alex Deucher)
  + amdgpu: update picasso ucode for 19.30 (thx Alex Deucher)
  + amdgpu: update raven2 ucode for 19.30 (thx Alex Deucher)
  + amdgpu: update raven ucode for 19.30 (thx Alex Deucher)
  + amdgpu: add new raven rlc firmware (thx Alex Deucher)

* Wed Sep 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190916-alt1
- upstream changes (GIT 417a9c6):
  + amdgpu: add initial navi10 firmware (thx Alex Deucher)
  + drm/i915/firmware: Add v9.0.0 of HuC for Icelake (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v4.0.0 of HuC for Cometlake (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v4.0.0 of HuC for Geminilake (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v2.0.0 of HuC for Broxton (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v4.0.0 of HuC for Kabylake (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v2.0.0 of HuC for Skylake (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v33 of GuC for CML (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v2.04 of DMC for TGL (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v1.09 of DMC for ICL (thx Anusha Srivatsa)

* Wed Sep 11 2019 Cronbuild Service <cronbuild@altlinux.org> 20190909-alt1
- upstream changes (GIT 6c6918a):
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)

* Wed Sep 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190904-alt1
- upstream changes (GIT 6ddb9d9):
  + nvidia: Add XUSB firmware for Tegra186 (thx Thierry Reding)
  + rtl_bt: Update RTL8723D BT FW to 0x828A_96F1 (thx Max Chou)
  + rtl_nic: add firmware rtl8125a-3 (thx Heiner Kallweit)
  + Add firmware file for Intel Bluetooth AX201 (thx Amit K Bag)

* Thu Aug 29 2019 Cronbuild Service <cronbuild@altlinux.org> 20190824-alt1
- upstream changes (GIT 7307a29):
  + brcm: Add 43455 based AP6255 NVRAM for the Minix Neo Z83-4
    Mini PC (thx Hans de Goede)
  + brcm: Add 43340 based AP6234 NVRAM for the PoV TAB-P1006W-232
    tablet (thx Hans de Goede)
  + iwlwifi: update FWs to core45-152 release (thx Luca Coelho)

* Wed Aug 21 2019 Cronbuild Service <cronbuild@altlinux.org> 20190821-alt1
- upstream changes (GIT c0fb3d9):
  + check_whence: Add copy-firmware.sh to the list of ignored files (thx Josh Boyer)
  + rtl_bt: Update RTL8822C BT FW to V0x098A_94A4 (thx Max Chou)
  + Update firmware file for Intel Bluetooth AX200 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Mellanox: Add new mlxsw_spectrum firmware 13.2000.1886 (thx Ido Schimmel)
  + rtw88: add a README file (thx Yan-Hsuan Chuang)
  + rtw88: RTL8822C: add WoW firmware v7.3 (thx Yan-Hsuan Chuang)
  + rtw88: RTL8822C: update rtw8822c_fw.bin to v7.3 (thx Yan-Hsuan Chuang)
  + ath10k: QCA9984 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00046 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00045 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00040 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00045 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00140-QCARMSWPZ-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + cxgb4: update firmware to revision 1.24.3.0 (thx Vishal Kulkarni)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.38 (thx Louis Peens)

* Wed Jul 31 2019 Cronbuild Service <cronbuild@altlinux.org> 20190726-alt1
- upstream changes (GIT dff98c6):
  + nvidia: add missing entries in WHENCE (thx Ben Skeggs)
  + Update NXP Management Complex firmware to version 10.16.2 (thx Cristian Sovaiala)
  + iwlwifi: update -48 FWs for Qu and cc (thx Luca Coelho)
  + iwlwifi: update FWs for 3168, 7265D, 9000, 9260, 8000, 8265
    and cc (thx Luca Coelho)

* Thu Jul 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20190717-alt1
- upstream changes (GIT bf13a71):
  + Update firmware file for Intel Bluetooth AX201 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + amdgpu: update vega10 VCE firmware (thx Alex Deucher)
  + amdgpu: update picasso vcn firmware (thx Alex Deucher)
  + amdgpu: update raven vcn firmware (thx Alex Deucher)
  + amdgpu: update tonga to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: update vega12 to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: partially revert 2579167548be33afb1fe2a9a5c141561ee5a8bbe (thx Alex Deucher)
  + amdgpu: update vega10 to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: update polaris12 to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: update raven2 to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: update raven to latest 19.20 firmware (thx Alex Deucher)
  + amdgpu: update picasso to latest 19.20 firmware (thx Alex Deucher)
  + drm/i915/firmware: Add v33 of GuC for ICL (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v33 of GuC for KBL (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v33 of GuC for SKL (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v33 of GuC for GLK (thx Anusha Srivatsa)
  + drm/i915/firmware: Add v33 of GuC for BXT (thx Anusha Srivatsa)

* Wed Jul 03 2019 Cronbuild Service <cronbuild@altlinux.org> 20190625-alt1
- upstream changes (GIT 70e4394):
  + rsi: add firmware image for redpine 9116 chipset (thx Siva Rebbagondla)
  + Add firmware file for Intel Bluetooth AX201 (thx Bag, Amit K)

* Thu Jun 27 2019 Cronbuild Service <cronbuild@altlinux.org> 20190620-alt1
- upstream changes (GIT 7ae3a09):
  + iwlwifi: add new firmwares for integrated 22000 series (thx Luca Coelho)
  + iwlwifi: update FW for 22000 to Core45-96 (thx Luca Coelho)
  + iwlwifi: update FWs for 9000 series to Core45-96 (thx Luca Coelho)
  + iwlwifi: update Core45 FWs for 22260, 9000 and 9260 (thx Luca Coelho)
  + iwlwifi: udpate -36 firmware for 8000 series (thx Emmanuel Grumbach)
  + cavium: Add firmware for CNN55XX crypto driver. (thx Phani Kiran Hemadri)
  + Update firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Update AMD SEV firmware (thx Allen, John)
  + update licence text for Marvell firmware (thx Ganapathi Bhat)

* Wed Jun 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190603-alt1
- upstream changes (GIT 1884732):
  + update firmware for mhdp8546 (thx Damian Kos)
  + rsi: update firmware images for Redpine 9113 chipset (thx Siva Rebbagondla)
  + imx: sdma: update firmware to v3.5/v4.5 (thx Robin Gong)
  + nvidia: update GP10[2467] SEC2 RTOS with the one already used
    on GP108 (thx Ben Skeggs)

* Thu May 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20190514-alt1
- upstream changes (GIT 711d329):
  + Update firmware file for Intel Bluetooth 8265 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + amlogic: add video decoder firmwares (thx Maxime Jourdan)
  + iwlwifi: update -46 firmwares for 22260 and 9000 series (thx Luca Coelho)
  + iwlwifi: add firmware for 22260 and update 9000 series -46
    firmwares (thx Luca Coelho)
  + iwlwifi: add -46.ucode firmwares for 9000 series (thx Luca Coelho)

* Wed May 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190429-alt1
- upstream changes (GIT 92e17d0):
  + amdgpu: update vega20 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update vega12 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update vega10 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update polaris11 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update polaris10 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update raven2 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update raven to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update picasso to the latest 19.10 firmware (thx Alex Deucher)
  + update fw for qat devices (thx Giovanni Cabiddu)
  + Mellanox: Add new mlxsw_spectrum firmware 13.2000.1122 (thx Ido Schimmel)

* Thu Apr 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190424-alt1
- upstream changes (GIT 4b6cf2b):
  + drm/i915/firmware: Add ICL HuC v8.4.3238 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add ICL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add GLK HuC v03.01.2893 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add GLK GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add KBL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add SKL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add BXT GuC v32.0.3 (thx Anusha Srivatsa)

* Wed Apr 10 2019 Cronbuild Service <cronbuild@altlinux.org> 20190409-alt1
- upstream changes (GIT 260cb35):
  + Add firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + cxgb4: update firmware to revision 1.23.4.0 (thx Vishal Kulkarni)
  + Update NXP Management Complex firmware to version 10.14.3 (thx Cristian Sovaiala)

* Thu Apr 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190326-alt1
- upstream changes (GIT 67b7579):
  + add firmware for MT7615E (thx Ryder Lee)
  + mediatek: update MT8173 VPU firmware to v1.1.2 [decoder] Enlarge
    struct vdec_pic_info to support more capture buffer plane and
    capture buffer format change. (thx Yunfei Dong)
  + update Marvell 8797/8997 firmware images (thx Ganapathi Bhat)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.23 (thx Louis Peens)

* Wed Mar 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190314-alt1
- upstream changes (GIT 7bc2464):
  + cxgb4: update firmware to revision 1.23.3.0 (thx Vishal Kulkarni)
  + Update firmware file for Intel Bluetooth 8265 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)

* Tue Mar 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190308-alt1
- upstream changes (GIT b0d9583):
  + drm/amdgpu: update picasso to latest from 18.50 branch (thx Alex Deucher)
  + drm/amdgpu: update polaris12 to latest from 18.50 branch (thx Alex Deucher)
  + drm/amdgpu: update vega20 to latest from 18.50 branch (thx Alex Deucher)
  + rtw88: RTL8822C: update rtw8822c_fw.bin to v5.0 (thx Yan-Hsuan Chuang)
  + rtl_bt: Update firmware for BT part of RTL8822C (thx Larry Finger)
  + update Marvell 8787/8801/8887 firmware images (thx Ganapathi Bhat)
  + update Marvell 8897/8997 firmware images (thx Ganapathi Bhat)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.16.1 (thx Louis Peens)
  + QCA: Add the fw files for BT Chip QCA6174. (thx Balakrishna Godavarthi)

* Sun Feb 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190221-alt1
- upstream changes (GIT 54b0a74):
  + WHENCE: Correct errant entries (thx Josh Boyer)
  + amdgpu: update raven2 rlc firmware (thx Alex Deucher)
  + amdgpu: drop raven2_sdma1.bin (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + qca: Add firmware files for BT chip wcn3990. (thx Balakrishna Godavarthi)

* Mon Feb 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20190213-alt1
- upstream changes (GIT 710963f):
  + nvidia: add TU10x typec controller firmware (thx Ajay Gupta)
  + bnx2x: Add FW 7.13.11.0. (thx Rahul Verma)
  + amdgpu: add firmware for vega20 from 18.50 (thx Alex Deucher)
  + amdgpu: bump year on license (thx Alex Deucher)
  + update Marvell PCIe-USB8997 firmware image (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image (thx Ganapathi Bhat)
  + add Marvell SD8977 firmware image (thx Ganapathi Bhat)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00021 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00043 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00024 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)

* Sun Jan 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190118-alt1
- upstream changes (GIT a8b75ca):
  + brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+ (thx Matthias Brugger)
  + brcm: Fix filename for BCM43430 NVRAM for the Raspberry Pi 3
    Model B (thx Matthias Brugger)
  + amdgpu: add raven2 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: add picasso fw for 18.50 release (thx Alex Deucher)
  + Revert "brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+" (thx Josh Boyer)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + brcm: Add BCM43430 NVRAM for the Raspberry Pi 3 Model B (thx Matthias Brugger)
  + brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+ (thx Matthias Brugger)
  + update Marvell USB8801 B0 firmware image (thx Ganapathi Bhat)
  + iwlwifi: update firmwares for 9000 series (thx Emmanuel Grumbach)
  + cxgb4: update firmware to revision 1.22.9.0 (thx Arjun Vynipadath)

* Sun Dec 23 2018 Cronbuild Service <cronbuild@altlinux.org> 20181218-alt1
- upstream changes (GIT 0f22c85):
  + Revert "amdgpu: update vega10 fw for 18.50 release" (thx Alex Deucher)
  + brcm: Add 4330 NVRAM for the Prowise PT301 tablet (thx Hans de Goede)
  + brcm: Add 43430 NVRAM for the Chuwi Vi8 Plus tablet (thx Hans de Goede)
  + brcm: Add 43340 based AP6234 NVRAM for the Meegopad T08 HDMI
    stick (thx Hans de Goede)
  + brcm: Add 43430a0 based AP6212 NVRAM for the Jumper EZpad mini
    3 tablet (thx Hans de Goede)
  + brcm: Add 43430a0 based AP6212 NVRAM for the Onda V80 Plus tablet (thx Hans de Goede)
  + brcm: Add 4356 based AP6356 NVRAM for the GPD win handheld (thx Hans de Goede)
  + brcm: Add brcmfmac43362-sdio.lemaker,bananapro.txt symlink (thx Hans de Goede)
  + brcm: Add 43362 based AP6210 NVRAM for the Cubietech Cubietruck (thx Hans de Goede)
  + WHENCE: Put quotes around brcmfmac NVRAM filenames (thx Hans de Goede)
  + check_whence.py: Add support for filenames with spaces in them (thx Hans de Goede)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    part of RTL8723BS (thx Hans de Goede)
  + iwlwifi: update firmwares for 8000 series (thx Emmanuel Grumbach)
  + iwlwifi: add -43.ucode for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update -41.ucode for 9000 series (thx Emmanuel Grumbach)
  + firmware/huc/bxt: Add huC Update for BXT (thx Anusha Srivatsa)

* Mon Dec 17 2018 Cronbuild Service <cronbuild@altlinux.org> 20181107-alt1
- upstream changes (GIT 211de16):
  + brcm: provide new firmwares for BCM4366 chipset (thx Arend van Spriel)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1910.622 (thx Shalom Toledo)
  + cavium: Update firmware for CNN55XX crypto driver (thx Nagadheeraj, Rottela)
  + amdgpu: update vega12 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update vega10 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update raven fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update polaris11 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update polaris10 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: add firmware for vega12 (thx Alex Deucher)
  + amdgpu: Add new polaris MC firmwares (thx Alex Deucher)
  + amdgpu: Add new polaris SMC firmwares (thx Alex Deucher)
  + Update AMD cpu microcode (thx Allen, John)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.13 (thx Louis Peens)
  + microchip: add firmware for VSC8574 and VSC8584 Ethernet PHYs (thx Quentin Schulz)
  + intel: Update Cannonlake audio firmware. (thx Cezary Rojewski)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.16 (thx Ciaran Toal)
  + cxgb4: update firmware to revision 1.21.5.0 (thx Ganesh Goudar)

* Mon Nov 05 2018 Cronbuild Service <cronbuild@altlinux.org> 20181026-alt1
- upstream changes (GIT 1baa348):
  + qed: Add 8.37.7.0 firmware image (thx Mody, Rasesh)
  + add MC firmware for NXP DPAA2 SoCs (thx Cristian Sovaiala)

* Sun Oct 28 2018 Cronbuild Service <cronbuild@altlinux.org> 20181024-alt1
- upstream changes (GIT 1cb4e51):
  + amdgpu: add raven dmcu firmware (thx Alex Deucher)
  + amdgpu: update raven firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update fiji firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update tonga firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update carrizo firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update polaris10 firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update vega10 firmware to 18.40 (thx Alex Deucher)
  + add firmware for mt7650e (thx Stanislaw Gruszka)
  + liquidio: fix GPL compliance issue (thx Manlunas, Felix)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + add firmware for mt7610e (thx Lorenzo Bianconi)
  + ath10k: QCA9984 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.6.0.1-00003 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00041 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.6-00140 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00041 (thx Kalle Valo)
  + ath10k: QCA9377 hw1.0: add firmware-6.bin to
    WLAN.TF.2.1-00021-QCARMSWP-1 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    RM.4.4.1.c2-00057-QCARMSWP-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update firmware-5.bin to 10.4-3.6-00140 (thx Kalle Valo)

* Mon Oct 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20181008-alt1
- upstream changes (GIT c6b6265):
  + rtw88: Add firmware file for driver rtw88 (thx Larry Finger)
  + iwlwifi: add -41.ucode firmwares for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update firmwares for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update firmwares for 7000, 8000 and 9000 series (thx Luca Coelho)

* Sun Oct 07 2018 Cronbuild Service <cronbuild@altlinux.org> 20180927-alt1
- upstream changes (GIT 68a4930):
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.37 (thx Louis Peens)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.13 (thx Edwin Peer)
  + ti-connectivity: add firmware for CC2560(A) Bluetooth (thx David Lechner)
  + mediatek: add firmware for mt7668u Bluetooth (thx Sean Wang)
  + nvidia: add GV100 signed firmware (thx Gourav Samaiya)
  + firmware/icl/dmc: Add v1.07 of DMC for Icelake (thx Anusha Srivatsa)
  + add Marvell SD8997 firmware image (thx Ganapathi Bhat)
  + qca: update BT firmware files for QCA ROME chip. (thx Balakrishna Godavarthi)

* Sun Sep 16 2018 Cronbuild Service <cronbuild@altlinux.org> 20180913-alt1
- upstream changes (GIT 44d4fca):
  + brcm: update firmware for bcm43362 sdio (thx Chi-Hsien Lin)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1703.4 (thx Petr Machata)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    part of RTL8822CU (thx Larry Finger)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1703.4 (thx Petr Machata)

* Sun Sep 09 2018 Cronbuild Service <cronbuild@altlinux.org> 20180903-alt1
- upstream changes (GIT 85c5d90):
  + nvidia: switch GP10[2467] to newer scrubber/ACR firmware
    (from GP108) (thx Ben Skeggs)

* Sun Aug 26 2018 Cronbuild Service <cronbuild@altlinux.org> 20180822-alt1
- upstream changes (GIT fea76a0):
  + amdgpu: sync up polaris10 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up polaris12 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up tonga firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up fiji firmware with 18.30 release (thx Alex Deucher)
  + add firmware for mhdp8546 (thx Damian Kos)
  + qed: Add firmware 8.37.7.0 (thx Rahul Verma)

* Sun Aug 19 2018 Cronbuild Service <cronbuild@altlinux.org> 20180730-alt1
- upstream changes (GIT f1b95fe):
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + add firmware for mt76x0 (thx Stanislaw Gruszka)
  + qcom: update venus firmware files for v5.2 (thx Vikash Garodia)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.31 (thx Louis Peens)

* Sun Aug 05 2018 Cronbuild Service <cronbuild@altlinux.org> 20180728-alt1
- upstream changes (GIT 7b5835f):
  + add firmware for mt76x2u (thx Lorenzo Bianconi)
  + wl18xx: update firmware file 8.9.0.0.79 (thx Guy Mishol)

* Sun Jul 29 2018 Cronbuild Service <cronbuild@altlinux.org> 20180722-alt1
- upstream changes (GIT b01151b):
  + Mellanox: Add new mlxsw_spectrum firmware 13.1702.6 (thx Nir Dotan)
  + WHENCE: Remove reference to amdgpu/vegam_me_2.bin (thx Josh Boyer)
  + mediatek: add MT7622 Bluetooth firmwares and license file (thx Sean Wang)
  + brcm: add 43430 based AP6212 and 1DX NVRAM (thx Ryan Harkin)
  + update Marvell USB8801 B0 firmware image (thx Ganapathi Bhat)

* Mon Jul 23 2018 Cronbuild Service <cronbuild@altlinux.org> 20180710-alt1
- upstream changes (GIT 8d69bab):
  + amdgpu: update copyright date (thx Alex Deucher)
  + amdgpu: add initial VegaM firmware (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris12 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris10 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up verde firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up pitcairn firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up tahiti firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up oland firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up hainan firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up kaveri firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up mullins firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up kabini firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up hawaii firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up bonaire firmware with 18.20 release (thx Alex Deucher)
  + WHENCE: Fix typo Version (thx Sedat Dilek)

* Sun Jul 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20180706-alt1
- upstream changes (GIT 6213586):
  + cxgb4: update firmware to revision 1.20.8.0 (thx Ganesh Goudar)

* Mon Jun 11 2018 Cronbuild Service <cronbuild@altlinux.org> 20180606-alt1
- upstream changes (GIT d114732):
  + brcm: update firmware for bcm4356 pcie (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm4354 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43362 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43340 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43430 sdio (thx Chi-Hsien Lin)
  + amdgpu: update vega10 VCE firmware to version 55.3 (thx Alex Deucher)
  + Update firmware patch for Intel Bluetooth 7265 (D0) (thx Amit K Bag)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + qcom: add venus firmware files for v5.2 (thx Vikash Garodia)

* Sun May 27 2018 Cronbuild Service <cronbuild@altlinux.org> 20180524-alt1
- upstream changes (GIT 7518922):
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + qed: Add firmware 8.37.2.0 (thx Rahul Verma)

* Sun May 20 2018 L.A. Kostis <lakostis@altlinux.ru> 20180518-alt1
- upstream changes (GIT 2a9b2cf):
  + amd-ucode: delete conflicting ucode
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 7260 (B5/B6) (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 7260 (B3/B4) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update AMD cpu microcode (thx Sherry Hurwitz)
  + amdgpu: sync up polaris12 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up polaris10 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up carrizo firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up topaz firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up stoney firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up tonga firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up fiji firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.10 release (thx Alex Deucher)
  + nfp: Add symlink for Agilio CX 1x40GbE flower firmware (thx Louis Peens)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.16 (thx Louis Peens)
  + liquidio: update firmware to v1.7.2 (thx Felix Manlunas)
  + update Marvell USB8997 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)

* Sat May 12 2018 Cronbuild Service <cronbuild@altlinux.org> 20180507-alt1
- upstream changes (GIT 8fc2d4e):
  + update Marvell USB8997 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)

* Sun May 06 2018 Cronbuild Service <cronbuild@altlinux.org> 20180430-alt1
- upstream changes (GIT 397a604):
  + qed: Add firmware 8.33.12.0 (thx Rasesh Mody)
  + Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + cxgb4: update firmware to revision 1.19.1.0 (thx Ganesh Goudar)
  + nfp: add symlink for mixed mode Agilio CX 2x25GbE cards (thx Louis Peens)
  + nfp: update Agilio SmartNIC flower firmware to rev 5701 (thx Louis Peens)

* Sat Apr 21 2018 Cronbuild Service <cronbuild@altlinux.org> 20180409-alt1
- upstream changes (GIT b562d2f):
  + update wil6210 firmware to 5.2.0.18 (thx Maya Erez)
  + rsi: update firmware images for Redpine 9113 chipset (thx Amitkumar Karwar)
  + iwlwifi: update firmwares for 3160, 3168 and 7265 (thx Luca Coelho)
  + iwlwifi: add some new FW versions and update older ones (thx Luca Coelho)

* Sun Apr 08 2018 L.A. Kostis <lakostis@altlinux.ru> 20180329-alt1
- configuration changes:
  +  fix cronbuild
- upstream changes (GIT 8c1e439):
  + amdgpu: update vce firmware for Polaris (thx Alex Deucher)
  + Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + nfp: update Agilio SmartNIC firmware to rev 2.0.7 (thx Edwin Peer)
  + cxgb4: update firmware to revision 1.18.9.0 (thx Ganesh Goudar)
  + intel: Update Geminilake audio firmware (thx Sanyog Kale)
  + intel: Update Kabylake audio firmware (thx Sanyog Kale)
  + intel: Update Broxton audio firmware (thx Sanyog Kale)
  + intel: Update Skylake audio firmware (thx Sanyog Kale)

* Tue Mar 27 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt3
- Fixed obsoleted fw list (tnx to mike@ and vseleznv@).

* Wed Mar 21 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt2
- .spec cleanup:
  + added provides/obsoletes for absorbed fw.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt1
- upstream changes (GIT 44476f2):
  + BCM-0bb4-0306: Update to Cypress license in WHENCE (thx kaihsiu_chen)

* Thu Mar 15 2018 L.A. Kostis <lakostis@altlinux.ru> 20180314-alt1
- upstream changes (GIT 4c0bf11):
  + intel: Update Kabylake audio firmware (thx Sanyog Kale)

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 20180227-alt1
- upstream changes (GIT 9cf0ec0):
  + Mellanox: Add new mlxsw_spectrum firmware 13.1620.192 (thx Tal Bar)
  + qed: Add firmware 8.33.11.0 (thx Rahul Verma)
  + BCM-0bb4-0306: Cypress Bluetooth firmware for HTC Vive (thx Kaihsiu Chen)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + qed: Add firmwares 8.20.0.0 8.18.9.0 and 8.14.6.0 (thx Rasesh Mody)
  + iwlwifi: update firmware version 34 for 9000 series (thx Luca Coelho)

* Sat Feb 24 2018 L.A. Kostis <lakostis@altlinux.ru> 20180222-alt1
- configuration changes:
  +  update changelog rules
- upstream changes (GIT 7344ec9):
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9377 hw1.0: update firmware-5.bin to
    WLAN.TF.1.0-00002-QCATFSWPZ-5 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00079-QCARMSWPZ-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    parts of RTL8821C and RTL8723D (thx Larry Finger)
  + qed: Add firmwares 8.30.12.0 and 8.10.9.0 (thx Rasesh Mody)
  + nfp: update Agilio SmartNIC firmware to rev 2.0.4 (thx Edwin Peer)

* Fri Feb 02 2018 L.A. Kostis <lakostis@altlinux.ru> 20180201-alt1
- configuration changes:
  + changelog.sh: get pkg name from specfile
  + cronbuild: initial config
- upstream changes (GIT 2aa2ac2):
  + linux-firmware: Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + linux-firmware: Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + linux-firmware: Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + wl127x/wl128x: update PLT firmwares (thx Guy Mishol)
  + linux-firmware: intel: Update Kabylake audio firmware (thx Guneshwor Singh)
  + .gear: simplify cronbuild scripts

* Tue Jan 23 2018 Konstantin A. Lepikhov <lakostis@altlinux.ru> 20180118-alt1
- Update 65b1c68 GIT:
  + amdgpu: update uvd firmware for polaris asics (thx Alex Deucher).
  + amdgpu: update vce firmware for Fiji (thx Alex Deucher).
  + amdgpu: update vcn firmware for raven (thx Alex Deucher).
  + amdgpu: update vce and uvd firmware for Vega10 (thx Alex Deucher).
  + mediatek: update MT8173 VPU firmware to 1.0.8 [decoder h264]
    Fix h264 decoder output delay for some low latency bitstreams
    (thx pochun.lin).
  + cxgb4: update firmware to revision 1.17.14.0 (thx Ganesh Goudar).
  + linux-firmware: update Marvell PCIe-USB8897/8997 firmware image
    to add WPA2 vulnerability fix (thx Xinming Hu).
  + LICENSE.nouveau-firmware: added.
  + linux-firmware: intel: Update Geminilake audio firmware
    (thx Pradeep Tewani).

* Sat Jan 13 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.2
- prepare .spec for cronbuild.

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.1
- amd-ucode: Add microcode_amd_fam17h.bin (bsc#1068032 CVE-2017-5715)

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1
- Updated to 65b1c68 GIT.

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 20171128-alt1
- updated from git

* Mon Oct 30 2017 Michael Shigorin <mike@altlinux.org> 20171009-alt1
- updated from git

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 20170901-alt1
- updated from git

* Mon Jun 26 2017 Michael Shigorin <mike@altlinux.org> 20170622-alt1
- updated from git

* Mon Jun 05 2017 Michael Shigorin <mike@altlinux.org> 20170531-alt1
- updated from git

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt2
- disable attempts to find R:/P: or ELF bugs automatically

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt1
- updated from git

* Wed Mar 22 2017 Michael Shigorin <mike@altlinux.org> 20170314-alt1
- updated from git

* Mon Jan 23 2017 Michael Shigorin <mike@altlinux.org> 20170113-alt1
- updated from git (closes: #33022)

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt2
- dropped /lib/firmware/check_whence.py (closes: #32754)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt1
- updated from git

* Wed Aug 03 2016 Michael Shigorin <mike@altlinux.org> 20160728-alt1
- updated from git

* Wed Jun 15 2016 Michael Shigorin <mike@altlinux.org> 20160608-alt1
- updated from git

* Tue Mar 01 2016 Michael Shigorin <mike@altlinux.org> 20160219-alt1
- updated from git

* Tue Feb 16 2016 Michael Shigorin <mike@altlinux.org> 20160216-alt1
- updated from git

* Sun Nov 29 2015 Michael Shigorin <mike@altlinux.org> 20151129-alt1
- updated from git

* Fri Nov 06 2015 Michael Shigorin <mike@altlinux.org> 20151104-alt1
- updated from git

* Thu Sep 10 2015 Michael Shigorin <mike@altlinux.org> 20150824-alt1
- updated from git
  + NB: amdgpu* have arrived (thx lakostis@ for the notice)

* Thu Aug 13 2015 Michael Shigorin <mike@altlinux.org> 20150811-alt1
- updated from git
- dropped Requires: firmware-ipw* (closes: #30308)

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 20150506-alt1
- updated from git

* Tue Apr 28 2015 Michael Shigorin <mike@altlinux.org> 20150410-alt1
- updated from git

* Fri Dec 26 2014 Michael Shigorin <mike@altlinux.org> 20141222-alt1
- updated from git

* Tue Nov 11 2014 Michael Shigorin <mike@altlinux.org> 20141009-alt1
- updated from git

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 20140926-alt1
- updated from git

* Tue Sep 30 2014 Michael Shigorin <mike@altlinux.org> 20140902-alt1
- updated from git

* Wed Sep 10 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt2
- add P:/O: firmware-amd-ucode

* Sat Aug 30 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt1
- updated from git

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140521-alt1
- updated from git

* Thu Jan 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140123-alt1
- updated from git

* Wed Nov 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20131106-alt1
- updated from git

* Wed Sep 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130904-alt1
- updated from git

* Thu Jun 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130613-alt1
- updated from git

* Tue Apr 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130423-alt1
- updated from git
- added prov/obs firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870
  firmware-rt3090 (closes #27624)

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt2
- sources exluded (closes: #28682)

* Wed Mar 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt1
- updated from git

* Wed Jan 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130109-alt1
- updated from git

* Wed Sep 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120905-alt1
- updated from git

* Wed Apr 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120304-alt1
- updated from g.k.o/pub/scm/linux/kernel/git/firmware/linux-firmware.git

* Wed Dec 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20111228-alt1
- updated from git

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110819-alt1
- updated from git

* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110726-alt1
- updated from git

* Fri May 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt3
- requires for firmware-ipw* added

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt2
- false ipw* provedes/obsoletes deleted (closes #25669)

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt1
- updated from git
- iwl* included and provided/obsoleted

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110331-alt1
- updated from git

* Fri Jan 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110114-alt1
- updated from git

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101217-alt1
- updated from git

* Fri Sep 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100924-alt1
- updated from git

* Tue Jun 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100629-alt1
- updated from git
- provides of linux-firmware added

* Fri May 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100521-alt1
- build to Sisyphus
- updated from git
- radeon and nouveau added to tree directly

* Mon Apr 12 2010 Michael Shigorin <mike@altlinux.org> 20100106-alt1
- adapted fedora spec for ALT Linux (thanks lakostis@ for proposal)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
