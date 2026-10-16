%define oname ConfirmAccount
%define mwversion 1.46
%define commit f358585
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: This extension disables direct account creation and requires submission and approval.

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
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
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- update to REL1_46 snapshot f358585 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- version follows the MediaWiki version (extension.json has no version)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.39-alt1.596e436
- new version (1.39) with rpmgs script

* Sat Jun 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.34-alt2.fa306e94
- new version (1.34) with rpmgs script

* Sun Dec 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.34-alt1.3ffa446
- new version 1.34 (with rpmrb script)

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1.31-alt1.5d98110
- new version (1.31) with rpmgs script

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
