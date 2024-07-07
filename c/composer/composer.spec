%if_feature php83 8.3.0
%def_with php83
%define defphp php8.3
%endif

%if_feature php80 8.0.0
%def_with php80
%define defphp php8.0
%endif

%if_feature php81 8.1.0
%def_with php81
%define defphp php8.1
%endif

%if_feature php82 8.2.0
%def_with php82
%define defphp php8.2
%endif

%if_feature php7 7.4.3
%def_with php7
%define defphp php7
%endif

%define minphp 7.3

# Note: /usr/bin/compose still use php command

Name: composer
Version: 2.7.7
Release: alt1

Summary: Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere

License: MIT
Group: System/Configuration/Packaging
Url: https://getcomposer.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/composer/composer/archive/%version.tar.gz
Source: %name-%version.tar
Source1: composer.sh
Source2: composer.sysconfig
Source3: compile
Source4: README.ALT

Source10: %name-production-%version.tar

Patch1: composer-compiler.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-features >= 0.8
BuildRequires: %defphp >= %minphp

Requires: %_bindir/%defphp
Requires: %defphp >= %minphp
Requires: %defphp-openssl

%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

%prep
%setup -a 10
%patch1 -p2
install %SOURCE3 -D ./compile
cp %SOURCE4 .
%__subst "s|src/Composer/Composer.php|disable-date-changing|" src/Composer/Composer.php
# disable selfupdate
%__subst "s|.*SelfUpdateCommand.*||" src/Composer/Console/Application.php

%build
# unused date
# Note! stat -c%%y output is incompatible with date in python!
export RELDATE="$(stat -c '%%y' composer.json | sed -e 's|\.[0-9]* | |')"
#build composer.phar
%defphp -d phar.readonly=off -d date.timezone='Europe/Moscow' ./compile %version "$RELDATE"

%install
install -m 0755 -D composer.phar %buildroot/%_datadir/composer.phar
install -m 0755 -D %SOURCE1 %buildroot/%_bindir/%name
install -m 0644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%files
%doc README.ALT
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_datadir/%name.phar
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Sun Jul 07 2024 Vitaly Lipatov <lav@altlinux.ru> 2.7.7-alt1
- new version 2.7.7 (with rpmrb script)
- CVE-2024-35241, CVE-2024-35242

* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 2.7.2-alt1
- new version 2.7.2 (with rpmrb script)

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script)
- build with php8.2 by default

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 2.5.8-alt1
- new version (2.5.8) with rpmgs script
- build with php8.1 if php7 is missed (ALT bug 44695)

* Tue Apr 26 2022 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt2
- return to php7.4 for compatibility

* Tue Apr 26 2022 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version 2.2.12 (with rpmrb script)
- switch to php8.1 by default
- drop selfupdate command
- CVE-2022-24828

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Thu Mar 11 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- new version 2.0.11 (with rpmrb script)

* Wed Feb 03 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- new version 2.0.9 (with rpmrb script)

* Wed Oct 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.10.15-alt2
- switch to build from tarball

* Tue Oct 13 2020 Vitaly Lipatov <lav@altlinux.ru> 1.10.15-alt1
- new version

* Wed Apr 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version
- set default memory limit to 512MB

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- new version 1.9.2 (with rpmrb script)

* Sat Nov 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1

* Fri Jun 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)
- improve autoupdate with rpmrb NEWVERSION

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.7.2-alt1
- new version
- configurable memory_limit PHP setting (Closes: 33520)
- remove PHP7 requirements - composer can be used with PHP5 too

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.5-alt1
- build new version
- switch to php7

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
