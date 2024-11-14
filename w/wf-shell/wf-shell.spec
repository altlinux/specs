# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wf-shell
Summary: GTK3-based panel for wayfire
Version: 0.9.0
Release: alt1
Group: Graphical desktop/Other
License: MIT
Url: https://github.com/WayfireWM/wf-shell

Source: %name-%version.tar
# Source1-url: https://github.com/GNOME/libgnome-volume-control
Source1: gvc.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libglm-devel
BuildRequires: meson >= 0.51.0
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(gtk-layer-shell-0) >= 0.6
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.24
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(wayfire)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wf-config) >= 0.8.0

Requires: wayland-logout
Requires: hicolor-icon-theme

%description
wf-shell is a repository which contains the various components needed to built a
fully functional DE based around wayfire. Currently it has only a GTK-based
panel and background client.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup
%patch -p1
tar -xvf %SOURCE1 -C subprojects/

%build
%meson \
    -Dwayland-logout=false
%meson_build

%install
%meson_install

%files
%doc LICENSE
%doc README.md %name.ini.example
%_bindir/wf-background
%_bindir/wf-dock
%_bindir/wf-panel
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/wayfire/

%files devel
%_pkgconfigdir/*.pc

%changelog
* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- initial build
