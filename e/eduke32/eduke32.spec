Name: eduke32
Version: 20221225
Release: alt1
Summary: Source port of Duke Nukem 3D
License: GPL-2.0-only
Group: Games/Arcade
Url: https://www.eduke32.com/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: eduke32-%version.tar.xz
Source1: %{name}_32x32.png
Source2: %{name}_48x48.png
Source3: %{name}_64x64.png
Source4: %{name}_128x128.png
Source5: %name.desktop
Source6: %name-demo-install.sh
Source7: %name-demo-install.1
BuildRequires: dos2unix
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: nasm
BuildRequires: pkg-config
BuildRequires: libSDL2_mixer-devel
BuildRequires: libalsa-devel
BuildRequires: libflac-devel
BuildRequires: libgtk+2-devel
BuildRequires: libpng-devel
BuildRequires: libSDL2-devel
BuildRequires: libvorbis-devel
BuildRequires: libvpx-devel
BuildRequires: libGLU-devel

ExcludeArch: %ix86

%description
EDuke32 is a source port of the classic PC first person shooter Duke Nukem 3D
to Windows, Linux and OS X, which adds a ton of awesome features and
upgrades for regular players and an arsenal of editing functions and
scripting extensions for mod authors and map makers.

Note: You need 'Duke Nukem 3D' data files to play.
You can put them under '%_gamesdatadir/eduke32/' for all users
or '~/.eduke32/' only for yourself.
You can also play the shareware version. Use 'eduke32-demo-install' to
install the shareware files.

%package mapeditor
Summary: Eduke32 map editor
Group: Games/Arcade

%description mapeditor
Eduke32 maps editor based on BUILD engine

%prep
%setup
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .
cp %SOURCE6 .
cp %SOURCE7 .

%build
export CFLAGS='%optflags -Wno-format'
make PACKAGE_REPOSITORY=1 \
     PRETTY_OUTPUT=1 \
     RELEASE=1 \
     SDL_TARGET=2 \
     BASECFLAGS="%{optflags}" \
%{?_smp_mflags} \
     VC_REV=%version

dos2unix source/build/buildlic.txt

%install
install -Dm 0755 %name %buildroot%_bindir/%name
install -Dm 0755 mapster32 %buildroot%_bindir/mapster32
# shareware demo installer script
install -Dm 0755 %name-demo-install.sh %buildroot%_bindir/%name-demo-install
# data files and help files for editor
install -Dm 0644 package/sdk/SEHELP.HLP %buildroot%_gamesdatadir/%name/sehelp.hlp
install -Dm 0644 package/sdk/STHELP.HLP %buildroot%_gamesdatadir/%name/sthelp.hlp
install -Dm 0644 package/sdk/m32help.hlp %buildroot%_gamesdatadir/%name/m32help.hlp
install -Dm 0644 package/sdk/tiles.cfg %buildroot%_gamesdatadir/%name/tiles.cfg
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %{name}_32x32.png %buildroot%_niconsdir/%name.png
install -Dm 0644 %{name}_48x48.png %buildroot%_liconsdir/%name.png
install -Dm 0644 %{name}_64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -Dm 0644 %{name}_128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%_bindir/%name
%_bindir/%name-demo-install
%dir %_gamesdatadir/%name/
%_gamesdatadir/%name/m32help.hlp
%_gamesdatadir/%name/sehelp.hlp
%_gamesdatadir/%name/sthelp.hlp
%_gamesdatadir/%name/tiles.cfg
%doc source/build/buildlic.txt
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files mapeditor
%_bindir/mapster32

%changelog
* Thu Jan 19 2023 Artyom Bystrov <arbars@altlinux.org> 20221225-alt1
- initial build for ALT Sisyphus

