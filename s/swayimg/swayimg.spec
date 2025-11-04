%define _unpackaged_files_terminate_build 1

Name: swayimg
Version: 4.5
Release: alt2
Summary: Image viewer for Wayland.
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/artemsen/swayimg

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-meson
BuildRequires: cmake
BuildRequires: giflib-devel
BuildRequires: hicolor-icon-theme
BuildRequires: meson >= 0.60.0
BuildRequires: scdoc
BuildRequires: zsh
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
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
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(libavif)
BuildRequires: pkgconfig(libsixel)
BuildRequires: pkgconfig(libraw)
BuildRequires: pkgconfig(libdrm)
BuildRequires: openexr-devel

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
%_datadir/zsh/site-functions/_%name

%changelog
* Tue Nov 04 2025 Pavel Shilov <zerospirit@altlinux.org> 4.5-alt2
- add dependencies to fix (ALT #56719)

* Sat Jul 26 2025 Pavel Shilov <zerospirit@altlinux.org> 4.5-alt1
- 4.4 -> 4.5

* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org> 4.4-alt1
- Update based on upstream version 4.4.

* Tue Oct 22 2024 Pavel Shilov <zerospirit@altlinux.org> 3.4-alt1
- initial build for Sisyphus
