%define pear_name Math_Integer

Name: pear-Math_Integer
Version: 0.8
Release: alt3

Summary: Package to represent and manipulate integers

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Math_Integer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Integer-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The class Math_Integer can represent integers bigger than the
signed longs that are the default of PHP, if either the GMP or
the BCMATH (bundled with PHP) are present. Otherwise it will fall
back to the internal integer representation.
The Math_IntegerOp class defines operations on Math_Integer objects.

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

