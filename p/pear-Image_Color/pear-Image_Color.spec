%define pear_name Image_Color

Name: pear-Image_Color
Version: 1.0.2
Release: alt3

Summary: Manage and handles color data and conversions

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_Color

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_Color-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: php5-gd2

%description
Manage and handles color data and conversions.

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
%pear_dir/Image
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

