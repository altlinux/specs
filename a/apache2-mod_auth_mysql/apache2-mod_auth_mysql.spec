Name: %apache2_name-mod_auth_mysql
Version: 3.0.0
Release: alt7.1

Summary: mod_auth_mysql module for Apache 2 HTTP Server
License: Apache (BSD-like)
Group: System/Servers

Url: http://modauthmysql.sourceforge.net

# http://modauthmysql.sourceforge.net/
Source0: mod_auth_mysql-%version.tar
Source1: auth_mysql.load
Source2: auth_mysql.start
Patch0: mod_auth_mysql-%version-%release.patch

Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn

BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires: libMySQL-devel zlib-devel

%description
mod_auth_mysql is an Apache module to authenticate users and authorize access
through a MySQL database.  It is flexible and support several encryption
methods.  The module will work on Apache 2.x.

%prep
%setup -n mod_auth_mysql-%version
%patch0 -p1

%build
%apache2_apxs -c -I%_includedir/mysql mod_auth_mysql.c -lmysqlclient -lm -lz -lapr-1 -laprutil-1

%install
install -pDm0644 .libs/mod_auth_mysql.so %buildroot%apache2_moduledir/mod_auth_mysql.so
install -pDm0644 %SOURCE1 %buildroot%apache2_mods_available/auth_mysql.load
install -pDm0644 %SOURCE2 %buildroot%apache2_mods_start/100-auth_mysql.conf

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/auth_mysql.load

%files
%config(noreplace) %apache2_mods_available/auth_mysql.load
%config(noreplace) %apache2_mods_start/100-auth_mysql.conf
%ghost %apache2_mods_enabled/*.load
%apache2_moduledir/*
%doc CHANGES CONFIGURE README

%changelog
* Fri Feb 08 2013 Aleksey Avdeev <solo@altlinux.ru> 3.0.0-alt7.1
- Rebuild with apache2-2.2.22-alt16 (fix unmets)
- Add %%apache2_mods_start/100-auth_mysql.conf file for auto loading
  module
- Add %%ghost for %%apache2_mods_enabled/*.load

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
