Name: gosa
Version: 2.6.11
Release: alt1

Summary: Web Based LDAP Administration Program
License: GPL
Group: Networking/WWW

Url: http://gosa.gonicus.de
BuildArch: noarch

Source0: gosa-core-%version.tar
Source1: gosa-plugins-%version.tar
Source2: %name.apache.conf
Source3: gosa-core.schema
Source4: gosa-schemas-fds.tar

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: rsync

Requires:  %name-common = %version-%release, %name-php, %name-httpd

%description
GOsa is a combination of system-administrator and end-user web
interface, designed to handle LDAP based setups.
Provided is access to posix, shadow, samba, proxy, fax, and kerberos
accounts. It is able to manage the postfix/cyrus server combination
and can write user adapted sieve scripts.

%package common
Group: Networking/WWW
Summary: gosa common stuff
Requires: fping smbldap-tools perl-Crypt-SmbHash gettext-tools
Requires: /usr/bin/convert

%description common
%summary

%package apache
Group: Networking/WWW
Summary: apache1 configs for gosa
Requires: %name-common = %version-%release, apache
Provides: gosa-httpd

%description apache
%summary

%package apache2
Group: Networking/WWW
Summary: apache2 configs for gosa
Requires: %name-common = %version-%release, apache2
Provides: gosa-httpd

%description apache2
%summary

%package php5
Group: Networking/WWW
Summary: package for install all php dependencies for gosa (php5)
Requires: %name-common = %version-%release
Requires: php-engine php5-ldap php5-imap php5-mysql php5-gd2
Requires: php5-mbstring php5-libs php5-mhash php5-snmp
#Requires: php5-imagick
Provides: gosa-php

%description php5
%summary

%package schema
Group: Networking/WWW
Summary: Schema Definitions for the GOSA package
Requires: openldap-servers openldap-clients

%description schema
Contains the Schema definition files for the GOSA admin package.

%package fds-schema
Group: Networking/WWW
Summary: Schema Definitions for the GOSA package (Fedora Directory Server)
Requires: fedora-ds

%description fds-schema
Contains the Schema definition files for the GOSA admin package (Fedora
Directory Server).

%package user-manual-en
Group: Networking/WWW
Summary: English online user-manual for GOSA package
Requires: %name-common = %version-%release

%description user-manual-en
English online user-manual page for GOSA package

%add_findreq_skiplist %_datadir/%name/plugins/mail/contrib/*
%add_findreq_skiplist %_datadir/%name/plugins/nagios/contrib/*
%add_findreq_skiplist %_datadir/%name/plugins/samba/contrib/*
%add_findreq_skiplist %_datadir/%name/plugins/squid/contrib/*

%prep
%setup -n gosa-core-%version -a 1 -a 4
# apply RH patches included in distribution
patch -p1 < redhat/02_fix_class_mapping.patch
patch -p1 < redhat/03_fix_locale_location.patch
patch -p1 < redhat/04_fix_online_help_location.patch

%install
install -dm1770 %buildroot%_var/spool/%name
install -d %buildroot%_var/cache/%name
install -dm0750 %buildroot%_sysconfdir/%name/

# Cleanup lyx warnings
find . -name WARNINGS -delete

# Cleanup latex shit
find . -name labels.pl -delete

# Cleanup guide
rm -rf doc/core/*/lyx-source

# php
mkdir -p %buildroot%_datadir/%name
DIRS="ihtml plugins html include locale setup"
for i in $DIRS; do
	cp -r $i %buildroot%_datadir/%name
done
install -d %buildroot%_datadir/%name/doc/core/
cp -r doc/core/en %buildroot%_datadir/%name/doc/core/

# binary
install -d %buildroot%_bindir/
install -pDm0755 update-gosa %buildroot%_sbindir/update-gosa
install -pDm0755 bin/mkntpasswd %buildroot%_bindir/
install -pDm0755 bin/gosa-encrypt-passwords %buildroot%_bindir/

# contrib
install -pD -m0644 contrib/gosa.conf %buildroot%_datadir/%name/doc/gosa.conf
install -pD -m0644 contrib/shells %buildroot%_sysconfdir/%name/
install -pD -m0644 contrib/encodings %buildroot%_sysconfdir/%name/
install -pD -m0644 contrib/openldap/slapd.conf %buildroot%_defaultdocdir/%name-common-%version/slapd.conf-example

