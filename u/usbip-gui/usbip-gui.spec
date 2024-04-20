Name:    usbip-gui
Version: 20210429
Release: alt1

Summary: GUI for the usbip for easier usability/configurability

License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/K-Francis-H/usbip-gui

Source: %name-%version.tar

Source1: %name.desktop
Source2: %name

BuildRequires(pre): rpm-macros-python3

BuildRequires: rpm-build-python3

BuildArch: noarch

# do not provide internal modules
AutoProv:no


%description
An attempt at wrapping the usbip linux kernel module with a gui
for easier usability/configurability.

%prep
%setup

subst '1i#!/usr/bin/python3' gui.py

%install
install -D -m0644 gui.py %buildroot%_datadir/%name/gui.py
install -D -m0755 %SOURCE2 %buildroot%_bindir/%name
install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop

%changelog
* Sat Apr 20 2024 Vitaly Lipatov <lav@altlinux.ru> 20210429-alt1
- initial build for ALT Sisyphus
