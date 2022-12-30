%define webappdir %webserver_webappsdir/mediawiki
%define major 1.39

%if_feature php7 7.4.3
%def_with php7
%define defphp php7
%endif

%if_feature php81 8.1.0
%def_with php81
%define defphp php8.1
%endif

%if_feature php80 8.0.0
%def_with php80
%define defphp php8.0
%endif


Name: mediawiki
Version: %major.0
Release: alt3

Summary: A wiki engine, typical installation (%defphp with Apache2 and MySQL support)

License: %gpl2plus
Group: Networking/WWW
Url: http://www.mediawiki.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source0: http://releases.wikimedia.org/mediawiki/%major/%name-%version.tar
Source1: mediawiki-apache2-alt-configs.tar
Source2: README.ALT-ru_RU.UTF-8
Source3: install_php_config.sh
Source4: mediawiki.ini
Source5: README.UPGRADE.ALT-ru_RU.UTF-8
Source6: AdminSettings.sample
Source7: 99-read-user-configs.php

Patch: %name-1.31-alt.patch
Patch1: %name-1.39-config-path.patch

BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-mediawiki >= 0.5
BuildRequires(pre): rpm-build-webserver-common
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-features >= 0.8

BuildRequires: apache2-devel

Requires: %name-common = %version-%release
Requires: %name-apache2
Requires: %defphp-mysqlnd-mysqli

%description
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers

This package supports wiki farms. Configure it through the web
interface. Remember to secure the config dir after completing the
configuration.

This is a typical %name installation (with Apache2 and MySQL support).

Also you can install %name-php8.0 (%name-php8.1, %name-php7)
package to get all needed php requires.

If you wish %name without any php dependencies, install only %name-common package.

%package -n %name-php7
Summary: Common files for %name
Group: Networking/WWW
Requires: webserver-common
# https://www.mediawiki.org/wiki/Compatibility
Requires: php7-libs >= 7.4.3
# inside php7-libs
# Requires: php7-ctype php7-iconv php7-json php7-xml
Requires: php7-dom php7-fileinfo php7-intl php7-mbstring
Requires: php7-mcrypt php7-xmlreader php7-gd
Requires: php7-opcache php7-apcu
Requires: php7-openssl

Requires: %name-common = %EVR


%package -n %name-php8.0
Summary: Common files for %name
Group: Networking/WWW
Requires: webserver-common
# https://www.mediawiki.org/wiki/Compatibility
Requires: php8.0-libs >= 8.0.0
# inside php8.0-libs
# Requires: php8.0-ctype php8.0-iconv php8.0-json php8.0-xml
Requires: php8.0-dom php8.0-fileinfo php8.0-intl php8.0-mbstring
Requires: php8.0-mcrypt php8.0-xmlreader php8.0-gd
Requires: php8.0-opcache php8.0-apcu
Requires: php8.0-openssl

Requires: %name-common = %EVR

%package -n %name-php8.1
Summary: Common files for %name
Group: Networking/WWW
Requires: webserver-common
# https://www.mediawiki.org/wiki/Compatibility
Requires: php8.1-libs >= 8.1.0
# inside php8.1-libs
# Requires: php8.1-ctype php8.1-iconv php8.1-json php8.1-xml
Requires: php8.1-dom php8.1-fileinfo php8.1-intl php8.1-mbstring
Requires: php8.1-mcrypt php8.1-xmlreader php8.1-gd
Requires: php8.1-opcache php8.1-apcu
Requires: php8.1-openssl

Requires: %name-common = %EVR


%package -n %name-common
Summary: Common files for %name
Group: Networking/WWW
Requires: webserver-common

Requires: diffutils
Requires: pear-Mail >= 1.4.1

AutoProv:no
AutoReq:yes,nomingw32,nomingw64,noerlang,noruby,nonodejs

# due shebang with node
%filter_from_requires /^node$/d

# since 1.20
Provides: mediawiki-extensions-ParserFunctions
Obsoletes: mediawiki-extensions-ParserFunctions

Provides: mediawiki-extensions-ConfirmEdit
Obsoletes: mediawiki-extensions-ConfirmEdit

