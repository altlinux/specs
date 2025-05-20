Name: relive
Epoch: 1
Version: 1.0.9
Release: alt1
Summary: An Open-Source Engine Replacement for Oddworld: Abe's Oddysee and Oddworld: Abe's Exoddus
Group: Games/Arcade
License: MIT
Url: https://aliveteam.github.io/

Source: %name-%version.tar
Source2: %name-ao.sh
Source3: %name-ae.sh

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libSDL2_mixer-devel
BuildRequires: zenity
BuildRequires: libglvnd-devel
BuildRequires: libGLEW-devel
BuildRequires: libXext-devel

%description
An Open-Source Engine Replacement for Oddworld: Abe's Oddysee and Oddworld: Abe's Exoddus

WARNING! This package contain only engine, you need get the game data, from GOG
or Steam, and put in in the :
 - .oddworld/ao subdirectory for Abe's Odissey
 - .oddworld/ae subdirectory for Abe's Exodus

%prep
%setup -n %name-%version

%build

%cmake
%cmake_insource \
    -DCMAKE_BUILD_TYPE=Release
%make_build

%install
install -D -m0755 ./Source/relive/relive %buildroot%_bindir/%name

mkdir -p %buildroot%_libexecdir/%name
cp ./assets/%name-ao %buildroot%_libexecdir/%name/%name-ao
cp ./assets/%name-ae %buildroot%_libexecdir/%name/%name-ae

mkdir -p %buildroot/%_desktopdir/
mkdir -p %buildroot/%_pixmapsdir/
cp ./assets/%name-ao.desktop %buildroot/%_desktopdir/
cp ./assets/%name-ae.desktop %buildroot/%_desktopdir/
cp ./assets/%name.png %buildroot/%_pixmapsdir/

cp -R ./assets/shaders %buildroot/%_datadir/%name
install -D -m0755 %SOURCE2 %buildroot%_bindir/%name-ao
install -D -m0755 %SOURCE3 %buildroot%_bindir/%name-ae

%files
%doc README.md
%_bindir/%name-ao
%_bindir/%name-ae
%_bindir/%name

%_libexecdir/%name/%name-ao
%_libexecdir/%name/%name-ae
%_desktopdir/*.desktop
%_pixmapsdir/%name.png
%_datadir/%name

%changelog
* Fri May 16 2025 Artyom Bystrov <arbars@altlinux.org> 1:1.0.9-alt1
- Add epoch
- Update sources with fix of build with CMake 4.0.x

* Sat Jun 24 2023 Artyom Bystrov <arbars@altlinux.org> 1.0.4587-alt2
- Update sources
- Fix build on GCC13

* Tue Jul 6 2022 Artyom Bystrov <arbars@altlinux.org> 1.0.4587-alt1
 - initial release
