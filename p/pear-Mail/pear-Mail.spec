%define pear_name Mail
Name: pear-%pear_name
Version: 1.2.0
Release: alt1

Summary: Class that provides multiple interfaces for sending emails

License: BSD Style
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Denis Klimov <zver@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch
Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PEAR's Mail package defines an interface for implementing mailers
under the PEAR hierarchy. It also provides supporting functions useful
to multiple mailer backends. Currently supported backends include:
PHP's native mail() function, sendmail, and SMTP. This package also
provides a RFC822 email address list validation utility class.

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
%pear_dir/Mail
%pear_dir/Mail.php
%pear_dir/tests/
%pear_dir/.pkgxml/Mail.xml

%changelog
* Mon Oct 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- build new version 1.2.0 (ALT bug #16091)
- fix Url, License

* Fri Jul 04 2008 Denis Klimov <zver@altlinux.ru> 1.1.14-alt2
- build with pear macros

* Fri Sep 28 2007 Denis Klimov <zver@altlinux.ru> 1.1.14-alt1
- Initial build for ALT Linux

