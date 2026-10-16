%define oname AdminLinks
%define mwversion 1.46
%define commit 9989837
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 0.7.1
Release: alt1

Summary: Defines a special page that holds links meant to be helpful for wiki administrators

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:Admin_Links

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Admin Links is an extension to MediaWiki that defines a special page,
"Special:AdminLinks", that holds links meant to be helpful for wiki
administrators; it is meant to serve as a "control panel" for the
functions an administrator would typically perform in a wiki. All users
can view this page; however, for those with the 'adminlinks' permission
(sysops/administrators, by default), a link to the page also shows up
in their user/navigation links, between "my talk" and "my preferences".

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,Gruntfile.js,package.json,package-lock.json,composer.lock}

%files -f %oname.files

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- update to REL1_46 snapshot 9989837 (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Sat Nov 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new version 0.2 (with rpmrb script)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- initial build for ALT Linux Sisyphus
