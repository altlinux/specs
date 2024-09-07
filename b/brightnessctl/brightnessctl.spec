%define _unpackaged_files_terminate_build 1

Name: brightnessctl
Version: 0.5.1
Release: alt2

Summary: Configuring display brightness
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/Hummer12007/brightnessctl

#Source-url: https://github.com/Hummer12007/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: systemd-devel

%description
This program allows you read and control device brightness on Linux. Devices,
by default, include backlight and LEDs (searched for in corresponding classes).
If omitted, the first found device is selected.

%prep
%setup

%build
export ENABLE_SYSTEMD=1
%make_build

%install
%makeinstall_std INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=%prefix

%files
%doc LICENSE
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Sat Sep 07 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.5.1-alt2
- use only systemd

* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux
