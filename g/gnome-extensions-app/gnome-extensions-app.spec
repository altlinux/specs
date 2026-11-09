%define _unpackaged_files_terminate_build 1
%define app_id org.gnome.Extensions

%def_enable check

Name: gnome-extensions-app
Version: 51.alpha
Release: alt1
Summary: Manage GNOME Shell Extensions
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
Url: https://gitlab.gnome.org/GNOME/gnome-extensions-app
Vcs: https://gitlab.gnome.org/GNOME/gnome-extensions-app

Source0: %name-%version.tar
Source1: libshew.tar

Requires: typelib(Adw)

BuildRequires: meson
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk4-gir-devel
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
GNOME Extensions is a small app for managing GNOME Shell
extensions. It is usually built as part of gnome-shell, but can be
used as a stand-alone project as well.

%prep
%setup -q -n %name-%version -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%doc COPYING
%_bindir/%name
%_libdir/%name/libshew-0.so
%_libdir/%name/girepository-1.0/Shew-0.typelib
%_datadir/%name/%app_id
%_datadir/%name/%app_id.*.gresource
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/icons/hicolor/*/apps/%{app_id}*.*

%changelog
* Thu Nov 05 2026 Vladislav Petrukhin <vladp@altlinux.org> 51.alpha-alt1
- Initial build.

