Name: commander-wars
Summary: The aim of this project is to create an Advance Wars Clone
License: LGPLv3
Version: 0.29.3.1
Release: alt1

Group: Games/Strategy
Url: https://github.com/Robosturm/Commander_Wars/
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar
Patch: Fix_path.patch

BuildRequires: qt6-base-devel libqt6-qml libqt6-qmlcore qt6-declarative-devel qt6-tools-devel qt6-multimedia-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib libssl-devel zlib-devel
BuildRequires: libfontconfig doxygen
BuildRequires: ImageMagick-tools
Requires: %name-data = %version-%release

ExcludeArch: armh

%description
The aim of this project is to create an Advance Wars Clone.

%package data
Summary: Data files for Commander Wars
Group: Games/Strategy
BuildArch: noarch

%description data
Data files (graphics, music, sounds) required by Commander Wars.

%prep
%setup
%patch0 -p1

%__subst '/RPATH/d' CMakeLists.txt #remove insecure RPATH '/../'

%build
mkdir build
cd build
cmake .. \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DUSEAPPCONFIGPATH=ON \
	-DOPENSSL_USE_STATIC_LIBS=OFF
%make_build

#%%cmake -DCMAKE_BUILD_TYPE=Release \
#		-DCMAKE_INSTALL_PREFIX=/usr \
#		-DUSEAPPCONFIGPATH=ON
#%%cmake_build

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
install -D -m0755 build/commander_wars %buildroot%_bindir/%name
cp -R templates %buildroot%_datadir/%name
cp -R data %buildroot%_datadir/%name

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Commander Wars
Comment=the open source Advance Wars Clone
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert icon.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files data
%_datadir/%name/

%changelog
* Sat Feb 25 2023 Artyom Bystrov <arbars@altlinux.org> 0.29.3.1-alt1
- update to new version

* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 0.25.5-alt1
- update to new version

* Thu Sep 24 2022 Artyom Bystrov <arbars@altlinux.org> 0.22.5.2-alt1
- initial build for ALT Sisyphus

