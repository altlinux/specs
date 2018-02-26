%define pear_name QA_Peardoc_Coverage

Name: pear-QA_Peardoc_Coverage
Version: 1.1.1
Release: alt3

Summary: PEAR documentation coverage analysis

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/QA_Peardoc_Coverage

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/QA_Peardoc_Coverage-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Takes the PEAR documentation CVS and the PEAR package CVS directories,
  and compares which packages have been documented.
  Also checks which classes and methods have been documented,
  and generates HTML reports.

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
%pear_dir/QA
%pear_testdir/QA_Peardoc_Coverage/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

