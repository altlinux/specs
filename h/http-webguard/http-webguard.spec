%define modname http
%define webguard webguard
%define user http-webguard
%define wg_group %user
%define home /var/lib/%modname-%webguard
%define home_tmp %home/tmp
%define logdir /var/log/%modname-%webguard
%define confdir %_sysconfdir/%modname-%webguard
%define datadir %_datadir/%modname-%webguard
%define webroot %datadir/html
%define smresources smresources
%define lockdir /var/lock/http-webguard

Name: %modname-%webguard
Version: 1.9
Release: alt1

Summary: HTTP proxy server
License: non-exclusive
Group: Security/Networking

Packager: Lenar Shakirov <snejok@altlinux.org>

BuildRequires: webguard webguard-devel
Requires: libpcre3, zlib

## for /usr/sbin/useradd
#Requires(pre): shadow-utils
#Requires(post): chkconfig
## for /sbin/service
#Requires(preun): chkconfig, initscripts
#Requires(postun): initscripts

Source: %name-%version.tar
Source1: %name.init
Source2: %name.logrotate

Conflicts: http-webguard-debug

ExclusiveArch: x86_64 %ix86

%ifarch x86_64
%define dir_arch 64bit
%endif
%ifarch %ix86
%define dir_arch 32bit
%endif

%description
The product is a software data protection designed to protect against unauthorized access to the Web-server queuing system. The product is responsible for the authentication and authorization of users, and makes registration of user activity in the system (audit), filtering HTTP- user requests.
Web-guard system is designed for external differentiation of user rights in the application due to restricting access the WEB resources for WEB-applications.

%prep
%setup

%install

cd %dir_arch/

install -p -d -m 0755 %buildroot%confdir
cp -r etc/http-webguard/* %buildroot%confdir

install -p -d -m 0755 %buildroot%_sbindir
cp usr/sbin/%name %buildroot%_sbindir/%name

cd -

find %buildroot -type f -name .packlist -exec rm -f {} \;
find %buildroot -type f -name perllocal.pod -exec rm -f {} \;
find %buildroot -type f -empty -exec rm -f {} \;
find %buildroot -type f -exec chmod 0644 {} \;
find %buildroot -type f -name '*.so' -exec chmod 0755 {} \;
chmod 0755 %buildroot%_sbindir/%name
#install -p -d -m 0755 %buildroot%confdir/conf.d
#install -p -d -m 0755 %buildroot%webroot
install -p -d -m 0755 %buildroot%home_tmp
install -p -d -m 0755 %buildroot%logdir
install -p -d -m 0755 %buildroot%datadir
#cp -r usr/share/http-webguard/* %buildroot%datadir
install -p -d -m 0755 %buildroot%datadir/%smresources
cp -r %smresources %buildroot%datadir

install -p -D -m 0755 %SOURCE1 %buildroot%_initdir/%name
install -p -d -m 0755 %buildroot%_sysconfdir/logrotate.d
install -p -D -m 0644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name

install -p -d -m 0755 %buildroot%lockdir

%pre
if [ $1 == 1 ]; then
    %_sbindir/useradd -c "Http-webguard user" -s /bin/false -r -d %home %user 2>/dev/null || :
fi

%post
%post_service %name
echo "Note: to start http-webguard type the following command:"
echo "service http-webguard start"

%preun
%preun_service %name

%files
#%_bindir/*
#%_man1dir/*
#%doc AUTHORS NEWS README
%doc LICENSE CHANGES README
%datadir/
%_sbindir/%name
#%_mandir/man3/%name.3pm.gz
%_initrddir/%name
%dir %confdir
#%dir %confdir/conf.d
%dir %logdir
%dir %lockdir
#%config(noreplace) %confdir/conf.d/*.conf
%config(noreplace) %confdir/win-utf
#%config(noreplace) %confdir/%name.conf.default
%config(noreplace) %confdir/%name.conf.default
%config(noreplace) %confdir/mime.types.default
%config(noreplace) %confdir/fastcgi.conf
%config(noreplace) %confdir/fastcgi.conf.default
%config(noreplace) %confdir/fastcgi_params
%config(noreplace) %confdir/fastcgi_params.default
%config(noreplace) %confdir/scgi_params
%config(noreplace) %confdir/scgi_params.default
%config(noreplace) %confdir/uwsgi_params
%config(noreplace) %confdir/uwsgi_params.default
%config(noreplace) %confdir/koi-win
%config(noreplace) %confdir/koi-utf
%config(noreplace) %confdir/%name.conf
%config(noreplace) %confdir/mime.types
%config(noreplace) %_sysconfdir/logrotate.d/%name
#%config(noreplace) %_sysconfdir/sysconfig/%name
#%dir %perl_vendorarch/auto/%name
#%perl_vendorarch/%name.pm
#%perl_vendorarch/auto/%name/%name.so
%attr(-,%user,%wg_group) %dir %home
%attr(-,%user,%wg_group) %dir %home_tmp

%changelog
* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.org> 1.9-alt1
- update to version 1.9; init scripts and logrotation added
* Thu Dec 12 2013 Lenar Shakirov <snejok@altlinux.org> 1.3-alt1
- initial build for ALT Linux Sisyphus
