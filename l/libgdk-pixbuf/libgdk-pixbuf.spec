%define _name gdk-pixbuf
%define api_ver 2.0
%define binary_ver 2.10.0
%define ver_major 2.26
%def_disable gtk_doc
%def_enable introspection
%def_with x11

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: An image loading and rendering library for Gdk
Group: System/Libraries
License: LGPL
Url: http://www.projects.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
Source1: %_name.map
Source2: %_name.lds
Source3: gdk-pixbuf-loaders.filetrigger

%define glib_ver 2.31.0
%define gi_ver 0.9.5

Requires: %name-locales = %version

Provides: %name-loaders = %version
Obsoletes: %name-loaders <= %version

BuildPreReq: glib2-devel >= %glib_ver
BuildRequires: docbook-utils gtk-doc libjpeg-devel libpng-devel libtiff-devel
%{?_with_x11:BuildRequires: libX11-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}

%description
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

%package xlib
Summary: An image loading and rendering library for Gdk
Group: System/Libraries
Requires: %name = %version-%release

%description xlib
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

This package provides Xlib version of %name.

%package locales
Summary: Internationalization for GdkPixBuf library
Group: System/Internationalization
Conflicts: %name < %version-%release
BuildArch: noarch

%description locales
This package provides internationalization support for GdkPixBuf,
an image loading and rendering library for Gdk.

%package devel
Summary: Development files for GdkPixBuf applications
Group: Development/C
Requires: %name = %version-%release
Requires: %name-xlib = %version-%release

%description devel
GdkPixBuf is an image loading and rendering library for Gdk.

This package provides include files needed for developing GdkPixBuf
applications.

%package devel-doc
Summary: Development documentation for GdkPixBuf library
Group: Development/C
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
GdkPixBuf is an image loading and rendering library for Gdk.

This package provides documentation needed for developing GdkPixBuf
applications.

%package gir
Summary: GObject introspection data for the GdkPixBuf library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GdkPixBuf library

%package gir-devel
Summary: GObject introspection devel data for the GdkPixBuf library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GdkPixBuf library

%prep
%setup -q -n %_name-%version
install -p -m644 %_sourcedir/%_name.map %_name/compat.map
install -p -m644 %_sourcedir/%_name.lds %_name/compat.lds

%build
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{?_with_x11:--with-x11}

%make_build LIBTOOL_EXPORT_OPTIONS=-Wl,--version-script=compat.map,compat.lds

%check
# due to version script
echo : >>%_name/abicheck.sh
%make check

%install
%make DESTDIR=%buildroot install

# rpm posttrans filetriggers
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/gdk-pixbuf-loaders.filetrigger
touch %buildroot%_libdir/%_name-%api_ver/%binary_ver/loaders.cache

%find_lang %_name

%files
%_bindir/gdk-pixbuf-query-loaders
%_libdir/libgdk_pixbuf-2.0.so.*
%dir %_libdir/%_name-%api_ver
%dir %_libdir/%_name-%api_ver/%binary_ver
%dir %_libdir/%_name-%api_ver/%binary_ver/loaders
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ani.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-bmp.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-gif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-icns.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ico.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-jpeg.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-pcx.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-png.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-pnm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-qtif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ras.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tga.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tiff.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-wbmp.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xbm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xpm.so
%exclude %_libdir/%_name-%api_ver/%binary_ver/loaders/*.la
%ghost %_libdir/%_name-%api_ver/%binary_ver/loaders.cache
%_man1dir/gdk-pixbuf-query-loaders*
%_rpmlibdir/gdk-pixbuf-loaders.filetrigger

%if_with x11
%files xlib
%_libdir/libgdk_pixbuf_xlib-2.0.so.*
%endif
%doc AUTHORS NEWS README

%files locales -f %_name.lang

%files devel
%_bindir/gdk-pixbuf-csource
%_bindir/%_name-pixdata
%_libdir/*.so
%dir %_includedir/%_name-%api_ver
%_includedir/%_name-%api_ver/%_name
%_includedir/%_name-%api_ver/%_name-xlib
%_libdir/pkgconfig/%_name-%api_ver.pc
%_libdir/pkgconfig/%_name-xlib-%api_ver.pc
%_man1dir/gdk-pixbuf-csource*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif

%changelog
* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sat Dec 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Aug 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.5-alt1
- 2.23.5

* Sat Jun 25 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt2
- fixed CVE-2011-2485 (ALT #25816)

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt1
- 2.23.4

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.3-alt1
- 2.23.3

* Sat Mar 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Thu Feb 17 2011 Alexey Tourbin <at@altlinux.ru> 2.23.0-alt2
- merged libgdk-pixbuf-loaders into libgdk-pixbuf
- split libgdk-pixbuf-locales noarch subpackage
- disabled symbol versioning

* Thu Dec 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.0-alt1
- 2.23.0

* Sat Nov 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Tue Oct 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt3
- try to unset GDK_PIXBUF_MODULEDIR before gdk-pixbuf-query-loaders call

* Mon Oct 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt2
- reduced priority for gdk-pixbuf-query-loaders-2.0.filetrigger
  (closes #24352)

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Fri Sep 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.7-alt1
- 2.21.7

* Tue Aug 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.6-alt1
- 2.21.6

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- first build for Sisyphus

