%define pear_name PHPUnit_MockObject

Name: pear-PHPUnit_MockObject
Version: 1.0.3
Release: alt1

Summary: Mock Object library for PHPUnit

License: BSD
Group: Development/Other
Url: http://pear.phpunit.de/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Mock Object library for PHPUnit.

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
* Tue Dec 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus

