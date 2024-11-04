%define optflags_lto %nil
%define APP_ID de.schmidhuberj.DieBahn
%def_enable check

Name: diebahn
Version: 2.7.1
Release: alt1

Summary: Find all your travel information
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://mobile.schmidhuberj.de/railway
Vcs: https://gitlab.com/schmiddi-on-mobile/railway
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59
BuildRequires: rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(glib-2.0) >= 2.66
BuildRequires: pkgconfig(gio-2.0) >= 2.66
BuildRequires: pkgconfig(gtk4) >= 4.0.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.6.0
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Railway lets you look up travel information across networks and borders
without having to navigate through different websites. Due to the adaptive
design, it is suitable to plan your trip in advance or mobile on the go:

* View your trips details including platforms and delays
* Bookmark current and future trips as well as frequent search
* Make use of advance search options like filtering by mode of transport

And all that for networks from all around the world, but mostly from Europe.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

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
%_desktopdir/%APP_ID.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Mon Nov 04 2024 Oleg Shchavelev <oleg@altlinux.org> 2.7.1-alt1
- Initial build
