%define pear_name PHP_TokenStream

Name: pear-PHP_TokenStream
Version: 1.0.1
Release: alt1

Summary: Wrapper around PHP's tokenizer extension

License: BSD
Group: Development/Other
Url: http://pear.phpunit.de/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-ConsoleTools >= 1.6

%description
Wrapper around PHP's tokenizer extension.

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
%_bindir/phptok
%pear_dir/PHP/Token/
%pear_dir/PHP/Token.php
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

