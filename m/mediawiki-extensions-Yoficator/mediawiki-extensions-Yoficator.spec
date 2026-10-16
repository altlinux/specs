%define oname Yoficator
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.0.0
Release: alt1

Summary: MediaWiki extension to restore the letter yo (yofication) in WikiEditor

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://soulibre.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

Source: %oname-%version.tar

%description
Yoficator is an extension for WikiEditor that restores the letter yo
(Russian letter with diaeresis) in the edited text. The dictionary is built
into the script.

The ext.yoficator ResourceLoader module is loaded by the extension itself
on the edit page, so it does not have to be declared in LocalSettings.php
($wgResourceModules) and does not have to be loaded from MediaWiki:Common.js.

Optional AI hints for ambiguous words are requested only on a user action
from a proxy on the editor's own machine (http://localhost:8667);
the proxy is not a part of this package.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# the extension requires WikiEditor (it is a part of mediawiki-common)
sed -i "s|^wfLoadExtension( '%oname' );|wfLoadExtension( 'WikiEditor' );\nwfLoadExtension( '%oname' );|" \
    %buildroot%_mediawiki_settings_dir/50-%oname.php
grep -q "'WikiEditor'" %buildroot%_mediawiki_settings_dir/50-%oname.php

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
