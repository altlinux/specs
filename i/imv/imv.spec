Name: imv
Version: 4.5.0
Release: alt1
License: MIT

Summary: Image viewer for X11 and Wayland

Group: Graphics

Url: https://sr.ht/~exec64/imv/

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson gcc-c++ cmake

BuildRequires: asciidoc-a2x
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(icu-io)
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xkbcommon)

# wayland
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-egl)

# x11
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon-x11)

# backends
BuildRequires: libfreeimage-devel
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(librsvg-2.0) >= 2.44
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(libjxl)
 
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
%meson \
    -Dlibnsgif=disabled
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
* Fri Aug 16 2024 Kirill Unitsaev <fiersik@altlinux.org> 4.5.0-alt1
- Initial build
