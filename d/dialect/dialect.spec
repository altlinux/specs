%def_enable snapshot
%define _name dialect
%define ver_major 2.4
%define rdn_name app.drey.Dialect

%def_enable check

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: A translation app for GNOME
License: GPL-3.0-or-later
Group: Text tools
Url: https://dialectapp.org

%if_disabled snapshot
Source: https://github.com/dialect-app/dialect/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/dialect-app/dialect.git
# AHTUNG: updated https://github.com/dialect-app/po required
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.10
%define gi_ver 1.35
%define gst_ver 1.18
%define gtk4_ver 4.6
%define adw_ver 1.5
%define pygobject_ver 3.40

Requires: typelib(Gtk) = 4.0 typelib(Soup) = 3.0
Requires: libgtk4-gir >= %gtk4_ver
Requires: libgst-plugins1.0-gir >= %gst_ver
Requires: python3(gtts)

%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver
BuildRequires: yelp-tools
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %gi_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libadwaita-gir-devel
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(pygobject-3.0) >= %pygobject_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Features:
- Translation based on Google Translate
- Translation based on the LibreTranslate API, allowing you to use any public instance
- Translation based on Lingva Translate API
- Translation based on Bing
- Translation based on Yandex
- Translation history
- Automatic language detection
- Text to speech
- Clipboard buttons

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang  %_name %_name-cldr-langs

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README* NEWS*


%changelog
* Mon Jul 29 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Jun 03 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Thu Apr 04 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Dec 09 2023 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt2
- updated to 2.2.0-21-gac86491
- updated translations from https://github.com/dialect-app/po

* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0-5-g478c4a4

* Tue Nov 29 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- first build for Sisyphus (2.1.1-7-g29dcb52)


