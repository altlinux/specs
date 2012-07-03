%define pear_name Math_Stats

Name: pear-Math_Stats
Version: 0.8.5
Release: alt3

Summary: Classes to calculate statistical parameters

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Math_Stats

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Math_Stats-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Classes to calculate statistical parameters of numerical arrays
of data. The data can be in a simple numerical array, or in a
cummulative numerical array. A cummulative array, has the value
as the index and the number of repeats as the value for the
array item, e.g. $data = array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3).
Nulls can be rejected, ignored or handled as zero values.

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
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt1
- initial build for ALT Linux Sisyphus

