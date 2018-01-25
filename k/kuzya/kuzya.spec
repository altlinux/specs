# Copyright (c) 2009 Fedora Linux, Lviv, Ukrain.
# Copyright (c) 2010 Michael Shigorin
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name: kuzya
Version: 2.1.12_rc20170720
Release: alt1

Summary: Integrated Development Environment for students
License: GPL
Group: Education

Url: http://sourceforge.net/projects/kuzya/
Source: %name-%version.tar
Patch1: %name-2.1.12-qscintilla.patch
Patch2: %name-2.1.12-e2k.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: qt5-base-devel rpm-macros-qt5 libqscintilla2-qt5-devel gcc-c++
BuildRequires: desktop-file-utils
# for generate.py (version.h generator)
BuildRequires: python-base python-modules

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
%patch1 -p1
%ifarch e2k
%patch2 -p1
%endif

%build
pushd src
python generate.py -v 2.1.12
popd

%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_bindir/*
#_datadir/%name/doc/
%_includedir/*
%_datadir/%name/
%_iconsdir/*
%_desktopdir/*

%changelog
* Thu Jan 25 2018 Andrew Savchenko <bircoph@altlinux.org> 2.1.12_rc20170720-alt1
- Update to latest git with qt5 support (mandatory for e2k).
- Simplify spec, use upstream tracking branch.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.10-alt2.5
- Rebuilt with qscintilla2 2.10.1.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt2.4
- Rebuilt with qscintilla2 2.9

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt2.3
- Rebuilt with new qscintilla2

* Fri Dec 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.10-alt2.2
- Rebuilt with new qscintilla2

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

