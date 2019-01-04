Name: tootle
Version: 0.2.0
Release: alt1

Summary: Simple Mastodon client

License: GPL-3.0-or-later
Group: Networking/Instant messaging
Url: https://github.com/bleakgrey/tootle

# Source-url:         https://github.com/bleakgrey/tootle/archive/%version.tar.gz#/%name-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

#BuildRequires: hicolor-icon-theme
BuildRequires: meson >= 0.40.0
BuildRequires: pkg-config
#BuildRequires: update-desktop-files
BuildRequires: vala
BuildRequires: pkgconfig(glib-2.0) >= 2.30.0
BuildRequires: libgranite-vala
BuildRequires: pkgconfig(granite) >= 0.5
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-2.4)
#Recommends:     %name-lang

%description
Simple Mastodon client with real-time notifications and multiple accounts
support.

#lang_package

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output %name.lang com.github.bleakgrey.tootle

%files -f %name.lang
%doc LICENSE
%doc README.md
%_bindir/com.github.bleakgrey.tootle
%_desktopdir/com.github.bleakgrey.tootle.desktop
%_datadir/glib-2.0/schemas/com.github.bleakgrey.tootle.gschema.xml
%_iconsdir/hicolor/*/apps/com.github.bleakgrey.tootle.??g
%_datadir/metainfo/com.github.bleakgrey.tootle.appdata.xml

%changelog
* Fri Jan 04 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus

