%define _libexecdir %_prefix/libexec

%define ver_major 42
%define xdg_name org.gnome.Console
%define binary_name kgx

%def_with nautilus

Name: gnome-console
Version: %ver_major.2
Release: alt1

Summary: GNOME Console
License: GPL-3.0
Group: Terminals
Url: https://gitlab.gnome.org/GNOME/console

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.66
%define gtk_ver 3.24.0
%define handy_ver 1.5
%define vte_ver 0.68.0

Requires(pre): libvte3 >= %vte_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson sassc yelp-tools
BuildRequires: desktop-file-utils %_bindir/appstream-util
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: libvte3-devel >= %vte_ver libpcre2-devel
BuildRequires: gsettings-desktop-schemas-devel
%{?_with_nautilus:BuildRequires: rpm-build-gnome libnautilus-devel}

%description
A simple user-friendly terminal emulator for the GNOME desktop.

%package nautilus
Summary: Nautilus extension for the GNOME Console
Group: Graphical desktop/GNOME
Requires: %name = %EVR

%description nautilus
This package provides integration with the GNOME Console for the
Nautilus file manager.

%prep
%setup

%build
%meson \
    %{?_without_nautilus:-Dnautilus=disabled}
%meson_build

%install
%meson_install

%find_lang --with-gnome %binary_name

%files -f %binary_name.lang
%_bindir/%binary_name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.*
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc NEWS README*

%if_with nautilus
%files nautilus
%nautilus_extdir/lib%binary_name-nautilus.so
%endif

%changelog
* Thu Jul 14 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Wed Jul 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- first build for Sisyphus


