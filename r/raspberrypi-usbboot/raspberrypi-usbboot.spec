Name: raspberrypi-usbboot
Version: 2021.10.27
Release: alt1
Summary: Raspberry Pi usbboot tool
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/raspberrypi/usbboot.git
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires: libusb-devel

%description
The Raspberry Pi usbboot allows you to flash the eMMC through an USB cable.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_bindir
install -c -m 0755 rpiboot %buildroot%_bindir

%files
%_bindir/rpiboot

%changelog
* Thu Oct 28 2021 Anton Midyukov <antohami@altlinux.org> 2021.10.27-alt1
- initial build for ALT Sisyphus
