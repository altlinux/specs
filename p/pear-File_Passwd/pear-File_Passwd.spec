%define pear_name File_Passwd

Name: pear-File_Passwd
Version: 1.1.6
Release: alt4

Summary: Manipulate many kinds of password files

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

#Requires: php5-pcre

%description
Provides methods to manipulate and authenticate against standard Unix,
SMB server, AuthUser (.htpasswd), AuthDigest (.htdigest), CVS pserver
and custom formatted password files.

%prep
%setup -c -n %pear_name-%version

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
%pear_dir/File/Passwd.php
%pear_dir/File/Passwd/
%pear_testdir/File_Passwd/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt4
- autorebuild for correct requires(pre) (see bug #16086)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt3
- fix file packing

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- initial build for ALT Linux Sisyphus

