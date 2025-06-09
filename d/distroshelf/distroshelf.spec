%define _unpackaged_files_terminate_build 1
%define app_id com.ranfdev.DistroShelf

Name: distroshelf
Version: 1.0.8
Release: alt1

Summary: Selected terminal emulator
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://github.com/ranfdev/DistroShelf
Vcs: https://github.com/ranfdev/DistroShelf
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio
BuildRequires: rust-cargo
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

Requires: distrobox

%description
The terminal emulator selected by the user.

%prep
%setup -a 1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%changelog
* Mon Jun 09 2025 David Sultaniiazov <x1z53@altlinux.org> 1.0.8-alt1
- Initial build
