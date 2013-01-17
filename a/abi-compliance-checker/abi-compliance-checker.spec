Name: abi-compliance-checker
Version: 1.98.6
Release: alt1

Summary: ABI compliance checker

Group: Development/Other
License: GPLv2+
Url: http://ispras.linuxbase.org/index.php/ABI_compliance_checker
# TODO: upstream seems to change source tarball publication policy
Source: %name-%version.tar.gz
Requires: gcc binutils

BuildArch: noarch

%description
ABI-compliance-checker is a lightweight tool for checking backward binary
compatibility of shared C/C++ libraries in OS Linux. It checks interface
signatures and data type definitions in two library versions (headers and
shared objects) and searches differences that may lead to incompatibility
according to ABI standards. Breakage of the compatibility may result in
crashing or incorrect behavior of applications built with an old version of
a library when it is running with a new one. ABI-compliance-checker was
intended for library developers that are interested in ensuring backward
binary compatibility. Also ABI-compliance-checker may be used for checking
forward binary compatibility and compliance checking of the same library
versions on different linux distributions.

%prep
%setup

%install
install -d %buildroot%_bindir
##install -m0755 abi-compliance-checker.pl %buildroot%_bindir/abi-compliance-checker
perl Makefile.pl -install --prefix=%_prefix --destdir=%buildroot

%files
%doc doc README INSTALL
%_bindir/abi-compliance-checker
%_datadir/%name

%changelog
* Fri Jan 11 2013 Fr. Br. George <george@altlinux.ru> 1.98.6-alt1
- Autobuild version bump to 1.98.6

* Wed Nov 17 2010 Vitaly Lipatov <lav@altlinux.ru> 1.21.9-alt1
- new version 1.21.9 (with rpmrb script)

* Tue Jul 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.19-alt1
- new version 1.19 (with rpmrb script)

* Thu Dec 31 2009 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- new version 1.12 (with rpmrb script)

* Thu Oct 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- initial build for ALT Linux Sisyphus

* Sat Sep 05 2009 Oden Eriksson <oeriksson@mandriva.com> 1.6-1mdv2010.0
+ Revision: 432064
- 1.6

* Thu Aug 06 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2010.0
+ Revision: 410938
- 1.1

* Sat Aug 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2010.0
+ Revision: 405312
- import abi-compliance-checker

* Sat Aug 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2009.0
- initial Mandriva package
