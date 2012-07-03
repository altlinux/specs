# vim: set ft=spec: -*- rpm-spec -*-

Name: installer-feature-shm-defaults-stage3
Version: 0.1
Release: alt1

Summary: Setup sane shared memory defaults
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup sane shared memory
defaults suitable for database server.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Sat Aug 01 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