Provides: mediawiki-extensions-SearchSuggest
Obsoletes: mediawiki-extensions-SearchSuggest

Provides: mediawiki-extensions-Nuke
Provides: mediawiki-extensions-Renameuser
Provides: mediawiki-extensions-WikiEditor

# since 1.21
Provides: mediawiki-extensions-Cite
Obsoletes: mediawiki-extensions-Cite

Provides: mediawiki-extensions-ImageMap
Obsoletes: mediawiki-extensions-ImageMap

Provides: mediawiki-extensions-Poem
Obsoletes: mediawiki-extensions-Poem

Conflicts: mediawiki-extensions-FCKEditor

Provides: mediawiki-extensions-TitleBlacklist
Provides: mediawiki-extensions-SpamBlacklist
Provides: mediawiki-extensions-InputBox
Provides: mediawiki-extensions-Interwiki
Provides: mediawiki-extensions-LocalisationUpdate
Provides: mediawiki-extensions-TitleBlacklist

# since 1.22
Provides: mediawiki-extensions-SimpleAntiSpam
Provides: mediawiki-extensions-PostEdit
Provides: mediawiki-extensions-Vector

# since 1.23
Provides: mediawiki-extensions-ExpandTemplates
Provides: mediawiki-extensions-AssertEdit

# since 1.27?
Provides: mediawiki-extensions-CiteThisPage
Provides: mediawiki-extensions-Gadgets

# since 1.29?
# we pack separate subpackage since 1.35
#Provides: mediawiki-extensions-PdfHandler
#Conflicts: mediawiki-extensions-PdfHandler < 1.24

# since 1.31
Provides: mediawiki-extensions-CategoryTree
Obsoletes: mediawiki-extensions-CategoryTree
Provides: mediawiki-extensions-CodeEditor
Obsoletes: mediawiki-extensions-CodeEditor
Provides: mediawiki-extensions-MultimediaViewer
Obsoletes: mediawiki-extensions-MultimediaViewer
Provides: mediawiki-extensions-OATHAuth
Obsoletes: mediawiki-extensions-OATHAuth
Provides: mediawiki-extensions-ReplaceText
Obsoletes: mediawiki-extensions-ReplaceText

# since 1.33
Obsoletes: mediawiki-extensions-StubManager

# since 1.34
# we pack separate subpackage since 1.37.1
#Provides: mediawiki-extensions-Scribunto
#Obsoletes: mediawiki-extensions-Scribunto

# since 1.35
Provides: mediawiki-extensions-VisualEditor
Obsoletes: mediawiki-extensions-VisualEditor

Provides: mediawiki-extensions-Parsoid
Obsoletes: mediawiki-extensions-Parsoid

# since 1.39
# we pack separate subpackage since 1.39
#Provides: mediawiki-extensions-Math

%description -n %name-common
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers.

%name-common have no php requires.

%description -n %name-php7
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers.

This package contains all needed php7 requires.

%description -n %name-php8.0
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers.

This package contains all needed php8.0 requires.

%description -n %name-php8.1
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers.

This package contains all needed php8.1 requires.

%package -n %name-apache2
Summary: Apache2's requires and config files for %name
Group: Networking/WWW
Requires: %name-common = %EVR
Requires: %name-%defphp = %EVR
Requires: apache2-common >= 2.2.0
Requires: %_initdir/%apache2_dname
Requires: apache2-httpd-prefork
Requires: apache2-mod_%defphp

%description -n %name-apache2
Install this package, if you wish to run %name under apache2 webserver.


%package -n %name-mysql
Summary: Virtual package for mysql requires for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: %defphp-mysqlnd-mysqli

%description -n %name-mysql
Install this package, if you wish to run %name with MySQL database.


%package -n %name-postgresql
Summary: Virtual package for postgresql requires for %name
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: %defphp-pgsql

%description -n %name-postgresql
Install this package, if you wish to run %name with PostgreSQL database.

%package -n %name-hiphop
Summary: Package with hihop support for %name
Group: Networking/WWW
Requires: %name-common = %version-%release

%description -n %name-hiphop
%summary

