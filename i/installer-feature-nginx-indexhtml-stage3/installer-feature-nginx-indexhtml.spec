Name: installer-feature-nginx-indexhtml-stage3
Version: 0.1
Release: alt1

%define hookdir %_datadir/install2/postinstall.d

Summary: Setup nginx's userdir module
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: nginx-webapps

Source1: 80-nginx-indexhtml.sh

%description
This package contains installer stage3 hook to setup
nginx's default http/https pages.

%prep

%install
mkdir -p %buildroot%hookdir
install -pm755 %SOURCE1 %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 18 2014 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

