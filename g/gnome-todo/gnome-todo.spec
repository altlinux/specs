%define _libexecdir %_prefix/libexec
%define ver_major 3.20
%define api_ver 1.0
%define xdg_name org.gnome.Todo

Name: gnome-todo
Version: %ver_major.1
Release: alt1

Summary: Todo manager for GNOME
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Todo

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%define gtk_ver 3.19.5
%define eds_ver 3.18.0

BuildRequires: intltool yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver evolution-data-server-devel >= %eds_ver
BuildRequires: libgnome-online-accounts-devel libical-devel libpeas-devel
BuildRequires: libgtk+3-gir-devel

%description
GNOME Todo is a simple task management application designed to integrate
with GNOME.

%package devel
Summary: Development files for GNOME Todo
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package provides files necessary to develop plugins for GNOME Todo.

%package gir
Summary: GObject introspection data for the GNOME Todo
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GNOME Todo.

%package gir-devel
Summary: GObject introspection devel data for the GNOME Todo
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GNOME Todo.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.todo.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.todo.enums.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/appdata/%xdg_name.appdata.xml
%doc NEWS README

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc

%files gir
%_typelibdir/Gtd-%api_ver.typelib

%files gir-devel
%_girdir/Gtd-%api_ver.gir

%changelog
* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt3
- rebuild against libicu*.so.56

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt2
- rebuilt against libical.so.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.3.1-alt1
- first build for people/gnome

