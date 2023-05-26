Name: opensurge
Summary: 2D retro platformer inspired by Sonic games
License: GPLv3
Version: 0.6.0.3
Release: alt1

Group: Games/Arcade
Url: https://opensurge2d.org
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar

BuildRequires: liballegro5.2-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: surgescript-devel libphysfs-devel
BuildRequires: fontconfig
BuildRequires: ImageMagick-tools
Requires: %name-data = %version-%release

%description
Open Surge is a fun 2D retro platformer inspired by Sonic games,
and a game creation system that lets you unleash your creativity!
Open Surge is two projects in one: a game
and a game creation system (game engine).

%package data
Summary: Data files for opensurge
Group: Games/Arcade
BuildArch: noarch

# Most of the game's assets are licensed under CC-BY 3.0.
# Some individual files are licensed under CC-BY-SA 3.0,
# CC0, Giftware, MIT, and Public Domain.
#
# There also bundled fonts (Google Roboto and HanYang Gothic A1),
# but we un-bundle them, so they don't apply to the License tag here.
#
# For a detailed list, consult src/misc/copyright_data.csv
# inside the source archive.

License: CC-BY and CC-BY-SA and CC0 and Giftware and MIT and Public Domain

%description data
Data files (graphics, music, sounds) required by Open Surge.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release  \
	-DALLEGRO_STATIC=OFF  \
	-DALLEGRO_MONOLITH=OFF  \
	"-DGAME_BINDIR=%_bindir/" \
	"-DGAME_DATADIR=%_datadir/%name"  \
	-DDESKTOP_INSTALL=ON  \
	"-DDESKTOP_ENTRY_PATH=%_desktopdir"  \
	"-DDESKTOP_ICON_PATH=%_pixmapsdir"  \
	"-DDESKTOP_METAINFO_PATH=%_datadir/metainfo"  \
	./
%cmake_build

%install

%cmake_install

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Open Surge
Comment=2D retro platformer inspired by Sonic games
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert surge.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png

%files data
%doc licenses/CC-BY-3.0-legalcode.txt
%doc licenses/CC-BY-SA-3.0-legalcode.txt
%doc licenses/CC0-1.0-legalcode.txt
%doc licenses/Giftware-license.txt
%doc licenses/MIT-license.txt
%_datadir/%name/

%changelog
* Fri May 26 2023 Artyom Bystrov <arbars@altlinux.org> 0.6.0.3-alt1
- update to new version

* Sun Sep 18 2022 Artyom Bystrov <arbars@altlinux.org> 0.6.0.2-alt1
- update to new version

* Thu Aug 12 2021 Artyom Bystrov <arbars@altlinux.org> 0.5.2.1-alt1
- initial build for ALT Sisyphus