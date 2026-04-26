%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: azpainter
Version: 3.0.12.3
Release: alt1

Summary: Paint software for editing illustrations and images
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.com/azelpg/azpainter

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ninja

BuildRequires: ninja-build
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(freetype2)

%description
AzPainter is a lightweight full color painting application for editing
illustrations and images.

Features include:

* Layers
* Many artistic filters
* Good range of selection tools
* Pen pressure support with automatic brush size adjustment
* Support for 16-bit color images with transparency (RGBA)
* Support for image formats like PSD, PNG, JPEG, TIFF, WebP

%prep
%setup
sed -i "s/Categories=.*/Categories=Graphics;2DGraphics;RasterGraphics;/" desktop/azpainter.desktop

%build
%configure
%ninja_build -C build --verbose

%install
%ninja_install -C build

%files
%doc AUTHORS ChangeLog README.md
%doc COPYING ReadMe_en ReadMe_ja about_mlk_en.txt about_mlk_ja.txt manual_ja.html
%_bindir/azpainter
%_desktopdir/azpainter.desktop
%dir %_datadir/azpainter3
%_datadir/azpainter3/*
%exclude %_datadir/doc/azpainter/COPYING
%exclude %_datadir/doc/azpainter/ReadMe_en
%exclude %_datadir/doc/azpainter/ReadMe_ja
%exclude %_datadir/doc/azpainter/about_mlk_en.txt
%exclude %_datadir/doc/azpainter/about_mlk_ja.txt
%exclude %_datadir/doc/azpainter/manual_ja.html
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/mime/packages/azpainter.xml

%changelog
* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 3.0.12.3-alt1
- new version 3.0.12.3 (with rpmrb script)

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.12-alt1
- Initial build for Sisyphus
