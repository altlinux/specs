%define _unpackaged_files_terminate_build 1

Name: swayimg
Version: 4.4
Release: alt1
Summary: Image viewer for Wayland.
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/artemsen/swayimg

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: giflib-devel
BuildRequires: hicolor-icon-theme
BuildRequires: meson >= 0.60.0
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(bash-completion)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(libpng16)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libwebpdemux)

%description
Swayimg is a lightweight image viewer for Wayland display servers.

In a Sway compatible mode, the viewer creates an "overlay" above
the currently active window, which gives the illusion that you are
opening the image directly in a terminal window.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/swayimgrc
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/bash-completion/completions/%name
%_man1dir/%name.1*
%_man5dir/swayimgrc.5*

%changelog
* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org> 4.4-alt1
- Update based on upstream version 4.4.

* Tue Oct 22 2024 Pavel Shilov <zerospirit@altlinux.org> 3.4-alt1
- initial build for Sisyphus
