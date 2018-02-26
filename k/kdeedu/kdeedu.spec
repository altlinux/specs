%undefine __libtoolize
%define unstable 0
%define _optlevel s
%def_enable boost
%define glibc_core_ver %{get_version glibc-core}
%define _keep_libtool_files 1
%_K_if_ver_lt %glibc_core_ver 2.5
%define _keep_libtool_files 0
%endif

%define qtdir %_qt3dir
%define cvsdate 20020401
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir
%add_findprov_lib_path %_libdir/kde3
%add_verify_elf_skiplist %_libdir/libkvoctraincore.so*
%set_verify_elf_method no

Name: kdeedu
Version: 3.5.13
Release: alt2

Group: Graphical desktop/KDE
Summary: K Desktop Environment - kdeedu
URL: http://www.kde.org/
License: GPL

Source: kdeedu-%version.tar
#Source: kdeedu-3.0.98.tar
Patch10: 3.5.0-flags.patch
Patch11: kdeedu-3.5.0-videodev-placement.patch
Patch13: kvoctrain-3.5.2-alt-fix-linking.patch
Patch14: ktouch-3.5.9-alt-ru-keys-install.patch
Patch15: kdeedu-3.5.8-alt-kturtle-default-language.patch
Patch16: kdeedu-3.5.9-alt-find-boost-python.patch
Patch17: kdeedu-3.5.9-alt-kturtle-speed.patch
Patch18: kdeedu-3.5.10-alt-desktop-directories.patch
Patch19: kdeedu-3.5.10-alt-rename-indiserver.patch
Patch21: tde-3.5.13-build-defdir-autotool.patch
Patch22: cvs-auto_version_check.patch

#Requires: %name-flashkard = %version-%release
Requires: %name-kalzium = %version-%release
Requires: %name-kbruch = %version-%release
Requires: %name-keduca = %version-%release
Requires: %name-khangman = %version-%release
Requires: %name-kig = %version-%release
Requires: %name-kiten = %version-%release
Requires: %name-klettres = %version-%release
#Requires: %name-kmessedwords = %version-%release
Requires: %name-kmplot = %version-%release
Requires: %name-kpercentage = %version-%release
Requires: %name-kstars = %version-%release
Requires: %name-ktouch = %version-%release
Requires: %name-kverbos = %version-%release
Requires: %name-kvoctrain = %version-%release
Requires: %name-kturtle = %version-%release
Requires: %name-klatin = %version-%release
Requires: %name-kwordquiz = %version-%release
Requires: %name-blinken = %version-%release
Requires: %name-kanagram = %version-%release
Requires: %name-kgeography = %version-%release

# Automatically added by buildreq on Mon Apr 08 2002
#BuildRequires: XFree86-devel XFree86-libs freetype2 gcc-c++ kde-common kdebase kdelibs-devel libarts-devel libjpeg-devel liblcms libmng libpng-devel libqt3-devel libstdc++-devel zlib-devel

BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++
BuildRequires: kde-common libart_lgpl-devel
BuildRequires: libjpeg-devel liblcms libmng libpng-devel
BuildRequires: python-devel boost-python-devel
BuildRequires: libqt3-devel libstdc++-devel zlib-devel libpcre-devel libusb-devel
BuildRequires: libacl-devel libattr-devel
#BuildRequires: ocaml rpm-build-ocaml
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
kdeedu

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdeedu <= 3.0.1
#
%description common
Common empty package for %name

%package blinken
Summary: Game to remember sequences of increasing length
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description blinken
Blinken is based on an electronic game released in 1978, which challenges
players to remember sequences of increasing length.

%package kanagram
Summary: A puzzle based on anagrams of words
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kanagram
Kanagram is a game based on anagrams of words: the puzzle is solved when
the letters of the scrambled word are put back in the correct order.

%package kgeography
Summary: A geography learning tool
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kgeography
Kgeography is a geography learning tool for KDE. Right now it has six usage modes: 
 * Browse the maps clicking in a map division to see its name
 * The game tells you a map division name and you have to click on it
 * The game tells you a capital and you have to guess the division it belongs to
 * The game tells you a division and you have to guess its capital
 * The game shows you a map division flag and you have to guess its name
 * The game tells you a map division name and you have to guess its flag

%package klatin
Summary: Program to help revise Latin
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description klatin
KLatin is a program to help revise Latin

%package kwordquiz
Summary: Tool to master new vocabularies.
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kwordquiz
KWordquiz is a tool that gives you a powerful way to master new vocabularies.
It may be a language or any other kind of terminology.

%package kturtle
Summary: LOGO programming language for KDE
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kturtle
KTurtle is an educational programming environment
using the LOGO programming language.

