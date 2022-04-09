Name: tootle
Version: 1.0
Release: alt3

Summary: Simple Mastodon client

License: GPL-3.0-or-later
Group: Networking/Instant messaging
Url: https://github.com/bleakgrey/tootle

# Source-url:         https://github.com/bleakgrey/tootle/archive/%version.tar.gz
Source: %name-%version.tar
Patch: fix-build-on-vala-46.patch
# https://github.com/bleakgrey/tootle/pull/322
Patch1: 858ee78fbebe161a4cdd707a469dc0f045211a51.patch
# https://github.com/bleakgrey/tootle/pull/339
Patch2: 0816105028c26965e37c9afc7c598854f3fecde1.patch
Patch3: Application-make-app_entries-private.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.50.0
BuildRequires: pkg-config cmake
BuildRequires: vala >= 0.48
BuildRequires: libgranite-vala

BuildRequires: pkgconfig(glib-2.0) >= 2.30.0
BuildRequires: pkgconfig(granite) >= 0.5
BuildRequires: pkgconfig(gtk4) >= 4.3.0
BuildRequires: pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires: pkgconfig(libsoup-2.4) >= 2.64
BuildRequires: pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.9.10
BuildRequires: pkgconfig(libhandy-1) >= 1.0.0

%description
Simple Mastodon client with real-time notifications and multiple accounts
support.

#lang_package

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%_iconsdir/hicolor/symbolic/apps/com.github.bleakgrey.tootle-symbolic.svg
%_datadir/metainfo/com.github.bleakgrey.tootle.appdata.xml

%changelog
* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- fix build with vala 0.56

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix build with vala 0.54.1

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt2
- fix build with vala 4.6

* Fri Jan 04 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus

