Name: numptyphysics
Version: 0.3.160
Release: alt1
Summary: A crayon-drawing based physics puzzle game

Group: Games/Puzzles
License: GPLv3+
Url: http://numptyphysics.garage.maemo.org/
# see .gear/autobuild.update
Source0: %name-%version.tar
Source1: numptyphysics.desktop
Source10: %name-levels-%version.tar

Patch0: numptyphysics-0.4-gcc47.patch

Requires: %name-levels

# Automatically added by buildreq on Thu Feb 11 2010
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_ttf-devel libX11-devel zlib-devel

%description
Harness gravity with your crayon and set about creating blocks, ramps,
levers, pulleys and whatever else you fancy to get the little red thing
to the little yellow thing.

%package levels
Summary: Level set for numptyphysics
License: GPLv3+
Group: Games/Puzzles
BuildArch: noarch

%description levels
Game levels for numptyphysics, including "NP-complete" level set.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make

%install
%make DESTDIR=%buildroot install
install -D data/icon48/%name.png %buildroot%_liconsdir/%name.png
# they put png here and use unusual sizes
rm -rf %buildroot%_iconsdir/hicolor/scalable
mv %buildroot%_iconsdir/hicolor/26x26 %buildroot%_iconsdir/hicolor/24x24

# Additional levels
tar xf %SOURCE10 -C %buildroot%_datadir/numptyphysics
#rm "%buildroot%_datadir/numptyphysics/levels/siminz/L02_bridge Gaps tut.nph"
#rm %buildroot%_datadir/numptyphysics/levels/*/*npz

%files
%_bindir/numptyphysics
%dir %_datadir/numptyphysics
%_datadir/numptyphysics/*
%_desktopdir/numptyphysics.desktop
%_iconsdir/hicolor/24x24/apps/*
%_iconsdir/hicolor/48x48/apps/*
%_iconsdir/hicolor/64x64/apps/*
%dir %_datadir/numptyphysics/levels
%exclude %_datadir/numptyphysics/levels/*

%files levels
%_datadir/numptyphysics/levels/*

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.3.160-alt1
- Autobuild version bump to 0.3.160

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 0.3.159-alt1
- Autobuild version bump to 0.3.159
- Drop all patches except gcc one
- Drop "full" package (it was actually empty)

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.146-alt1.1
- Fixed build with glibc 2.16

* Fri Feb 12 2010 Fr. Br. George <george@altlinux.ru> 0.3.146-alt1
- Version up

* Fri Feb 12 2010 Fr. Br. George <george@altlinux.ru> 0.3.145-alt2
- Use git-svn for updating

* Thu Feb 11 2010 Fr. Br. George <george@altlinux.ru> 0.3.145-alt1
- Version up

* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from FC

* Tue Sep 30 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.4.20080925svn
- Add more levels

* Mon Sep 29 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.2.20080925svn
- Review, small tidy-ups

* Thu Sep 25 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.1.20080925svn
- Initial packaging attempt
