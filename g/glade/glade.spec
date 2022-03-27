%define _unpackaged_files_terminate_build 1
%def_enable snapshot

%define ver_major 3.39
%define api_ver 2.0
%define xdg_name org.gnome.Glade
%def_enable gtk_doc
%def_enable python
%def_enable gjs
%def_enable gladeui
%def_disable webkit2gtk
%def_disable check

Name: glade
Version: %ver_major.0
Release: alt0.4

Summary: A user interface designer for Gtk+ and GNOME
Group: Development/GNOME and GTK+
License: GPL-2.0 and LGPL-2.0
Url: http://glade.gnome.org/

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: libgladeui%api_ver = %version-%release

%define gtk_ver 3.24
%define gjs_ver 1.64
%define webkit_ver 2.28

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson yelp-tools %_bindir/appstream-util
BuildRequires: libgtk+3-devel >= %gtk_ver libxml2-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%if_enabled python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pygobject3-devel
%endif
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_gjs:BuildRequires: libgjs-devel >= %gjs_ver}
%{?_enable_webkit2gtk:BuildRequires: libwebkit2gtk-devel >= %webkit_ver}
%{?_enable_check:BuildRequires: xvfb-run icon-theme-hicolor gnome-icon-theme xmllint}

%description
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with GladeUI library.

%package -n libgladeui%api_ver
Summary: GTK+/GNOME3 widget builder library
Group:   Development/GNOME and GTK+

%description -n libgladeui%api_ver
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.
This is library that can be used for embed builder into other
applications.

%package -n libgladeui%api_ver-devel
Summary: GTK+3/GNOME3 widget builder library
Group:   Development/GNOME and GTK+
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-devel
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.

This package contains development files for GladeUI library.

%package -n libgladeui%api_ver-devel-doc
Summary: GladeUI development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: libgladeui%api_ver-devel < %version

%description -n libgladeui%api_ver-devel-doc
This package contains documentation needed to develop applications using
GladeUI library.

%package -n libgladeui%api_ver-gir
Summary: GObject introspection data for the GladeUI
Group: System/Libraries
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-gir
GObject introspection data for the GladeUI library.

%package -n libgladeui%api_ver-gir-devel
Summary: GObject introspection devel data for the GladeUI
Group: Development/Other
BuildArch: noarch
Requires: libgladeui%api_ver-gir = %version-%release
Requires: libgladeui%api_ver-devel = %version-%release

%description -n libgladeui%api_ver-gir-devel
GObject introspection devel data for the GladeUI library.

%prep
%setup
# fix build with meson >= 0.61
sed -E -i "/^[[:space:]]*('desktop'|'appdata')\,/d" data/meson.build
# comment out duplicate "da" entry from help/LINGUAS
sed -i '0,/^da$/s/\(^da$\)/#\1/' help/LINGUAS

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	%{?_disable_python:-Dpython=disabled} \
	%{?_disable_gjs:-Dgjs=disabled} \
	%{?_enable_gladeui:-Dgladeui=true} \
	%{?_disable_webkit2gtk:-Dwebkit2gtk=disabled}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%name
%_bindir/%name-previewer
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/glade-previewer.1.*
%_man1dir/glade.1.*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS COPYING NEWS TODO
%doc README*

%files -n libgladeui%api_ver
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/libgladegtk.so
%{?_enable_python:%_libdir/%name/modules/libgladepython.so}
%{?_enable_gladeui:%_libdir/%name/modules/libgladeglade.so}
%{?_enable_webkit2gtk:%_libdir/%name/modules/libgladewebkit2gtk.so}
%{?_enable_gjs:%_libdir/%name/modules/libgladegjs.so}
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/catalogs
%_datadir/%name/catalogs/*.xml
%_datadir/%name/catalogs/glade-catalog.dtd
%_datadir/%name/pixmaps

%files -n libgladeui%api_ver-devel
%_includedir/libgladeui-%api_ver/
%_libdir/*.so
%_pkgconfigdir/gladeui-%api_ver.pc
%_datadir/gettext/its/glade-catalog.*

%if_enabled gtk_doc
%files -n libgladeui%api_ver-devel-doc
%_datadir/gtk-doc/html/*
%endif

%files -n libgladeui%api_ver-gir
%_typelibdir/Gladeui-%api_ver.typelib

%files -n libgladeui%api_ver-gir-devel
%_girdir/Gladeui-%api_ver.gir

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.39.0-alt0.4
- updated to 3.39.0-120-g8d52d1ec (updated translations)
- fixed build with meson >= 0.61

* Thu Sep 02 2021 Yuri N. Sedunov <aris@altlinux.org> 3.39.0-alt0.3
- temporarily disabled webkit2gtk support (not ready for 4.1)

* Thu Sep 02 2021 Yuri N. Sedunov <aris@altlinux.org> 3.39.0-alt0.2
- updated to 3.39.0-106-g5e46bd65

* Sun Apr 25 2021 Yuri N. Sedunov <aris@altlinux.org> 3.39.0-alt0.1
- updated to 3.39.0-91-g86b45d9a
- disabled %%check

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Oct 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Thu May 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2
- enabled %%check

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt3
- updated to GLADE_3_22_1-25-gc2cd95a1
- switched python module build to python3
- mike@: E2K: disabled -Werror=pointer-arith (EDG bug workaround)

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt2
- updated buildreqs

* Tue Apr 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Sun Feb 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon Nov 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2
- removed upstreamed patch from previous release

* Fri Oct 13 2017 Paul Wolneykien <manowar@altlinux.org> 3.20.1-alt2
- Apply fix-xorg-100-percent patch (thx arnaud-preevio@).

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Mar 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Apr 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.15.1-alt1
- 3.15.1

* Thu Mar 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.15.0-alt1
- 3.15.0

* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- first build for Sisyphus

