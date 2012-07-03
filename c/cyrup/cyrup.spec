Name: cyrup
Version: 2.2.3
Release: alt3

Summary: Web interface for mail system based on Postfix MTA, Cyrus IMAP and MySQL/PostgreSQL
License: GPL
Group: System/Servers

Url: http://cyrup.sourceforge.net/
Source0: %name-%version.tar.bz2
Source1: %name.apache.conf
Source2: %name.htaccess.conf
Source3: README.ALT
Patch0: %name-alt-config.patch
Patch1: %name-alt-imaploginerror.patch

BuildArch: noarch
Packager: Timur Batyrshin <erthad@altlinux.org>

BuildRequires: rpm-macros-webserver-common
Requires: webserver-common, php-engine, php5-mysql

%description
The CyrUp is a web interface for mail system based on Postfix MTA, Cyrus IMAP
and MySQL/PostgreSQL. The CyrUp features multi-domain support in 2 ways and
rights delegation per domain. The Cyrup is best for mail systems with up to 100
mailboxes per domain.


%package apache
Summary: %name's apache config file
Group: System/Servers
Requires: %name = %version-%release, apache

%description apache
%name's apache config file


%prep
%setup
%patch0 -p2
%patch1 -p2

%install
mkdir -p %buildroot%_datadir/%name

cp -ar index.php install.php *.css %buildroot%_datadir/%name
cp -ar img includes js %buildroot%_datadir/%name

install -pD -m0640 config.inc.php %buildroot%_sysconfdir/%name/config.inc.php
ln -s %_sysconfdir/%name/config.inc.php %buildroot%_datadir/%name/
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/%name/htaccess
ln -s %_sysconfdir/%name/htaccess %buildroot%_datadir/%name/.htaccess

mv INSTALL.rpm INSTALL.rpm-based
rm -rf scripts/CVS

install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/%name.conf

#	quick hack to install files from %SOURCE to %docdir in %files section
cp %SOURCE3 .

%post apache
service httpd condreload

%postun apache
service httpd condreload



%files
%_datadir/%name
%dir %attr(0750,root,%webserver_group) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,%webserver_group) %_sysconfdir/%name/config.inc.php
%config(noreplace) %attr(0640,root,%webserver_group) %_sysconfdir/%name/htaccess
%doc CHANGELOG COPYING INSTALL* README TODO UPGRADE scripts README.ALT


%files apache
%_sysconfdir/httpd/conf/addon-modules.d/%name.conf
%_datadir/%name/.htaccess

%changelog
* Mon Mar 29 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.3-alt3
- Updated README.ALT

* Wed Nov 25 2009 Timur Batyrshin <erthad@altlinux.org> 2.2.3-alt2
- moved .htaccess from %_datadir to %_sysconfdir (closes #22372)
- added dependency for php5-mysql (closes #22373)
- added README.ALT, thanks to vvk@ (closes #22377)

* Mon Apr 06 2009 Timur Batyrshin <erthad@altlinux.org> 2.2.3-alt1
- Initial build for sisyphus
