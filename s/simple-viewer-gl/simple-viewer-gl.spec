%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: simple-viewer-gl
Version: 3.05
Release: alt1

Summary: Simple and tiny image viewer based on OpenGL
License: GPL-2.0
Group: Graphics
Url: https://github.com/reybits/simple-viewer-gl

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(zlib)
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(lcms2)
BuildRequires: giflib-devel
BuildRequires: libtiff-devel
BuildRequires: libvxl-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: libwebp-devel
BuildRequires: libcurl-devel
BuildRequires: imlib2-devel

ExcludeArch: i586

%description
Simple Viewer GL is a simple and tiny image viewer based on OpenGL.

The primary goal of Simple Viewer GL is to provide a fast, efficient
image viewer with only the essential features required for quick image
browsing. It includes vi-like key bindings and integrates seamlessly
with tiling window managers such as ion3/notion, i3wm, dwm, xmonad,
hyprland, sway, and others.

Supported formats include PNG, JPEG, JPEG 2000, PSD (Adobe Photoshop),
AI (Adobe Illustrator), EPS, XCF (GIMP), GIF, SVG, TIFF, TARGA, ICO,
ICNS (Apple Icon Image), BMP, PNM, DDS, XWD, SCR (ZX-Spectrum screen),
XPM, WebP, OpenEXR, and many more.

%prep
%setup
sed -i "s|; cmake|; cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5|" Makefile

%build
%make
%make_build

%install
%makeinstall_std PREFIX=/usr
install -Dm 644 sviewgl.desktop %buildroot%_desktopdir/sviewgl.desktop
install -p -Dm644 res/Icon-16.png %buildroot%_datadir/icons/hicolor/16x16/apps/sviewgl.png
install -p -Dm644 res/Icon-32.png %buildroot%_datadir/icons/hicolor/32x32/apps/sviewgl.png

%files
%doc Copying.txt README.md
%_bindir/sviewgl
%_desktopdir/sviewgl.desktop
%_datadir/icons/hicolor/16x16/apps/sviewgl.png
%_datadir/icons/hicolor/32x32/apps/sviewgl.png

%changelog
* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.05-alt1
- Initial build for Sisyphus
