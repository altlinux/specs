%define oname jevix
%define php5_extension jevix

Name: php5-%php5_extension
Version: 1.1
Release: alt1

Summary: HTML/XHTML filter and typograph for PHP

License: MIT
Group: System/Servers
Url: http://code.google.com/p/jevix/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# It is the new feature etersoft-build-utils since 1.7.6: supports commented real source
# Source-svn: http://jevix.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: rpm-build-php5

BuildArch: noarch

%description
HTML/XHTML filter and typograph for PHP

%prep
%setup

%build
#php -dsafe_mode=0 examples/detect.php

%install
mkdir -p %buildroot%php5_moddir/%oname
cp -a *.php %buildroot%php5_moddir/%oname

%files
%php5_moddir/%oname/

%changelog
* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus
