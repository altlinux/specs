%define pear_name Math_Matrix

Name: pear-Math_Matrix
Version: 0.8.0
Release: alt3

Summary: Class to represent matrices and matrix operations

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Math_Matrix

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Matrix-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Math_Vector

%description
Matrices are represented as 2 dimensional arrays of numbers.
This class defines methods for matrix objects, as well as static methods
to read, write and manipulate matrices, including methods to solve systems

of linear equations (with and without iterative error correction).
Requires the Math_Vector package.

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
%pear_dir/Math
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- initial build for ALT Linux Sisyphus

