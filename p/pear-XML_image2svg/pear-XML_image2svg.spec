%define pear_name XML_image2svg

Name: pear-XML_image2svg
Version: 0.1
Release: alt3

Summary: Image to SVG conversion

License: PHP 2.02
Group: Development/Other
Url: http://pear.php.net/package/XML_image2svg

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_image2svg-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The class converts images, such as of the format JPEG, PNG
and GIF to a standalone SVG representation. The image is being encoded
by the PHP native encode_base64() function. You can use it to get back
a complete SVG file, which is based on a predefinded, easy adaptable
template file, or you can take the encoded file as a return value, using
the get() method. Due to the encoding by base64, the SVG files will
increase approx. 30%% in size compared to the conventional image.

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
%pear_dir/XML
%pear_testdir/XML_image2svg/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

