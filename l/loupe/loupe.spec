%def_disable snapshot

%define optflags_lto %nil
%define _libexecdir %_prefix/libexec

%define ver_major 45
%define beta %nil
%define xdg_name org.gnome.Loupe

%def_disable bootstrap

Name: loupe
Version: %ver_major.2
Release: alt1%beta

Summary: GNOME Image Viewer
License: GPL-3.0
Group: Graphics
Url: https://gitlab.gnome.org/Incubator/loupe

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/Incubator/loupe.git
Source: %name-%version%beta.tar
%endif
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define glib_ver 2.76
%define gtk_ver 4.11.3
%define adwaita_ver 1.4
%define gweather_ver 4.0.0
%define heif_ver 1.14.2
%define lcms2_ver 2.12.0

Provides: gnome-image-viewer = %EVR
Requires: glycin-loaders

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gweather4) >= %gweather_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: pkgconfig(lcms2) >= %lcms2_ver
BuildRequires: librsvg-devel libxml2-devel

%description
%summary

%prep
%setup -n %name-%version%beta %{?_enable_snapshot:%{?_disable_bootstrap:-a1}}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Tue Nov 14 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sat Jul 01 2023 Yuri N. Sedunov <aris@altlinux.org> 44.3-alt1
- 44.3

* Wed Apr 05 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- first build for Sisyphus


