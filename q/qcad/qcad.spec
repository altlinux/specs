Name: qcad
Summary: a professional CAD system
Summary(ru_RU.UTF-8): Профессиональная CAD система
Version: 2.0.5.0
Release: alt6.qa2
Url: http://www.ribbonsoft.com/qcad.html
License: GPL
Group: Graphics

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: qt3-assistant

Source0: qcad-%version.tar.bz2
Source1: qcad.desktop

Source10: qcad-icons.tar.bz2
Source11: qcad-tango-icons.tar.bz2

Patch0: qcad-2.0.5.0-x86_64.patch
Patch1: qcad-2.0.5.0-alt-qassistant.patch
Patch2: qcad-2.0.5.0-alt-qcaddoc.adp.patch
Patch3: qcad-2.0.5.0-alt-gcc43.patch

# Automatically added by buildreq on Sat Apr 14 2007
BuildRequires: gcc-c++ libqt3-devel python
BuildRequires: desktop-file-utils

%description
QCad is a professional CAD System. With QCad you can easily construct and
change drawings with ISO-text and many other features and save them as
DXF-files. These DXF-files are the interface to many CAD-systems such
as AutoCAD(TM) and many others.

%description -l ru_RU.UTF-8
QCad это профессиональная CAD система. С QCad вы можете легко создавать и
изменять рисунки с вставленным текстом и сохранять это в DXF файлы.
Через DXF файлы есть возможность обмениваться данными с другими CAD системами
(например AutoCAD(TM)).

%prep
%setup -q

tar -xjf %SOURCE11

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

subst "s,FULLASSISTANTPATH,%_libdir/qt3/bin," qcad/src/qc_applicationwindow.cpp
subst "s,QCADDOCPATH,%_docdir/%name-%version," qcad/src/qc_applicationwindow.cpp

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
export QTDIR=%_libdir/qt3
export PATH=$PATH:$QTDIR/bin
cd scripts
./build_qcad.sh

cd ..
find -name \*.ts -exec lrelease {} \;

%install
install -pD -m755 qcad/qcad %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name
cp -pR qcad/{fonts,patterns,qm} %buildroot%_datadir/qcad
find -name \*.qm -exec cp -t %buildroot%_datadir/qcad/qm {} \;

for l in $(find %buildroot%_datadir/%name/qm -name \*.qm); do
	echo -n $l | sed 's,.*_\(.*\)\.qm,%lang\(\1\) ,' >> %name.lang
	echo $l | sed "s,%buildroot,," >> %name.lang
done

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/qcad.desktop
mkdir -p %buildroot%_iconsdir
tar -xjf %SOURCE10 -C %buildroot%_iconsdir
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Engineering \
	%buildroot%_desktopdir/qcad.desktop

%files -f %name.lang
%doc qcad/doc/*
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/qm
%_datadir/%name/fonts
%_datadir/%name/patterns
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat May 21 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.5.0-alt6.qa2
- NMU: fix desktop permissions

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.5.0-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for qcad

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5.0-alt6
- fixed build with gcc4.3

* Thu May 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5.0-alt5
- drop old menu, added freedesktop menu
- build translations
- install help
- added Tango icons by default
- updated build dependencies

* Sun Oct 01 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt4
- support x86_64
- fix bug 10051

* Mon May 29 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt3
- gcc4.1

* Tue Mar 21 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt2
- dependense cleanup (fix bug 9274) 

* Wed Mar 08 2006 Michail Yakushin <silicium@altlinux.ru> 2.0.5.0-alt1
- new version

* Sun Feb 20 2005 Michail Yakushin <silicium@altlinux.ru> 2.0.4.0-alt2
- fix bug 6023

* Wed Nov 17 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.4.0-alt1
- new version

* Wed Jun 30 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt3
- fix bug 4539

* Wed May 26 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt2
- fixes in spec for python 

* Sun Mar 28 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.3.1-alt1
- new version 

* Sat Feb 07 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.2.0-alt1
- new version

* Sat Jan 10 2004 Michail Yakushin <silicium@altlinux.ru> 2.0.1.3-alt2
- fix spec

* Wed Dec 10 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.3-alt1
- new version

* Mon Dec 01 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.2-alt1
- new version

* Fri Oct 31 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.1-alt1
- new version

* Mon Oct 20 2003 Michail Yakushin <silicium@altlinux.ru> 2.0.1.0-alt1
- new version,
- some cleanup in requries

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 1.5.4-alt1
- new version

* Fri Sep 20 2002 Rider <rider@altlinux.ru> 1.5.3-alt1
- new version

* Wed Aug 14 2002 Rider <rider@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Jan 29 2002 Rider <rider@altlinux.ru>
- specfile bugfix and cleanup
- russian summary and description

* Wed Apr 10 2001 Rider <rider@altlinux.ru>
- 1.4.7

* Sat Dec 16 2000 AEN <aen@logic.ru>
- 1.4.4
- new gcc296 patch

* Sat Nov 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.4.1-5mdk
- fix gcc2.96 compilation.

* Fri Sep 08 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.4.1-4mdk
- recompiled with the right flags

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.1-3mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.1-2mdk
- macroszifications
- rebuild for the BM

* Tue Jun 20 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.4.1-1mdk
- packaged version 1.4.1

* Wed May 03 2000 Geoffrey Lee <snailtalk@linux-mandrake.com>
- _prefix && _tmppath

* Wed Apr 26 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.3.3-5mdk
- Adapted to the new location of the qt2 includes

* Tue Apr 11 2000 Enzo Maggi <enzo@mandrakesoft.com> 1.3.3-4mdk
- Changed group
- New menu entry

* Thu Jan 27 2000 Camille BИgnis <camille@mandrakesoft.com> 1.3.3-2mdk
- fixed typo in qcad.kdelink

* Tue Dec 30 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- Updated to version 1.3.3.

* Mon Nov  8 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
