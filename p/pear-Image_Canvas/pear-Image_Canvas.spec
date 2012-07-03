%define pear_name Image_Canvas

Name: pear-Image_Canvas
Version: 0.3.1
Release: alt2

Summary: A package providing a common interface to image drawing, making image source code independent on the library used

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.0b1

%description
A package providing a common interface to image drawing, making image
source code independent on the library used.

%prep
%setup -c -n %pear_name-%version
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Image/Canvas.php
%pear_dir/Image/Canvas/
%pear_testdir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Mon Jan 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus

