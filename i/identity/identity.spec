%def_enable snapshot
%define optflags_lto %nil

%define _name identity
%define ver_major 26.03
%define xdg_name org.gnome.gitlab.YaLTeR.Identity

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major
Release: alt1

Summary: Compare images and videos
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Identity

Vcs: https://gitlab.gnome.org/YaLTeR/identity.git

Source: %_name-%version.tar
Source1: %_name-%version-cargo.tar

%define gtk_ver 4.20
%define adwaita_ver 1.8.0
%define gst_api_ver 1.0
%define gst_ver 1.24
%define dav1d_ver 1.0.0
%define webp_ver 0.5
%define glycin_api_ver 2
%define glycin_ver 2.0

Requires: glycin-%glycin_api_ver-loaders >= %glycin_ver
Requires: gst-plugins-base%gst_api_ver >= %gst_ver
Requires: gst-plugin-gtk4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo gcc-c++ blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-video-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(dav1d) >= %dav1d_ver
BuildRequires: pkgconfig(libwebpdemux) >= %webp_ver
BuildRequires: pkgconfig(glycin-gtk4-%glycin_api_ver) >= %glycin_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Identity is program for comparing multiple versions of an image or video.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*

%changelog
* Tue Mar 31 2026 Yuri N. Sedunov <aris@altlinux.org> 26.03-alt1
- v26.03-2-g59a681f

* Wed Oct 29 2025 Yuri N. Sedunov <aris@altlinux.org> 25.10.1-alt1
- 25.10.1

* Tue Oct 28 2025 Yuri N. Sedunov <aris@altlinux.org> 25.10-alt1
- 25.10

* Mon Mar 31 2025 Yuri N. Sedunov <aris@altlinux.org> 25.03-alt1
- 25.03

* Wed Oct 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus (v0.6.0-5-gead645e)

