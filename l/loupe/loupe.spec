%def_disable snapshot

%define optflags_lto %nil
%define _libexecdir %_prefix/libexec

%define ver_major 47
%define beta %nil
%define xdg_name org.gnome.Loupe

%def_enable check
%def_disable bootstrap

Name: loupe
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Image Viewer
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Loupe

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/loupe.git
Source: %name-%version%beta.tar
%endif
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define glib_ver 2.76
%define gtk_ver 4.15.3
%define adwaita_ver 1.6
%define gweather_ver 4.0.0
%define lcms2_ver 2.12.0
%define seccomp_ver 2.5.0

Provides: gnome-image-viewer = %EVR
Requires: glycin-loaders >= 1.1.0
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: yelp-tools
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gweather4) >= %gweather_ver
BuildRequires: pkgconfig(lcms2) >= %lcms2_ver
BuildRequires: librsvg-devel libxml2-devel
BuildRequires: pkgconfig(libseccomp) >= %seccomp_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

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

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* NEWS


%changelog
* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Wed Apr 10 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- 46.2

* Wed Apr 03 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Fri Mar 15 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1
- 45.3

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


