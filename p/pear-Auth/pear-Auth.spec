%define pear_name Auth

Name: pear-Auth
Version: 1.6.1
Release: alt1

Summary: Creating an authentication system

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Auth

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Auth-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The PEAR::Auth package provides methods for creating an authentication
system using PHP.

Currently it supports the following storage containers to read/write
the login data:

* All databases supported by the PEAR database layer
* All databases supported by the MDB database layer
* All databases supported by the MDB2 database layer
* Plaintext files
* LDAP servers
* POP3 servers
* IMAP servers
* vpopmail accounts
* RADIUS
* SAMBA password files
* SOAP (Using either PEAR SOAP package or PHP5 SOAP extension)
* PEAR website
* Kerberos V servers
* SAP servers

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
%pear_dir/Auth
%pear_testdir/Auth/
%pear_dir/Auth.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- new version 1.6.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- initial build for ALT Linux Sisyphus

