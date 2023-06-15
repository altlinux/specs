Name: endless-sky
Version: 0.10.0
Release: alt1

Summary: Space exploration and combat game
License: GPLv3
Group: Games/Strategy

Url: https://endless-sky.github.io/
VCS: https://github.com/endless-sky/endless-sky
Source: %name-%version.tar

ExclusiveArch: x86_64

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
Requires: %name-gamedata = %EVR

%description
Endless Sky is a 2D space trading and combat game similar to the classic 
Escape Velocity series. Explore other star systems. Earn money by trading, 
carrying passengers, or completing missions. Use your earnings to buy 
a better ship or to upgrade the weapons and engines on your current one. 
Blow up pirates. Take sides in a civil war. Or leave human space behind 
and hope to find friendly aliens whose culture is more civilized than your own.

%package gamedata
Summary: Game data for Endless Sky
License: CC-BY-SA-4.0 AND CC-BY-SA-3.0 AND CC-BY-4.0 AND CC-BY-3.0 AND CC-BY-2.0 AND CC0 AND GPL-2
Group: Games/Strategy
#Game data license differs from game binary license

%description gamedata
Game data for Endless Sky. Licensing details see in /usr/share/doc/%name-gamedata-%version/copyright.

%prep
%setup 

%build

%cmake  -DES_USE_VCPKG=OFF 
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_bindir/
install -m755 x86_64-alt-linux/endless-sky %buildroot%_bindir/endless-sky
rm -rv %buildroot/usr/share/doc/%name
%find_lang %name

%files -f %name.lang
%doc CONTRIBUTING.md README.md changelog

%_bindir/%name
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/22x22/
%_iconsdir/hicolor/24x24/
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/128x128/
%_iconsdir/hicolor/256x256/
%_iconsdir/hicolor/512x512/
%_desktopdir/%name.desktop
%_man6dir/%name.6.xz
%_datadir/metainfo/

%files gamedata
%doc copyright
%_datadir/games/endless-sky/

%changelog
* Mon May 29 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.10.0-alt1
- initial build for ALT


