# spec file for PEAR PHP package Image_Barcode2
#

%define pear_name Image_Barcode2

Name: pear-%pear_name
Version: 0.2.3
Release: alt1

Summary: PHP/PEAR class for barcode generation

License: PHP License 3.0
Group: Development/Other
Url: http://pear.php.net/package/Image_Barcode2
#Url: https://github.com/pear/Image_Barcode2

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %pear_name-%version.tar

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear
Requires: pear-core php5-gd2

%description
PHP PEAR class Image_Barcode2 is a way to create a barcode
representation of a given string.

This class uses GD function because of this the generated
graphic can be any of GD supported supported image types.


%prep
%setup -n %pear_name-%version

mkdir %pear_name-%version

mv -- Image tests docs README build.xml phpunit.xml %pear_name-%version/

# Fix md5 sums:
#sed -e 's/5a3f7691cee306adc8b2eaf645401426/d134d6824cc5625de57f1fe6b4970c4d/' -i package.xml

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc CHANGELOG LICENSE
%pear_xmldir/%pear_name.xml
%pear_dir/Image*
%pear_dir/docs*
%exclude %pear_dir/data*
%exclude %pear_dir/tests*


%changelog
* Tue Mar 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.3-alt1
- initial build for ALT Linux Sisyphus
