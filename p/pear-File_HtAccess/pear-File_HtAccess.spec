%define pear_name File_HtAccess

Name: pear-File_HtAccess
Version: 1.2.1
Release: alt3

Summary: Manipulate .htaccess files

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/File_HtAccess

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/File_HtAccess-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides methods to create and manipulate .htaccess files.

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
%pear_testdir/File_HtAccess/
%pear_dir/File
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

