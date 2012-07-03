%define pear_name Image_Barcode

Name: pear-Image_Barcode
Version: 1.1.0
Release: alt3

Summary: Barcode generation

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_Barcode

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_Barcode-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
With Image_Barcode class you can create a barcode
representation of a given string.

This class uses GD function because of this the generated graphic can be
any of GD supported supported image types.

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

