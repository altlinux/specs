%define php7_name php7

Name:		rpm-build-php7
Version:	7.1
Release:	alt2
Summary:	RPM helper macros to rebuild PHP packages
Requires:	rpm-build-php7-version
Group:		Development/Other
License:	GPL
BuildArch:	noarch
Source0:	php.rpm.macros.standalone

%description
These helper macros provide possibility to rebuild
PHP7 packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/%php7_name

%files
%_sysconfdir/rpm/macros.d/%php7_name

%changelog
* Fri Oct 12 2018 Anton Farygin <rider@altlinux.ru> 7.1-alt2
- drop %%ubt

* Wed Dec 28 2016 Anton Farygin <rider@altlinux.ru> 7.1-alt1
- added rpm-build-php7-version requires

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 7.1-alt0
- first build for ALT, based on php5
