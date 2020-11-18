%def_disable snapshot
%define _name gdk-pixbuf-xlib
%define libname libgdk_pixbuf_xlib
%define api_ver 2.0
%define ver_major 2.40

%def_disable gtk_doc

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: GdkPixbuf-Xlib deprecated library
Group: System/Libraries
License: LGPL-2.1
Url: http://www.gtk.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib.git
Source: %_name-%version.tar
%endif

%define gdk_pixbuf_ver 2.42

BuildRequires(pre): meson
BuildRequires: libgdk-pixbuf-devel >= %gdk_pixbuf_ver libX11-devel
%{?_enable_gtk_doc:BuildRequires: gtk_doc}

%description
GdkPixbuf-Xlib contains the deprecated API for integrating GdkPixbuf with
Xlib data types.

This library was originally shipped by GdkPixbuf, and has since been
moved out of the original repository.

No newly written code should ever use this library.

If your existing code depends on gdk-pixbuf-xlib, then you're strongly
encouraged to port away from it.

%package devel
Summary: Development files for GdkPixBuf-Xlib applications
Group: Development/C
Requires: %name = %version-%release
Conflicts: libgdk-pixbuf-devel < 2.42.0

%description devel
This package provides include files needed for building GdkPixBuf-Xlib
applications.

%package devel-doc
Summary: Development documentation for GdkPixBuf-Xlib library
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version
Conflicts: libgdk-pixbuf-devel-doc < 2.42.0

%description devel-doc
This package provides documentation needed for developing GdkPixBuf-Xlib
applications.

%prep
%setup -n %_name-%version

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true}
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%_libdir/%libname-%api_ver.so.*
%doc README.md

%files devel
%_libdir/%libname-%api_ver.so
%_includedir/gdk-pixbuf-%api_ver/%_name
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Fri Nov 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2


