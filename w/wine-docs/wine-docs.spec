Name: wine-docs
Version: 1.0
Release: alt1

Summary: WINE documentation
Summary(ru_RU.KOI8-R): Документация к WINE

License: LGPL
Group: Documentation
Url: http://www.winehq.org/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ibiblio.org/pub/linux/system/emulators/wine/%name-%version.tar.bz2
Provides: wine-doc
Obsoletes: wine-doc

# manually removed: docbook-utils-print
# Automatically added by buildreq on Sun Mar 05 2006
BuildRequires: OpenSP docbook-dtds docbook-style-dsssl openjade sgml-common
BuildRequires: docbook-utils

%description
WINE documentation

%prep
%setup -q
# remove fr language support
%__subst "s|fr||" Makefile.in

%build
%configure
%make html

%files
%doc en/*.html

%changelog
* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.52-alt1
- new version (0.9.52)

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.46-alt1
- new version 0.9.46 (with rpmrb script)

* Fri Apr 07 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt0.1
- new version 0.9.11 (with rpmrb script)

* Sun Mar 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt0.1
- new version 0.9.9 (with rpmrb script)
- disable pdf/ps/txt building
- update buildreqs

* Sat Feb 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 20050725-alt1
- new version (build from original package), only html packaged

* Fri Jun 17 2005 Vitaly Lipatov <lav@altlinux.ru> 20050617-alt1
- first standalone WINE docs package build for ALT Linux Sisyphus

