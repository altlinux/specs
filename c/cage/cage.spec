Name:    cage
Version: 0.3.1
Release: alt1

Summary: A Wayland kiosk
License: MIT
Group:   Graphical desktop/Other
URL:     https://github.com/cage-kiosk/cage
VCS:     https://github.com/cage-kiosk/cage.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(wlroots-0.20)
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)

Requires: xorg-xwayland
Requires: seatd

%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Thu Jul 02 2026 Anton Midyukov <antohami@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Sat Apr 11 2026 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Mon Dec 29 2025 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt3
- Upstream fixes:
  + Fix segfault when title or app_id is NULL.
  + xdg_shell: skip configure in request_fullscreen handler if unmapped.

* Fri Dec 12 2025 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt2
- Upstream fixes:
  + Add support for wlr-foreign-toplevel-management
  + xwayland: remove associate/dissociate listeners

* Sat Oct 04 2025 Anton Midyukov <antohami@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Wed Jul 30 2025 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt3.2e593fe5.1
- New snapshot.

* Thu Oct 10 2024 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt2
- Add dependency on seatd

* Sun Oct 06 2024 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- New version 0.2.

* Mon Feb 26 2024 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt2.20240216
- New snapshot for build wlroots 0.17

* Thu Aug 03 2023 Anton Midyukov <antohami@altlinux.org> 0.1.5-alt1
- New version 0.1.5

* Tue May 16 2023 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1.20230107
- Initial build for Sisyphus
