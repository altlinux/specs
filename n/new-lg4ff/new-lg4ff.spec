Name:    new-lg4ff
Version: 0.5.0
Release: alt1

Summary: Experimental Logitech force feedback module for Linux
License: GPL-2.0
Group:   System/Configuration/Hardware
Url:     https://github.com/berarma/new-lg4ff
VCS:     https://github.com/berarma/new-lg4ff.git

Source: %name-%version.tar

ExclusiveArch: i586 x86_64

Requires: dkms-%name = %EVR

%description
Improved Linux module driver for Logitech driving wheels.

Supported devices:

Logitech WingMan Formula GP (without force feedback)
Logitech WingMan Formula Force GP
Logitech Driving Force
Logitech MOMO Force Feedback Racing Wheel
Logitech Driving Force Pro
Logitech G25 Racing Wheel
Logitech Driving Force GT
Logitech G27 Racing Wheel
Logitech G29 Driving Force (switch in PS3 mode)
Logitech G923 Racing Wheel for PlayStation 4 and PC (046d:c267, 046d:c266)
Logitech MOMO Racing
Logitech Speed Force Wireless Wheel for Wii
This module is not compatible with the Logitech G920 Driving Force and
XBOX/PC version of the Logitech G923 (046d:c26d, 046d:c26e). Both wheels
use the HID++ protocol and are supported by the HID++ driver as of
kernel 6.3.

%package -n dkms-%name
Summary: %name DKMS package
Group: System/Configuration/Hardware
Requires: dkms

%description -n dkms-%name
%summary

%prep
%setup

sed -e s/0.1/%version/ -i dkms.conf

%build

%install
install -dm755 %buildroot%_usrsrc/%name-%version
install -dm755 %buildroot%_usrsrc/%name-%version/usbhid
install -m644 usbhid/usbhid.h %buildroot%_usrsrc/%name-%version/usbhid/
install -m644 hid-ids.h hid-lg.h hid-lg4ff.h %buildroot%_usrsrc/%name-%version/
install -m644 hid-lg.c hid-lg2ff.c hid-lg3ff.c hid-lg4ff.c hid-lgff.c %buildroot%_usrsrc/%name-%version/
install -m 644 Kbuild Makefile dkms.conf %buildroot%_usrsrc/%name-%version/


# %files
# %doc LICENSE README.md

%files -n dkms-%name
%_usrsrc/%name-%version/

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 0.5.0-alt1
- new version 0.5.0

* Mon Feb 24 2025 Sergey Palcheh <minergenon@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
