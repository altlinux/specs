%define pear_name Console_Table

Name: pear-Console_Table
Version: 1.1.1
Release: alt1

Summary: Class that makes it easy to build console style tables

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/Console_Table

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Console_Table-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides methods such as addRow(), insertRow(), addCol() etc. to build
console tables with or without headers.

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
%pear_testdir/Console_Table/
%pear_dir/Console
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- initial build for ALT Linux Sisyphus

