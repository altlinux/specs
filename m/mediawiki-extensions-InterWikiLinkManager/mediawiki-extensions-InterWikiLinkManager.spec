%define oname InterWikiLinkManager
%define major 1.15
%define revision r1223

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

Summary: This MediaWiki extension for manage the InterWiki Links

License:  No license specified
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.15.1-alt4

Requires: mediawiki-extensions-StubManager

# http://mediawiki.googlecode.com/svn/trunk/extensions/InterWikiLinkManager/
Source0: %oname-%version.tar

%description
This MediaWiki extension enables a user with the appropriate
rights to manage the InterWiki Links of the database.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
subst "4i\$wgGroupPermissions['sysop']['interwiki'] = true;" %buildroot%_mediawiki_settings_dir/50-%oname.php
subst "4i\$wgGroupPermissions['*']['interwiki'] = false;" %buildroot%_mediawiki_settings_dir/50-%oname.php


%files -f %oname.files

%changelog
* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r1223-alt1
- initial build for ALT Linux Sisyphus

