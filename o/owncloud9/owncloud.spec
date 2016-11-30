%define major 9

Name: owncloud%major
Version: 9.1.2
Release: alt1
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
Requires: memcached php5-memcache php5-memcached apache2-mod_php5
Requires: MySQL-server php5-pdo php5-pdo_mysql

Source0: %name-%version.tar

# Automatically added by buildreq on Mon Oct 03 2016
# optimized out: python-base python-modules python3
BuildRequires: python3-base

%description
ownCloud gives you easy and universal access to all of your files.
It also provides a platform to easily view, sync and share your contacts
calendars, bookmarks and files across all your devices.

%prep
%setup

%install
mkdir -p %buildroot%installdir
cp -rp %name/* %buildroot%installdir/
cp %name/.htaccess %buildroot%installdir/
cp %name/.user.ini %buildroot%installdir/

find %buildroot%installdir/ -name tests -type d | xargs rm -fr
rm -f %buildroot%installdir/l10n/l10n.pl

mkdir -p %buildroot%_sysconfdir/%name
mv %buildroot%installdir/config/ %buildroot%_sysconfdir/%name/.
ln -s %_sysconfdir/%name/config %buildroot%installdir/config

mkdir -p %buildroot%_localstatedir/%name
ln -s %_localstatedir/%name %buildroot%installdir/data

%post
chmod -R 777 %installdir
chown -R apache2:apache2 %installdir

%files
%installdir/
%dir %attr(0770,root,_webserver) %_sysconfdir/%name/config/
%_sysconfdir/%name
%dir %attr(0770,root,_webserver) %_localstatedir/%name

%changelog
* Wed Nov 30 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.2-alt1
- 9.1.2

* Tue Oct 04 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt3
- Fix path to %installdir

* Mon Oct 03 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt2
- Fixed requires

* Thu Sep 29 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 9.1.1-alt1
- 9.1.1