%package extensions-SyntaxHighlight_GeSHi
Epoch: 1
Summary: Extension for mediawiki to highlight source code with GeSHi
Summary(ru_RU.UTF-8): Расширение mediawiki для раскраски синтаксиса исходников с помощью GeSHi
Group: Networking/WWW
Requires: %name-common = %version-%release
Requires: python3-module-Pygments >= 2.2.0

%description extensions-SyntaxHighlight_GeSHi
The <syntaxhighlight> tags allow the display of preformatted code modules but in addition
they add coloring according to the code language settings. Like the <pre> tags
and the <poem> tags, they preserve white space, that is, they depict the code
module exactly as it was typed.

%package extensions-PdfHandler
Summary: PdfHandler extension shows uploaded pdf files in a multipage preview layout
Group: Networking/WWW
Requires: %name-common = %version-%release
Conflicts: %name-common < 1.35.0-alt4
# There are commands used. See https://www.mediawiki.org/wiki/Extension:PdfHandler
Requires: /usr/bin/gs
# poppler (needed for retrieving metainfo)
# Requires: /usr/bin/pdfinfo /usr/bin/pdftotext
# use convert wrapper from ImageMagick-tools or GraphicsMagick-ImageMagick-compat
Requires: /usr/bin/convert

%description extensions-PdfHandler
The extension shows uploaded pdf files in a multipage preview layout. With
enabled WebStore the extension generates automatically Images from the
specified page.

Recommended: poppler (for PDF metainfo retrieving)

%package extensions-Scribunto
Summary: The extension allows for embedding scripting languages in MediaWiki
Group: Networking/WWW
Requires: %name-common = %version-%release
Conflicts: %name-common < 1.37.1-alt1

# TODO: also can use php module luasandbox
Requires: /usr/bin/lua5.1
# we miss module versions
#Requires: php7-pcre >= 8.33
#Requires: php7-mbstring

%description extensions-Scribunto
The Scribunto (Latin: "they shall write") extension allows for embedding scripting languages in MediaWiki.
Currently the only supported scripting language is Lua.

%prep
%setup
%patch -p2
%patch1 -p2

