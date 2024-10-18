%def_enable snapshot

%define ver_major 4.0
%define rdn_name de.haeckerfelix.Shortwave

%define optflags_lto %nil

%def_disable bootstrap

Name: shortwave
Version: %ver_major.0
Release: alt1

Summary: Shortwave is an internet radio player
License: GPL-3.0-or-later
Group: Sound
Url: https://gitlab.gnome.org/World/Shortwave

Vcs: https://gitlab.gnome.org/World/Shortwave.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.16
%define adwaita_ver 1.6
%define shumate_ver 1.3

Requires: gst-plugins-base1.0
Requires: gst-plugins-bad1.0
Requires: yelp
# since 4.0.0
Requires: glycin-loaders

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo git
BuildRequires: yelp-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(shumate-1.0) >= %shumate_ver
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-bad-audio-1.0)
# for glycin
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libseccomp)

%description
Shortwave is an internet radio player that provides access to a station
database with over 30,000 stations.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Fri Oct 18 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- updated to 4.0.0-2-g80528e7

* Tue Jul 04 2023 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- first build for Sisyphus (3.2.0-41-g70fb09f)


