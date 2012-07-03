Name: installer-feature-systemd-stage3
Version: 0.2
Release: alt1

Summary: Set up systemd support
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch
Requires: installer-common-stage3

%description
%summary

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Nov 16 2011 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- ported from stage2 to stage3 (now suitable for livecd as well)

* Fri Nov 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- init with installer-sdk

