Name: sqliteman
Version: 2.0.0
Release: alt1

Url: http://sqliteman.com/
License: GPL-3.0-or-later
Group: Databases

Summary: Lightweigth but powerfull Sqlite3 manager

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pvanek/sqliteman/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch1: sqliteman-desktop-ru.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++ libqscintilla2-qt6-devel qt6-base-devel qt6-tools-devel libsqlite3-devel
BuildRequires: desktop-file-utils

%description
The best developer's and/or admin's GUI tool for Sqlite3
in the world. No joking here (or just a bit only) - it
contains the most complette feature set of all tools available.

%prep
%setup
%patch1 -p1

%build
%cmake -DSQLITEMAN_WITH_DOCS=OFF

%cmake_build

%install
%cmake_install

%files
%_bindir/sqliteman
%_datadir/applications/cz.yarpen.sqliteman.desktop
%_datadir/metainfo/cz.yarpen.sqliteman.metainfo.xml
%_datadir/icons/hicolor/*/apps/cz.yarpen.sqliteman.png
%_datadir/icons/hicolor/scalable/apps/cz.yarpen.sqliteman.svg

%changelog
* Mon Oct 26 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- update to 2.0.0 with Qt 6
- port to the Qt 6 based upstream build
- build with Qt Help support
- remove BuildRequires: libqscintilla2-qt5-devel and qt5-base-devel.
- remove BuildRequires: xorg-sdk.
- add BuildRequires: libqscintilla2-qt6-devel and qt6-base-devel.
- add BuildRequires: qt6-tools-devel.
- add BuildRequires: libsqlite3-devel.
- replace BuildRequires: cmake with rpm-build-cmake.
- replace BuildRequires: cmake with rpm-build-cmake.
- fixes: desktop-file categories (closes: #24919).
- add Russian desktop-file translations.

* Tue Apr 08 2025 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- fix build with cmake 4.0.0

* Wed Oct 11 2023 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1.qa9.1
- NMU: fix requires

* Mon Jun 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1.qa9
- Rebuilt with Qt5.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.2.2-alt1.qa8
- NMU: spec: adapted to new cmake macros.

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1.qa7
- Rebuilt with qscintilla2 2.10.1.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa6
- Rebuilt with qscintilla2 2.9

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa5
- Rebuilt with new qscintilla2

* Fri Dec 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa4
- Rebuilt with new qscintilla2

* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa3
- Rebuilt with qscintilla2 2.6

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.qa2
- Rebuilt with qscintilla2 2.5.1

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for sqliteman

* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- rebuild with new cmake macro, moved to git

* Sat Nov 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- rebuild (fix bug #21434)

* Tue Jul 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Jan 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- cleanup spec

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Fri May 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- initial build for ALT Linux Sisyphus

* Wed Feb 20 2007 - Petr Vanek <petr@scribus.info>
- initial package
