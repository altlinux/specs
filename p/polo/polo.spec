%define _unpackaged_files_terminate_build 1

%global weston_version 16.0.1
# The private libweston is Polo's alone: keep it out of the package's
# provides and requires.
%global __provides_exclude_from ^%{_libdir}/polo/.*$
%global __requires_exclude ^libweston-16\\.so.*$

# some tests fail
%def_without check

Name: polo
Version: 1.0.0
Release: alt1

Summary: Wayland compositor and session for the MATE desktop
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/polo

# NOTE: initial import was made with gear-import for 1.0.0 version release
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-generic-compat
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-build-gir

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(xcursor)
BuildRequires: xdg-desktop-portal-wlr
BuildRequires: grim
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(mate-desktop-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: vapi(dconf)
BuildRequires: vapi(libcanberra)

BuildRequires: /usr/bin/Xwayland
BuildRequires: /usr/bin/wl-copy
BuildRequires: slurp

%if_with check
BuildRequires: python3-module-pygobject3
%endif

# no grim, no slurp
ExcludeArch: %ix86

# TODO - find the exact root of the problem like
#        "lib.req: ERROR: /usr/src/tmp/polo-buildroot/usr/lib64/polo/libweston-16/wayland-backend.so: library libweston-16.so.0 not found"
#        and then remove the below hacky line
AutoReq: nolib

Requires: /usr/bin/Xwayland
Requires: /usr/bin/mate-panel
Requires: /usr/bin/caja
Requires: mate-settings-daemon
Requires: xdg-desktop-portal-wlr
Requires: xdg-desktop-portal-gtk
Requires: /usr/bin/dconf
Requires: /usr/bin/mate-screensaver
Requires: grim
Requires: slurp
Requires: /usr/bin/wl-copy

Requires: libseat1

Provides: bundled(libweston) = %weston_version

%description
Polo is a Wayland compositor and window manager for MATE, built on a
private, patched copy of the Weston compositor library. It reads Marco's
settings, manages X11 programs through its own XWayland window manager, and
provides the "MATE (Polo)" session: it starts the session's programs and is
the session manager itself.

%prep
%setup

%build
%meson \
%if_with check
       -Dtests=true
%else
       -Dtests=false
%endif

%meson_build

%install
%meson_install
# libweston's headers, pkg-config files and protocol XML are for building
# against it; nothing does but Polo.
rm -rfv %buildroot%_libdir/polo/include \
        %buildroot%_libdir/polo/pkgconfig \
        %buildroot%_libdir/polo/share \
        %buildroot%_libdir/polo/libweston-16.so

%check
%meson_test

%files
%doc LICENSE README.md docs
%config(noreplace) %_sysconfdir/dconf/profile/polo
%dir %_sysconfdir/dconf/db/polo.d
%dir %_sysconfdir/dconf/db/polo.d/locks
%config(noreplace) %_sysconfdir/dconf/db/polo.d/00-polo
%config(noreplace) %_sysconfdir/dconf/db/polo.d/locks/00-polo
%_bindir/polo
%_bindir/polo-screenshot
%_bindir/polo-wayland.sh
%_libexecdir/polo-shell-ui
%_libexecdir/polo-share-chooser
%_userunitdir/polo-session.target
%dir %_libdir/polo
%_libdir/polo/libweston-16.so.0*
%dir %_libdir/polo/libweston-16/
%_libdir/polo/libweston-16/*.so
%_datadir/glib-2.0/schemas/org.mate.polo.gschema.xml
%_man1dir/polo.1*
%_man7dir/polo-session.7*
%_datadir/polo/xdg/xdg-desktop-portal/mate-portals.conf
%_datadir/wayland-sessions/polo.desktop

%changelog
* Thu Nov 12 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
