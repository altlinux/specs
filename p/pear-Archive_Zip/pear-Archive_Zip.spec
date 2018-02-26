%define pear_name Archive_Zip

Name: pear-Archive_Zip
Version: 0.1.1
Release: alt3

Summary: Zip file management class

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Archive_Zip

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Archive_Zip-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This class provides handling of zip files in PHP.
It supports creating, listing, extracting and adding to zip files.

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
%pear_dir/Archive
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus

