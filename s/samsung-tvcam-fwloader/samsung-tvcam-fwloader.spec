%define _unpackaged_files_terminate_build 1

Name: samsung-tvcam-fwloader
Version: 0.1
Release: alt1

Summary: Firmware loader for Samsung TV cameras
License: GPL-3.0
Group: System/Configuration/Hardware
URL: https://github.com/ondrej-zary/samsung-tvcam-fwloader
VCS: https://github.com/ondrej-zary/samsung-tvcam-fwloader

Source0: %name-%version.tar

BuildRequires: pkgconfig(libusb-1.0)

%description
This package provides the GPL-licensed firmware loader for Samsung TV cameras.
The actual firmware binaries are in the separate firmware-samsung-tvcam package.

%package -n firmware-samsung-tvcam
Summary: Proprietary firmware for Samsung TV cameras
License: Proprietary
Group: System/Kernel and hardware
Requires: samsung-tvcam-fwloader = %EVR

%description -n firmware-samsung-tvcam
This package contains proprietary firmware binaries for Samsung TV cameras.
These files are required by samsung-tvcam-fwloader to operate the camera hardware.

%prep
%setup

%build
%make_build

%install
install -D -m 0755 samsung_tvcam_fwload \
    %buildroot%_bindir/samsung_tvcam_fwload
install -D -m 0644 40-%name.rules \
    %buildroot%_udevrulesdir/40-%name.rules

install -d %buildroot/lib/firmware/samsung-tvcam
install -m 0644 raptor_firmware.img \
    %buildroot/lib/firmware/samsung-tvcam/raptor_firmware.img
install -m 0644 FalconFW.bin \
    %buildroot/lib/firmware/samsung-tvcam/FalconFW.bin
install -m 0644 FalconPlus_FW.bin \
    %buildroot/lib/firmware/samsung-tvcam/FalconPlus_FW.bin
install -m 0644 Heron_Ext_FW.bin \
    %buildroot/lib/firmware/samsung-tvcam/Heron_Ext_FW.bin

%files
%_bindir/samsung_tvcam_fwload
%_udevrulesdir/40-%name.rules

%files -n firmware-samsung-tvcam
%dir /lib/firmware/samsung-tvcam
/lib/firmware/samsung-tvcam/raptor_firmware.img
/lib/firmware/samsung-tvcam/FalconFW.bin
/lib/firmware/samsung-tvcam/FalconPlus_FW.bin
/lib/firmware/samsung-tvcam/Heron_Ext_FW.bin

%changelog
* Mon Apr 27 2026 Anton Osipov <radiolamp@altlinux.org> 0.1-alt1
- Initial build for ALT.
