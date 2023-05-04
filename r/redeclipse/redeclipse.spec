%define _appdatadir %_datadir/appdata/
Summary: Fast paced first person ego-shooter
Name: redeclipse
Version: 2.0.0
Release: alt1
## See doc/all-licenses.txt
License: CC-BY-SA and zlib and OFL
Group: Games/Arcade
Url: http://www.redeclipse.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/red-eclipse/base/releases/download/v%version/%{name}_%{version}_nix.tar.bz2
Patch: redeclipse-2.0.0-fix-cube2font-install.patch
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++ make
BuildRequires: ed
BuildRequires: ImageMagick-tools
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)
Requires: %name-data = %version

%description
The game is a single-player and multi-player first-person ego-shooter, built
as a total conversion of Cube Engine 2, which lends itself toward a balanced
gameplay, completely at the control of map makers, while maintaining a general
theme of agility in a variety of environments.

%package server
Summary: Server for RedEclipse game
License: CC-BY-SA and zlib
Group: Games/Arcade
Requires: %name-data = %version
Conflicts: %name < %version

%description server
The game is a single-player and multi-player first-person ego-shooter, built
as a total conversion of Cube Engine 2, which lends itself toward a balanced
gameplay, completely at the control of map makers, while maintaining a general
theme of agility in a variety of environments.
This package contains the dedicated server for the Red Eclipse FPS game. It
also includes some example scripts for configuring the server.

%package data
Summary: Data files for RedEclipse game
License: CC-BY-SA
Group: Games/Arcade
Requires: %name = %version
BuildArch: noarch

%description data
The game is a single-player and multi-player first-person ego-shooter, built
as a total conversion of Cube Engine 2, which lends itself toward a balanced
gameplay, completely at the control of map makers, while maintaining a general
theme of agility in a variety of environments.
This package contains the data files needed by %name.

%package -n cube2font
Summary: Utility program for creating font bitmaps for Cube Engine games
Group: Games/Arcade
License: zlib

%description -n cube2font
This is a utility program designed to create font bitmaps for Cube Engine
games, it works by taking a Truetype font and building it into a set of
coordinates in an image. It's an improved version of the previous TTF2Font,
supporting a much larger range of characters.

%prep
%setup
%patch0 -p1

%build
%make CXXFLAGS="%optflags" -C src client server cube2font

%install
%makeinstall_std -C src \
	prefix=%prefix \
	libexecdir=%buildroot%_libdir \
	system-install system-install-cube2font

# Fix some rpmlint noises
find %buildroot -size 0 -delete
rm -fr %buildroot%_datadir/%name/data/*/{.gitmodules,.gitattributes,.github}

%files
%doc readme.* doc/*.txt
%_bindir/%name
%dir %_libdir/%name/
%_libdir/%name/%name

%_libdir/%name/config
%_libdir/%name/data
%_libdir/%name/doc
%_desktopdir/%name.desktop
%_appdatadir/%name.appdata.xml
%_docdir/redeclipse/examples/servinit.cfg
%_pixmapsdir/%name.xpm
%_iconsdir/hicolor/*/apps/%name.png
%_man6dir/%name.6.*

%files server
%doc doc/examples/servinit.cfg
%_bindir/%name-server
%_libdir/%name/%name-server
%_man6dir/%name-server.6*

%files data
%doc readme.txt
%dir %_datadir/%name
%_datadir/%name/*

%files -n cube2font
%doc readme.txt
%_bindir/cube2font
%_man1dir/cube2font.1*

%changelog
* Thu May 04 2023 Artyom Bystrov <arbars@altlinux.org> 2.0.0-alt1
- initial build for ALT Sisyphus

