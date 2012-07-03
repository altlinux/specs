Name: installer-feature-apache2-userdir-stage3
Version: 0.1
Release: alt1

%define hookdir %_datadir/install2/postinstall.d

Summary: setup apache's userdir module
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: apache2

Source: %name-%version.tar

%description
This package contains installer stage3 hook to setup
apache's userdir.

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
