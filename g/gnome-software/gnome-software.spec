%define ver_major 3.26
%define plugins_ver 11
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Software

%def_enable gtkspell
%def_enable gudev
%def_enable gnome_desktop
%def_enable polkit
%def_disable fwupd
%def_enable flatpak
%def_enable ostree
%def_disable limba
%def_enable rpm
%def_disable packagekit
%def_enable webapps
%def_enable odrs
%def_disable tests

Name: gnome-software
Version: %ver_major.3
Release: alt1

Summary: Software manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Software

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.46
%define gtk_ver 3.20
%define appstream_glib_ver 0.7.0
%define json_glib_ver 1.1.1
%define soup_ver 2.52
%define packagekit_ver 1.1.0
%define gnome_desktop_ver 3.18
%define fwupd_ver 0.7.0
%define flatpak_ver 0.6.12
%define limba_ver 0.5.6

BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libappstream-glib-devel >= %appstream_glib_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: gnome-common rpm-build-xdg intltool yelp-tools gtk-doc xsltproc docbook-style-xsl
BuildRequires: libsqlite3-devel libsecret-devel gsettings-desktop-schemas-devel liboauth-devel
BuildRequires: valgrind-tool-devel
%{?_enable_rpm:BuildRequires: librpm-devel}
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_enable_gtkspell:BuildRequires: libgtkspell3-devel}
%{?_enable_gnome_desktop:BuildRequires: libgnome-desktop3-devel >= %gnome_desktop_ver}
%{?_enable_polkit:BuildRequires: libpolkit-devel}
%{?_enable_fwupd:BuildRequires: libfwupd-devel >= %fwupd_ver}
%{?_enable_flatpak:BuildRequires: libflatpak-devel >= %flatpak_ver}
%{?_enable_ostree:BuildRequires: libostree-devel >= %flatpak_ver}
%{?_enable_limba:BuildRequires: liblimba-devel >= %limba_ver}
%{?_enable_packagekit:BuildRequires: libpackage-kit-devel >= %packagekit_ver}

%description
GNOME Software is a software center for GNOME.

%package devel
Summary: Development files for GNOME Software
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains files necessary to develop plugins for GNOME
Software.

%package devel-doc
Summary: Development documentation for GNOME Software
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains documentation necessary to develop plugins for
GNOME Software.


%prep
%setup

%build
%meson \
	-Denable-schemas-compile=false \
	%{?_enable_gtkspell:-Denable-gtkspell=true} \
	%{?_enable_gudev:-Denable-gudev=true} \
	%{?_enable_gnome_desktop:-Denable-gnome-desktop=true} \
	%{?_enable_polkit:-Denable-polkit=true} \
	%{?_disable_fwupd:-Denable-fwupd=false} \
	%{?_enable_flatpak:-Denable-flatpak=true} \
	%{?_enable_ostree:-Denable-ostree=true} \
	%{?_disable_limba:-Denable-limba=false} \
	%{?_disable_rpm:-Denable-rpm=false} \
	%{?_disable_packagekit:-Denable-packagekit=false} \
	%{?_disable_tests:-Denable-tests=false}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_xdgconfigdir/autostart/%name-service.desktop
%_bindir/%name
%_bindir/%name-editor
%_libexecdir/gnome-software-cmd
%_libexecdir/gnome-software-restarter
%_libdir/gs-plugins-%plugins_ver/
%_desktopdir/%name-local-file.desktop
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Editor.desktop
%_datadir/app-info/xmls/%xdg_name.Featured.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/%name/
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_iconsdir/hicolor/*x*/*/%xdg_name.png
%_iconsdir/hicolor/scalable/apps/%xdg_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/software-installed-symbolic.svg
%_datadir/glib-2.0/schemas/org.gnome.software.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/metainfo/%xdg_name.Plugin.Epiphany.metainfo.xml
%_datadir/metainfo/%xdg_name.Plugin.Flatpak.metainfo.xml
%_datadir/metainfo/%xdg_name.Plugin.Odrs.metainfo.xml
%_datadir/metainfo/%xdg_name.Plugin.Steam.metainfo.xml
%_man1dir/%name.1.*
%_man1dir/%name-editor.1.*
%doc AUTHORS README

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Tue Nov 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Thu Nov 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt2
- new -devel, -devel-doc subpackages

* Mon May 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt0.2
- 3.24.1

* Sun Mar 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt0.2
- 3.24.0

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt0.2
- 3.22.7
- enabled ostree/flatpak support

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt0.1
- 3.22.6

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt0.1
- 3.22.5

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt0.1
- first preview for Sisyphus


