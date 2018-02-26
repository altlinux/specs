Name: installer-feature-apache2-indexhtml-stage3
Version: 0.1
Release: alt6

%define hookdir %_datadir/install2/postinstall.d

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Summary: setup apache's userdir module
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Requires: apache2 apache2-mod_ssl

Source1: 80-apache-indexhtml.sh

%description
This package contains installer stage3 hook to setup
apache's default http/https pages.

%prep

%install
mkdir -p %buildroot%hookdir
install -pm755 %SOURCE1 %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Oct 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt6
- fix typo

* Mon Oct 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt5
- add /documentation addon

* Mon Oct 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt4
- fix httpd2 startup

* Fri Oct 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix indexhtml directory location

* Mon Aug 31 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2
- fix default apache2 configs

* Fri Aug 28 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- Initial

