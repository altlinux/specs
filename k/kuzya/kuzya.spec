# Copyright (c) 2009 Fedora Linux, Lviv, Ukrain.
# Copyright (c) 2010 Michael Shigorin
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name: kuzya
Version: 2.1.10
Release: alt2.1

Summary: Integrated Development Environment for students
License: GPL
Group: Education

Url: http://sourceforge.net/projects/kuzya/
Source: %name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libqt4-devel libqscintilla2-qt4-devel gcc-c++
BuildRequires: desktop-file-utils

%description
Kuzya is simple crossplatform IDE for people who study
programming. Main idea of it is to concentrate attention
of the users only on learning the programming language
but not on usage of IDE.

Idea:
--------
  Grygoriy Zlobin <zlobin@electronics.wups.lviv.ua>

Team leader:
--------
  Andriy Shevchyk <shevchyk@users.sourceforge.net>

Developers:
--------
  Volodymyr Shevchyk <volder@users.sourceforge.net>
  Viktor Sklyar <bouyantgrambler@users.sourceforge.net>
  Alex Chmykhalo <alexchmykhalo@users.sourceforge.net>

%prep
%setup

%build
qmake-qt4
make

%install
mkdir -p %buildroot%_datadir/%name/doc/
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_iconsdir/
mkdir -p %buildroot%_desktopdir/
mkdir -p %buildroot%_datadir/%name/
mkdir -p %buildroot%_datadir/%name/resources/translations
mkdir -p %buildroot/usr/lib64/fpc/2.2.4/units/x86_64-linux/graph/
mkdir -p %buildroot/usr/bin

cp -fr doc/Kuzya_Help/* %buildroot%_datadir/%name/doc/
cp -f graphics/c/graphics.h %buildroot%_includedir/
cp -fr profiles %buildroot%_datadir/%name/
cp -fr resources %buildroot%_datadir/%name/
cp -f resources/icon/kuzya.png %buildroot%_iconsdir/
cp -f resources/linux/kuzya.desktop %buildroot%_desktopdir/
cp -fr src/images %buildroot%_datadir/%name/src/
cp -fr resources/qss %buildroot%_datadir/%name/resources/
cp -fr src/images/kuzya.png %buildroot%_datadir/%name/
cp -f graphics/fpc/unit/graph.o		%buildroot%_bindir/
cp -f graphics/fpc/unit/graph.ppu 	%buildroot%_bindir/

install -pDm755 bin/%{name}graph %buildroot%_bindir/%{name}graph
install -pDm755 bin/%name      %buildroot%_bindir/%name
install -pDm755 resources/translations/*.qm %buildroot%_datadir/%name/resources/translations
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=IDE \
	--add-category=ComputerScience \
	%buildroot%_desktopdir/kuzya.desktop

%files
%_bindir/*
#_datadir/%name/doc/
%_includedir/*
%_datadir/%name/
%_iconsdir/*
%_desktopdir/*

%changelog
* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt2.1
- Rebuilt with qscintilla2 2.6

* Mon Jul 25 2011 Michael Shigorin <mike@altlinux.org> 2.1.10-alt2
- rebuilt against current qscintilla2 (thx real@)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.10-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kuzya

* Mon Jul 26 2010 Michael Shigorin <mike@altlinux.org> 2.1.10-alt1
- built for ALT Linux based on upstream spec

