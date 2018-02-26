%define pear_name PHPUnit_Selenium

Name: pear-PHPUnit_Selenium
Version: 1.0.1
Release: alt1

Summary: Selenium RC integration for PHPUnit

License: BSD
Group: Development/Other
Url: http://pear.phpunit.de/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Selenium RC integration for PHPUnit.

%prep
%setup -c
# Hack against Unknown channel "pear.phpunit.de"
%__subst "s|pear.phpunit.de|pear.php.net|g" package.xml

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
%pear_dir/PHPUnit/
%pear_xmldir/%pear_name.xml

%changelog
* Tue Dec 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