* Sun Oct 17 2021 boris@steki.net
- Update to version 1633892719.d307f703c:
  * Fix dumbass oversight in 6839e418e34bff05bdd5debad9bf9146a09d9d72
  * Revert "engine: make floor sprites clip a little more like floors"
  * SW: fix buffer overflow preventing the game from starting, exposed by switching to the new memory allocation systems
  * engine: fix SDL fullscreen issues
  * engine: remove r_pr_vbos cvar and the code paths used for values 0 and 1
  * engine: add GL context version to glinfo, allow in 8 bpp mode (it's still backed by a GL surface, after all...)
  * engine: manually flush console log file ptr in crash handler
  * editor: fix "gameexecutable" option in configuration file
  * Fury: don't block input when player .hard_landing is set
  * Duke3d: zero player .horizRecenter and .horizSkew when zeroing return_to_center from CON
* Sun Apr 11 2021 Ferdinand Thiessen <rpm@fthiessen.de>
- Update to latest revision 9321 on 20210404
* Thu Aug 27 2020 Matthias Mailänder <mailaender@opensuse.org>
- Update to latest revision 8798 snapshot on 20200404
* Sat Apr 20 2019 Martin Hauke <mardnh@gmx.de>
- Update to latest revision 7615 snapshot on 20190419
- Use switch to SDL2
- Build with CFLAGS
- Run spec-cleaner
* Sat Apr 22 2017 boris@steki.net
- update to latest revision 6120 snapshot on 20170412
* Fri Jul 22 2016 boris@steki.net
- updated to latest revision 5811 snapshot on 20160704
- added gcc-c++ as build requirement
* Sat Nov  8 2014 kieltux@gmail.com
- Update to 2.0.0rev4584 (20140831)
  Still building against SDL because of a bug in the timidity
  implementation of SDL2_mixer which has already been fixed
  upstream, but there has not been any release since.
  https://hg.libsdl.org/SDL_mixer/rev/8ef083375857
- Removed subpackage eduke32-gui, eduke32-console
  It is now just eduke32 without a non-gui version.
- Updated eduke32-demo-install.sh, because ftp.3drealms.com is down.
  Using now archive.org.
- Spec file cleaning.
- Using _service for source download.
* Sat Aug 27 2011 boris@steki.net
- updated package to 2.0.0 rev 1992
  a lot of fixes some highlights
  Engine stuff:
  * Polymer light access to m32script (light[<lightidx>].<field>).
    As an application, provide a state 'insertlights' that takes the
    currently active lights and puts them into the map as SEs (e.g. for
    maphack recovery).
  * Prototype of a mechanism to gray out certain portion of a map,
    making them inactive to various, but not all, editing operations.
    Highlighting a set of sectors and pressing Ctrl-R will make the Z
    bounds be [(least ceiling z), (greatest floor z)] of all selected
    ones, pressing Ctrl-R when no sectors are highlighted will reset
    them. Not sure if it's for production use at this stage.
  * The 'align walls' feature [.] now has three independently
    toggleable behaviours: recurse nextwalls (toggled when Ctrl is
    pressed), iterate point2s (disabled when Shift is pressed), and also
    copy pixel width (toggled when Alt is pressed).
  * Make shades clamp instead of overflowing in the editor
  * Add 'r_shadescale_unbounded' cvar. When set to 0, OpenGL
    renderers should never draw completely black objects (currently
    only implemented for Polymost)
  * sector-like sprite clipping now works with x- xor y-flipped
    actual sprites
  Mapster32:
  * Add 'r_shadescale' to config
  * In 3D mode, make SPACE behave the same as holding down a mose
    button: the currently pointed-at object is locked. Required some
    modification of a.m32 to play well (i.e. not reset SPACE).
    This is useful by itself but more so in conjunction with the next point
  * make Alt behave as a modifier with PGUP/PGDN: when aiming at a
    2-sided wall, move the other side's sector's ceiling or floor (only
    this is new).
  * Auto-alignment of walls can be controlled in a finer grained
    fashion now:
    When pressing '.', only the immediate neighbors get aligned.
    Use Ctrl-. for the old behaviour.
  * When inserting a point in 2D mode, auto-align the neighboring
    wall
  * corruption checker has been hooked up to loading/saving
    routines to inform/warn the user
  * also warn if mouse pointer is over corrupt wall which is shown
    in pink then: you should not move such a wall!
  * faster map loading by deferring polymer_loadboard to 3d mode
    entrance (also removes some 'glGetTexLevelParameteriv returned
    GL_FALSE' warnings)
  * more logical maphack light handling, the logic is still a bit
    dodgy though
  * some menu and misc. function fixup
  * redundancy elimination...
  API:
  * added consts various for 'char *filename' parameters
  * loadboard() now accepts bit 4 for flags (formerly 'fromwhere')
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Tue Nov  2 2010 boris@steki.net
- updated package to 2.0.0 rev 1723
  * Polymost-style HUD model support for Polymer.
    It properly displays all HRP HUD models as far as I can tell.
  * New CON commands
  * mostly multiplayer fixes among other things
  * SDL and menu joystick fixes
  * Link debug builds with -rdynamic in order to get symbol
    names when printing backtraces from the signal handler.
  * Make the "Start" button of the GTK start-up window the default
    button of the window, which means pressing Enter now works at
    you'd expect.
  + Lot of other bugs fixed
* Tue Jan 19 2010 boris@steki.net
- Added demo files installation script called
  eduke32-demo-install which will download package
  extract it and show its license to user and force
  him to accept terms within
* Tue Jan 19 2010 boris@steki.net
- Added obsolete tag in spec file for removing -common
  package on upgrade
* Mon Jan 18 2010 boris@steki.net
- Removed -common package as it was unnecessary and
  was just confusing
* Sat Jan 16 2010 boris@steki.net
- Added Desktop integration files and icons
* Sat Jan 16 2010 boris@steki.net
- Packages for gui,console and mapeditor are created
  so now it can be selected on install or after can
  be changed with use of update-alternatives
* Fri Jan 15 2010 boris@steki.net
- Created inital rpm package from svn export
