%define ShortName AdminLinks

Name: mediawiki-extensions-%ShortName
Version: 0.2
Release: alt1

BuildArch: noarch

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Summary: Defines a special page that holds links meant to be helpful for wiki administrators

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.23

# Source-url: https://git.wikimedia.org/zip/?r=mediawiki/extensions/AdminLinks&format=gz
Source: %name-%version.tar

%description
Admin Links is an extension to MediaWiki that defines a special page,
"Special:AdminLinks", that holds links meant to be helpful for wiki
administrators; it is meant to serve as a "control panel" for the
functions an administrator would typically perform in a wiki. All users
can view this page; however, for those with the 'adminlinks' permission
(sysops/administrators, by default), a link to the page also shows up
in their user/navigation links, between "my talk" and "my preferences".

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Sat Nov 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new version 0.2 (with rpmrb script)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- initial build for ALT Linux Sisyphus
