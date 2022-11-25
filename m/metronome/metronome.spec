%def_enable snapshot
%define _name metronome
%define ver_major 1.2
%define rdn_name com.adrienplazas.Metronome

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Metronome for GNOME Desktop
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/metronome

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/metronome.git
Source: %_name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %_name-%version-cargo.tar}

%define gtk_ver 4.0.0
%define adwaita_ver 1.0.0
%define gst_api_ver 1.0
%define gst_ver 1.18

Requires: gst-plugins-base%gst_api_ver >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-player-%gst_api_ver) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-plugins-base-%gst_api_ver) >= %gst_ver

%description
Metronome beats the rhythm for you, you simply need to tell it the
required time signature and beats per minutes.

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
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Fri Nov 25 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0-15-g4f49660

* Thu Jan 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus (1.1.0-33-g633d84d)

