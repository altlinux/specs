%def_disable snapshot
%define ver_major 44
%define xdg_name org.gnome.Loupe

%def_disable bootstrap

Name: loupe
Version: %ver_major.0
Release: alt1

Summary: A simple image viewer application written with GTK4 and Rust
License: GPL-3.0
Group: Graphics
Url: https://gitlab.gnome.org/Incubator/loupe

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/Incubator/loupe.git
Source: %name-%version.tar
%endif
#Source1: %name-%version-cargo.tar

%define glib_ver 2.76
%define gtk_ver 4.10
%define adwaita_ver 1.3
%define gweather_ver 4.0.0
%define heif_ver 1.14.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gweather4) >= %gweather_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: librsvg-devel libxml2-devel

%description
%summary

%prep
%setup -n %name-%version
# %{?_disable_bootstrap:-a1}
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

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Wed Apr 05 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- first build for Sisyphus


