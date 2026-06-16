%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mangowc
Version: 0.14.4
Release: alt1

Summary: wayland compositor base wlroots and scenefx (dwm but wayland)
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/DreamMaoMao/mangowc

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: /usr/bin/wayland-scanner
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots-0.19)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(scenefx-0.4)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libcjson)

# Defined in config.conf
Requires: /usr/bin/rofi
Requires: /usr/bin/foot

%description
MangoWC is a lightweight, high-performance Wayland compositor built on dwl,
designed for speed, flexibility, and a modern, customizable desktop experience.

For configuration hints see %_datadir/doc/%name-%version/README.md and
https://github.com/DreamMaoMao/mangowc/wiki .

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%doc LICENSE
%doc LICENSE.wlroots
%doc LICENSE.tinywl
%doc LICENSE.sway
%doc LICENSE.dwm
%doc LICENSE.dwl
%dir %_sysconfdir/mango
%config(noreplace) %_sysconfdir/mango/config.conf
%_bindir/mango
%_bindir/mmsg
%_man1dir/mmsg.1.*
%_datadir/wayland-sessions/mango.desktop
%_datadir/xdg-desktop-portal/mango-portals.conf

%changelog
* Tue Jun 16 2026 Nikolay Strelkov <snk@altlinux.org> 0.14.4-alt1
- New version 0.14.4.

* Sun Jun 07 2026 Nikolay Strelkov <snk@altlinux.org> 0.14.2-alt1
- New version 0.14.2.

* Sat Jun 06 2026 Nikolay Strelkov <snk@altlinux.org> 0.14.1-alt1
- New version 0.14.1.

* Sat May 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.14.0-alt1
- New version 0.14.0.

* Tue May 19 2026 Nikolay Strelkov <snk@altlinux.org> 0.13.1-alt1
- New version 0.13.1.

* Fri May 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.13.0-alt1
- New version 0.13.0.

* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.9-alt1
- New version 0.12.9.

* Sun Mar 29 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.8-alt1
- New version 0.12.8.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.7-alt1
- New version 0.12.7.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.6-alt1
- New version 0.12.6.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.5-alt1
- New version 0.12.5.

* Thu Feb 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.4-alt1
- New version 0.12.4.

* Fri Feb 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.3-alt1
- New version 0.12.3.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.2-alt1
- New version 0.12.2.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.12.0-alt1
- New version 0.12.0.

* Thu Jan 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.11.0-alt1
- New version 0.11.0.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 0.10.10-alt1
- New version 0.10.10.

* Wed Dec 31 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.9-alt1
- New version 0.10.9.

* Sun Dec 21 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.8-alt1
- Initial build for Sisyphus
