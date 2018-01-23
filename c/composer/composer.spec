#!!! Create new vendor cache for new composer version by get_vendor_cache.sh !!!

Name: composer
Version: 1.6.2
Release: alt1

Summary: Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/composer/composer

# Source-git: https://github.com/composer/composer
Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

Requires: php5-openssl php5 php5-curl

BuildRequires: git-core php5-openssl php5

BuildArch: noarch

%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

%prep
%setup

%build

#Move vendor cache with build requires
mv .gear/vendor/ vendor/

#Compile need git log -n1 --pretty=ct HEAD #TODO remove it
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add bin/compile
git commit -am "Fix for compile"

#build composer.phar
php -d phar.readonly=off -d date.timezone='Europe/Moscow' bin/compile

%install
mkdir -p %buildroot/%_datadir/
cp composer.phar %buildroot/%_datadir/

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
php -d suhosin.executor.include.whitelist=phar -d memory_limit=256M %_datadir/composer.phar "\$@"
EOF

%pre

%files
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_datadir/%name.phar

%changelog
* Tue Jan 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- build new version

* Tue Oct 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- build new version

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- build new version

* Mon Mar 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- build new version

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- build new version 1.1.3
- set memory_limit 256M

* Wed Nov 25 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt4
- Added php5 req

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt3
- Remove install section, added vendor cache

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt2
- Change libdir to datadir, add commets

* Thu May 28 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
