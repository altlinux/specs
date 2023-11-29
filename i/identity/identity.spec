%def_enable snapshot
%define optflags_lto %nil

%define _name identity
%define ver_major 0.6
%define xdg_name org.gnome.gitlab.YaLTeR.Identity

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Compare images and videos
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Identity

Vcs: https://gitlab.gnome.org/YaLTeR/identity.git
Source: %_name-%version.tar
Source1: %_name-%version-cargo.tar

%define gtk_ver 4.12
%define adwaita_ver 1.4.0
%define gst_api_ver 1.0
%define gst_ver 1.20
%define dav1d_ver 1.0.0
%define webp_ver 0.5

Requires: gst-plugins-base%gst_api_ver >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo gcc-c++ blueprint-compiler
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-video-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(dav1d) >= %dav1d_ver
BuildRequires: pkgconfig(libwebpdemux) >= %webp_ver

%description
Identity is program for comparing multiple versions of an image or video.

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
%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus (v0.6.0-5-gead645e)

