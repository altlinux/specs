%def_disable snapshot
%define _name sysd-manager
%define ver_major 1.3
%define rdn_name io.github.plrigaux.%name

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: A GUI to manage systemd units
License: GPL-3.0
Group: System/Configuration/Boot and Init
Url: https://github.com/plrigaux/sysd-manager

Vcs: https://github.com/plrigaux/sysd-manager.git

%if_disabled snapshot
Source: https://github.com/plrigaux/sysd-manager/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adw_ver 1.6

Requires: dconf polkit

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Manage your Services, Timers, Sockets and other units. You can enable,
disable, stop and start them. Also, you can view their config file
and peak at their journal logs.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install
install -v -Dm644 data/applications/%rdn_name.desktop \
    -t %buildroot%_datadir/applications
install -v -Dm644 data/icons/hicolor/scalable/apps/%rdn_name.svg \
    -t %buildroot%_iconsdir/hicolor/scalable/apps
install -v -Dm644 data/schemas/%rdn_name.gschema.xml \
    -t %buildroot%_datadir/glib-2.0/schemas
install -v -Dm644 data/metainfo/%rdn_name.metainfo.xml \
    -t %buildroot%_datadir/metainfo

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Nov 29 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Nov 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Nov 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus

