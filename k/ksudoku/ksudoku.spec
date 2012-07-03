Name: ksudoku
Version: 0.4
Release: alt2.qa2

Summary: Sudoku Puzzle Generator and solver for KDE

License: GPL v2
Group: Games/Puzzles
Url: http://ksudoku.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sourceforge.net/ksudoku/%name-%version.tar.bz2
Patch: %name-gcc43.patch
Patch1: %name-0.4-alt-DSO.patch

# Automatically added by buildreq on Sun Oct 26 2008
BuildRequires: ccmake gcc-c++ kdepim-devel libGL-devel libXScrnSaver-devel libXcomposite-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libxkbfile-devel qt3-designer xorg-xf86vidmodeproto-devel

%description
Sudoku Puzzle Generator and Solver for KDE. Boards supported: 9x9 and
16x16. GUI for playing, saving, printing, solving and dubbing puzzles.
The program is fully expandable since the algorithm is extendible to
any general graph coloring problem.

%prep
%setup -q
%patch
%patch1 -p2
find -name "CMakeLists.txt" | xargs %__subst "s/QT_AND_KDECORE_LIBRARIES/QT_AND_KDECORE_LIBS/g"

%build
%add_optflags -I%_includedir/tqtinterface
%K3build

%install
%K3install
%K3find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_K3bindir/*
%_K3xdg_apps/ksudoku.desktop
%_K3apps/%name
%_K3conf/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2.qa2
- Fixed build

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.4-alt2.qa1
- Adapt to new KDE3 placement

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- update buildreq

* Tue Apr 17 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- new version 0.4 (with rpmrb script)

* Tue Apr 17 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