%package kbruch
Summary: Fraction calculation teaching tool
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kbruch
KBruch  is  a program that generate tasks with fractions.
The user has to solve the given task by entering the right value
for numerator and denominator. The program checks the user's solution
and gives feedback.

%package khangman
Summary: Classical hangman game
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description khangman
KHangMan  is  a game based on the well known hangman game.
It is aimed for children aged 6 and above. It has four levels
of difficulty.

%package kig
Summary: Interactive geometry program
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Obsoletes: kdeedu-kgeo
#
%description kig
Kig is an application for interactive geometry. It is intended to
serve two purposes:
  - to allow students to interactively explore mathematical figures and
    concepts using the computer;
  - to serve as a WYSIWYG tool for drawing mathematical figures and
    including them in other documents.

%package libs
Summary: Base library for kdeedu programs
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description libs
Base library for kdeedu programs

%package devel
Summary: Development files for %name-libs
Group: Graphical desktop/KDE
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: %name-libs %name-kstars
#
%description devel
Development files for %name-libs

%package flashkard
Summary: Questions on cards
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description flashkard
FlashKard is based on a rather old learning method
used to teach children facts. The teacher will present
a number of cards with questions on it, on which the
pupil will write down the answers on the back of the cards,
which will be checked later on by the teacher.
The cards with the correct answers will be removed
from the pile and the incorrectly answered question
will be repeated over and over again, until the answer
is drilled into the memory.

%package kalzium
Summary: Information about the PSE
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kalzium
Information about the PSE (Periodic System of Elements).

%package kiten
Summary: Japanese Reference/Study Tool
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kiten
Japanese Reference/Study Tool

%package kmplot
Summary: Function Plotter
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmplot
Kmplot supports functions with parameters
and functions in polar coordinates.
Several grid modes are possible.
Plots may be printed with high precision
in correct scale.

%package kpercentage
Summary: Calculating percentages
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kpercentage
Small math application that will help pupils
to improve their skills in calculating percentages.

%package kverbos
Summary: Learn the forms of Spanish verbs
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kverbos
Learn the forms of Spanish verbs

%package keduca
Summary: Tests and Exams
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description keduca
Tests and Exams

%package klettres
Summary: French alphabet tutor
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description klettres
French alphabet tutor

%package kmessedwords
Summary: Letter Order Game
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmessedwords
Letter Order Game

%package kstars
Summary: Desktop Planetarium
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kstars
Desktop Planetarium

%package ktouch
Summary: Touch Typing Tutor
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktouch
Touch Typing Tutor

%package kvoctrain
Summary: Vocabulary Trainer
Group: Education
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kvoctrain
Vocabulary Trainer

%prep
%setup -q -n %name-%version
#%setup -q -n %name-3.0.98
#%patch10 -p1
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
#%patch18 -p1
# %patch19 -p1
%patch21
%patch22

%if %_keep_libtool_files
for f in `find $PWD -type f -name Makefile.am`
do
    grep -q LDFLAGS $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
%else
#subst "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" admin/acinclude.m4.in
subst "s|-Wl,--no-undefined|-Wl,--allow-shlib-undefined|g" admin/acinclude.m4.in
subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
subst "s/\.la/.so/g" admin/acinclude.m4.in
%endif

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
%add_optflags -I/usr/include/linux-libc-headers/include
export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final \
    --enable-shared \
    --disable-static \
    --disable-embedded \
    --disable-qtopia \
    --disable-rpath \
    --with-gnu-ld \
    --enable-new-ldflags \
    --enable-gcc-hidden-visibility \
    --enable-pch \
    --enable-dependency-tracking \
    --with-pic \
    --program-transform-name="" \
    --with-xinerama \
%if_disabled boost
    --disable-kig-python-scripting \
%endif
%ifarch x86_64
    --enable-libsuffix=64 \
%endif
    --enable-v4l2 \
    --without-arts

%make_build

%install
%if %unstable
%set_strip_method none
%endif
export PATH=%_bindir:$PATH

%make_build DESTDIR=%buildroot install
%make_build DESTDIR=%buildroot install -C blinken

chmod 0644 %buildroot/%_libdir/*.la ||:
chmod 0644 %buildroot/%_libkde/*.la ||:

#
chmod a-s %buildroot/%_bindir/*

#mv %buildroot/%_datadir/applnk/klettres/level*.txt %buildroot/%_datadir/apps/klettres


%files
%files common

%files blinken
%_bindir/blinken
%_datadir/apps/blinken/
%_docdir/HTML/en/blinken/
%_iconsdir/*/*/apps/blinken.*
%_Kmenudir/blinken.desktop

