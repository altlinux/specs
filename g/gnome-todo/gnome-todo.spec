%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 3.26
%define api_ver 1.0
%define xdg_name org.gnome.Todo

%def_disable gtk_doc

Name: gnome-todo
Version: %ver_major.2
Release: alt2

Summary: Todo manager for GNOME
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Todo

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: gnome-todo-3.26.2-fc-libical-3.0.patch

%define gtk_ver 3.22.0
%define eds_ver 3.18.0

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/%name/plugins
BuildPreReq: rpm-build-python3 python3-devel
Requires: libpeas-python3-loader

BuildRequires: meson yelp-tools libappstream-glib-devel gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver evolution-data-server-devel >= %eds_ver
BuildRequires: libgnome-online-accounts-devel libical-devel libpeas-devel
BuildRequires: librest-devel libjson-glib-devel
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
%patch -p1
##subst 's/\(install_dir: doc_path\)/\1,/' doc/reference/meson.build

%build
%meson %{?_enable_gtk_doc:-Denable-gtk-doc=true}
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*
%dir %_datadir/%name
%_datadir/%name/%xdg_name.Autostart.desktop
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.todo.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.todo.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.todo.txt.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.*.xml
%doc NEWS README

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc
%{?_enable_gtk_doc:%_datadir/gtk-doc/html/%name/}

%files gir
%_typelibdir/Gtd-%api_ver.typelib

%files gir-devel
%_girdir/Gtd-%api_ver.gir

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- rebuilt against libical.so.3

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0.1-alt1
- 3.24.0.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Dec 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt2
- rebuilt against libedataserver-1.2.so.22

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

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

