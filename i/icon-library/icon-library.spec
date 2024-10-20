%define APP_ID org.gnome.design.IconLibrary
%def_enable check

Name: icon-library
Version: 0.0.19
Release: alt1

Summary: Symbolic icons for your apps
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/icon-library
Vcs: https://gitlab.gnome.org/World/design/icon-library
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Find the right icon to use on your GNOME application.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.SearchProvider.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/gnome-shell/search-providers/%APP_ID.search-provider.ini
%_datadir/%name
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sun Oct 20 2024 Oleg Shchavelev <oleg@altlinux.org> 0.0.19-alt1
- Initial build
