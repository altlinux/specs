# vim: set ft=spec: -*- rpm-spec -*-

Name: installer-feature-pkcs11_eventmgr-gnome-stage3
Version: 0.3
Release: alt1

Summary: Enable pkcs11_eventmgr (GNOME)
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: pam_pkcs11 libopensc xinitrc gnome-screensaver gnome-session gnome-pkcs11-eventmgr GConf

Source: %name-%version.tar

%description
This package contains installer stage3 hook to enable pkcs11_eventmgr
for GNOME environment.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3-alt1
- Switch to gnome-pkcs11-eventmgr

* Tue Aug 11 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2-alt1
- Use XDG autostart

* Sat Aug 01 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

