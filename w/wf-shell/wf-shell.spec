# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wf-shell
Summary: GTK4-based panel for wayfire
Version: 0.11.0
Release: alt1
Group: Graphical desktop/Other
License: MIT
URL: https://github.com/WayfireWM/wf-shell
VCS: https://github.com/WayfireWM/wf-shell.git

Source: %name-%version.tar
# Source1-url: https://github.com/GNOME/libgnome-volume-control
Source1: gvc.tar
# Source2-url: https://github.com/WayfireWM/wf-json
Source2: wf-json.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libglm-devel
BuildRequires: meson >= 0.51.0
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(wayfire) >= 0.11.0
BuildRequires: wayfire >= 0.11.0
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wf-config) >= 0.11.0
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(xkbregistry)
BuildRequires: pkgconfig(yyjson)
BuildRequires: libssl-devel
BuildRequires: libgbm-devel

Requires: wayfire >= 0.11.0
Requires: wayland-logout
Requires: hicolor-icon-theme

%description
wf-shell is a repository which contains the various components needed to built a
fully functional DE based around wayfire. Currently it has only a GTK-based
panel and background client.

%prep
%setup
%patch -p1
tar -xvf %SOURCE1 -C subprojects/
tar -xvf %SOURCE2 -C subprojects/

%build
%meson \
    -Dwayland-logout=false
%meson_build

%install
%meson_install

rm -v %buildroot%_libdir/pkgconfig/wf-shell.pc

%files
%doc LICENSE
%doc README.md %name.ini.example
%_bindir/wf-background
%_bindir/wf-dock
%_bindir/wf-locker
%_bindir/wf-locker-pin
%_bindir/wf-stream-chooser
%_bindir/wf-panel
%_desktopdir/wf-locker-pin.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/wf-shell/
%_sysconfdir/pam.d/wf-locker
%_sysconfdir/xdg/xdg-desktop-portal-wlr/wayfire

%changelog
* Sat Sep 05 2026 Anton Midyukov <antohami@altlinux.org> 0.11.0-alt1
- New version 0.11.0.
- Remove unused devel package.

* Fri Aug 29 2025 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- Initial build.
