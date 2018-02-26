Name: wcalc
Version: 2.4
Release: alt2

Summary: A flexible command-line calculator
Summary(ru_RU.KOI8-R): Гибкий калькулятор командной строки

License: GPL
Group: Office
Url: http://w-calc.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/w-calc/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Jul 17 2005
BuildRequires: flex libgmp-devel libmpfr-devel libreadline-devel

%description
Wcalc is a command-line calculator designed to accept all valid mathematical expressions.
It supports all standart mathematical operations, parenthesis, brackets, braces,
trigonometric functions, hyperbolic functions, logs, and most boolean operators.

%description -l KOI8-R
Wcalc - это консольный калькулятор, работающий со всеми допустимыми математическими
выражениями. Он поддерживает все стандартные математические операции, тригонометрические
и гиперболические функции, логарифмы и большинство логических операторов.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc NEWS COPYRIGHT AUTHORS README
%_bindir/%name
%_man1dir/*

%changelog
* Tue Mar 24 2009 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt2
- fix russian description (bug #19305)

* Sat Dec 27 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 (with rpmrb script)

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)

* Sat Jul 15 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt0.1
- new version 2.2.2 (with rpmrb script)

* Tue Feb 14 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1
- new version
- remove INSTALL, add NEWS, README

* Tue Aug 30 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- stable release
 + Arbitrary precision!
 + Command-line unit conversion!
 + Lots of little tweaks!
 + Bugfixes!

* Sun Jul 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt0.1cvs20050717
- new version from CVS (20050717)

* Thu Apr 01 2004 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- first build for Sisyphus

