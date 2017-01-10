%define major 9

Name: owncloud%major
Version: 9.1.3
Release: alt3
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

%define installdir %webserver_webappsdir/%name

Summary: Cloud platform
Group: Networking/WWW
License: AGPLv3
Url: https://owncloud.org/

BuildRequires(pre): rpm-macros-webserver-common
BuildArch: noarch

Requires(pre): webserver-common

#https://doc.owncloud.org/server/9.1/admin_manual/installation/source_installation.html
Requires: php5 >= 5.4 php5-libs php5-dom php5-gd2 php5-mbstring php5-xmlreader php5-zip php5-curl php5-fileinfo
Requires: memcached php5-memcache php5-memcached 
#For SQLite:
Requires: php5-pdo
#For MySQL:
#Requires: MySQL-server php5-pdo_mysql

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%description
ownCloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %version-%release apache2-mod_php5 apache2-mod_ssl

%description apache2
Apache 2.x web-server default configuration for %name.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
Requires: %name = %version-%release nginx
#Requires: php5-cgi php5-fpm-fcgi php5-apcu

%description nginx
nginx web-server default configuration for %name.

%prep
%setup

%install
mkdir -p %buildroot%installdir
cp -rp %name/* %buildroot%installdir/
cp %name/.htaccess %buildroot%installdir/
cp %name/.user.ini %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr
find %buildroot%installdir/ -name .gitignore -type f | xargs -L 1 rm
rm -f %buildroot%installdir/l10n/l10n.pl

mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%installdir/config/ %buildroot%_sysconfdir/%name/.
ln -s %_sysconfdir/%name/config %buildroot%installdir/config

mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

#install apache2
install -pD -m0644 apache2/default.conf %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

#install nginx
install -pD -m0644 nginx/default.conf %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf

%post
chmod -R 777 %installdir

%post apache2
chown -R apache2:apache2 %installdir
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%installdir/
%dir %attr(0770,root,_webserver) %_sysconfdir/%name/config/
%_sysconfdir/%name
%dir %attr(0770,root,_webserver) %_localstatedir/%name

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%files nginx
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf 

%changelog
* Tue Jan 10 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt3
- Cleanup requires for *-nginx

* Fri Dec 30 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt2
- Added package *-nginx (default config)

* Thu Dec 29 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.3-alt1
- 9.1.3
- Added package *-apache2 (default config)

* Wed Nov 30 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.2-alt1
- 9.1.2

* Tue Oct 04 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt3
- Fix path to %installdir

* Mon Oct 03 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt2
- Fixed requires

* Thu Sep 29 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt1
- 9.1.1
