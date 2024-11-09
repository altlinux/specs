%define APP_ID org.gnome.design.AppIconPreview
%def_enable check

Name: app-icon-preview
Version: 3.4.0
Release: alt1

Summary: Tool for designing applications icons
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/app-icon-preview
Vcs: https://gitlab.gnome.org/World/design/app-icon-preview
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0) >= 2.66
BuildRequires: pkgconfig(gio-2.0) >= 2.66
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gtk4) >= 4.0.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.5.beta
BuildRequires: pkgconfig(libxml-2.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
App Icon Preview is a tool for designing icons which target the GNOME desktop.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/icons/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%{APP_ID}.metainfo.xml

%changelog
* Fri Nov 08 2024 Oleg Shchavelev <oleg@altlinux.org> 3.4.0-alt1
- Initial build
