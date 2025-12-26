Name: imv
Version: 5.0.1
Release: alt1
License: MIT

Summary: Image viewer for X11 and Wayland

Group: Graphics

Url: https://sr.ht/~exec64/imv/
Vcs: https://git.sr.ht/~exec64/imv

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson gcc-c++ cmake

BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xkbcommon)

# man
BuildRequires: asciidoc-a2x

# wayland
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)

# x11
BuildRequires: pkgconfig(xkbcommon-x11)

# backends
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libwebpdecoder) 

%description
Native Wayland and X11 support.

Support for dozens of image formats including:
PNG, JPEG, Animated GIFs, SVG, TIFF, Various RAW formats, 
Photoshop PSD files.
Configurable key bindings and behaviour.
Highly scriptable with IPC via imv-msg.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md LICENSE
%config(noreplace) %_sysconfdir/%{name}_config
%_bindir/%name
%_bindir/%name-*
%_desktopdir/*.desktop
%_man1dir/*.1.*
%_man5dir/*.5.*

%changelog
* Fri Dec 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.0.1-alt1
- new version 5.0.1 (with rpmrb script)

* Mon Mar 10 2025 Constantin Sunzow <protvin@altlinux.org> 4.5.0-alt2
- Fix FTBFS: build with icu 76.

* Fri Aug 16 2024 Kirill Unitsaev <fiersik@altlinux.org> 4.5.0-alt1
- Initial build
