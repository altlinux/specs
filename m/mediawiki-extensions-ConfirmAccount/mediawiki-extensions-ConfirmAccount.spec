%define oname ConfirmAccount
%define major 1.23
%define revision b0651c1

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

Summary: This extension disables direct account creation and requires submission and approval.

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.23

# Source-url: https://extdist.wmflabs.org/dist/extensions/ConfirmAccount-REL1_23-b0651c1.tar.gz
Source: %oname-%version.tar

%description
The ConfirmAccount extension disables direct account creation
and requires submission and approval of accounts by bureaucrats.
Account creations can be enabled through configuring user rights,
such as if you wanted Sysops/Bureaucrats to be able to directly make them.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.23.b0651c1-alt1
- new version (1.23.b0651c1) with rpmgs script

* Wed Feb 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.74fabfc-alt1
- new version (1.22.74fabfc) with rpmgs script

* Tue Sep 10 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.d8632fb-alt1
- new version 1.21.d8632fb (with rpmrb script)

* Wed Jul 24 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.83ae0c9-alt1
- new version (1.20.83ae0c9)

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt2
- rename spec
- fixes for MW > 1.16

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt1
- new version (1.16.r62787) import in git