# schemas
install -dm0755 %buildroot%_sysconfdir/openldap/schema/%name
mv contrib/openldap/*.schema %buildroot%_sysconfdir/openldap/schema/%name

# manpages
install -pDm0644 update-%name.1 %buildroot%_man1dir/update-%name.1
install -pDm0644 gosa-encrypt-passwords.1 %buildroot%_man1dir/gosa-encrypt-passwords.1
install -pDm0644 contrib/%name.1 %buildroot%_man1dir/%name.1
install -pDm0644 contrib/%name.conf.5 %buildroot%_man5dir/%name.conf.5

# configs
touch %buildroot%_sysconfdir/%name/gosa.secrets
install -p doc/core/guide.xml %buildroot%_sysconfdir/%name/guide.xml

install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/httpd2/conf/addon.d/%name.conf

install -dm0755 %buildroot%_datadir/%name/fedora-ds/schema/
mv gosa-schemas-fds/*.ldif %buildroot%_datadir/%name/fedora-ds/schema/

# plugins
pushd gosa-plugins
for plugin in *; do
	if [ `stat -c%%h $plugin/html` -gt 2 ] 2>/dev/null; then
		install -d %buildroot%_datadir/%name/html/plugins/$plugin
		mv $plugin/html/* %buildroot%_datadir/%name/html/plugins/$plugin/
	fi
	if [ `stat -c%%h $plugin/contrib` -gt 2 ] 2>/dev/null; then
		install -d %buildroot%_defaultdocdir/%name-common-%version/plugins/$plugin/
		mv $plugin/contrib/* %buildroot%_defaultdocdir/%name-common-%version/plugins/$plugin/
	fi
	if [ `stat -c%%h $plugin/help` -gt 2 ] 2>/dev/null; then
		install -d %buildroot%_datadir/%name/doc/plugins/$plugin
		mv $plugin/help/* %buildroot%_datadir/%name/doc/plugins/$plugin/
	fi
	if [ `stat -c%%h $plugin/etc` -gt 2 ] 2>/dev/null; then
		mv $plugin/etc/* %buildroot%_sysconfdir/%name/
	fi
	if [ `stat -c%%h $plugin/locale` -gt 2 ] 2>/dev/null; then
		install -d %buildroot%_datadir/%name/locale/plugins/$plugin
		mv $plugin/locale/* %buildroot%_datadir/%name/locale/plugins/$plugin/
	fi
	for s in addons admin generic personal; do
		if [ -d $plugin/$s ]; then
			rsync -rt $plugin/$s %buildroot%_datadir/%name/plugins/
		fi
	done
done
popd

%post apache
/sbin/service httpd condreload

%postun apache
/sbin/service httpd condreload

%post apache2
/sbin/service httpd2 condreload

%postun apache2
/sbin/service httpd2 condreload

%post common
%_sbindir/update-gosa ||:

%files

%files common
%doc AUTHORS README* Changelog COPYING INSTALL FAQ
%_mandir/man?/*
%dir %_datadir/%name
%dir %_datadir/%name/doc
%_datadir/%name/html
%_datadir/%name/ihtml
%_datadir/%name/include
%_datadir/%name/locale
%_datadir/%name/plugins
%_datadir/%name/setup
%_bindir/*
%_sbindir/*
%dir %attr(1770,root,%webserver_group) %_spooldir/%name
%dir %attr(1770,root,%webserver_group) %_var/cache/%name
%dir %attr(0750,root,%webserver_group) %_sysconfdir/%name
%_sysconfdir/%name/*
%dir %_datadir/%name/doc/core
%_datadir/%name/doc/gosa.conf
%_datadir/%name/doc/plugins

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/%name.conf

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/addon.d/%name.conf

%files php5

%files schema
%dir %_sysconfdir/openldap/schema/%name
%_sysconfdir/openldap/schema/%name/*

%files fds-schema
%_datadir/%name/fedora-ds/schema/*.ldif

%files user-manual-en
%_datadir/%name/doc/core/en

%changelog
* Tue Dec 07 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.6.11-alt1
- 2.6.11
- Apply RH patches fixes paths.
- Remove control(8) support and use %%webserver_group where needed.
- Package manpages.
- Drop user-manual subpackages except -en.

* Wed Jul 01 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.19-alt1
- 2.5.19

* Mon May 18 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.17-alt1
- 2.5.17
- drop php4 support

* Thu Dec 27 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.14-alt1
- New upstream 2.5.14
- see Changelog for details

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.13-alt2
- Fixed "undefined class dhcpplugin" bug
- Added schema files for Fedora DS

* Tue Oct 02 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.13-alt1
- New upstream 2.5.13
- Russian translation update
- Minor bugfixes and improvements
- see Changelog for details

* Thu Aug 09 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.12-alt2
- Resolve bug #12510,#12512,#12514

* Mon Jul 23 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.12-alt1
- New upstream 2.5.12
- Translation update (now russian translation realy works)
- Archive cleanup
- Minor bugfixes and improvements
- see Changelog for details

* Tue Jul 03 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.11a-alt2
- setup dir was unpackaged, fixed

* Mon Jun 18 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.11a-alt1
- New upstream 2.5.11a
- Added chinese translation
- Fixed language detection and removed line wraps in tab headers
- Fixed french translation

* Thu May 31 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.11-alt1
- New upstream 2.5.11
- Add workaround for failing is_php4() when using PHP5 with "zend.ze1_compatibility_mode" set to "On"
- Backported new sieve filter editor from trunk
- Backported new setup from trunk
- Fixed double loaded pages in gecko based browsers when js is activated
- Replaced a set of PHP <? short tag occurences
- Updated locales (de/fr)

* Fri May 25 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.10-alt1
- New upstream 2.5.10
- Included hook to make use of dynamic uid-bases
- Included vacation date range specification
- Fixed non-saved Samba-Domain changes in groups
- Freezed application parameters are not editable anymore
- Fixed problem with removing commata based DN's
- Corrected setup generated perl mkntpasswd string
- Fixed month listing in fax reports - february was march
- Enabled 9 digits for gid-/uidNumbers
- Fixed acl's for saving printers
- Fixed saving of disabled samba acl's
- Added support for rfc2307bis compliant groups

* Thu May 24 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.9-alt1
- spec file change to vvk@

* Fri Apr 20 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.9-alt0.2
- changed httpd to webserver

* Tue Mar 27 2007 Michail Yakushin <silicium@altlinux.ru> 2.5.9-alt0.1
- intial build for ALT

* Wed Jun 21 2006 Lars Scheiter <lars.scheiter@GONICUS.de> 2.5.1
- New upstream version

* Tue May 30 2006 Lars Scheiter <lars.scheiter@GONICUS.de> 2.5
- Updated RedHat dependencies
- New upstream version
- Spelling errors fixed ;)
- Seperation of online manual

* Mon Dec 19 2005 Lars Scheiter <lars.scheiter@GONICUS.de> 2.4-2
- Updated SuSE dependencies to php5

* Mon Nov 21 2005 Lars Scheiter <lars.scheiter@GONICUS.de> 2.4
- New upstream version
- Removed %%doc for postgresql and openexchange

* Wed Jun 01 2005 Lars Scheiter <lars.scheiter@GONICUS.de> 2.4beta1
- New upstream version
- Added gosa.conf to contrib dir
- Rearranged documentation stuff
- Updated dependencies
- compress some files

* Mon Feb 21 2005 Lars Scheiter <lars.scheiter@GONICUS.de> 2.3
- Update version to 2.3 (upstream)

* Mon Dec 13 2004 Lars Scheiter <lars.scheiter@GONICUS.de> 2.2-2
- Optionally allow different sourcenames

* Mon Nov 22 2004 Lars Scheiter <lars.scheiter@GONICUS.de> 2.2
- Update to 2.2 (upstream)
- reintroduction of suse detection
- small fixes
- Corrected URL
- Synchronize schema package name with debian

* Mon May 19 2004 Levente Farkas <lfarkas@lfarkas.org> 2.1.1
- update to 2.1.1

* Mon Apr 19 2004 Levente Farkas <lfarkas@lfarkas.org> 2.1
- update to 2.1

* Fri Apr 16 2004 Levente Farkas <lfarkas@lfarkas.org> 2.1
- minor fixes
- update to 2.1rc2

* Tue Jan 24 2004 Henning P. Schmiedehausen <hps@intermeta.de> 2.1-2t
- bumped to 2.1beta2
- first INTERMETA internal build

* Mon Oct 20 2003 Lars Scheiter <lars.scheiter@GONICUS.de>
- Update to new upstream release (2.0rc1)

* Fri Oct 17 2003 Lars Scheiter <lars.scheiter@GONICUS.de>
- First build of GOsa as an RPM, should work on SuSE and RedHat
