Name: gtkglext
Version: 1.2.0
Release: alt3

Summary: An OpenGL extention to GTK2

License: LGPLv2+
Group: System/Libraries
Url: http://gtkglext.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: gtkglext-support-pango.patch
Patch1: gtkglext-1.2.0-newer-gtk.patch
Patch2: gtkglext-1.2.0-alt-DSO.patch
Patch3: gtkglext-1.2.0-alt-pangox.patch

%define gtk_ver 2.4.0
%define gtk_doc_ver 1.1
%def_disable static

BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver

# Automatically added by buildreq on Wed Dec 08 2010
BuildRequires: gtk-doc imake libGLU-devel libXmu-devel libgtk+2-devel
BuildPreReq: xorg-cf-files libGL-devel libXext-devel gcc-c++
BuildPreReq: pkgconfig(pangox)

%description
GtkGLExt is an OpenGL extension to GTK2.

This package is composed of GdkGLExt library and GtkGLExt library.
GdkGLExt library provides the GDK objects which support OpenGL
rendering in GTK. GtkGLExt library provides the GtkWidget API add-ons
to make GTK+ widgets OpenGL-capable.

%package -n lib%name
Summary: An OpenGL extention to GTK2
Group: System/Libraries

%description -n lib%name
A library of dynamically linked GtkGLExt

%package -n lib%name-devel
Summary: An OpenGL extention to GTK2 development files
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
# FC compat
Provides: %name-devel = %version-%release

%description -n lib%name-devel
This package contents development files and documentation
for compiling programs that use GtkGLExt.

%package -n lib%name-devel-static
Summary: An OpenGL extention to GTK2 static libraries
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the libraries needed for compiling programs
statically linked against GtkGLExt.

%prep
%setup
%patch0 -p0
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%autoreconf
%configure --disable-gtk-doc %{subst_enable static}

%make_build
#%make_build examples

%install
%makeinstall_std
rm -rf %buildroot%_datadir/gtk-doc/html

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README TODO

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_aclocaldir/*
%_pkgconfigdir/*
%_libdir/%name-1.0/

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Dec 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt3
- disable build doc

* Wed Oct 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.4
- Fixed build

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.3
- Fixed build

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.2
- Rebuilt for debuginfo

* Wed Dec 08 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt2.1
- Fixed build.
- Updated build dependencies.
- Cleaned up package dependnecies.

* Sat Jun 12 2010 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- fix build with gtk 2.20
- build with pango (thanks, Mandriva)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libgtkglext
  * postun_ldconfig for libgtkglext
  * postclean-05-filetriggers for spec file

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.1
- NMU:
  * updated build dependencies

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- enable autoreconf

* Sun Nov 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- new version 1.2
- cleanup spec, change maintainter
- update buildreqs, remove glib1-devel requires

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.6-alt1.1.1
- Rebuilt for new pkg-config dependencies.

* Sun Nov 07 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt1.1
- fix build with new pango.
- update buildrequires.

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Thu Dec 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt1
- 1.0.5
- do not package .la files.
- do not build devel-static subpackage by default.

* Wed Mar 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sun Dec 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sat Dec 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt2
- rebuild with new pango, gtk+

* Sat Sep 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Jun 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3

* Thu Jun 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Wed Jun 12 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.1.1-alt1
- First build for Sisyphus
