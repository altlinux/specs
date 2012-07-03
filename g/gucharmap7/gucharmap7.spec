%define _name gucharmap

%define ver_major 2.32
%define gtk_api_ver 2.0
%define so_ver 7

%def_disable introspection
%def_disable python

Name: gucharmap%so_ver
Version: %ver_major.1
Release: alt1

Summary: gucharmap is a featureful Unicode character map
License: %gpl3plus
Group: Text tools

Source: %gnome_ftp/%name/%ver_major/%_name-%version.tar.bz2

# From configure.ac
%define glib_ver 2.16.3
%define gtk_ver 2.21.6
%define pygtk_ver 2.7.1

Requires: lib%name = %version-%release
Requires(post,preun): GConf

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.ac
BuildPreReq: intltool >= 0.40.0
BuildPreReq: gnome-common
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: gnome-doc-utils >= 0.9.0
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: libcairo-gobject-devel libGConf-devel GConf
%{?_enable_python:BuildPreReq: python-module-pygtk-devel >= %pygtk_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+2-gir-devel}

%description
This package provides a featureful Unicode character map for GNOME2.

%package -n lib%name
Summary: gucharmap shared library
Group: System/Libraries

%description -n lib%name
This package provides shared library for programs that show character maps
(including Gucharmap and a character map applet for the GNOME panel).

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains headers and libraries needed to compile
applications against lib%name

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GNOME Unicode character map library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Unicode character map library

%{?_enable_python:%setup_python_module %name}
%package -n python-module-%name
Summary: Python bindings for %name library
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
%name is a featureful Unicode character map. This package contains
bindings to  for the GNOME Unicode character map library.

%prep
%setup -q -n %_name-%version

%build
%configure \
    --disable-scrollkeeper \
    --disable-static \
    --enable-gconf \
    --disable-schemas-install \
    %{subst_enable introspection} \
    %{?_enable_python:--enable-python-bindings} \
    --with-gtk=%gtk_api_ver

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%if 0
%files -f %name.lang
%_bindir/*
%_desktopdir/*
%config %gconf_schemasdir/%name.schemas
%endif

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README TODO COPYING COPYING.UNICODE

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/gtk-2.0/gucharmap.so
%_datadir/pygtk/2.0/defs/gucharmap.defs

%exclude %python_sitelibdir/gtk-2.0/gucharmap.la
%endif

%changelog
* Thu May 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- first build for Sisyphus

