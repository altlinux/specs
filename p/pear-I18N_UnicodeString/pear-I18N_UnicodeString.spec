%define pear_name I18N_UnicodeString

Name: pear-I18N_UnicodeString
Version: 0.2.1
Release: alt1

Summary: Provides a way to work with self contained multibyte strings

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Provides a method of storing and manipulating multibyte strings in PHP
without using ext/mbstring. Also allows conversion between various methods
of storing Unicode in 8 byte strings like UTF-8 and HTML entities.

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
%dir %pear_dir/I18N/
%pear_dir/I18N/UnicodeString.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

