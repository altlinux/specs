%def_enable snapshot
%define optflags_lto %nil

%define ver_major 0.5
%define rdn_name com.rafaelmardojai.SharePreview

%def_disable bootstrap
%def_enable check

Name: share-preview
Version: %ver_major.0
Release: alt1

Summary: Share Preview
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://apps.gnome.org/SharePreview

Vcs: https://github.com/rafaelmardojai/share-preview.git

%if_disabled snapshot
Source: https://github.com/rafaelmardojai/share-preview/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.10
%define adwaita_ver 1.4

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libcurl)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Preview and debug websites metadata tags for social media share.

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
* Sat May 18 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- updated to 0.5.0-9-g66a8aa4

* Fri Dec 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- first build for Sisyphus (0.4.0-14-g37de45a)


