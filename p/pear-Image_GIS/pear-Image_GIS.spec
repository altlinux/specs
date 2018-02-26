%define pear_name Image_GIS

Name: pear-Image_GIS
Version: 1.1.1
Release: alt3

Summary: Visualization of GIS data

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_GIS

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_GIS-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: php5-gd2, pear-Cache_Lite, pear-Image_Color, pear-XML_SVG

%description
Generating maps on demand can be a hard job as most often you don't
have the maps you need in digital form.
But you can generate your own maps based on raw, digital data files
which are available for free on the net.
This package provides a parser for the most common format for
geographical data, the Arcinfo/E00 format as well as renderers to
produce images using GD or Scalable Vector Graphics (SVG).

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

