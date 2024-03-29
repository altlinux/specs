%define pear_name Math_Numerical_RootFinding

Name: pear-Math_Numerical_RootFinding
Version: 1.1.0a2
Release: alt1

Summary: Numerical Methods Root-Finding collection package

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/Math_Numerical_RootFinding

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Numerical_RootFinding-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Math_Numerical_RootFinding is the package
provide various Numerical Methods Root-Finding
functions implemented in PHP, e.g Bisection .
Newton-Raphson, Fixed Point, Secant etc

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
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.0a2-alt1
- new version 1.1.0a2 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

