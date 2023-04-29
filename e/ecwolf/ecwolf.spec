Name: ecwolf
Version: 1.4.1
Release: alt1
Summary: An opensource implementation of Wolfenstein3D engine
License: GPL-2.0-only
Group: Games/Arcade
Url: https://maniacsvault.net/ecwolf
#Git-Clone:     https://bitbucket.org/ecwolf/ecwolf.git
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch1: ecwolf-no-rpath.patch
Patch2: ecwolf-fix-path.patch
Patch3: 0001-locating-main-binary-in-usr-bin.patch
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: hicolor-icon-theme
BuildRequires: libjpeg-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libSDL2_net-devel
BuildRequires: bzip2-devel
BuildRequires: libfluidsynth-devel
BuildRequires: libgtk+2-devel
BuildRequires: libSDL2-devel
BuildRequires: zlib-devel
Provides: bundled(gdtoa)
Provides: bundled(lzma)

%description
ECWolf is a port of the Wolfenstein 3D engine based of Wolf4SDL.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

# remove bundled libs
rm -Rf deps/{bzip2,zlib,jpeg-6b,SDL,SDL_mixer,SDL_net,textscreen}
sed -e 's|/usr/local/share/games/wolf3d|%_datadir/wolf3d|g' -i docs/ecwolf.6

%build
%cmake \
    -DINTERNAL_ZLIB=OFF \
    -DINTERNAL_BZIP2=OFF \
    -DINTERNAL_JPEG=OFF \
    -DUSE_LIBTEXTSCREEN=OFF \
    -DGPL=ON
%cmake_build

%install
%cmake_install

%files
%doc docs/license-gpl.txt docs/license-id.txt
%doc README.md PHILOSOPHY.md docs/changelog
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/ecwolf.svg
%_docdir/%name/copyright
%_bindir/ecwolf
%dir %_datadir/ecwolf
%_datadir/ecwolf/ecwolf.pk3
%_man6dir/*

%changelog
* Fri Apr 28 2023 Artyom Bystrov <arbars@altlinux.org> 1.4.1-alt1
- initial build for ALT Sisyphus
