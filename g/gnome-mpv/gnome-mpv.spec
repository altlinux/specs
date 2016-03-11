Name: gnome-mpv
Version: 0.7
Release: alt2

Summary: GNOME MPV is a simple GTK+ frontend for mpv
License: GPLv3
Group: Video

Url: https://github.com/gnome-mpv/gnome-mpv.git
Source: %name-%version.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildRequires: libappstream-glib-devel
BuildRequires: gcc5
BuildRequires: autoconf-archive
BuildRequires: intltool
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

%build
./autogen.sh
%make_build

%install
%makeinstall

%files
%doc COPYING README.md
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Fri Mar 11 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7-alt2
- initial build for ALT Linux Sisyphus

