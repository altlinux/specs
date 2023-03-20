%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define nautilus_extdir %_libdir/nautilus/extensions-4

%define ver_major 44
%define beta %nil
%define xdg_name org.gnome.Console
%define binary_name kgx

%def_without nautilus

Name: gnome-console
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Console
License: GPL-3.0
Group: Terminals
Url: https://gitlab.gnome.org/GNOME/console

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/console.git
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.72
%define gtk4_ver 4.6
%define adwaita_ver 1.3
%define vte_ver 0.69.91
%define nautilus_ver 43

Requires(pre): libvte3 >= %vte_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson yelp-tools
BuildRequires: desktop-file-utils %_bindir/appstream-util
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(vte-2.91-gtk4) >= %vte_ver libpcre2-devel
BuildRequires: gsettings-desktop-schemas-devel
%{?_with_nautilus:BuildRequires: rpm-build-gnome
BuildRequires: pkgconfig(libnautilus-extension-4) >= %nautilus_ver}

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
%setup -n %name-%version%beta

%build
%meson
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
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Sun Sep 25 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.9.rc
- 43.rc (ported to GTK4)

* Thu Jul 14 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Wed Jul 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- first build for Sisyphus


