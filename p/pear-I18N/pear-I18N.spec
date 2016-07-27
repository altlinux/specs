%define pear_name I18N

Name: pear-I18N
Version: 1.0.0
Release: alt1

Summary: Internationalization package

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
This package supports you to localize your applications.
Multiple ways of supporting translation are implemented
and methods to determine the current users (browser-)language.
Localizing Numbers, DateTime and currency is also implemented.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/I18N/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- initial build for ALT Linux Sisyphus

