%define confname apt.eter.conf
%define vendorname etersoft.list

Name: apt-conf-etersoft-common
Version: 2.0
Release: alt2

BuildArch: noarch

Summary: Etersoft vendor configuration files for apt

License: GPL
Group: System/Configuration/Packaging
Url: http://git.etersoft.ru/people/sin/packages/apt-conf-etersoft-common.git

Packager: Evgemy Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar

Requires: alt-gpgkeys >= 0.7.35

%description
This package contains vendor configuration for Etersoft repositories.

%package -n apt-conf-etersoft-hold
Summary: Etersoft addittional configuration files for apt
Group: System/Configuration/Packaging
Obsoletes: apt-conf-etersoft <= 1.0

%description -n apt-conf-etersoft-hold
This package contains configuration file, which set HOLD on packages:
 kernel-headers* and kernel-headers-modules*

%prep
%setup -q

%install
mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
mkdir -p %buildroot%_sysconfdir/apt/vendors.list.d
install -p -m644 %confname %buildroot%_sysconfdir/apt/apt.conf.d/%confname
install -p -m644 %vendorname %buildroot%_sysconfdir/apt/vendors.list.d/%vendorname

%files
%config(noreplace) %_sysconfdir/apt/vendors.list.d/%vendorname
%doc README

%files -n apt-conf-etersoft-hold
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%confname

%changelog
* Wed Mar 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.0-alt2
- add requires to apt-gpgkeys with Etersoft keys

* Wed Feb 09 2011 Evgeny Sinelnikov <sin@altlinux.ru> 2.0-alt1
- rename package to apt-conf-etersoft-common
- add subpackage apt-conf-etersoft-hold with original holds

* Fri Oct 17 2008 Konstantin Baev <kipruss@altlinux.org> 1.0-alt1
- initial build