%files kanagram
%_bindir/kanagram
%_datadir/apps/kanagram/
%_docdir/HTML/en/kanagram/
%_iconsdir/*/*/apps/kanagram.*
%_Kmenudir/kanagram.desktop

%files kgeography
%_bindir/kgeography
%_datadir/apps/kgeography/
%_docdir/HTML/en/kgeography/
%_iconsdir/*/*/apps/kgeography.*
%_Kmenudir/kgeography.desktop

%files klatin
%_bindir/klatin
%_datadir/apps/klatin/
%_iconsdir/*/*/apps/klatin.*
%_docdir/HTML/en/klatin/
%_Kmenudir/klatin.desktop

%files kwordquiz
%_bindir/kwordquiz
%_datadir/apps/kwordquiz
%_datadir/mimelnk/application/x-kwordquiz.desktop
%_iconsdir/*/*/*/kwordquiz*
%_docdir/HTML/en/kwordquiz/
%_Kmenudir/kwordquiz.desktop

%files kturtle
%_bindir/kturtle
%_datadir/apps/kturtle/
%_datadir/apps/katepart/syntax/logohighlightstyle.*
%_iconsdir/*/*/apps/kturtle.*
%_docdir/HTML/en/kturtle
%_Kmenudir/kturtle.desktop

%files kbruch
%_bindir/kbruch
%_datadir/apps/kbruch/kbruchui.rc
%_iconsdir/*/*/apps/kbruch.*
%_iconsdir/*/*/*/kbruch_*
%_docdir/HTML/en/kbruch
%_Kmenudir/kbruch.desktop

%files khangman
%_bindir/khangman
%_datadir/apps/khangman
%_iconsdir/*/*/apps/khangman.*
%_docdir/HTML/en/khangman
%_Kmenudir/khangman.desktop

%files kig
%_bindir/pykig.py
%_bindir/kig
%_libdir/kde3/libkigpart.so*
%_datadir/apps/kig
%_datadir/apps/katepart/syntax/python-kig.xml
#%_datadir/apps/kigpart
%_iconsdir/*/*/apps/kig.*
%_datadir/mimelnk/application/x-kig.desktop
%_datadir/mimelnk/application/x-kgeo.desktop
#
%_datadir/mimelnk/application/x-kseg.desktop
%_datadir/mimelnk/application/x-drgeo.desktop
%_datadir/mimelnk/application/x-cabri.desktop
#
%_datadir/services/kig_part.desktop
%_docdir/HTML/en/kig
%_Kmenudir/kig.desktop
%_iconsdir/*/*/mimetypes/kig_doc.*
# kfile
%_libdir/kde3/kfile_drgeo.so*
%_libdir/kde3/kfile_kig.so*
%_datadir/services/kfile_drgeo.desktop
%_datadir/services/kfile_kig.desktop

%files keduca
%_bindir/keduca*
%_libdir/kde3/libkeducapart.so*
%_datadir/apps/keduca
%_datadir/mimelnk/application/x-edu.desktop
%_datadir/services/keduca_*.desktop
%_iconsdir/*/*/*/keduca*
%_docdir/HTML/en/keduca
%_Kmenudir/keduca.desktop
%_Kmenudir/keducabuilder.desktop

%files kiten
%_bindir/kiten
%_bindir/kitengen
%_libdir/libkiten.so*
#%_libdir/kiten.so*
%_datadir/apps/kiten
%_docdir/HTML/en/kiten
%_iconsdir/*/*/apps/kiten.*
%_iconsdir/*/*/actions/edit_add.png
%_iconsdir/*/*/actions/edit_remove.png
%_iconsdir/*/*/actions/kanjidic.png
%_Kmenudir/kiten.desktop

%files kverbos
%_bindir/kverbos
%_datadir/apps/kverbos
%_docdir/HTML/en/kverbos
%_iconsdir/*/*/actions/kverbosuser.png
%_iconsdir/*/*/*/kverbos.*
%_Kmenudir/kverbos.desktop

%files kmplot
%_bindir/kmplot
%_libdir/kde3/libkmplotpart.so*
%_datadir/apps/kmplot
%_datadir/mimelnk/application/x-kmplot.desktop
%_datadir/services/kmplot_*.desktop
%_iconsdir/*/*/apps/kmplot.*
%_docdir/HTML/en/kmplot
%_Kmenudir/kmplot.desktop

#%files flashkard
#%_bindir/flashkard
#%_datadir/apps/flashkard
#%_docdir/HTML/en/flashkard
#%_iconsdir/*/*/apps/flashkard.*
#%_Kmenudir/flashkard.desktop

