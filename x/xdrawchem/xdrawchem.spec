Name: xdrawchem
Version: 1.9.9
Release: alt3.qa2

Summary: XDrawChem is a two-dimensional molecule drawing program
Summary(ru_RU.KOI8-R): XDrawChem - программа двумерного рисования молекул

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Sciences/Chemistry
Url: http://xdrawchem.sourceforge.net/

Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Source1: xdrawchem.desktop
Source2: xdrawchem.png
#Source3: %name-%version.ru.po
Patch0: %name-gcc43.patch
Patch1: xdrawchem-ob22.patch
Patch2: new-openbabel-string-type-fix.patch

# Automatically added by buildreq on Fri Dec 16 2005
BuildRequires: fontconfig freetype2 gcc-c++ libopenbabel-devel libqt3-devel libqt3-qsa-devel libstdc++-devel pkg-config 

BuildPreReq: libopenbabel-devel >= 2.0.0

%description
XDrawChem is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft). It can read
and write MDL Molfiles and CML files to allow sharing between
XDrawChem and other chemistry applications.

%description -l ru_RU.KOI8-R
XDrawChem - это программа двумерного рисования молекул для операционных
систем класса Unix. По функциональности она аналогична другим программам
рисования молекул, таким как ChemDraw (TM, CambridgeSoft). Она может
считывать и записывать файлы MDL Molfiles и CML, что позволяет
использовать XDrawChem вместе с другими приложениями для химии.

%prep
%setup
%patch0
%patch1 -p1
%patch2 -p1

%build
%configure --with-qtdir=%_prefix --with-qtlibdir=%_qt3dir/lib
%make_build
#%_qt3dir/bin/msg2qm translation/%name-ru.po translation/%{name}_ru.qm

%install
%makeinstall_std
install -pD -m 644 %SOURCE1 %buildroot/%_desktopdir/xdrawchem.desktop
install -pD -m 644 %SOURCE2 %buildroot/%_niconsdir/xdrawchem.png

%files
%doc COPYRIGHT.txt README.txt TODO.txt
%_bindir/%name
%_datadir/xdrawchem/
%_desktopdir/xdrawchem.desktop
%_niconsdir/xdrawchem.png

%changelog
* Fri Dec 16 2011 Michael Shigorin <mike@altlinux.org> 1.9.9-alt3.qa2
- NMU: rebuilt with new openbabel (using patches from opensuse)
- minor spec cleanup

* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.9.9-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xdrawchem
  * update_menus for xdrawchem
  * postclean-05-filetriggers for spec file

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt3
- fix build with gcc 4.3

* Sun Oct 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt2
- rebuild with new openbabel

* Thu May 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt1
- replace menu file with desktop file
- cleanup build section
- use make install for install files
- fix path to doc files fix (bug #15572)

* Fri Dec 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt0.1
- new version (build with openbabel 2)

* Sat Feb 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version

* Sat Jul 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version
- fix menu entry (bug #4283)
- add russian translation

* Fri May 14 2004 Ott Alex <ott@altlinux.ru> 1.8.2-alt1
- New version

* Wed May 12 2004 Ott Alex <ott@altlinux.ru> 1.8.1-alt1
- New version

* Tue Apr 13 2004 Ott Alex <ott@altlinux.ru> 1.8-alt1
- New version

* Mon Feb 16 2004 Ott Alex <ott@altlinux.ru> 1.7.7-alt1
- New version
- added menu entry

* Wed Nov 26 2003 Ott Alex <ott@altlinux.ru> 1.7.6-alt1
- New version

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 1.7.5-alt1
- New version

* Fri Sep 05 2003 Ott Alex <ott@altlinux.ru> 1.7.4-alt2
- fixing spec

* Sun Aug 03 2003 Ott Alex <ott@altlinux.ru> 1.7.4-alt1
- New release

* Thu Jul 17 2003 Ott Alex <ott@altlinux.ru> 1.7.3-alt1
- New release

* Mon Jun 02 2003 Ott Alex <ott@altlinux.ru> 1.7.1-alt1
- Initial build

