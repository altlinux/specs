%define pear_name HTML_Javascript

Name: pear-HTML_Javascript
Version: 1.1.1
Release: alt3

Summary: Provides an interface for creating simple JS scripts

License: PHP 3.0
Group: Development/Other
Url: http://pear.php.net/package/HTML_Javascript

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Javascript-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides two classes:
HTML_Javascript for performing basic JS operations.
HTML_Javascript_Convert for converting variables
Allow output data to a file, to the standart output(print), or return

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
%pear_dir/HTML
%pear_testdir/HTML_Javascript/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

