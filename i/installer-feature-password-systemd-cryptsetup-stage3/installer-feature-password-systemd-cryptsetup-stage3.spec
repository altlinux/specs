Name: installer-feature-password-systemd-cryptsetup-stage3
Version: 0.1
Release: alt1

Summary: Store password for systemd-cryptsetup in encrypted root fs
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%define hookdir %_datadir/install2/postinstall.d
%define script 40-password-systemd-cryptsetup.sh
%define travers disk-tree-travers.py

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 %script %buildroot%hookdir/
install -pD -m755 %travers %buildroot%_bindir/%travers

%files
%hookdir/%script
%_bindir/%travers

%changelog
* Tue Jun 21 2022 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
