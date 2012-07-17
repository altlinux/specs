Version: 0.1.0
Release: alt0.3.1

Summary: Tartarus DNS client support
Name: Tartarus-dnsupdate
License: %gpl2plus
Group: System/Configuration/Other
Url: http://www.tartarus.ru
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar
Source1: tdnsupdate.init.%_vendor
Patch: Tartarus-dnsupate-0.1.0-alt-DSO.patch

Requires: Tartarus-common >= 0.1.0

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ python-base scons Tartarus-DNS-slice
BuildRequires: libkrb5user-devel >= 0.1.0
BuildRequires: libice-devel

%description
Tartarus DNS client support

%prep
%setup -q
%patch -p2

%build
scons

%install
scons install --install-sandbox=%buildroot

mkdir -p %buildroot%_initdir
cp %SOURCE1 %buildroot%_initdir/tdnsupdate

%post
%post_service tdnsupdate

%preun
%preun_service tdnsupdate

%files
%_sbindir/*
%_initdir/*
%config(noreplace) %_sysconfdir/Tartarus/clients/*

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt0.3.1
- Fixed build

* Mon Dec 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt0.3
- fix required version of Tartarus-common

* Thu Nov 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt0.2
- add init script for ALTLinux build

* Wed Nov 26 2008 Ivan A. Melnikov <iv@altlinux.org> 0.1.0-alt0.1
- new version:
  - removed join functionality
  - renamed tdnsupdatge to Tartarus-dnsupdate
- renamed package Tartarus-dnsupdate

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt4
- Rename tjoin to Tartarus-join
- Fixed name of DNS/Server identity

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt3
- Fix deploy, rename templates

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt2
- Fix for renamed Kadmin5 to Kerberos and System python module to system

* Wed Nov 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt1
- Build tdnsupdate with alpha interface
- Problem with time sync for SPN kinit not fixed yet...

* Thu Oct 23 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt5
- Fixed for using krb5user_set_ccname()

* Wed Oct 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt4
- Fixed tdnsupdate for keytab kinit and exception handling
- Remove old keytab records before adds new records in tjoin
- Added tdnsupdate config

* Tue Oct 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt3
- Fixed tjoin
- Changed Sconstruct

* Mon Oct 20 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt2
- Added config templates
- Added tdnsupdate utility

* Sat Jul 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt1
- Initial client deployment utility for Tartarus
