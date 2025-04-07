%def_enable snapshot
%define _name solanum
%define ver_major 6.0
%define xdg_name org.gnome.Solanum

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Pomodoro timer for GNOME Desktop
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/Solanum

Vcs: https://gitlab.gnome.org/World/Solanum.git

Source: %_name-%version.tar
Source1: %_name-%version-cargo.tar

%define gtk_ver 4.11.3
%define adwaita_ver 1.4.0
%define gst_api_ver 1.0
%define gst_ver 1.20

Requires: gst-plugins-base%gst_api_ver >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver typelib(Adw) = 1
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-player-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver) >= %gst_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Solanum is a pomodoro timer for the GNOME desktop. It keeps you on track,
with frequent short breaks, and a long break after sessions of
productivity.

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
* Mon Apr 07 2025 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- 6.0.0

* Tue Oct 31 2023 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sun Jun 11 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Wed Jan 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- first build for Sisyphus (v3.0.1-30-ge5c5d88)

