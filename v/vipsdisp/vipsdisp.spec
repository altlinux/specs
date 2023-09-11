%define app org.libvips.vipsdisp

Summary: Tiny libvips / gtk+4 image viewer
Name: vipsdisp
Version: 2.6.0
Release: alt1
License: MIT
Group: Graphics
Url: https://github.com/jcupitt/vipsdisp
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: L.A. Kostis <lakostis@altlinux.org>

BuildRequires(pre): meson cmake
BuildRequires: libgnome-devel libvips-devel libgtk4-devel

%description
This program displays an image with libvips and gtk+4. This is supposed to be a
slightly useful image viewer. It can display huge (many, many GB) images
quickly and without using much memory. It supports many scientific and
technical image formats, including TIFF, WEBP, JP2K, JXL, PNG, JPEG, SVS, MRXS,
OpenEXR, GIF, PDF, SVG, FITS, Matlab, NIfTI, Analyze, etc. It supports pixel
types from 1 bit mono to 128-bit double precision complex.

%prep
%setup -q
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%doc README.md CHANGELOG.md
%_bindir/%name
%_iconsdir/hicolor/128x128/apps/%app.png
%_desktopdir/%app.desktop
%_datadir/glib-2.0/schemas/%app.gschema.xml
%_datadir/metainfo/%app.metainfo.xml

%changelog
* Mon Sep 11 2023 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt1
- 2.6.0.

* Mon Aug 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2.5.1-alt1
- 2.5.1.

* Tue May 23 2023 L.A. Kostis <lakostis@altlinux.ru> 2.4.1-alt1
- Initial build for ALTLinux.

