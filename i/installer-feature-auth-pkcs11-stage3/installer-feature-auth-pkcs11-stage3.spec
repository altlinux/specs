# vim: set ft=spec: -*- rpm-spec -*-

Name: installer-feature-auth-pkcs11-stage3
Version: 0.1
Release: alt1

Summary: Enable PKCS#11 authentication
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup PKCS#11
authentication.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Aug 05 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

