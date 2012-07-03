%define pear_name I18Nv2
Name: pear-I18Nv2
Version: 0.11.4
Release: alt3

Summary: Internationalization
License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArch: noarch
Requires: pear-core

# Automatically added by buildreq on Tue Jan 08 2008
BuildRequires: php5-dom php5-gd2 rpm-build-pear

BuildRequires: pear-core rpm-build-pear

%description
This package provides basic support to localize your application,
like locale based formatting of dates, numbers and currencies.

Beside that it attempts to provide an OS independent way to setlocale()
and aims to provide language, country and currency names translated into
many languages.

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
%pear_dir/%pear_name.php
%pear_dir/%pear_name/
%pear_xmldir/%pear_name.xml
%pear_testdir/%pear_name
%pear_docdir/%pear_name/

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.4-alt2
- update according to rpm-build-pear 0.3

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.11.4-alt1
- Initial build for ALT Linux

