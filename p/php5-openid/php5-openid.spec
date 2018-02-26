%define oname php-openid
%define php5_extension openid
Name: php5-%php5_extension
Version: 2.2.2
Release: alt1

Summary: PHP OpenID library

License: Apache
Group: System/Servers
Url: http://www.openidenabled.com/

Source: http://openidenabled.com/files/php-openid/packages/%oname-%version.tar.bz2

# Automatically added by buildreq on Wed Jan 23 2008
BuildRequires: php5 php5-curl php5-dom php5-gd2 php5-gmp php5-simplexml

BuildRequires(pre): rpm-build-php5

BuildArch: noarch

BuildArch: noarch

%description
This is the PHP OpenID library by JanRain, Inc.

Note:
Allow dl function using in php.ini (mediawiki.ini)

%prep
%setup -q -n %oname-%version

%build
php -dsafe_mode=0 examples/detect.php

%install
mkdir -p %buildroot%php5_moddir
cp -ar Auth %buildroot%php5_moddir

%files
%doc examples
%doc admin
%doc COPYING NEWS README
%php5_moddir/Auth/

%changelog
* Tue May 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Apr 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Feb 01 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build as noarch, fix module placement

* Wed May 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Wed Apr 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- rebuild with php 5.2.5

* Wed Jan 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus
