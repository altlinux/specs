Name: lyx-rusdoc
Version: 1.5.0
Release: alt1

Summary: The documentation for LyX and GOST text class
Summary(ru_RU.KOI8-R): Русская документация по LyX и классу текста GOST
License: GPL
Group: Office
Url: http://www.etersoft.ru

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

BuildArchitectures: noarch
Requires: lyx-gost

%description
The %name package contains additional describes in russian
for LyX, and the documentation for LyX/LaTeX class GOST.

%description -l ru_RU.KOI8-R
Пакет %name содержит дополнительные описания LyX'а
на русском языке, а также документацию для класса текста GOST LyX/LaTeX,
предназначенного для подготовки технической текстовой документации
в соответствии с ГОСТ 2.105-95.

%prep
%setup

%install
for i in doc/*.sh
do
	install -D -m755 $i %buildroot%_bindir/`basename $i .sh`
done

%files
%doc GOST-LyX/* lyx-ug/* doc/*.lyx
%_bindir/*

%changelog
* Wed Dec 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- cleanup spec, convert docs to new lyx format

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- update LyX-GOST for last LyX features
- rename scripts and set execute permission on it

* Mon Jan 05 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- update all files for LyX 1.3.3
- spec cleanup
- add scripts for PS-booklets printing

* Fri Jun 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- update all files for LyX 1.2.0
- add noarch option

* Sun Apr 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- update GOST-LyX
- add lyx-ug (introduction in LyX for newbie)

* Tue Dec 24 2001 23:01:01 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first version
