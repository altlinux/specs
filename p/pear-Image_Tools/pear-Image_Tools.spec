%define pear_name Image_Tools

Name: pear-Image_Tools
Version: 1.0.0
Release: alt1

Summary: PHP/PEAR class for image manipulation

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %pear_name-%version.tar

BuildArchitectures: noarch

BuildRequires: pear-core rpm-build-pear
Requires: pear-core pear-Image_Color pear-PHP_Compat php5-gd2

%description
Image_Tools PEAR class is a tools collection of common image manipulations.
Available extensions are Blend, Border, Marquee, Mask, Swap, Thumbnail and
Watermark.

%prep
%setup -c -n %pear_name-%version

mv Image_Tools-1.0.0RC1 Image_Tools-1.0.0

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
%pear_dir/Image*
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
