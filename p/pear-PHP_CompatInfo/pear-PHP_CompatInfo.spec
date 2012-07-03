%define pear_name PHP_CompatInfo

Name: pear-PHP_CompatInfo
Version: 1.7.0
Release: alt1

Summary: Find out the minimum version and the extensions required for a piece of code to run

License: PHP License 3.01
Group: Development/Other
Url: http://pear.php.net/package/PHP_CompatInfo

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_CompatInfo-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PHP_CompatInfo will parse a file/folder/script/array to find out the
minimum
version and extensions required for it to run. Features advanced debug
output
which shows which functions require which version and CLI output script

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
%pear_dir/PHP/
%_bindir/pci
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml
%pear_testdir/%pear_name/


%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- initial build for ALT Linux Sisyphus

