Name: ipplan
Version: 6.00
Release: alt1.BETA2

%define ipplandir %_datadir/%name
%define ipplanconfdir %_sysconfdir/%name


Summary: IP address management and tracking
Group: Networking/Other
License: GPL
Url: http://sourceforge.net/projects/iptrack/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source0: %name-%version-BETA2.tar.gz
# Patch0: %name-mdv_conf.diff

Requires: nmap
Requires: %name-config = %version-%release webserver webserver-common
BuildPreReq: rpm-macros-webserver-common

BuildArch: noarch

%description
IPplan is a Web-based, multilingual IP address management and
tracking tool based on PHP which simplifies the administration of
your IP address space. It can handle a single network or multiple
networks with overlapping address spaces. It features
internationalization, importing of network definitions from
routing tables, importing of definitions from TAB-delimited files
and NMAP's XML format, support for multiple administrators with
different access profiles (per group, per customer, per network
etc.), definitions of address space authority boundaries per
group, finding free address space across a range, display of
overlapping address spaces between networks, search capabilities,
an audit log, statistics, and tracking and sending SWIP/registrar
information.

%package config-php5
License: GPL
Group: Networking/Other
Summary: Virtual package for php's depend.
Requires: php5-mysql php5-adodb php5-gettext php5-snmp
# Requires: php-layers-menu, php-PHPMailer
Provides: %name-config = %version-%release

%description config-php5
Virtual package for php5's depend.

%prep
%setup -q -n %{name}v6
# %patch0 -p0

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

# It is the file in the package whose name matches the format emacs or vim uses
# for backup and autosave files. It may have been installed by  accident.
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete


# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

# use external adodb
find . -name "*.php*" | xargs perl -pi -e "s|\"adodb/adodb.inc.php\"|\"%_datadir/php/modules/adodb/adodb.inc.php\"|g"
find . -name "*.php*" | xargs perl -pi -e "s|\"\.\./adodb/adodb.inc.php\"|\"%_datadir/php/modules/adodb/adodb.inc.php\"|g"
find . -name "*.php*" | xargs perl -pi -e 's|$this->ds->qstr|$this->ds->QMagic|g'


# strip away annoying ^M
find . -type f -name "*.php" -print0 | xargs -0 sed -i 's/\r//'
find . -type f -name "*.pl" -print0 | xargs -0 sed -i 's/\r//'

# path fix
find . -type f |  xargs perl -pi -e "s|/usr/local|/usr|g"

perl -pi -e "s|/var/spool/ipplanuploads|%_localstatedir/%name/uploads|" config.php
perl -pi -e "s|/tmp/export|/tmp/%name/export|" config.php
perl -pi -e "s|/tmp/dns|%_localstatedir/%name/dns|" config.php
perl -pi -e "s|/tmp/dhcp|%_localstatedir/%name/dhcp|" config.php

#remove bundled adodb
rm -rf adodb/

%build
%install

install -d %buildroot%ipplandir
cp -aRf * %buildroot%ipplandir

install -d %buildroot%_localstatedir/%name/uploads
install -d %buildroot%_localstatedir/%name/dns
install -d %buildroot%_localstatedir/%name/dhcp

# cleanup
rm -f %buildroot%ipplandir/CHANGELOG
rm -f %buildroot%ipplandir/CONTRIBUTORS
rm -f %buildroot%ipplandir/DNS-USAGE
rm -f %buildroot%ipplandir/INSTALL*
rm -f %buildroot%ipplandir/INTERNALS
rm -f %buildroot%ipplandir/LICENSE
rm -f %buildroot%ipplandir/README*
rm -f %buildroot%ipplandir/TODO
rm -f %buildroot%ipplandir/TRANSLATIONS
rm -f %buildroot%ipplandir/UPGRADE
rm -f %buildroot%ipplandir/TRIGGERS
rm -f %buildroot%ipplandir/messages.po
rm -rf %buildroot%ipplandir/contrib

# apache configuration
cat > %name.conf <<EOF
# %name Apache configuration file
Alias /%name %ipplandir
# Alias /menus %{_datadir}/php/php-layers-menu

<Directory %ipplandir>
	Options +FollowSymLinks
	AllowOverride Limit Options FileInfo
	Allow from all
</Directory>

<Directory %ipplanconfdir>
	Order Deny,Allow
	Deny from all
</Directory>

<DirectoryMatch "^%ipplandir/(.*/)?(adodb|templates)/(.*)?">
	Order Deny,Allow
	Deny from all
</DirectoryMatch>
EOF

# fix config
install -d %buildroot%ipplanconfdir
mv %buildroot%ipplandir/config.php %buildroot%ipplanconfdir/
pushd %buildroot%ipplandir/
    ln -s %ipplanconfdir/config.php config.php
popd

for lang in locale/*; do
	mkdir -p %buildroot%_datadir/locale/`basename $lang`/LC_MESSAGES
	mkdir -p %buildroot%ipplandir/locale/`basename $lang`/LC_MESSAGES
	if [ -f $lang/LC_MESSAGES/*.mo ]; then
		for file in $lang/LC_MESSAGES/*.mo; do
			rm -f %buildroot%ipplandir/locale/`basename $lang`/LC_MESSAGES/`basename $file`
			cp -a $file %buildroot%_datadir/locale/`basename $lang`/LC_MESSAGES/%name.mo
			pushd %buildroot%ipplandir/locale/`basename $lang`/LC_MESSAGES
			ln -fs ../../../../locale/`basename $lang`/LC_MESSAGES/%name.mo messages.mo
			popd
		done
	fi
done
%find_lang %name

%files -f %name.lang
%doc  CHANGELOG CONTRIBUTORS INSTALL INSTALL-POSTGRESQL contrib
%doc INTERNALS README README.html TODO TRANSLATIONS UPGRADE TRIGGERS %name.conf
# %config(noreplace) %_sysconfdir/httpd/conf/webapps.d/%name.conf
%dir %ipplandir
%ipplandir/*
%dir %ipplanconfdir
%attr(640,root,%webserver_group) %config(noreplace) %ipplanconfdir/config.php
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name/uploads
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name/dns
%attr(2775,root,%webserver_group) %dir %_localstatedir/%name/dhcp

%files config-php5

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 6.00-alt1.BETA2
- 6.00-BETA2

* Tue Apr 06 2010 Alexey Shabalin <shaba@altlinux.ru> 6.00-alt1.BETA1
- initial build
