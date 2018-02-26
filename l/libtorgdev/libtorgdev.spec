%define oname torgdev
Name: libtorgdev
Version: 3.5
Release: alt2

Summary: support for the special commercial devices
Summary(ru_RU.KOI8-R): поддержка торговых устройств

License: GPL
Group: Communications
Url: http://www.iceb.com.ua

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/download/%oname-%version.tar.bz2
Patch: %name-%version.patch

# Automatically added by buildreq on Sun Dec 28 2008
BuildRequires: libconfig-devel

%description
This library provides basic functions for work with devices:
- electronic scales
- bar code scanners
- electronic cashe-mashine
- plastic card reader

%description -l ru_RU.KOI8-R
Данная библиотека предоставляет базовые функции для работы со
следующими устройствами:
- электронные весы
- сканеры штрих-кодов
- фискальные регистраторы
- устройства чтения пластиковых карт

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%package -n %oname
Summary: support for the special commercial devices
Group: Communications
Requires: %name = %version-%release

%description -n %oname
support for the special commercial devices

%prep
%setup -q -n %oname
%patch

%build
export LANG=ru_UA.KOI8-U
%make_build || %make

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_docdir/%name-%version
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
%make_install install install-bin install-doc \
	BINDIR=%buildroot%_libexecdir/%oname \
	LIBDIR=%buildroot%_libdir \
	LOCALE_PATH=%buildroot%_datadir/locale \
	DOCDIR=%buildroot%_docdir/%name-%version \
	HDIR=%buildroot%_includedir
install -pD -m640 example/fisc-amc %buildroot%_sysconfdir/xinetd.d/fisc-amc
install -pD -m640 example/fisc-mariamtm %buildroot%_sysconfdir/xinetd.d/fisc-mariamtm
install -pD -m640 example/cardread-gp %buildroot%_sysconfdir/xinetd.d/cardread-gp

%files -n %oname
%_libexecdir/%oname/
%config(noreplace) %_sysconfdir/xinetd.d/*

%files
%_docdir/%name-%version/
%_libdir/%name.so.*
%_datadir/locale/*/*/*

%files devel
%doc README.html TODO
%_libdir/%name.so
%_includedir/*

%changelog
* Sat Jan 10 2009 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt2
- hack library building

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- initial build to ALT Linux Sisyphus
- disable build tests (due incompatible libconfig using)

* Thu Jun  9 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- Version 3.3

* Sun Apr 17 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- Version 3.2

* Tue Apr 12 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- xinitrd files

* Tue Apr 12 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- Version 3.1

* Fri Apr  8 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- Version 3.0

* Thu Mar 31 2005 Yura Kalinichenko <yuk@iceb.vinnitsa.com>
- Initial rpm version 1.2.21