%__subst "s|/usr/bin/python|/usr/bin/python3|" extensions/ConfirmEdit/*.py

%install
mkdir -p %buildroot%_mediawikidir/

# Copying to buildroot all files and directories and remove unneeded
cp -r * %buildroot%_mediawikidir/

# Not needed in the package (generate extra dependencies)
rm -rf %buildroot%_mediawikidir/maintenance/dev/
rm -rf %buildroot%_mediawikidir/maintenance/cssjanus/
rm -rf %buildroot%_mediawikidir/maintenance/hhvm/
rm -rf %buildroot%_mediawikidir/maintenance/resources/
rm -rf %buildroot%_mediawikidir/maintenance/{Makefile,mwjsduck-gen,jsduck/,resources/update-oojs.sh}
rm -rf %buildroot%_mediawikidir/tests/
rm -rf %buildroot%_mediawikidir/{*.php5,*.phtml}
rm -rf %buildroot%_mediawikidir/{COPYING,CREDITS,FAQ,HISTORY,README*,RELEASE-NOTES-*,UPGRADE}
rm -rf %buildroot%_mediawikidir/resources/lib/oojs-ui/update-oojs-ui.sh

rm -fr %buildroot%_mediawikidir/includes/zhtable
rm -rf %buildroot%_mediawikidir/maintenance/language/zhtable

rm -rf %buildroot%_mediawikidir/vendor/zordius/lightncandy/build/

# remove embedded lua binaries
rm -rv %buildroot%_mediawikidir/extensions/Scribunto/includes/engines/LuaStandalone/binaries

# devel tools, reqs node
rm -rfv %buildroot%_mediawikidir/vendor/wikimedia/parsoid/tools/test.selser.sh
rm -rfv %buildroot%_mediawikidir/vendor/wikimedia/parsoid/bin/
rm -rv %buildroot%_mediawikidir/extensions/VisualEditor/lib/ve/bin/
rm -rv %buildroot%_mediawikidir/extensions/VisualEditor/bin/
rm -rv %buildroot%_mediawikidir/vendor/wikimedia/wikipeg/tools/impact
rm -rfv  %buildroot%_mediawikidir/skins/MinervaNeue/dev-scripts


find %buildroot%_mediawikidir/ \
  \( -name .htaccess -or -name \*.cmi \) \
  -print0 \
  | xargs -r0 rm

# packed as docs
rm -rf %buildroot%_mediawikidir/docs/


mkdir -p %buildroot%_mediawikidir/config/

sed -i -e "s/__VERSION__/%version/g" %SOURCE2
sed -i -e "s/__VERSION__/%version/g" %SOURCE5
install -m 644 %SOURCE2 ./
install -m 755 %SOURCE3 ./
install -m 644 %SOURCE4 ./
install -m 644 %SOURCE5 ./


# fix permissions
#chmod +x %buildroot%_mediawikidir/bin/*
find %buildroot%_mediawikidir -name \*.pl -print0 | xargs -r0 chmod +x


mkdir -p %buildroot%webappdir/
cd %buildroot%_mediawikidir/
mv cache images %buildroot%webappdir/
ln -sf %webappdir/{cache,images} .

mkdir config/LocalSettings.d/
install -m 644 %SOURCE7 config/LocalSettings.d/
ln -sf %webappdir/config/LocalSettings.php config/

cd %buildroot%webappdir/
mkdir -p config/LocalSettings.d
install -m 600 %SOURCE6 config/
ln -s %_mediawikidir wiki

# Configs for apache2
mkdir -p %buildroot%apache2_confdir
pushd %buildroot%apache2_confdir
tar xvSf %SOURCE1
find -name \*.conf |xargs sed -i "s|WEBAPPDIR|%webappdir|"
popd

# TODO: use macro
# config for enable bundled ParserFunctions
cat > %buildroot%_mediawiki_settings_dir/50-ParserFunctions.php << EOF
<?php
wfLoadExtension('ParserFunctions');

# enable StringFunctions (like {{#pos, {{#len) by default
\$wgPFEnableStringFunctions = true;
EOF

cat > %buildroot%_mediawiki_settings_dir/50-PdfHandler.php << EOF
<?php
wfLoadExtension('PdfHandler');

\$wgFileExtensions[] = 'pdf';
EOF

cat > %buildroot%_mediawiki_settings_dir/50-Scribunto.php << EOF
<?php
wfLoadExtension('Scribunto');
\$wgScribuntoDefaultEngine = 'luastandalone';
\$wgScribuntoEngineConf['luastandalone']['luaPath'] = '/usr/bin/lua5.1';
EOF

# remove embedded python module
rm -rv %buildroot%_mediawikidir/extensions/SyntaxHighlight_GeSHi/pygments/*
# instead of set wgPygmentizePath
ln -s %_bindir/pygmentize3 %buildroot%_mediawikidir/extensions/SyntaxHighlight_GeSHi/pygments/pygmentize

# TODO: use macro
# config for enable bundled SyntaxHighlight_GeSHi
cat > %buildroot%_mediawiki_settings_dir/50-SyntaxHighlight_GeSHi.php << EOF
<?php
wfLoadExtension('SyntaxHighlight_GeSHi');
EOF

# pack separately
rm -rv %buildroot%_mediawikidir/extensions/Math/

%pre -n %name-common
if [ -L %_mediawikidir/config ]; then
	rm -f %_mediawikidir/config
fi
if [ -d %_datadir/%name/images -a ! -L %_datadir/%name/images ]; then
	rmdir %_datadir/%name/images 2>/dev/null || {
		mv %_datadir/%name/images %_datadir/%name/images.rpmsave
		echo "%_datadir/%name/images saved as %_datadir/%name/images.rpmsave"
	}
fi

%post -n %name-common
if [ $1 -eq 2 ] ; then
	cat <<EOF
Running MediaWiki update:
 # php %webappdir/wiki/maintenance/update.php
Check full upgrading manual on https://www.mediawiki.org/wiki/Manual:Upgrading
EOF
php %webappdir/wiki/maintenance/update.php || :
fi

%post -n %name-apache2
if [ "$CONF_OK" = "1" ]; then
    service %apache2_dname condrestart ||:
fi

%postun -n %name-apache2
if [ "$1" = "0" ] ; then # last uninstall
    service %apache2_dname condrestart ||:
fi

%files

%if_with php7
%files -n %name-php7
%endif

%if_with php80
%files -n %name-php8.0
%endif

%if_with php81
%files -n %name-php8.1
%endif

%files -n %name-common
%add_findreq_skiplist %_datadir/%name/config/LocalSettings.php
%_mediawikidir/
%exclude %_mediawikidir/extensions/SyntaxHighlight_GeSHi/
%exclude %_mediawiki_settings_dir/50-SyntaxHighlight_GeSHi.php
%exclude %_mediawikidir/extensions/PdfHandler/
%exclude %_mediawikidir/extensions/Scribunto/
%exclude %_mediawiki_settings_dir/50-PdfHandler.php
%exclude %_mediawiki_settings_dir/50-Scribunto.php
#exclude %_datadir/%name/maintenance/hiphop/
%attr(2750,root,%webserver_group) %dir %webappdir/
%attr(2770,root,%webserver_group) %dir %webappdir/config/
%attr(2770,root,%webserver_group) %dir %webappdir/config/LocalSettings.d/
%attr(2775,root,%webserver_group) %dir %webappdir/images/
%attr(2770,root,%webserver_group) %dir %webappdir/cache/
%webappdir/wiki/
%webappdir/images/*
%webappdir/config/AdminSettings.sample

%doc COPYING CREDITS FAQ HISTORY README.md RELEASE-NOTES-%major UPGRADE
%doc README.ALT-ru_RU.UTF-8 README.UPGRADE.ALT-ru_RU.UTF-8 install_php_config.sh mediawiki.ini
%doc docs

%files -n %name-apache2
%config %apache2_mods_start/*.conf
%config %apache2_extra_available/*.conf
%config %apache2_extra_start/*.conf
%config(noreplace) %apache2_sites_available/*.conf

# deprecated
%files -n %name-mysql

# deprecated
%files -n %name-postgresql

#%files -n %name-hiphop
#%_datadir/%name/maintenance/hiphop/

%files extensions-SyntaxHighlight_GeSHi
%_mediawikidir/extensions/SyntaxHighlight_GeSHi/
%_mediawiki_settings_dir/50-SyntaxHighlight_GeSHi.php
%doc extensions/SyntaxHighlight_GeSHi/README

%files extensions-PdfHandler
%_mediawikidir/extensions/PdfHandler/
%_mediawiki_settings_dir/50-PdfHandler.php

%files extensions-Scribunto
%_mediawikidir/extensions/Scribunto/
%_mediawiki_settings_dir/50-Scribunto.php

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.39.0-alt3
- remove embedded extension-Math (ALT bug 44708)

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 1.39.0-alt2
- use rpm-macros-features for build with supported php only

* Sun Dec 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1.39.0-alt1
- new version 1.39.0 (with rpmrb script)
- (T316304, CVE-2022-41767) (T309894, CVE-2022-41765)
- (T307278, CVE-2022-41766) (T311384, CVE-2022-27776)
- add mediawiki-php7, mediawiki-php8.0, mediawiki-php8.1 subpackages
- deprecate mediawiki-mysql and mediawiki-postgresql
  (install mediawiki-apache2 or php8.0-mysqlnd-mysqli)

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1.37.2-alt1
- new version 1.37.2 (with rpmrb script)
- (T297571, CVE-2022-28201) (T297731, CVE-2022-28203)
- (T297754, CVE-2022-28204) (T297543, CVE-2022-28202)

* Thu Feb 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1.37.1-alt2
- pack Scribunto extension separately

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.37.1-alt1
- new version 1.37.1 (with rpmrb script)
- (T292763, CVE-2021-44854) (T271037, CVE-2021-44856)
- (T297322, CVE-2021-44857) (T297322, CVE-2021-44858)
- (T297574, CVE-2021-45038) (T293589, CVE-2021-44855) (T294686)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36.2-alt1
- new version 1.36.2 (with rpmrb script)

* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36.1-alt1
- new version 1.36.1 (with rpmrb script)
- (T280226, CVE-2021-35197): Prevent blocked users from purging pages

* Sat Jun 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36.0-alt2
- fix httpd2 reload

* Sun Jun 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.36.0-alt1
- new version 1.36.0 (with rpmrb script)

* Wed May 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.35.2-alt2
- fix build

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.35.2-alt1
- new version 1.35.2 (with rpmrb script)
- (T270453, CVE-2021-30153) (T270713, CVE-2021-30152)
- (T270988, CVE-2021-30155) (T272386, CVE-2021-30159)
- (T276843, CVE-2021-20270, CVE-2021-27291)
- (T277009, CVE-2021-30158) (T278014, CVE-2021-30154)
- (T278058, CVE-2021-30157) (T279451, CVE-2021-30458)

* Wed Dec 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.35.1-alt1
- new version 1.35.1 (with rpmrb script)
- T268894, CVE-2020-35474, T268917, CVE-2020-35475
- T268938, CVE-2020-35478, CVE-2020-35479
- T205908, CVE-2020-35477, T120883, CVE-2020-35480

* Mon Nov 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1.35.0-alt4
- pack extensions-PdfHandler separately in a subpackage

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.35.0-alt3
- pack subpackage extensions-SyntaxHighlight_GeSHi

* Thu Oct 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.35.0-alt2
- use php7-gd instead of ImageMagick by default
- use php7-mysqlnd-mysqli instead of php7-mysqli (ALT bug 39162)

* Fri Oct 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1.35.0-alt1
- new version 1.35.0 LTS (with rpmrb script)
- CVE-2020-25813, CVE-2020-25812, CVE-2020-25815
- CVE-2020-17367, CVE-2020-17368, CVE-2020-25814
- CVE-2020-25828, CVE-2020-25869, CVE-2020-25827

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.34.2-alt1
- new version 1.34.2 (with rpmrb script)
- CVE-2020-15005

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.34.1-alt2
- add Obsoletes: mediawiki-extensions-Scribunto (ALT bug 38653)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.34.1-alt1
- new version 1.34.1 (with rpmrb script)
- security fixes T232932, T246602

* Wed Jan 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.34.0-alt2
- add pear-Mail requires
- add php7-opcache requires (ALT bug 31471)

* Sun Dec 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.34.0-alt1
- new version 1.34.0 (with rpmrb script)
- CVE-2019-19709

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.33.1-alt1
- new version 1.33.1 (with rpmrb script)
- CVE-2019-16738

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.33.0-alt1
- new version 1.33.0 (with rpmrb script)

* Thu Jun 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.32.2-alt1
- new version 1.32.2 (with rpmrb script)
- CVE-2019-12468, CVE-2019-12473, CVE-2019-12471
- CVE-2019-12472, CVE-2019-12474, CVE-2019-12467
- CVE-2019-12466, CVE-2019-12469, CVE-2019-12470
- CVE-2019-11358

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1.32.1-alt1
- new version 1.32.1 (with rpmrb script)

* Sun Mar 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.32.0-alt1
- new version 1.32.0 (with rpmrb script)

* Sat Sep 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1.31.1-alt1
- new version 1.31.1 (with rpmrb script)
- CVE-2018-0503, CVE-2018-0505, CVE-2018-1325
- fix apache configs

* Mon Jul 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt1
- new version 1.31.0 (with rpmrb script)

* Sun Apr 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1.30.0-alt2
- switch to php7 using

* Fri Mar 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.30.0-alt1
- new version 1.30.0 (with rpmrb script)

* Thu Mar 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.29.2-alt2
- NMU: added conflict with mediawiki-extensions-PdfHandler
  (included in 1.29) (closes: #34708)

* Mon Dec 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.29.2-alt1
- new version 1.29.2 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.29.1-alt1
- new version 1.29.1 (with rpmrb script)

* Sun Aug 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.29.0-alt1
- new version 1.29.0 (with rpmrb script)

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.28.2-alt1
- new version 1.28.2 (with rpmrb script)

* Thu Aug 04 2016 Vitaly Lipatov <lav@altlinux.ru> 1.27.0-alt1
- new version 1.27.0 (with rpmrb script)

* Fri Oct 30 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23.11-alt3
- cleanup spec, fix error in post install script

* Fri Oct 30 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23.11-alt2
- cleanup spec, fix error in config

* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23.11-alt1
- new version 1.23.11 (with rpmrb script)
- security fixes

* Sat Feb 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23.8-alt2
- it seems PdfHandler was bundled by mistake. drop provides/obsoletes for it
- enable StringFunctions by default

* Sat Feb 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.23.8-alt1
- new version 1.23.8 (with rpmrb script)
- disable skin using autodiscovery mechanism warning

* Tue Dec 09 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.7-alt1
- just import mediawiki-1.23.7.tar with rpmgs script
- disable skin using autodiscovery mechanism warning

* Thu Nov 13 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.6-alt1
- new version 1.23.6 (with rpmrb script)

* Fri Sep 26 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.4-alt1
- new version 1.23.4 (with rpmrb script)

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.3-alt1
- new version 1.23.3 (with rpmrb script)

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.2-alt2
- cleanup spec, drop -tex subpackage (use mediawiki-extensions-Math package)

* Wed Aug 20 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.2-alt1
- new version 1.23.2 (with rpmrb script)

* Sat Jul 26 2014 Vitaly Lipatov <lav@altlinux.ru> 1.23.1-alt1
- new version 1.23.1 (with rpmrb script)

* Thu Mar 13 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.4-alt1
- new version 1.22.4 (with rpmrb script)
- drop php5-apc requires

* Mon Mar 03 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.3-alt1
- new version 1.22.3 (with rpmrb script)

* Thu Feb 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.2-alt1
- new version 1.22.2 (with rpmrb script)

* Wed Sep 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.2-alt2
- drop phpinfo from blacklist (ALT bug #29329)
- add provides/obsoletes for the bundled extension PdfHandler

* Fri Sep 06 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.2-alt1
- new version 1.21.2 (with rpmrb script)
- add php5-dom requires (ALT bug #29328)

* Tue Sep 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.1-alt1
- new version 1.21.1 (with rpmrb script)
- move intree changes to the patch file
- add provides/obsoletes for follow bundled extensions:
  Cite, ImageMap, Poem

* Sat Apr 27 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.4-alt2
- update README.UPGRADE.ALT
- use macros from rpm-build-mediawiki
- enable ParserFunctions

* Mon Apr 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.4-alt1
- 1.20.4 release

* Tue Feb 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.2-alt1
- 1.20.2 release

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.16.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt1
- 1.16.0 release
- Engine to read user's configs from %webappdir/config/LocalSettings.d/

* Mon May 31 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt0.beta3
- New beta release

* Fri May 21 2010 Michael A. Kangin <prividen@altlinux.org> 1.16.0-alt0.beta2
- Pre-release of new version

* Mon Mar 22 2010 Michael A. Kangin <prividen@altlinux.org> 1.15.2-alt1
- 1.15.2

* Wed Jan 20 2010 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt5
- Fix installation with active mod_rewrite (Closes: #22768)
- Move TeX support into mediawiki-tex package

* Fri Dec 25 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt4
- Fix upgrade from previous version (Closes: #22585)
- New configs layout
- Upgrade notes

* Sun Dec 20 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt3
- Spec cleanup
- Change packages layout

* Sun Jul 19 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt2
- LocalSettings.d/ engine

* Sat Jul 18 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.1-alt0
- 1.15.1

* Mon Jun 22 2009 Michael A. Kangin <prividen@altlinux.org> 1.15.0-alt0
- 1.15.0
- redesign package

* Wed Apr 15 2009 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt4
- Fix Requires (Closes: #19506)

* Thu Sep 04 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt3
- Add README.ALT-ru_RU.UTF-8

* Wed Sep 03 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt2
- Removed Requires: tetex-latex, tetex-dvips
- Fix aliases.

* Sat Aug 30 2008 Aleksey Avdeev <solo@altlinux.ru> 1.13.0-alt1
- Update to 1.13.0.

* Tue Jun 03 2008 Aleksey Avdeev <solo@altlinux.ru> 1.10.4-alt1
- First build for ALT.

