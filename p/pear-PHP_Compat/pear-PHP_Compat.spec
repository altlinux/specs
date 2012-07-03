%define pear_name PHP_Compat

Name: pear-PHP_Compat
Version: 1.5.0
Release: alt3

Summary: Provides missing functionality for older versions of PHP

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/PHP_Compat

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_Compat-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PHP_Compat provides missing functionality for older versions of PHP.

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
%pear_dir/PHP
%pear_testdir/PHP_Compat/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux Sisyphus

