%def_disable snapshot
%define ver_major 0.5
%define rdn_name io.github.kaii_lb.Overskride

%def_disable bootstrap
%def_disable check

Name: overskride
Version: %ver_major.6
Release: alt1

Summary: A simple but powerful bluetooth app
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/kaii-lb/overskride

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/kaii-lb/overskride.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10
%define adwaita_ver 1.4

Requires: bluez obexd

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: typelib(Adw)
BuildRequires: pkgconfig(dbus-1)

%description
A Bluetooth and Obex client that is straight to the point, DE/WM
agnostic, and beautiful.

The main features are:
- Dynamically enumerate and list all devices known/in range
- Authenticating with devices (aka passkey confirmation)
- Sending/receiving files - Multiple adapter support
- Audio Profile support
- Sorting devices by RSSI (signal strength)
- Battery polling over Bluetooth (enable experimental Bluetooth options)
- Distance approximation
- ...and many more

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
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- first build for Sisyphus


