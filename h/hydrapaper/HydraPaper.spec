%define nameL org.gabmus.hydrapaper

Name: hydrapaper
Version: 3.3.2
Release: alt1

Summary:  Wallpaper manager with multimonitor support for GNOME
License: GPL-3.0-only
Group: Other

Url: https://gitlab.com/gabmus/HydraPaper
Vcs: https://gitlab.com/gabmus/HydraPaper

Source: %name-%version.tar

Requires: python3-module-%name = %EVR

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: meson cmake pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4) pkgconfig(dbus-1)
BuildRequires: pkgconfig(libadwaita-1) typelib(Adw)
BuildRequires: blueprint-compiler

BuildArch: noarch

%description
A Gtk utility to set two different backgrounds for each monitor
on GNOME (which lacks this feature).

%package -n python3-module-%name
Group: Development/Python3
Summary: Python3 module for HydraPaper

%description -n python3-module-%name
Python3 module for HydraPaper

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_datadir/dbus-1/services/%nameL.service
%_datadir/glib-2.0/schemas/%nameL.gschema.xml
%_datadir/%name/%nameL.gresource
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/metainfo/%nameL.appdata.xml
%doc *.md LICENSE

%files -n python3-module-%name
%_libexecdir/python3/site-packages/%name/

%changelog
* Mon May 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.3.2-alt1
- Initial build for ALT Linux.
