%def_disable snapshot

%define ver_major 0.10
%define rdn_name org.freedesktop.Bustle

%def_disable check
%def_disable bootstrap

Name: bustle
Version: %ver_major.0
Release: alt1

Summary: D-Bus activity visualiser
License: LGPL-2.1
Group: Development/Debug
Url: https://gitlab.gnome.org/World/bustle

Vcs: https://gitlab.gnome.org/World/bustle.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/bustle/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adw_ver 1.6

# /usr/bin/dbus-monitor
Requires: dbus-tools

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: dbus-tools /usr/bin/appstreamcli desktop-file-utils clippy}

%description
Bustle draws sequence diagrams of D-Bus activity, showing signal
emissions, method calls and their corresponding returns, with timestamps
for each individual event and the duration of each method call. This can
help you check for unwanted D-Bus traffic, and pinpoint why your
D-Bus-based application isn't performing as well as you like. It also
provides statistics like signal frequencies and average method call
times.

%prep
%setup %{?_disable_bootstrap:-a1}
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
dbus-run-session %__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Sep 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0 (new homepage, ported to Rust/Libadwaita/Meson)

* Fri Sep 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4 (new url)

* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 0.4.3-alt1
- 0.4.3

* Wed Sep 04 2013 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1
- build for Sisyphus

