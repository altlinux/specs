%def_enable snapshot
%define optflags_lto %nil

%define ver_major 4.5
%define rdn_name com.belmoussaoui.Authenticator

%def_enable check
%def_disable bootstrap

Name: authenticator
Version: %ver_major.0
Release: alt1

Summary: Generate Two-Factor Codes
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://apps.gnome.org/Authenticator

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Authenticator/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Authenticator.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.6
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(zbar)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}

%description
Simple application for generating Two-Factor Authentication Codes.

Features:
* Time-based/Counter-based/Steam methods support
* SHA-1/SHA-256/SHA-512 algorithms support
* QR code scanner using a camera or from a screenshot
* Lock the application with a password
* Beautiful UI
* GNOME Shell search provider
* Backup/Restore from/into known applications like FreeOTP+,
  Aegis (encrypted / plain-text), andOTP, Google Authenticator

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

# remove broken build.rs from zbar-rust (the same in decoder)
rm -f vendor/zbar-rust/build.rs
sed -i 's|"build.rs":"894b33392971ba9dad1dd4e45869478198f86e911e0b29f7e0d9fbf1342672c2",||' \
vendor/zbar-rust/.cargo-checksum.json

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test -t 2

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.search-provider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Sat Sep 7 2024 Yuri N. Sedunov <aris@altlinux.org> 4.5.0-alt1
- 4.5.0-4-g404131d

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt2
- updated to 4.4.0-46-gb8dbe84

* Wed Dec 27 2023 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- first build for Sisyphus (4.4.0-12-g1e99792)


