%define ShortName ReplaceText

Name: mediawiki-extensions-%ShortName
Version: 0.9.7
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: GPL

%define mwversion 1.22
# convert version for Source URL (set before Summary:)
%define REL %(echo "REL%mwversion" | sed -e "s|\\.|_|g")

Summary: MediaWiki extension for allow administrators to do a global string find-and-replace

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= %mwversion

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-ReplaceText/legacy.tar.gz/%REL
Source: %name-%version.tar

%description
Replace Text is an extension to MediaWiki that provides a special page
to allow administrators to do a global string find-and-replace on both
the text and titles of the wiki's content pages.

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName
%__subst "4i\$wgGroupPermissions['sysop']['replacetext'] = true;" %buildroot%_mediawiki_settings_dir/50-%ShortName.php

%files -f %ShortName.files

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Mon May 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus
