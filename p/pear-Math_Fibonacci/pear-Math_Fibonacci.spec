%define pear_name Math_Fibonacci

Name: pear-Math_Fibonacci
Version: 0.8
Release: alt3

Summary: Package to calculat and manipulate Fibonacci numbers

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Math_Fibonacci

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Fibonacci-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Math_Integer

%description
The Fibonacci series is constructed using the formula:
      F(n) = F(n - 1) + F (n - 2),
By convention F(0) = 0, and F(1) = 1.
An alternative formula that uses the Golden Ratio can also be used:
      F(n) = (PHI^n - phi^n)/sqrt(5) [Lucas' formula],
where PHI = (1 + sqrt(5))/2 is the Golden Ratio, and
      phi = (1 - sqrt(5))/2 is its reciprocal
Requires Math_Integer, and can be used with big integers if the GMP or
the BCMATH libraries are present.

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- initial build for ALT Linux Sisyphus