%files kpercentage
%_bindir/kpercentage
%_datadir/apps/kpercentage
%_docdir/HTML/en/kpercentage
%_iconsdir/*/*/apps/kpercentage.*
%_Kmenudir/kpercentage.desktop

%files kalzium
%_bindir/kalzium
%_datadir/apps/kalzium
%_docdir/HTML/en/kalzium
%_iconsdir/*/*/apps/kalzium.*
%_Kmenudir/kalzium.desktop

%files klettres
%_bindir/klettres
%_datadir/apps/klettres
%_datadir/icons/*/*/*/klettres.*
#%_datadir/icons/*/*/apps/grownup.png
#%_datadir/icons/*/*/apps/kids.png
#%_datadir/icons/*/*/apps/menubar.png
%_Kmenudir/klettres.desktop
%doc %_docdir/HTML/en/klettres

#%files kmessedwords
#%_bindir/kmessedwords
#%_datadir/apps/kmessedwords
#%_datadir/icons/*/*/*/kmessedwords*
#%doc %_docdir/HTML/en/kmessedwords
#%_Kmenudir/kmessedwords.desktop

%files kstars
%_bindir/apmount
%_bindir/apogee_ppi
%_bindir/celestrongps
%_bindir/indiserver
%_bindir/fliccd
%_bindir/fliwheel
%_bindir/lx200*
%_bindir/kstars
%_bindir/meade_lpi
%_bindir/temma
%_bindir/sbigccd
%_bindir/skycommander
%_bindir/v4ldriver
%_bindir/v4lphilips
%_Kmenudir/kstars.desktop
%_datadir/apps/kstars
%_datadir/icons/*/*/*/kstars*
%doc %_docdir/HTML/en/kstars

%files ktouch
%_bindir/ktouch
%_Kmenudir/ktouch.desktop
%_datadir/apps/ktouch
%_datadir/icons/*/*/*/ktouch*
%doc %_docdir/HTML/en/ktouch

%files kvoctrain
%_bindir/kvoctrain
%_bindir/*kvtml
%_libdir/libkvoctraincore.so*
%_Kmenudir/kvoctrain.desktop
%_datadir/apps/kvoctrain
%_datadir/icons/*/*/*/kvoctrain*
%_Kmimelnk/text/x-kvtml.desktop
#%_datadir/icons/kvoctrain*
%doc %_docdir/HTML/en/kvoctrain

%files libs
#%_bindir/test_extdate*
%_libdir/libextdate.so*
%_libdir/libkdeeduplot.so*
%_libdir/libkdeeduui.so*
%_libdir/libkdeeducore.so*
#%_iconsdir/*/*/apps/edu_*.png
%_datadir/applnk/Edutainment
%_datadir/mimelnk/application/x-edugallery.desktop

%files devel
%if %_keep_libtool_files
%_libdir/*.la
%_libdir/kde3/*.la
%endif
%_includedir/*.h
%_includedir/libkiten/
%_includedir/libkdeedu/

%changelog
* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Automake version is fixed to 1.11.5 detect.

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.13-alt1.1
- Rebuilt with Boost 1.49.0

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- rebuilt with new boost

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt3
- rename indiserver to resolve conflict with indilib

* Mon Dec 15 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt2
- rebuilt with new boost
- remove deprecated macroses from specfile

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Thu Mar 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt3
- set kturtle speed to slowest by default

* Thu Feb 28 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt2
- fix find boost-python

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt3
- rebuilt with new python

* Mon Dec 10 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt2
- setup kturtle default language from current locale

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Tue Jun 05 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- install ru and uk keyboard layouts for ktouch

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon May 07 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- fix saved file encoding in kturtle; thanks cas@alt

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Fri Dec 09 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Fri Feb 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- add patch for fliccd

* Thu Jan 27 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- rebuild with new gcc
- remove setuid root permissions for fliccd until review or resmgr support 

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Mon Oct 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- fix khangman menu

* Wed Jun 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix requires

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version
- fix menu sections

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Mon Mar 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Fri Sep 19 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Thu May 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH

* Mon May 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH

* Tue Apr 01 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Wed Feb 05 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update code from cvs

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update code from cvs

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs

* Wed Oct 16 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.2
- update from cvs
- increase %%release to upgrade Daedalus

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- sync patches with cooker
- rebuild with gcc3.2 && objprelink

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Mon Aug 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version
- split

* Mon Jun 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Mon Apr 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.3mdk
- RC3

* Wed Feb 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix BuildRequires on 8.2

* Sat Feb 09 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.2mdk
- Fix ./configure
- Enable debug
- Set unstable macro to 1

* Wed Feb 06 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.1mdk
- Rename to allow KDE 2 & 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-1mdk
- kde 3.0 beta1

