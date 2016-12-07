%define php7_name php7

Name:		rpm-build-php7
Version:	7.1
Release:	alt0%ubt
Summary:	RPM helper macros to rebuild PHP5 packages
Group:		Development/Other
License:	GPL
BuildArch:	noarch
Source0:	php.rpm.macros.standalone
BuildRequires(pre):rpm-build-ubt
Requires: rpm-build-ubt

%description
These helper macros provide possibility to rebuild
PHP7 packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/%php7_name

%files
%_sysconfdir/rpm/macros.d/%php7_name

%changelog
* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 7.1-alt0%ubt
- first build for ALT, based on php5
