%define vdata 20220914

Name: sddm-sweet-nova-theme
Version: 1.0.%vdata
Release: alt1.1
BuildArch: noarch

%define sname Sweet-nova
%define mname sweet-nova-theme
%define sddm_user sddm
%define sddm_conf %_sysconfdir/X11/sddm/sddm.conf

Summary: SDDM theme with Apple TV sweet-nova videos
License: GPL-3.0
Group: Other
Url: https://store.kde.org/p/1334945

Requires: libkf5plasmaquick sddm

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %sname-%version.tar
Source1: sweet-nova-theme.conf

%description
%summary

%prep
%setup -n %sname
subst 's/Different User/List Users/'  Main.qml

%install
install -d %buildroot%_datadir/sddm/themes/%mname/
cp -ar .  %buildroot%_datadir/sddm/themes/%mname
install -d  %buildroot%_sysconfdir/sddm.conf.d/
install -D  %SOURCE1  %buildroot%_sysconfdir/sddm.conf.d/

%files
%_datadir/sddm/themes/%mname/
%attr(0640,root,%sddm_user) %_sysconfdir/sddm.conf.d/%mname.conf

%changelog
* Sun Mar 19 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.20220914-alt1.1
- Fix spec

* Sat Mar 18 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.20220914-alt1
- initial build for ALT Sisyphus

