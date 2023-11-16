%def_enable snapshot
%define optflags_lto %nil

%define _name Mousai
%define ver_major 0.7
%define rdn_name io.github.seadve.Mousai

%def_disable bootstrap
%def_disable check

Name: mousai
Version: %ver_major.5
Release: alt1

Summary: Identify songs in seconds
License: GPL-3.0
Group: Sound
Url: https://apps.gnome.org/Mousai

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/SeaDve/Mousai.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.66
%define gtk_ver 4.12
%define adwaita_ver 1.4
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-player-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(dbus-1)

%description
Mousai is a simple application that can recognize songs similar to
Shazam. Just click the listen button, and then wait a few seconds. It
will magically return the title and artist of that song.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- first build for Sisyphus (v0.7.5-134-gd53fb71)


