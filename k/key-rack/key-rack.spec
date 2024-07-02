%def_enable snapshot

%define _name KeyRack
%define ver_major 0.4
%define rdn_name app.drey.%_name

%def_disable bootstrap

Name: key-rack
Version: %ver_major.0
Release: alt1

Summary: Key Rack
License: GPL-3.0
Group: Security/Networking
Url: https://gitlab.gnome.org/sophie-h/key-rack

Vcs: https://gitlab.gnome.org/sophie-h/key-rack.git

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.66
%define gtk_ver 4.6
%define adw_ver 1.3

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Key Rack allows to view and edit keys, like passwords or tokens, stored
by apps. It supports Flatpak secrets as well as system wide secrets.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version %{?_disable_bootstrap:-a1}
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
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- updated to 0.4.0-2-g0fbde30

* Sun Jan 14 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus (0.2.0-30-g696fdf7)


