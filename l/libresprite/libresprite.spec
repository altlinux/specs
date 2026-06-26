Name: libresprite
Version: 1.2
Release: alt1

Summary: Animated sprite editor and pixel art tool
License: GPL-2.0-only
Group: Graphics
Url: https://github.com/LibreSprite/LibreSprite

# Source has git submodules, repacked together (see .gear/rules)
# Source-url: https://github.com/LibreSprite/LibreSprite.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libfreetype-devel
BuildRequires: libgif-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libpixman-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libwebp-devel
BuildRequires: libarchive-devel
BuildRequires: zlib-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel

%description
LibreSprite is a free and open source program for creating and animating
your sprites. It is a fork of the last GPLv2 commit of Aseprite.

Features:
 * Create 2D animations for games, including sprites, textures and patterns.
 * Pixel-art tools such as drawing tools, color palettes, animation timeline,
   onion skinning and export options.
 * Load and save sequences of PNG files and GIF animations, as well as other
   file formats.

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DWITH_DESKTOP_INTEGRATION=ON \
    -DWITH_WEBP_SUPPORT=ON \
    -DUSE_SHARED_PIXMAN=ON \
    -DUSE_SHARED_LIBWEBP=ON \
    -DUSE_SHARED_CURL=ON \
    -DUSE_SHARED_GIFLIB=ON \
    -DUSE_SHARED_JPEGLIB=ON \
    -DUSE_SHARED_ZLIB=ON \
    -DUSE_SHARED_LIBPNG=ON \
    -DUSE_SHARED_LIBLOADPNG=OFF \
    -DUSE_SHARED_TINYXML=ON \
    -DUSE_SHARED_SDL2=ON \
    -DUSE_SDL2_BACKEND=ON \
    -DUSE_SHARED_FREETYPE=ON \
    -DENABLE_UPDATER=OFF
%cmake_build

%install
%cmakeinstall_std

# ALT provides the shell as /bin/sh, not /usr/bin/sh
subst 's|^#!/usr/bin/sh|#!/bin/sh|' %buildroot%_bindir/libresprite-thumbnailer

%files
%doc README.md LICENSE.txt
%_bindir/libresprite
%_bindir/libresprite-thumbnailer
%_datadir/libresprite/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/libresprite.png
%_datadir/metainfo/*.metainfo.xml
%_datadir/mime/packages/aseprite.xml
%_datadir/thumbnailers/libresprite.thumbnailer

%changelog
* Fri Jun 26 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Sisyphus (the free GPLv2 fork of Aseprite)
