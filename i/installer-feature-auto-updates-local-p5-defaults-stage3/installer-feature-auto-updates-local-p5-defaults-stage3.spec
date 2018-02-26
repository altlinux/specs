# vim: set ft=spec: -*- rpm-spec -*-

Name: installer-feature-auto-updates-local-p5-defaults-stage3
Version: 0.1
Release: alt1

Summary: Automatic updates from local source
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: alterator-updates avahi-daemon

Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup automatic updates
from local source.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Oct 08 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build

