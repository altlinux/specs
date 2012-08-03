Name: firmware-amd-ucode
Version: 20120117
Release: alt1

Packager: L.A. Kostis <lakostis@altlinux.ru>

Summary: Latest microcode patches for AMD processors
License: ADVANCED MICRO DEVICES INC SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware

URL: http://www.amd64.org/support/microcode.html
Source0: http://www.amd64.org/pub/microcode/amd-ucode-latest.tar 

Provides: microcode-data-amd
BuildArch: noarch

Requires: udev

%description
This package provides latest microcode patches for AMD processor
families >= 0x10.

See http://www.amd64.org/support/microcode.html for details.

%prep
%setup -n amd-ucode-latest

%build

%install
mkdir -p %buildroot/lib/firmware/amd-ucode/
install -pm644 microcode_amd.bin %buildroot/lib/firmware/amd-ucode/
install -pm644 microcode_amd_fam15h.bin %buildroot/lib/firmware/amd-ucode/

%files
%dir /lib/firmware/amd-ucode
/lib/firmware/amd-ucode/*.bin
%doc README INSTALL LICENSE *amd.bin.README *fam15h.bin.README

%changelog
* Fri Aug 03 2012 L.A. Kostis <lakostis@altlinux.ru> 20120117-alt1
- Initial build.

