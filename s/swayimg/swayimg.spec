%define _unpackaged_files_terminate_build 1

Name: swayimg
Version: 5.2
Release: alt1
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
BuildRequires: libraw0-devel
BuildRequires: pkgconfig(libdrm)
BuildRequires: libluajit-devel
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

rm -v %buildroot/%_datadir/licenses/%name/LICENSE

%check
%meson_test

%files
%doc *.md LICENSE
%_bindir/%name
%dir %_datadir/%name
%_datadir/doc/%name
%_datadir/%name/*.lua
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/bash-completion/completions/%name
%_man1dir/%name.1*
%_datadir/zsh/site-functions/_%name

%changelog
* Thu Apr 30 2026 Pavel Shilov <zerospirit@altlinux.org> 5.2-alt1
- Update to new version and fix buildrequires to close (ALT #58952).

* Wed Mar 18 2026 Pavel Shilov <zerospirit@altlinux.org> 5.0-alt1
- Update to new version 5.0.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 4.7-alt1
- Update to new version 4.7.

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 4.6-alt1
- Update to new version 4.6.

* Tue Nov 04 2025 Pavel Shilov <zerospirit@altlinux.org> 4.5-alt2
- add dependencies to fix (ALT #56719)

* Sat Jul 26 2025 Pavel Shilov <zerospirit@altlinux.org> 4.5-alt1
- 4.4 -> 4.5

* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org> 4.4-alt1
- Update based on upstream version 4.4.

* Tue Oct 22 2024 Pavel Shilov <zerospirit@altlinux.org> 3.4-alt1
- initial build for Sisyphus
