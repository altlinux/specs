%define pear_name Text_Template

Name: pear-Text_Template
Version: 1.1.0
Release: alt1

Summary: Simple template engine

License: BSD
Group: Development/Other
Url: http://pear.phpunit.de/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Simple template engine.

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
%pear_dir/Text/Template/
%pear_dir/Text/Template.php
%pear_xmldir/%pear_name.xml

%changelog
* Tue Dec 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

