# vim: set ft=spec: -*- rpm-spec -*-

Name: installer-feature-auth-pkcs11-workbench-defaults-stage3
Version: 0.2
Release: alt1

Summary: PKCS#11 authentication defaults
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: pam_pkcs11

Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup PKCS#11
authentication defaults:

 - card_only true;
 - wait_for_card true;
 - cert_policy signature;
 - use_mappers pwent;

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Sep 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2-alt1
- Enabled CA check

* Wed Aug 05 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

