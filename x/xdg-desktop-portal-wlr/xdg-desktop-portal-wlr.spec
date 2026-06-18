%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define ver_major 0.8

%def_enable check

Name: xdg-desktop-portal-wlr
Version: %ver_major.3
Release: alt1

Summary: xdg-desktop-portal backend for wlroots
Group: Graphical desktop/Other
License: MIT
Url: https://github.com/emersion/xdg-desktop-portal-wlr

Vcs: https://github.com/emersion/xdg-desktop-portal-wlr.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define xdg_desktop_portal_ver 1.15.0

BuildRequires(pre): rpm-macros-meson rpm-build-systemd rpm-build-xdg
BuildRequires: meson
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.64
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
XDG Desktop Portal implementation for wlroots.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %buildroot/%_xdgconfigdir/%name
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%dir %_xdgconfigdir/%name
%_libexecdir/%name
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.wlr.service
%_datadir/xdg-desktop-portal/portals/wlr.portal
%_userunitdir/%name.service
%_man5dir/%name.5*
%doc README*


%changelog
* Thu Jun 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Fri Apr 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Dec 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Wed Oct 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Tue Jan 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- updated to v0.7.1-3-g1eae4bf

* Mon Aug 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1.1
- /etc/xdg/xdg-desktop-portal-wlr directory owned by package

* Mon Jul 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- first build for Sisyphus (v0.7.0-1-gf17582b)

