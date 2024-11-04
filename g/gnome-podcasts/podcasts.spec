%define APP_ID org.gnome.Podcasts

Name: gnome-podcasts
Version: 0.7.1
Release: alt1

Summary: Listen to your favorite shows
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://apps.gnome.org/Podcasts
Vcs: https://gitlab.gnome.org/World/podcasts
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-play-1.0)

%description
Play, update, and manage your podcasts from a lightweight interface that
seamlessly integrates with GNOME. Podcasts can play various audio formats and
remember where you stopped listening. You can subscribe to shows via RSS/Atom,
iTunes, and Soundcloud links. Subscriptions from other apps can be imported via
OPML files.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.appdata.xml

%changelog
* Mon Nov 04 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.1-alt1
- Initial build
