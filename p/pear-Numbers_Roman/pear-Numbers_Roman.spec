%define pear_name Numbers_Roman

Name: pear-Numbers_Roman
Version: 1.0.2
Release: alt3

Summary: Provides methods for converting to and from Roman Numerals

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Numbers_Roman

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Numbers_Roman-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Numbers_Roman provides static methods for converting to and from Roman
numerals. It supports Roman numerals in both uppercase and lowercase
styles and conversion for and to numbers up to 5 999 999

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
%pear_testdir/Numbers_Roman/tests
%pear_dir/Numbers
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

