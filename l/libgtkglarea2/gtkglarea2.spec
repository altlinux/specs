%define version 1.99.0
%define release alt4.3
%define fname gtkglarea
#define name gtkglarea2
%def_disable static

Summary: GtkGLArea is an OpenGL widget for GTK+ GUI toolkit
Name: libgtkglarea2
Version: %version
Release: %release
License: LGPLv2+
Group: System/Libraries
Source: %fname-%version.tar.bz2
Url: http://www.student.oulu.fi/~jlof/gtkglarea/
Provides: gtkglarea2
Obsoletes: gtkglarea2
BuildPreReq: pkgconfig libgtk+2-devel  libGLU-devel

Packager: Ilya Mashkin <oddity@altlinux.ru>

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

Related project which may iterest those who use GTK-- is GtkGLArea--. It is a
C++ wrapper for gtkglarea written by Karl Nelson <kenelson@ece.ucdavis.edu>.

%package devel
Summary: GtkGLArea is an OpenGL widget for GTK+ -- include files
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: gtkglarea2-devel
Obsoletes: gtkglarea2-devel

%description devel
include files you can use for GtkGLArea development

%package devel-static
Summary: GtkGLArea is an OpenGL widget for GTK+ --  static libs
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: gtkglarea2-devel-static
Obsoletes: gtkglarea2-devel-static

%description devel-static
Static libraries you can use for GtkGLArea development

%prep
%setup -q -n%fname-%version

%configure %{subst_enable static}
%make_build

%install
%makeinstall
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;


%files
%doc AUTHORS COPYING ChangeLog NEWS README docs/*.txt
%_libdir/libgtkgl-2.0.so.*

%files devel
%_libdir/*.so
#_libdir/*.la
%_libdir/pkgconfig/gtkgl*
%_includedir/gtkgl-2.0/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif # static

%changelog

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 1.99.0-alt4.3
- update requires

* Sat Dec 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.99.0-alt4.2
- update requires

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.99.0-alt4.1
- add Obsoletes: gtkglarea2

* Thu Apr 09 2009 Ilya Mashkin <oddity@altlinux.ru> 1.99.0-alt4
- rename to %name according policy
- remove deprecated macros
- change License

* Tue Apr 25 2006 LAKostis <lakostis at altlinux.ru> 1.99.0-alt3
- NMU;
- .spec cleanup;
- disable static builds by default.

* Tue Feb 10 2004 Egor S. Orlov <oes@altlinux.ru> 1.99.0-alt2
- remove la-files 

* Wed Jun 18 2003 AEN <aen@altlinux.ru> 1.99.0-alt1
- first build for Sisyphus

