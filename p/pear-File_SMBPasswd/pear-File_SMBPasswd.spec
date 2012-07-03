%define pear_name File_SMBPasswd

Name: pear-File_SMBPasswd
Version: 1.0.2
Release: alt3

Summary: Class for managing SAMBA style password files

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/File_SMBPasswd

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_SMBPasswd-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Crypt_CHAP >= 1.0.0, php5-mhash

%description
With this package, you can maintain smbpasswd-files, usualy used by SAMBA.

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
%pear_dir/File
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

