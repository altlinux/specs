Name:    cage
Version: 0.1.5
Release: alt1

Summary: A Wayland kiosk
License: MIT
Group:   Graphical desktop/Other
Url:     https://github.com/cage-kiosk/cage

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(wlroots) >= 0.16
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)

Requires: xorg-xwayland

%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

%prep
%setup

%build
%meson -Dxwayland=true
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Thu Aug 03 2023 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt1
- New version 0.1.5

* Tue May 16 2023 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1.20230107
- Initial build for Sisyphus
