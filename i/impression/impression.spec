%def_enable snapshot
%define ver_major 3.0
%define rdn_name io.gitlab.adhami3310.Impression

%def_disable bootstrap
%def_disable check

Name: impression
Version: %ver_major
Release: alt1

Summary: Impression is a tool to create bootable drives
License: GPL-3.0
Group: System/Configuration/Other
Url: https://gitlab.com/adhami3310/Impression

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.com/adhami3310/Impression.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10
%define adwaita_ver 1.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)

%description
A tool to write images to portable drives like flash drives or memory
cards.

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
#%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc PRESS* README*


%changelog
* Mon Nov 06 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Mon Sep 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- first build for Sisyphus (v2.1-15-g8840b25)


