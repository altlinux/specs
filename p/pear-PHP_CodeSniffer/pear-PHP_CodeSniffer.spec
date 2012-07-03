%define pear_name PHP_CodeSniffer

Name: pear-PHP_CodeSniffer
Version: 1.0.1
Release: alt1

Summary: PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/PHP_CodeSniffer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_CodeSniffer-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PHP_CodeSniffer is a PHP5 script that tokenises and "sniffs" PHP code to
detect violations of a defined set of coding standards. It is an essential
development tool that ensures that your code remains clean and consistent.
It can even help prevent some common semantic errors made by developers.

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
%_bindir/phpcs
%pear_testdir/PHP_CodeSniffer/
%pear_dir/PHP/
%pear_datadir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

