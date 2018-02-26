%def_enable servers

%define Name Warmux
Name: warmux
Version: 11.01
Release: alt1
Summary: 2D convivial mass murder game
Group: Games/Arcade
License: %gpl2plus
Url: http://www.%name.org
Source: http://download.gna.org/%name/%name-%version.tar
Patch: %name-%version-%release.patch
Requires: %name-data >= %version
Requires: fonts-ttf-dejavu
Provides: wormux = %version-%release
Obsoletes: wormux < %version-%release
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sat Jul 26 2008
BuildRequires: ImageMagick gcc-c++ libSDL-devel libSDL_gfx-devel
BuildRequires: libSDL_image-devel libSDL_mixer-devel libSDL_net-devel
BuildRequires: libSDL_ttf-devel libX11-devel libcurl-devel libpng-devel
BuildRequires: libxml2-devel

%description
Battle your favorite free software mascots in the %Name arena. With
big sticks of dynamite, grenades, baseball bats, and bazookas you can
exterminate your opponent in a 2D cartoon style scenery. The goal of
the game is to destroy all of your opponents' mascots.


%if_enabled servers
%package server
Summary: %Name dedicated game server
Group: Games/Arcade
Provides: wormux-server = %version-%release
Obsoletes: wormux-server < %version-%release

%description server
Battle your favorite free software mascots in the %Name arena. With
big sticks of dynamite, grenades, baseball bats, and bazookas you can
exterminate your opponent in a 2D cartoon style scenery. The goal of
the game is to destroy all of your opponents' mascots.

This package contains dedicated game server for %Name.
%endif


%package data
Summary: Data files for %name
Group: Games/Arcade
BuildArch: noarch
Requires: %name >= %version
Provides: wormux-data = %version-%release
Obsoletes: wormux-data < %version-%release

%description data
Data files for %name.


%prep
%setup
%patch -p1


%build
%configure \
    --with-datadir-name=%_datadir/%name \
    --with-font-path=%_datadir/fonts/ttf/dejavu/DejaVuSans.ttf \
    %{subst_enable servers} \
    CFLAGS="%optflags" CPPFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build
for s in 16 22 24 36 48 72 96 192; do
    convert -resize ${s}x$s -depth 8 \
			data/icon/%{name}_{256x256,${s}x$s}.png
done
bzip2 -9fk ChangeLog



%install
%make_install DESTDIR="%buildroot" install
rm -f %buildroot%_datadir/%name/*.{icns,png,xpm}
for s in 16 22 24 32 36 48 64 72 96 128 192; do
  install -D -m 0644 \
		{data/icon/%{name}_${s}x$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
install -d -m 0755 %buildroot{%_iconsdir/hicolor/scalable/apps,%_docdir/%name-%version}
mv %buildroot{%_datadir/%name/icon,%_iconsdir/hicolor/scalable/apps}/%name.svg
install -m 0644 AUTHORS ChangeLog.* README %buildroot%_docdir/%name-%version/

%find_lang %name


%files
%_bindir/%name
%_bindir/%name-list-games


%if_enabled servers
%files server
%_bindir/*-server
%endif


%files data -f %name.lang
%doc %_docdir/%name-%version/AUTHORS
%doc %_docdir/%name-%version/ChangeLog.*
%doc %_docdir/%name-%version/README
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_man6dir/*


%changelog
* Mon Feb 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.01-alt1
- Version 11.01 (ALT #25080)

* Wed Dec 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2.1-alt1
- Version 0.9.2.1

* Tue Sep 22 2009 Led <led@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Sat Jul 11 2009 Led <led@altlinux.ru> 0.8.4-alt1
- 0.8.4:
  + added dedicated game server

* Sat Mar 14 2009 Led <led@altlinux.ru> 0.8.3-alt1
- 0.8.3
- cleaned up spec

* Sun Nov 09 2008 Led <led@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sun Oct 12 2008 Led <led@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.8-alt3
- fixed %name.desktop

* Sat Jul 26 2008 Led <led@altlinux.ru> 0.8-alt2
- 0.8 release
- clean up spec
- added %name-0.8-alt.patch
- fixed License

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1.alpha1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for wormux

* Fri Nov 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8-alt1.alpha1
- Modified a bit wormux.desktop file.
- Game binary moved to %%_gamesbindir.

* Fri Nov 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.8-alt0.alpha1
- ALTLinuxized.

* Fri Sep 1 2006 Wart <wart@kobold.org> 0.7.4-1
- Update to 0.7.4

* Fri Aug 04 2006 Wart <wart@kobold.org> 0.7.2-6
- Add 'ArcadeGame' category to .desktop file

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-5
- Improve grammar in description

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-4
- Fix broken path to desktop icon
- Fix typo in description

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-3
- Use RPM_BUILD_ROOT consistently
- Put the wormux icon in a size-specific directory
- Removed INSTALL from the documentation files

* Fri Jun 09 2006 Wart <wart@kobold.org> 0.7.2-2
- Expanded the description
- Separated game data into a subpackage

* Fri Jun 02 2006 Wart <wart@kobold.org> 0.7.2-1
- Initial Fedora Extras package
