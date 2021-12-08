Name: xdrawchem
Version: 1.10.2
Release: alt2

Summary: XDrawChem is a two-dimensional molecule drawing program
Summary(ru_RU.UTF-8): XDrawChem - программа двумерного рисования молекул

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL-2.0-or-later
Group: Sciences/Chemistry
Url: http://www.woodsidelabs.com/chemistry/xdrawchem.php

# Source-url: https://github.com/bryanherger/xdrawchem/archive/%version-1.tar.gz
Source: %name-%version.tar

Source1: xdrawchem.desktop
Source2: xdrawchem.png
#Source3: %name-%version.ru.po
Patch0: %name-gcc43.patch
Patch1: xdrawchem-ob22.patch
Patch2: new-openbabel-string-type-fix.patch
Patch3: xdrawchem-1.9.9-alt-glibc-2.16.patch

Patch10: xdrawchem-1.10.2-1-HEAD.patch

BuildRequires: gcc-c++ openbabel pkgconfig(openbabel-3) qt5-base-devel

%description
XDrawChem is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft). It can read
and write MDL Molfiles and CML files to allow sharing between
XDrawChem and other chemistry applications.

%description -l ru_RU.UTF-8
XDrawChem - это программа двумерного рисования молекул для операционных
систем класса Unix. По функциональности она аналогична другим программам
рисования молекул, таким как ChemDraw (TM, CambridgeSoft). Она может
считывать и записывать файлы MDL Molfiles и CML, что позволяет
использовать XDrawChem вместе с другими приложениями для химии.

%prep
%setup
%patch10 -p1
cd xdrawchem-qt5

%build
cd xdrawchem-qt5
qmake-qt5 PREFIX="%_prefix"
%make_build

%install
cd xdrawchem-qt5
%makeinstall_std INSTALL_ROOT=%buildroot
install -pD -m 644 %SOURCE1 %buildroot/%_desktopdir/xdrawchem.desktop
install -pD -m 644 %SOURCE2 %buildroot/%_niconsdir/xdrawchem.png

%files
%doc README.md
%_bindir/%name
%_datadir/xdrawchem/
%_desktopdir/xdrawchem.desktop
%_niconsdir/xdrawchem.png

%changelog
* Wed Dec 08 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt2
- updated from upstream git to 1.10.2-1-9-g892acac (required openbabel-3)
- fixed License tag

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version (1.10.2) with rpmgs script
- build with Qt5

* Tue Oct 18 2016 Michael Shigorin <mike@altlinux.org> 1.9.9-alt3.qa3.2
- NMU:
  + rebuilt against current openbabel
  + changed description encoding to UTF-8

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 1.9.9-alt3.qa3.1
- NMU: rebuild with new openbabel

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.9-alt3.qa3
- Fixed build with glibc 2.16

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

