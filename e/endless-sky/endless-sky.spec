%define _unpackaged_files_terminate_build 1

Name: endless-sky
Version: 0.11.0
Release: alt1

Summary: Space exploration and combat game
License: GPL-3.0-or-later
Group: Games/Strategy

Url: https://endless-sky.github.io/
VCS: https://github.com/endless-sky/endless-sky

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: git
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libpng-devel
BuildRequires: libturbojpeg-devel
BuildRequires: libjpeg-devel
BuildRequires: libGL-devel
BuildRequires: libGLEW-devel
BuildRequires: libopenal-devel
BuildRequires: libmad-devel
BuildRequires: libuuid-devel
BuildRequires: libavif-devel
BuildRequires: libflac++-devel
BuildRequires: libminizip-devel
BuildRequires: libogg-devel
BuildRequires: catch-devel
Requires: endless-sky-gamedata = %EVR

%description
Endless Sky is a 2D space trading and combat game similar to the classic
Escape Velocity series. Explore other star systems. Earn money by trading,
carrying passengers, or completing missions. Use your earnings to buy
a better ship or to upgrade the weapons and engines on your current one.
Blow up pirates. Take sides in a civil war. Or leave human space behind
and hope to find friendly aliens whose culture is more civilized than your own.

# game data license differs from game binary license
%package gamedata
Summary: Game data for Endless Sky
License: CC-BY-SA-4.0 AND CC-BY-SA-3.0 AND CC-BY-4.0 AND CC-BY-3.0 AND CC-BY-2.0 AND CC0 AND GPL-2
Group: Games/Strategy
BuildArch: noarch

%description gamedata
Game data for Endless Sky.
See /usr/share/doc/endless-sky-gamedata-%version/copyright for licensing.

%prep
%setup 

%build
%cmake -DES_USE_VCPKG=OFF
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_bindir/
install -m755 %_arch-alt-linux/endless-sky %buildroot%_bindir/endless-sky
rm -rv %buildroot/usr/share/doc/endless-sky
%find_lang endless-sky

%files -f endless-sky.lang
%doc README.md changelog

%_bindir/endless-sky
%_iconsdir/hicolor/16x16/apps/endless-sky.png
%_iconsdir/hicolor/22x22/
%_iconsdir/hicolor/24x24/
%_iconsdir/hicolor/32x32/apps/endless-sky.png
%_iconsdir/hicolor/48x48/apps/endless-sky.png
%_iconsdir/hicolor/128x128/
%_iconsdir/hicolor/256x256/
%_iconsdir/hicolor/512x512/
%_desktopdir/io.github.endless_sky.endless_sky.desktop
%_man6dir/endless-sky.6*
%_datadir/metainfo/

%files gamedata
%doc copyright
%_datadir/games/endless-sky/

%changelog
* Tue Mar 31 2026 Pavel Petrykin <silverducks@altlinux.org> 0.11.0-alt1
- New version.

* Tue Nov 11 2025 Pavel Petrykin <silverducks@altlinux.org> 0.10.16-alt1
- New version.

* Mon Nov 13 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.10.4-alt1
- Update to version 0.10.4.

* Tue Aug 22 2023 Michael Shigorin <mike@altlinux.org> 0.10.2-alt2
- Tweak EA: while fixing %%install properly wrt non-x86_64.
- Minor spec cleanup.

* Thu Jun 29 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.10.2-alt1
- New version 0.10.2. This is a stable release, focused on fixing bugs
  and making some other small improvements.

- Some of those improvements are:
    + More customisation options for rings drawn through interfaces.
    + A new personality that will prevent ships from ever cloaking.
    + Various new spaceport news items and civilian ship hails.

- Some notable bug fixes include:
    + Various missions and spaceport news items will no longer appear at inappropriate locations.
    + Fixed some instances of ships ceasing to act and drifting forever inappropriately.
    + Fixed a problem with out of system escorts not landing to refuel when an appropriate planet is available.

* Mon May 29 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.10.0-alt1
- Initial build for ALT.


