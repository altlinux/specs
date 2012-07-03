%define bname librsvg
%define ver_major 2.36
%define api_ver 2.0
%define gtk_api_ver 2.0
%define gtk3_api_ver 3.0

%def_disable static
%def_disable gtk_doc
%def_enable pixbuf_loader
%def_enable gtk_theme
%def_enable introspection

Name: %bname
Version: %ver_major.1
Release: alt1

Summary: An SVG library based on libart
License: LGPLv2+
Group: System/Libraries
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%bname/%ver_major/%bname-%version.tar.xz

# From configure.in
%define fontconfig_ver 1.0.1
%define glib_ver 2.12.0
%define gio_ver 2.24.0
%define gtk_ver 2.22.0
%define gtk3_ver 3.0.0
%define libxml2_ver 2.7.0
%define cairo_ver 1.2.0
%define pango_ver 1.10.0
%define libgsf_ver 1.6.0
%define croco_ver 0.6.4

PreReq: libcroco >= %croco_ver

# From configure.in
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libgtk+3-devel >= %gtk3_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: fontconfig-devel freetype2-devel
BuildPreReq: libcroco-devel >= %croco_ver
BuildPreReq: libgsf-devel >= %libgsf_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgdk-pixbuf-gir-devel}
BuildPreReq: libX11-devel libXt-devel
BuildRequires: gcc-c++ gtk-doc sgml-common zlib-devel

%description
An SVG library based on libart.

%package devel
Summary: Libraries and include files for developing with librsvg
Group: Development/C
Requires: %bname = %version-%release

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package devel-doc
Summary: Development documentation for %bname
Group: Development/C
BuildArch: noarch
Conflicts: %bname < %version-%release

%description devel-doc
%bname is a SVG library based on libart.
This package contains development documentation for %bname

%package devel-static
Summary: Static libraries for developing with librsvg
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package provides the necessary static libraries files to allow you
to build static software with librsvg.

%package utils
Summary: Utilities to manipulate SVG files
Group: Graphics
Requires: %bname = %version-%release

%description utils
This package contains small utilities to manipulate SVG files found in
%bname package.

%package utils-gtk3
Summary: Utility to view SVG files
Group: Graphics
Requires: %bname = %version-%release

%description utils-gtk3
This package provides simple GTK+3 based SVG viewer.

%package -n libgtk-engine-svg
Summary: A GTK+ engine for graphical themes that use SVG images.
Group: Graphical desktop/GNOME
Requires: %bname = %version-%release

%description -n libgtk-engine-svg
This package contains a GTK+2 engine that renders graphical themes with SVG
images in them.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library


%define _gtk_docdir %_datadir/gtk-doc/html/

