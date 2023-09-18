%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 45
%define beta %nil
%define xdg_name org.gnome.Tecla

Name: tecla
Version: %ver_major.0
Release: alt1%beta

Summary: Tecla is a keyboard layout viewer
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/GNOME/tecla

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/tecla.git
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.76
%define gtk_ver 4.11.3
%define adwaita_ver 1.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)

%description
%summary

%package devel
Summary: Development package for %name
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package contains development files for %name

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%doc README*

%files devel
%_datadir/pkgconfig/%name.pc

%changelog
* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Wed Jul 05 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.1.alpha
- first build for Sisyphus



