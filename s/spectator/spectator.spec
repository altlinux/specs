%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.treagod.spectator

Name: spectator
Version: 0.6.3
Release: alt1

Summary: Client to test web endpoints
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/treagod/spectator

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(duktape)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: vapi(granite)

%description
Spectator is a native application written in Vala using GTK.
It's enables you to test the API endpoints of your HTTP server.

Features:

* Do requests to a web server
* Handle Basic Proxy Server
* Scripting capabilities
* Create collections of requests
* Create request enviroments

%prep
%setup
sed -i 's|^Categories=.*|Categories=GTK;Development;WebDevelopment;|' data/com.github.treagod.spectator.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_iconsdir/hicolor/*/mimetypes/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
