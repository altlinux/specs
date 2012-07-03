%define _name gnome-menus
%define ver_major 3.0
%def_disable introspection

Name: %{_name}2
Version: %ver_major.0
Release: alt4.1.1

Summary: GNOME desktop menu
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.bz2
Patch1: %_name-2.14-alt-add-config-dir.patch
Patch2: %_name-alt-applications-menu-no-legacy-kde.patch

BuildPreReq: rpm-build-gnome rpm-build-xdg

# From configure.in
BuildPreReq: intltool >= 0.35 gnome-common
BuildPreReq: glib2-devel >= 2.26.0
BuildPreReq: libgio-devel >= 2.26.0
BuildPreReq: python-devel
BuildRequires: gobject-introspection-devel

%description
This package should not be in a repository. If you see this, please file
a bug to http://bugzilla.altlinux.org against gnome-menus component.

%package common
Summary: GNOME Menus common data
License: GPLv2+
Group: Graphical desktop/GNOME
BuildArch: noarch

%description common
The package contains data common to GNOME menus of any ALT Linux
distribution. Normally you should not install this package manually, it
will be installed as a dependency.

%package -n lib%name
Summary: Desktop Menu Library for GNOME
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package provides Desktop Menu Library for GNOME.

%package -n lib%name-devel
Summary: Development files for GNOME Desktop Menu Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Desktop Menu Library.

%package -n lib%name-devel-examples
Summary: Development utilities and examples for GNOME Desktop Menu Library
License: LGPLv2+
Group: Development/Python
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-devel-examples
This package provides some examples that use Desktop Menu Library.

%package -n lib%name-gir
Summary: GObject introspection data for the GNOME Desktop Menu Library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GNOME Desktop Menu Library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GNOME Desktop Menu Library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Desktop Menu Library

%setup_python_module %_name
%package -n python-module-%_name
Summary: Python bindings for %name
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%_name
This package contains files that are needed to work with GNOME menus from
Python.

%package -n gnome-menu-editor
Summary: A simple GNOME menu editor
Group: Graphical desktop/GNOME
Requires: python-module-%name = %version-%release

%description -n gnome-menu-editor
This package contains a simple GNOME menu editor.

%prep
%setup -n %_name-%version
%patch1 -p0
%patch2 -p1

# Link with current python
sed -i -e 's,^\(gmenu_la_LIBADD  = $(GLIB_LIBS) $(top_builddir)/libmenu/libgnome-menu.la\),\1 -lpython%__python_version,g' python/Makefile.am
sed -i -e 's,^\(gmenu_la_LIBADD = $(GLIB_LIBS) $(top_builddir)/libmenu/libgnome-menu.la\),\1 -lpython%__python_version,g' python/Makefile.in
%build
%autoreconf
%configure \
    --enable-python \
    --disable-static \
    %{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

mv %buildroot%_xdgmenusdir/{,gnome3-}applications.menu

%find_lang %_name

%files -n lib%name -f %_name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif

%files -n python-module-%_name
%python_sitelibdir/gmenu.so

%exclude %python_sitelibdir/gmenu.la

%if 0
%files -n lib%name-devel-examples
# like the gnome-menu-spec-test
%dir %_datadir/%name/examples
%_datadir/%name/examples/gnome-menus-ls.py

%define editor_name gmenu-simple-editor

%files -n gnome-menu-editor
%_bindir/%editor_name
%_desktopdir/%editor_name.desktop
%dir %_datadir/gnome-menus/ui
%_datadir/gnome-menus/ui/%editor_name.ui
%dir %python_sitelibdir/GMenuSimpleEditor
%python_sitelibdir/GMenuSimpleEditor/*
%endif

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt4.1
- Rebuild with Python-2.7

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt4
- first build for Sisyphus

