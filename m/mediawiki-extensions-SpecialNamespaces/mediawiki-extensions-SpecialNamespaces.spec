%define oname SpecialNamespaces

Name: mediawiki-extensions-%oname
Version: 1.0gerrit
Release: alt1

Summary: Add new namespaces from Special:Namespaces page

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.20

Source: %oname-%version.tar

%description
Special:Namespaces is a MediaWiki extension that allows administrators
to create and modify custom namespaces without directly editing the
configuration files. It is based on Extension:SpecialInterwiki code,
originally released under GPL by Stephanie Amanda Stevens.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files
%doc README

%changelog
* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0gerrit-alt1
- update to gerrit:39720 (unreviewed)

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix missed <?php ?>

* Thu Sep 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