%prep
%setup -n %bname-%version

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{?_enable_pixbuf_loader:--enable-pixbuf-loader} \
	%{?_enable_gtk_theme:--enable-gtk-theme} \
	%{?_enable_introspection:--enable-introspection=yes}

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%{?_enable_pixbuf_loader:%_libdir/gdk-pixbuf-%gtk_api_ver/*/loaders/*.so}
%{?_enable_pixbuf_loader:%_datadir/themes/*/gtk-%gtk_api_ver/*}
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%bname-%gtk_api_ver.pc

%files devel-doc
%_gtk_docdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%{?_enable_pixbuf_loader:%_libdir/gdk-pixbuf-%gtk_api_ver/*/loaders/*.a}
%endif

%files utils
%_bindir/*
%exclude %_bindir/rsvg-view-3
%_man1dir/*

%files utils-gtk3
%_bindir/rsvg-view-3

%files -n libgtk-engine-svg
%_libdir/gtk-%gtk_api_ver/*/engines/libsvg.so

%if_enabled introspection
%files gir
%_typelibdir/Rsvg-%api_ver.typelib

%files gir-devel
%_girdir/Rsvg-%api_ver.gir
%endif

%exclude %_libdir/gtk-%gtk_api_ver/*/*/*.la
%{?_enable_pixbuf_loader:%exclude %_libdir/gdk-pixbuf-%gtk_api_ver/*/loaders/*.la}

%changelog
* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.34.1-alt1.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 2.34.0-alt1.qa1
- Rebuilt with libcairo-1.10.2-alt7.

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- rebuilt for debuginfo

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3 

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.26.0-alt2.1
- Rebuilt with python 2.6

* Mon Jul 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- removed gdk-pixbuf-query-loaders call in %post

* Wed Mar 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete %%post{,un}_ldconfig
- drop upstreamed patch
- mozilla plugin disabled (not ready for our new xulrunner)

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version 2.22.3
- build devel-doc as noarch

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version 2.22.2
- cleanup spec (remove gnome-vfs, gnomeprint)
- plug memory leaks(patch1 from RH)

* Sun Jan 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt2
- from now on, two librsvg packages are built, one with gnome-vfs
  (librsvg-gnome) and the other without it (librsvg).
- use xulrunner instead of seamonkey to build the browser plugin.

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- new version (2.16.1)
- fixed packaging for the case when mozilla plugin is not built.
- added a subpackage for the GTK+ engine.

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0 (with rpmrb script)

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt2
- fixed Provides/Obsoletes pairs.

* Tue Aug 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version (2.15.90)
- updated dependencies
- spec cleanup
- removed '2' from package name

* Thu Mar 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version (2.14.2)

* Mon Feb 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- spec cleanup, dependencies revised.

* Fri Oct 07 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.5-alt1
- new version

* Fri Sep 23 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.1-alt1
- 2.11.1
- Removed excess buildreqs.

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.5-alt1
- 2.9.5.
- development documentation moved to devel-doc subpackage.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0
- mozilla-plugin-svg subpackage.

* Wed Mar 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Fri Mar 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt3
- do not package .la files.
- do not build devel-static subpackage by default.

* Tue Oct 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- no more gimp plugin.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt2
- rebuild for new gimp2 (1.3.18).

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt3
- disable croco support.

* Thu Jul 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt2
- rebuild with new libgimp.
- css support via libcroco enabled.

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.5-alt1
- 2.2.5

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Sun Feb 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Jan 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt2
- rebuild with new gtk-2.1.5.

* Mon Nov 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Nov 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2
- rebuild with new gtk+2.
- Run gdk-pixbuf-query-loaders in %%post.
- utils subpackage.

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Sun Jun 23 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- Adopted for AltLinux
- .a moved to %name-devel-static
- Fix *Req*

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May 02 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr 18 2002 Havoc Pennington <hp@redhat.com>
- 1.1.6

* Mon Feb 11 2002 Alex Larsson <alexl@redhat.com> 1.1.3-1
- Update to 1.1.3

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new CVS snap 1.1.0.91
- remove automake/autoconf calls

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- convert to librsvg2 RPM

* Tue Oct 23 2001 Havoc Pennington <hp@redhat.com>
- 1.0.2

* Fri Jul 27 2001 Alexander Larsson <alexl@redhat.com>
- Add a patch that moves the includes to librsvg-1/librsvg
- in preparation for a later librsvg 2 library.

* Tue Jul 24 2001 Havoc Pennington <hp@redhat.com>
- build requires gnome-libs-devel, #49509

* Thu Jul 19 2001 Havoc Pennington <hp@redhat.com>
- own /usr/include/librsvg

* Wed Jul 18 2001 Akira TAGOH <tagoh@redhat.com> 1.0.0-4
- fixed the linefeed problem in multibyte environment. (Bug#49310)

* Mon Jul 09 2001 Havoc Pennington <hp@redhat.com>
- put .la file back in package

* Fri Jul  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Put changelog at the end
- Move .so files to devel subpackage
- Don't mess with ld.so.conf
- Don't use %%{prefix}, this isn't a relocatable package
- Don't define a bad docdir
- Add BuildRequires
- Use %%{_tmppath}
- Don't define name, version etc. on top of the file (why do so many do that?)
- s/Copyright/License/

* Wed May  9 2001 Jonathan Blandford <jrb@redhat.com>
- Put into Red Hat Build system

* Tue Oct 10 2000 Robin Slomkowski <rslomkow@eazel.com>
- removed obsoletes from sub packages and added mozilla and trilobite
subpackages

* Wed Apr 26 2000 Ramiro Estrugo <ramiro@eazel.com>
- created this thing
