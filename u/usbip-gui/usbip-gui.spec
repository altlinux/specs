Name:    usbip-gui
Version: 20210429
Release: alt2

Summary: GUI for the usbip for easier usability/configurability

License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/K-Francis-H/usbip-gui

Source: %name-%version.tar

Source1: %name.desktop
Source2: %name
Source3: com.kfrancish.pkexec.usbip-gui.policy
Patch1: usbip-gui-fixemptylist.patch

BuildRequires(pre): rpm-macros-python3

BuildRequires: rpm-build-python3

BuildRequires: libpolkit-devel

Requires: usbip

BuildArch: noarch

# do not provide internal modules
AutoProv:no


%description
An attempt at wrapping the usbip linux kernel module with a gui
for easier usability/configurability.

%prep
%setup

%patch1 -p1

subst '1i#!/usr/bin/python3' gui.py

%install
install -D -m0644 gui.py %buildroot%_datadir/%name/gui.py
install -D -m0755 %SOURCE2 %buildroot%_bindir/%name
install -D -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D -m0644 %SOURCE3 %buildroot%_datadir/polkit-1/actions/com.kfrancish.pkexec.usbip-gui.policy

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/polkit-1/actions/com.kfrancish.pkexec.usbip-gui.policy

%changelog
* Tue Oct 08 2024 Elena Mishina <lepata@altlinux.org> 20210429-alt2
- run usbip-gui as root (closes #50508)
- fix empty local list (closes #50494)

* Sat Apr 20 2024 Vitaly Lipatov <lav@altlinux.ru> 20210429-alt1
- initial build for ALT Sisyphus
