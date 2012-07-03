%define pear_name DB_ldap

Name: pear-DB_ldap
Version: 1.2.0
Release: alt1

Summary: DB interface to LDAP server

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/DB_ldap

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB_ldap-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-DB

%description
The PEAR::DB_ldap class provides a DB compliant interface to LDAP servers

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/DB
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

