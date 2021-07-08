Name:		rpm-build-php
Version:	8.0
Release:	alt1
Summary:	RPM helper macros to rebuild PHP packages
Group:		Development/Other
License:	GPLv2+
BuildArch:	noarch
Source0:	php.rpm.macros.standalone

%description
These helper macros provide possibility to rebuild
PHP packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/php

%files
%_sysconfdir/rpm/macros.d/php

%changelog
* Thu Jun 24 2021 Anton Farygin <rider@altlinux.ru> 8.0-alt1
- made universal, version independed macros

* Fri Oct 12 2018 Anton Farygin <rider@altlinux.ru> 7.1-alt2
- drop %%ubt

* Wed Dec 28 2016 Anton Farygin <rider@altlinux.ru> 7.1-alt1
- added rpm-build-php7-version requires

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 7.1-alt0
- first build for ALT, based on php5
