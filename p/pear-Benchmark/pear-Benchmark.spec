%define pear_name Benchmark

Name: pear-Benchmark
Version: 1.2.9
Release: alt1

Summary: Framework to benchmark PHP scripts or function calls

License: New BSD
Group: Development/Other
Url: http://pear.php.net/package/Benchmark

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Benchmark-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Framework to benchmark PHP scripts or function calls.

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
%pear_dir/Benchmark/
%pear_dir/data/Benchmark/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)

* Fri Dec 17 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version 1.2.8 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt1
- initial build for ALT Linux Sisyphus

