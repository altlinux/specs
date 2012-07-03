%define pear_name Math_Combinatorics

Name: pear-Math_Combinatorics
Version: 1.0.0
Release: alt3

Summary: A package that produces combinations and permutations

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Math_Combinatorics

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Combinatorics-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
A package that returns all the combinations and permutations, without
repitition, of a given set and subset size. Associative arrays are
preserved.

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
%pear_testdir/Math_Combinatorics/
%pear_dir/Math
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

