Summary: Firmware for lt11i Tablet
Name: firmware-lt11i
Version: 0
Release: alt1
Url: https://gitlab.mig-mdm.ru/Timofey/lt11i-freeware
License: distributable
Group: System/Kernel and hardware

Source0: HSD1095_HX83102-E_T12N_HXD_D00_C00_20230411.bin
Source1: novatek_ts_fw.bin
Source2: sdiouartiw416_combo_v0.bin

BuildArch: noarch

Requires: firmware-linux

%description
%summary.

%install
mkdir -p %buildroot/lib/firmware/mrvl
install -m644 %SOURCE0 %buildroot/lib/firmware/
install -m644 %SOURCE1 %buildroot/lib/firmware/
install -m644 %SOURCE2 %buildroot/lib/firmware/mrvl/

%files
/lib/firmware/HSD1095_HX83102-E_T12N_HXD_D00_C00_20230411.bin
/lib/firmware/novatek_ts_fw.bin
/lib/firmware/mrvl/sdiouartiw416_combo_v0.bin

%changelog
* Wed Jul 31 2024 Anton Midyukov <antohami@altlinux.org> 0-alt1
- Initial build

