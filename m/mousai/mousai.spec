%def_enable snapshot
%define optflags_lto %nil

%define _name Mousai
%define ver_major 0.7
%define rdn_name io.github.seadve.Mousai

%def_disable bootstrap
#cargo test failed
%def_disable check

Name: mousai
Version: %ver_major.8
Release: alt1

Summary: Identify songs in seconds
License: GPL-3.0
Group: Sound
Url: https://apps.gnome.org/Mousai

Vcs: https://github.com/SeaDve/Mousai.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.66
%define gtk_ver 4.16
%define adwaita_ver 1.6
%define gst_ver 1.22

Requires: gst-plugins-base1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
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
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}

%description
Mousai is a simple application that can recognize songs similar to
Shazam. Just click the listen button, and then wait a few seconds. It
will magically return the title and artist of that song.

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
* Wed Sep 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- 0.7.8

* Sun Mar 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- 0.7.7

* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6

* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- first build for Sisyphus (v0.7.5-134-gd53fb71)


