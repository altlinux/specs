%define _unpackaged_files_terminate_build 1

Name: lightning-image-viewer
Version: 0.3.0
Release: alt1

Summary: Fast and lightweight desktop image (pre)viewer
License: GPL-3.0
Group: Graphics
Url: https://github.com/shatsky/lightning-image-viewer

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(sdl3-image)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libheif)

Requires: zenity

%description
Fast and lightweight desktop image viewer featuring minimalistic
"transparent fullscreen overlay" UI/UX with controls similar to map
apps, implemented in C with SDL3 and SDL3_image; pan/zoom/fullscreen
controls basically replicate controls of leaflet.js which powers most
web maps (but zoom and keyboard pan are 2x more granular) and Firefox
and Chrome browsers.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Graphics;Viewer;|' share/applications/lightning-image-viewer.desktop

%build
gcc %optflags -DWITH_LIBEXIF -DWITH_LIBHEIF \
              src/viewer.c \
              -lSDL3 -lSDL3_image -lexif -lheif -lm \
              -o lightning-image-viewer

%install
install -Dm755 lightning-image-viewer %buildroot%_bindir/lightning-image-viewer
mkdir -p %buildroot%_datadir
cp -av share/* %buildroot%_datadir/

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/scalable/apps/%{name}.*

%changelog
* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
