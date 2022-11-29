%def_enable snapshot
%define _name dialect
%define ver_major 2.1
%define rdn_name app.drey.Dialect

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: A translation app for GNOME
License: GPL-3.0-or-later
Group: Text tools
Url: https://github.com/dialect-app/dialect

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/dialect-app/dialect.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define gi_ver 1.35
%define gst_ver 1.18
%define gtk4_ver 4.6
%define adw_ver 1.0
%define pygobject_ver 3.40

Requires: typelib(Gtk) = 4.0 typelib(Soup) = 3.0
Requires: libgtk4-gir >= %gtk4_ver
Requires: libgst-plugins1.0-gir >= %gst_ver
Requires: python3(gtts)

%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %gi_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libadwaita-gir-devel
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(pygobject-3.0) >= %pygobject_ver


%description
Features:
Translation based on Google Translate
Translation based on the LibreTranslate API, allowing you to use any public instance
Translation history
Automatic language detection
Text to speech
Clipboard buttons

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*


%changelog
* Thu Nov 29 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus (2.1.1-7-g29dcb52)


