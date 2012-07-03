Name: trackballs
Version: 1.1.4
Release: alt1

Summary: Steer a marble ball through a labyrinth
License: GPLv2+
Group: Games/Arcade
Url: http://trackballs.sourceforge.net/

# http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: trackballs-1.1.4-alt-install-data.patch
Patch2: trackballs-1.1.4-alt-desktop.patch
Patch3: trackballs-1.1.4-alt-bound.patch
Patch4: trackballs-1.1.4-alt-SHARE_DIR.patch
Patch5: trackballs-1.1.4-deb-doc.patch
Patch6: trackballs-1.1.4-rh-black-vertices-fix.patch
Patch7: trackballs-1.1.4-rh555877.patch

Requires: %name-game = %version-%release
Requires: %name-music >= 2:1.4

# Automatically added by buildreq on Sun Jun 06 2010
BuildRequires: gcc-c++ guile-devel libGL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel zlib-devel

%description
Trackballs is a game in which you steer a marble ball through tracks
of varying difficulty.  The game features 3D graphics, an integerated
level editor and high quality soundeffects and background music.

%package game
Summary: Steer a marble ball through a labyrinth
Group: Games/Arcade
Conflicts: %name < %version-%release
Requires: %name-data = %version-%release

%description game
Trackballs is a game in which you steer a marble ball through tracks
of varying difficulty.  The game features 3D graphics, an integerated
level editor and high quality soundeffects and background music.

Music for this game is available via %name-music package.

%package data
Summary: Steer a marble ball through a labyrinth
Group: Games/Arcade
BuildArch: noarch
Requires: %name-game = %version-%release

%description data
Trackballs is a game in which you steer a marble ball through tracks
of varying difficulty.  The game features 3D graphics, an integerated
level editor and high quality soundeffects and background music.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
sed -i '/kenny/d' configure.ac

%build
mkdir -p m4
%add_optflags -Wno-unused
%autoreconf
%configure --with-highscores='~'
%make_build

%install
%makeinstall_std
ln -sf ../../fonts/ttf/dejavu/DejaVuSans.ttf \
	%buildroot%_datadir/%name/fonts/menuFont.ttf
%find_lang %name

%files

%files game
%_bindir/*

%files data -f %name.lang
%_datadir/%name
%_man6dir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%doc AUTHORS ChangeLog FAQ README TODO

%changelog
* Mon Jun 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.
- Really fixed "will always overflow destination buffer" bug.
- Built with default version of system g++ and guile.
- Imported patches from FC and Debian trackballs packages.
- Replaced included font file with a symlink to DejaVuSans.ttf.
- Relocated installed files to standard locations.
- Relocated highscores file to $HOME/.trackballs/ directory.
- Dropped menu file.
- Fixed and packaged desktop file.
- Updated summary and description.
- Cleaned up specfile.

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.2-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for trackballs
  * postclean-05-filetriggers for spec file

* Mon Aug 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1.2
- fix build

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1.1
- rebuild
- update requires

* Thu Apr 12 2007 Sergey V Turchin <zerg at altlinux dot org> 1.1.2-alt1
- new version

* Thu Sep 01 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1.0-alt1
- new version

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt2
- fix menu-file

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Fri Nov 21 2003 Sergey V Turchin <zerg at altlinux dot org> 0.9.1-alt1
- new version

* Wed Jul 30 2003 Sergey V Turchin <zerg at altlinux dot org> 0.9.0-alt5
- fix menu

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.9.0-alt4
- move music to it's own .src.rpm
- fix BuildRequires

* Thu Apr 10 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.9.0-alt2
- fix requires

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 0.9.0-alt1
- new version

* Wed Feb 26 2003 Sergey V Turchin <zerg@altlinux.ru> 0.7.1-alt1
- new version

* Tue Feb 18 2003 Sergey V Turchin <zerg@altlinux.ru> 0.6.0-alt1
- new version

* Mon Feb 10 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt1
- new version

* Sat Feb 08 2003 ZerG <zerg@altlinux.ru> 0.5.0-alt1
- cleaunup spec
- build for ALT

* Thu Feb 6 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.5.0-1mdk
- Upgraded to 0.5.0. Changed Copyright. Separated game & music.

* Wed Feb 5 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.4.1-2mdk
- Moved to /usr/games, added icons, fixed rights for directories (new levels can be created),
              build requires fixes, build with macros, french description.

* Sun Feb 2 2003 Guillaume Bedot <guillaume.bedot@wanadoo.fr> 0.4.1-1mdk
- First Mandrake package for Trackballs

