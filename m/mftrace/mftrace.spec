Name: mftrace
Version: 1.2.5
Release: alt2.1.1

Summary: Generates scalable fonts for TeX
Summary(ru_RU.KOI8-R): Программа конвертации растровых шрифтов в векторные

Group: Publishing
License: GPL
Packager: Grigory Batalov <bga@altlinux.ru>
Url: http://www.xs4all.nl/~hanwen/mftrace/


Source: http://www.xs4all.nl/~hanwen/mftrace/%name-%version.tar.gz

Requires: python potrace t1utils fontforge
Requires: %_bindir/mf, %_bindir/gf2pbm
Obsoletes: pktrace
Provides: pktrace = %version-%release

# Automatically added by buildreq on Tue Mar 29 2005 (-bi)
BuildRequires: potrace python-base python-modules-compiler python-modules-encodings

%description
Mftrace is a small Python program that lets you trace a @TeX{}
bitmap font into a PFA or PFB font (A PostScript Type1 Scalable Font).

Type1 fonts offer many advantages over bitmaps, as they allow PostScript
files to render correctly on printers with many resolutions. Moreover,
Ghostscript can generate much better PDF, if given scalable fonts.

%description -l ru_RU.KOI8-R
Mftrace - программа конвертации растровых шрифтов TeX в векторные Type 1 шрифты.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall datadir=%buildroot%_datadir/%name

%files
%_bindir/*
%_man1dir/*
%_datadir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.5-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt2.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Grigory Batalov <bga@altlinux.ru> 1.2.5-alt2
- Replace tetex-core requirement with mf and gf2pbm binaries.

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.2.5-alt1.1
- Rebuilt with python-2.5.

* Sat Dec 02 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.2.5-alt1
- reanimated for lilypond building
- new version

* Mon Feb 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt0.1
- new version (1.1.18)
- fix Url, fix Source URL
- change Packager

* Tue Mar 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Mon Jun 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.33-alt1
- 1.0.33
- requires potrace, not autotrace, as a default tracing program.
- requires fontforge (pfaedit new name).

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Sat Dec 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Tue Nov 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Fri Sep 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Apr 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue Mar 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Mar 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.11-alt1
- Adopted for Sisyphus.

* Tue Feb 19 2002 Han-Wen Nienhuys <hanwen@cs.uu.nl>
- Initial build.
