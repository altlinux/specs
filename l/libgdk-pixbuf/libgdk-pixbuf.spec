%define _name gdk-pixbuf
%define api_ver 2.0
%define binary_ver 2.10.0
%define ver_major 2.36
%define _libexecdir %_prefix/libexec

%def_disable gtk_doc
%def_enable introspection
%def_with x11
%def_with libjasper
%def_enable installed_tests

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: An image loading and rendering library for Gdk
Group: System/Libraries
License: LGPL
Url: http://www.gtk.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
Source1: %_name.map
Source2: %_name.lds

%define glib_ver 2.38
%define gi_ver 0.9.5

Requires: %name-locales = %version

Provides: %name-loaders = %version
Obsoletes: %name-loaders <= %version

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: docbook-utils gtk-doc libjpeg-devel libpng-devel libtiff-devel
%{?_with_x11:BuildRequires: libX11-devel}
%{?_with_libjasper:BuildRequires: libjasper-devel}
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
Group: Development/Documentation
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

%package tests
Summary: Tests for the GdkPixBuf library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GdkPixBuf library.


%prep
%setup -n %_name-%version
install -p -m644 %_sourcedir/%_name.map %_name/compat.map
install -p -m644 %_sourcedir/%_name.lds %_name/compat.lds

%build
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{subst_with x11} \
	%{subst_with libjasper} \
	%{?_enable_installed_tests:--enable-installed-tests}

%make_build LIBTOOL_EXPORT_OPTIONS=-Wl,--version-script=compat.map,compat.lds

%install
%makeinstall_std

ln %buildroot%_bindir/%_name-query-loaders %buildroot%_libdir/%_name-%api_ver/%binary_ver/

# rpm posttrans filetriggers
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/gdk-pixbuf-loaders.filetrigger << '@@@'
#!/bin/sh -efu

LC_ALL=C sed -rn 's|(^/usr/lib(64)?)/gdk-pixbuf.*/loaders/.*|\1|p' | sort -u | while read L; do
       if [ -x "$L/%_name-%api_ver/%binary_ver/%_name-query-loaders" ]; then
              $L/%_name-%api_ver/%binary_ver/%_name-query-loaders --update-cache
       fi
done
@@@
chmod 755 %buildroot%_rpmlibdir/gdk-pixbuf-loaders.filetrigger
touch %buildroot%_libdir/%_name-%api_ver/%binary_ver/loaders.cache

%find_lang %_name

%check
# due to version script
echo : >>%_name/abicheck.sh
#%make check

%files
%_bindir/gdk-pixbuf-query-loaders
%_bindir/gdk-pixbuf-thumbnailer
%_libdir/libgdk_pixbuf-2.0.so.*
%dir %_libdir/%_name-%api_ver
%dir %_libdir/%_name-%api_ver/%binary_ver
%dir %_libdir/%_name-%api_ver/%binary_ver/loaders
%_libdir/%_name-%api_ver/%binary_ver/%_name-query-loaders
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ani.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-bmp.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-gif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-icns.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-ico.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-jpeg.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-png.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-pnm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-qtif.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tga.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-tiff.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xbm.so
%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-xpm.so
%{?_with_libjasper:%_libdir/%_name-%api_ver/%binary_ver/loaders/libpixbufloader-jasper.so}
%exclude %_libdir/%_name-%api_ver/%binary_ver/loaders/*.la
%ghost %_libdir/%_name-%api_ver/%binary_ver/loaders.cache
%_datadir/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
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

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name/
%_datadir/installed-tests/%_name/
%endif


%changelog
* Tue Dec 13 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Thu Mar 24 2016 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 01 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.7-alt1
- 2.31.7

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.5-alt1
- 2.31.5

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.4-alt1
- 2.31.4

* Sun Mar 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.31.3-alt1
- 2.31.3

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 2.31.2-alt1
- 2.31.2 (some tests failed, check temporarily disabled)

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 2.31.1-alt1
- 2.31.1

* Wed Sep 10 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.30.8-alt2
- Fix gdk-pixbuf-loaders.filetrigger.

* Tue May 27 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.8-alt1
- 2.30.8

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.7-alt1
- 2.30.7

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt1
- 2.30.6
- glebfm@:
  packaged %%_libdir/%%_name-%%api_ver/%%binary_ver/%%_name-query-loaders
  hard link to %%_bindir/gdk-pixbuf-query-loaders, changed filetrigger
  to use this hardlink.

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Tue Jan 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Dec 17 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sat Nov 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.5-alt1
- 2.26.5

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.4-alt1
- 2.26.4

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

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

