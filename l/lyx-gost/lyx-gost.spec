Name: lyx-gost
Version: 1.5.0
Release: alt1

Summary: The GOST class files for LyX
Summary(ru_RU.KOI8-R): Класс документа по ГОСТ для LyX

License: GPL
Group: Office
URL: http://www.etersoft.ru/content/category/9/80/63/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

BuildArchitectures: noarch
BuildPreReq: iconv
PreReq: lyx >= 1.5.0

Conflicts: lyx-gost-cp1251
Obsoletes: lyx-gost-cp1251

Conflicts: lyx-gost-koi8-r
Obsoletes: lyx-gost-koi8-r

%description
The %name package contains the LyX/LaTeX class for preparing documents
according to Russian GOST's demands.

%description -l ru_RU.KOI8-R
Пакет %name содержит класс для LyX/LaTeX, предназначенный для
подготовки технической текстовой документации в соответствии
с ГОСТ 2.105-95 (с рамками и основными надписями).

%prep
%setup -q

%install

mkdir -p %buildroot%_datadir/lyx/
cp -a layouts templates clipart %buildroot%_datadir/lyx/

%post
echo "Configuring LyX for your system..."
cd %_datadir/lyx
./configure.py --without-latex-config

%postun
echo "Configuring LyX for your system..."
cd %_datadir/lyx
./configure.py --without-latex-config

%files
%doc doc
%_datadir/lyx/layouts/*.inc
%_datadir/lyx/layouts/gost.layout
%_datadir/lyx/clipart/*
%_datadir/lyx/templates/*.lyx

%changelog
* Wed Dec 05 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- adopted layouts for new LyX version, recode to UTF-8
- cleanup spec
- tested with LyX 1.5.2

* Thu Mar 03 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt2
- add requires for lyx-common (bug #6197)

* Mon Feb 14 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- tested with LyX 1.3.5

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- fix bug with formulae
- fix URL
- tested with LyX 1.3.4

* Tue May 13 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- fixed encoding for docs in cp1251
- fixed name of docs dir

* Mon Mar 31 2003 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- updated for LyX 1.3.1
- new version of lyx-gost (see ChangeLog)

* Wed Dec 04 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt5
- corrected for tetex-2.0
- cleanup spec
- tested with LyX 1.2.1

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt4
- rebuild

* Sat Jul 06 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt3
- normalize code of textclass and gost frames
- packages for both encoding (koi8-r & cp1251)

* Fri Jun 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- back to single source package for two destination
- update for LyX 1.2.0
- doc2lyx convertor removed
- add noarch option

* Sun Apr 14 2002 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version
- split in two package

* Tue Dec 22 2001 23:01:01 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- russian description charset fixed
- add new template delop.lyx
- new version of class GOST
- russian documentation for LyX moved to lyx-rusdoc

* Tue Dec 11 2001 11:19:09 Vitaly Lipatov <vitlav@mail.ru> 1.0-alt1
- first version
