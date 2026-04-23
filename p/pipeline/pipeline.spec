%def_disable snapshot

%define _name pipeline
%define binary_name tubefeeder
%define ver_major 4.0
%define rdn_name de.schmidhuberj.%binary_name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Follow your favorite video creators
License: GPL-3.0-or-later
Group: Video
Url: https://gitlab.com/schmiddi-on-mobile/pipeline

Vcs: https://gitlab.com/schmiddi-on-mobile/pipeline.git

%if_disabled snapshot
Source: https://gitlab.com/schmiddi-on-mobile/%name/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.0
%define clapper_api_ver 0.0
%define clapper_ver 0.10

Requires: yt-dlp

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(clapper-gtk-%clapper_api_ver) >= %clapper_ver
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(openssl)
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Features:
- Search for you favorite channels and subscribe to them.
- Aggregate videos from all subscriptions into a single feed
- Filter out unwanted items from the feed, like short videos or videos from a series.
- Play those videos either in the built-in video player or with any other video player of your choice.
- Download videos for offline viewing.
- Manage videos you want to watch later.
- Import subscriptions from https://github.com/TeamNewPipe/NewPipe/ or YouTube
- Multiple platforms:
    - YouTube (using Piped as the backend to prevent throttling)
    - PeerTube
    - suggest any other platform with a good API and it will be considered

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %binary_name

%check
%__meson_test

%files -f %binary_name.lang
%_bindir/%binary_name
%_datadir/%binary_name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
#%_datadir/dbus-1/services/%rdn_name.service
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README.*

%changelog
* Thu Apr 23 2026 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Thu Feb 26 2026 Yuri N. Sedunov <aris@altlinux.org> 3.2.4-alt1
- 3.2.4

* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Thu Feb 05 2026 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- first build for Sisyphus


