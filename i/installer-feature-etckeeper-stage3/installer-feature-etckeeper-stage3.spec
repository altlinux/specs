Name: installer-feature-etckeeper-stage3
Version: 1.0
Release: alt1

Summary: Installer stage3 etckeeper hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer stage3 hook for
etckeeper module.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Jun 06 2014 Anton Farygin <rider@altlinux.ru> 1.0-alt1
- first build for Sisyphus
