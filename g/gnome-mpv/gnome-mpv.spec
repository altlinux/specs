%define xdg_name io.github.GnomeMpv

Name: gnome-mpv
Version: 0.13
Release: alt1

Summary: GNOME MPV is a simple GTK+ frontend for mpv
License: GPLv3
Group: Video

Url: https://github.com/gnome-mpv/gnome-mpv.git
Source: %name-%version.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>
Patch1: %name-%version-alt-update-appdata-and-add-missing-meson-file.patch

BuildRequires: libappstream-glib-devel
BuildRequires: meson
BuildRequires: python-dev
BuildRequires: glib2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libmpv-devel
BuildRequires: libepoxy-devel

%description
GNOME MPV interacts with mpv via the client API exported by libmpv,
allowing access to mpv's powerful playback capabilities.

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_datadir/appdata/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/dbus-1/services/%xdg_name.service
%_man1dir/*.1.*

%changelog
* Fri Dec 1 2017 Vladimir Didenko <cow@altlinux.org> 0.13-alt1
- new version

* Fri Jul 28 2017 Vladimir Didenko <cow@altlinux.org> 0.12-alt1
- new version
- switch to meson build

* Fri Mar 11 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7-alt2
- initial build for ALT Linux Sisyphus
