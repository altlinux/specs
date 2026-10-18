%define _unpackaged_files_terminate_build 1

%define appname io.elementary.appcenter

%def_with check

Name: elementary-appcenter
Version: 8.4.0
Release: alt1

Summary: Application store for elementary OS
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/appcenter

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(appstream)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: /usr/bin/sassc
BuildRequires: pkgconfig(appstream-compose)
BuildRequires: appstream
BuildRequires: libappstream-devel
BuildRequires: libappstream-gir
BuildRequires: libappstream-compose-gir
BuildRequires: libappstream-glib-gir
BuildRequires: libappstream-glib-gir-devel

Requires: flatpak
Requires: xdg-desktop-portal

%description
Install, update and remove apps with ease.
Helps independent developers.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %appname.lang
%dir %_sysconfdir/%appname
%_sysconfdir/%appname/appcenter.hiddenapps
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/dbus-1/services/%{appname}.service
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/gnome-shell/search-providers/%{appname}.search-provider.ini
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/io.elementary.appcenter.mo

%changelog
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 8.4.0-alt1
- Initial build for Sisyphus
