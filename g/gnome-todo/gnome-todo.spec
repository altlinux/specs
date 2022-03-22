%def_enable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 41
%define beta %nil
%define api_ver 1.0
%define xdg_name org.gnome.Todo

# disabled by default
%def_disable todo_txt_plugin
%def_disable todoist_plugin
%def_disable gtk_doc

Name: gnome-todo
Version: %ver_major.0
Release: alt2%beta

Summary: Todo manager for GNOME
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Todo

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: gnome-todo-40.1-alt-build.patch

%define gtk_ver 4.2.1
%define libadwaita_ver 1.0
%define eds_ver 3.18.0

%add_python3_path %_libdir/%name/plugins
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
# no python3 plugins now
#Requires: libpeas-python3-loader

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson yelp-tools libappstream-glib-devel gtk-doc
BuildRequires: libgtk4-devel >= %gtk_ver pkgconfig(libadwaita-1) >= %libadwaita_ver
BuildRequires: libpeas-devel
BuildRequires: evolution-data-server-devel >= %eds_ver libical-devel
BuildRequires: libgnome-online-accounts-devel 
BuildRequires: librest-devel libjson-glib-devel libportal-gtk4-devel
BuildRequires: gir(Gtk) = 3.0 gir(Adw) = 1

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
%setup -n %name-%version%beta
%patch

%build
%meson %{?_enable_gtk_doc:-Ddocumentation=true} \
    %{?_enable_todo_txt_plugin:-Dtodo_txt_plugin=true} \
    %{?_enable_todoist_plugin:-Dtodoist_plugin=true}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.todo.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%xdg_name.*.xml
%doc NEWS README*

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc
%{?_enable_gtk_doc:%_datadir/gtk-doc/html/%name/}

%files gir
%_typelibdir/Gtd-%api_ver.typelib

%files gir-devel
%_girdir/Gtd-%api_ver.gir

%changelog
* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt2
- updated to 41.0-97-g6878771 from master (42.alpha)

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue Jul 06 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1.1
- fixed build

* Wed Jun 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Tue May 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0 (ported to GTK4/libadwaita)

* Thu Nov 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- updated to 3.28.1-11-g2082517
- fixed BR

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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

