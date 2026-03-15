%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: simple-viewer-gl
Epoch: 1
Version: 3.3.4
# WARNING: do not forget to run
#          sed -i '/^If you like/d' third-party/fmtlib/README.rst
#          sed -i '/^help/d' third-party/fmtlib/README.rst
#          on each version update.
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
%ifnarch %ix86
BuildRequires: libopenjpeg2.0-devel
%endif
BuildRequires: libwebp-devel
BuildRequires: libcurl-devel
BuildRequires: imlib2-devel
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(libheif)

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

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc Copying.txt README.md
%_bindir/sviewgl
%_desktopdir/sviewgl.desktop
%_iconsdir/hicolor/*/apps/sviewgl.png

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 1:3.3.4-alt1
- New version 3.3.4 with enabled support of OpenEXR and HEIF.

* Sat Jan 31 2026 Nikolay Strelkov <snk@altlinux.org> 3.05-alt2
- Enabled build on i586 without OpenJPEG. 

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.05-alt1
- Initial build for Sisyphus
