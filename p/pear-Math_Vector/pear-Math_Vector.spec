%define pear_name Math_Vector

Name: pear-Math_Vector
Version: 0.6.2
Release: alt2

Summary: Vector and vector operation classes

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Classes to represent Tuples, general Vectors, and 2D-/3D-vectors,
as well as a static class for vector operations.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%dir %pear_dir/Math/
%pear_dir/Math/Vector/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- initial build for ALT Linux Sisyphus

