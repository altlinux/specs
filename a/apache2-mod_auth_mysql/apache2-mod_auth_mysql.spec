Name: apache2-mod_auth_mysql
Version: 3.0.0
Release: alt7

Summary: mod_auth_mysql module for Apache 2 HTTP Server
License: Apache (BSD-like)
Group: System/Servers

Url: http://modauthmysql.sourceforge.net

# http://modauthmysql.sourceforge.net/
Source0: mod_auth_mysql-%version.tar
Source1: auth_mysql.load
Patch0: mod_auth_mysql-%version-%release.patch

Requires: apache2

# Automatically added by buildreq on Sat Jun 04 2005
BuildRequires: apache2-devel libMySQL-devel libapr1-devel libaprutil1-devel zlib-devel

%description
mod_auth_mysql is an Apache module to authenticate users and authorize access
through a MySQL database.  It is flexible and support several encryption
methods.  The module will work on Apache 2.x.

%prep
%setup -n mod_auth_mysql-%version
%patch0 -p1

%build
%_sbindir/apxs2 -c -I%_includedir/mysql mod_auth_mysql.c -lmysqlclient -lm -lz -lapr-1 -laprutil-1

%install
install -pDm0644 .libs/mod_auth_mysql.so %buildroot%_libdir/apache2/modules/mod_auth_mysql.so
install -pDm0644 %SOURCE1 %buildroot%_sysconfdir/httpd2/conf/mods-available/auth_mysql.load

%post
a2enmod auth_mysql >/dev/null
%_initdir/httpd2 condreload

%preun
if [ $1 -eq 0 ]; then
	a2dismod auth_mysql
	%_initdir/httpd2 condreload
fi

%files
%config(noreplace) %_sysconfdir/httpd2/conf/mods-available/auth_mysql.load
%_libdir/apache2/modules/*
%doc CHANGES CONFIGURE README

%changelog
* Thu Jan 12 2012 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt7
- Restore in Sisyphus

* Mon Sep 21 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.0.0-alt6
- auth_mysql.load: use relative path to module (Closes: #21591)

* Fri Sep 28 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.0.0-alt5
- Fix preun scriplet code (Closes: #12952)

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.0.0-alt4
- Rename package from mod_auth_mysql to apache2-mod_auth_mysql
- Drop all apache1 stuff
- Drop docs subpackage

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.0.0-alt3
- Change module activation way accordind to new apache2 scheme
- Fix working with apache2: use apr_pstrcat instead of ap_pstrcat

* Tue Mar 13 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.0.0-alt2
- Fix building with new apr
- Update buildrequires
- Switch to use .gear-tags

* Fri Dec 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.0.0-alt1
- 3.0.0 (Closes: #10409)
- Rebuild with new libmysqlclient (Closes: #10312)
- Cleanup spec
- Change Packager

* Sat Jun 04 2005 Vladimir Lettiev <crux@altlinux.ru> 2.9.0-alt1
- Initial release for ALT Linux Sisyphus
