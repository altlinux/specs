%def_enable snapshot
%define optflags_lto %nil

%define _name health
%define ver_major 0.95
%define rdn_name dev.Cogitri.Health

%def_disable bootstrap
%def_disable check

Name: gnome-%_name
Version: %ver_major.0
Release: alt1

Summary: GNOME Health
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Health

%if_disabled snapshot
Source: %url/-/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Health.git
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

# [ppc64le]    Compiling rand_chacha v0.3.1
# [ppc64le] error: failed to run custom build command for `ring v0.16.20`
ExcludeArch: ppc64le

%define glib_ver 2.76
%define gtk_ver 4.6
%define adwaita_ver 1.0.1
%define tracker_ver 3.1

Requires: dconf gnome-keyring
Requires: tracker3 tracker3-miners >= %tracker_ver
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(tracker-sparql-3.0) >= %tracker_ver
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}

%description
A health tracking app for the GNOME desktop.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %rdn_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_desktopdir/%rdn_name.Autostart.desktop
%_datadir/%rdn_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Tue Dec 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.95.0-alt1
- first build for Sisyphus (0.95.0-16-g99f49a1)


