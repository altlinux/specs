Name: installer-feature-network-settings-copy
Version: 0.1.1
Release: alt1

Summary: Copying network settings from stage2 to installed system
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: https://www.altlinux.org/Installer/beans

Source: %name-%version.tar
BuildArch: noarch

%description
%summary.

%prep
%setup

%install
%makeinstall

%files
%_datadir/install2/preinstall.d/*

%changelog
* Wed Mar 19 2025 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- copy /etc/resolv.conf, if symlink

* Tue Mar 18 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
