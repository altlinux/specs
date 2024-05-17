%define git cd99f0d

Name: uhubctl
Version: 2.5.0
Release: alt0.2.g%{git}
Summary: Utility to control USB power per-port on smart USB hubs
Group: System/Configuration/Hardware
License: GPLv2
Url: https://github.com/mvp/uhubctl

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libusb-devel

%description
uhubctl is utility to control USB power per-port on smart USB hubs.
Smart hub is defined as one that implements per-port power switching.

Original idea for this code was inspired by hub-ctrl.c by Niibe Yutaka:
https://www.gniibe.org/development/ac-power-control-by-USB-hub

Compatible USB hubs
===================

Note that very few hubs actually support per-port power switching.
Some of them are no longer manufactured and can be hard to find.

%prep
%setup

%build
CFLAGS="%optflags" %make_build

%install
mkdir -p %buildroot{%_sbindir,%_udevrulesdir}
install -m755 %name %buildroot%_sbindir/
install -m644 udev/rules.d/*.rules %buildroot%_udevrulesdir/

%files
%doc README.md LICENSE COPYING
%_udevrulesdir/*.rules
%_sbindir/%name

%changelog
* Fri May 17 2024 L.A. Kostis <lakostis@altlinux.ru> 2.5.0-alt0.2.gcd99f0d
- Updated to v2.5.0-36-gcd99f0d.

* Wed Sep 27 2023 L.A. Kostis <lakostis@altlinux.ru> 2.5.0-alt0.1
- Initial build for ALTLinux.
