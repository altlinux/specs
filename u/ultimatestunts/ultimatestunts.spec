Name: ultimatestunts
Version: 0.7.6
Release: alt1
Summary: Ultimate Stunts is a remake of the famous DOS game 'stunts'

Group: Games/Arcade
License: GPL
Url: http://www.ultimatestunts.nl

Source: %name-srcdata-%version.tar
Source2: %name.desktop
Source3: %name-16.png
Source4: %name-32.png
Source5: %name-48.png
Patch0: %name-install.patch
Patch1: %name-conf.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: gcc-c++ libopenal-devel libSDL_image-devel libSDL-devel libalut-devel libvorbis-devel

%description
Ultimate Stunts is a remake of the famous DOS game 'stunts', a 3D racing
game with simple CGA/EGA/VGA graphics and no texture or smooth shading.
Spectacular stunts with loopings and bridges to jump over make the game
fun to play. One of the best aspects of Ultimate Stunts is the track
editor. Because of the tile-based tracks, every games is able to make
their own tracks.

%prep
%setup -q -n %name-srcdata-%version
%patch0 -p2
%patch1 -p2

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_desktopdir,%_miconsdir,%_niconsdir,%_liconsdir}
cp %SOURCE2 %buildroot%_desktopdir
cp %SOURCE3 %buildroot%_miconsdir/%name.png
cp %SOURCE4 %buildroot%_niconsdir/%name.png
cp %SOURCE5 %buildroot%_liconsdir/%name.png

%files
%_sysconfdir/%name.conf
%_bindir/ustunts*
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%doc AUTHORS ChangeLog COPYING

%changelog
* Mon Feb 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.7.6-alt1
- initial build

