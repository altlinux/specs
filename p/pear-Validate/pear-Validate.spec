%define pear_name Validate

Name: pear-Validate
Version: 0.8.1
Release: alt1

Summary: Validation class 

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/Validate

Packager: Maxim Ivanov <redbaron at altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tgz

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Date, pear-core >= 1.4.0b1

%description
Package to validate various datas. It includes :
 - numbers (min/max, decimal or not)
 - email (syntax, domain check, rfc822)
 - string (predifined type alpha upper and/or lowercase, numeric,...)
 - date (min, max, rfc822 compliant)
 - uri (RFC2396)
 - possibility valid multiple data with a single method call (::multiple)

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
%doc LICENSE 
%pear_dir/%pear_name.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Jun 08 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.8.1-alt1
- Initial build for Sisyphus
