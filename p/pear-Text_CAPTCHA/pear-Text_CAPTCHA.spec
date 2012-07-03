%define pear_name Text_CAPTCHA

Name: pear-Text_CAPTCHA
Version: 0.3.1
Release: alt1

Summary: Generation of CAPTCHAs

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Implementation of CAPTCHAs (completely automated public Turing test to tell
computers and humans apart)

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
%pear_dir/Text/CAPTCHA/
%pear_dir/Text/CAPTCHA.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

