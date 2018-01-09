%def_disable snapshot

%define _name gtk+
%define api_ver 2.0
%define binary_ver 2.10.0
%define ver_major 2.24

%def_enable xkb

%if_enabled snapshot
%def_enable gtk_doc
%else
%def_disable gtk_doc
%endif

%def_enable man
%def_enable introspection

Name: libgtk+2
Version: %ver_major.32
Release: alt1

Summary: The GIMP ToolKit (GTK+), a library for creating GUIs
License: %lgpl2plus
Group: System/Libraries
Url: http://www.gtk.org
Icon: gtk+-logo.xpm

Provides: libgtk2 = %version gtk2 = %version gtk+2 = %version gtk-engines-pixmap = %version
Obsoletes: libgtk2 < %version gtk2 < %version gtk+2 < %version gtk-engines-pixmap < %version
Provides: %name-common = %version
Obsoletes: %name-common <= %version

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%endif

Source1: %name-gdk.map
Source2: %name-gdk.lds
Source3: %name-gtk.map
Source4: %name-gtk.lds
Source5: gtk-icon-cache.filetrigger

Patch1: gtk+-2.16.5-alt-stop-spam.patch
Patch6: gtk+-2.10.6-fix-drop-gdk_colormap_change.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=583273
Patch10: gtk+-2.24.30-icon-padding.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599618
Patch12: gtk+-2.24.30-tooltip-positioning.patch

Patch20: gtk+-2.24.10-fixdso.patch

%define glib_ver 2.28.0
%define cairo_ver 1.6
%define pango_ver 1.28.3
%define atk_ver 1.32.0
%define directfb_ver 0.9.24
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.6

Requires: %name-locales = %version
Requires: gtk-update-icon-cache = %version
Requires: icon-theme-hicolor

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libatk-devel >= %atk_ver
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
BuildRequires: libgio-devel libgdk-pixbuf-devel libcairo-gobject-devel libcups-devel gcc-c++ indent zlib-devel
%if_enabled introspection
BuildRequires: gobject-introspection-devel libpango-gir-devel libatk-gir-devel >= %atk_ver libgdk-pixbuf-gir-devel
%endif
BuildRequires: libXdamage-devel libXcomposite-devel libX11-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package locales
Summary: Internationalization for GTK+
Group: System/Internationalization
Conflicts: %name < %version-%release
BuildArch: noarch

%description locales
This package provides internationalization support for GTK+,
the GIMP toolkit.

%package -n gtk-update-icon-cache
Summary: Icon theme caching utility for GTK+
Group: System/Libraries

%description -n gtk-update-icon-cache
gtk-update-icon-cache creates mmap()able cache files for icon themes.
GTK+ can use the cache files created by gtk-update-icon-cache to avoid
a lot of system call and disk seek overhead when the application starts.

%package -n gtk-builder-convert
Summary: Glade file conversion utility
Group: Development/GNOME and GTK+
BuildArch: noarch

%description -n gtk-builder-convert
gtk-builder-convert converts glade files into XML files which can be
loaded with GtkBuilder.

%package devel
Summary: Development files and tools for GTK+ applications
Group: Development/GNOME and GTK+
Icon: gtk+-devel-logo.xpm
Requires: %name = %version-%release
Requires: gtk-builder-convert = %version
Provides: libgtk2-devel = %version gtk2-devel = %version gtk+2-devel = %version
Obsoletes: libgtk2-devel < %version gtk2-devel < %version gtk+2-devel < %version
Provides: %name-common-devel = %version
Obsoletes: %name-common-devel <= %version

%description devel
This package contains development files for GTK+, X11 version. Use this to
build programs that use GTK+.

%package -n gtk-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gtk-demo
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains a program, along with its source code, that
demonstrates GTK+ variety of all its widgets.

%package devel-doc
Summary: Development documentation for GTK+
Group: Development/GNOME and GTK+
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains documentation needed for developing GTK+ applications.

%package devel-doc-examples
Summary: Examples for developing applications which will use GTK+
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc-examples
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains sources for example programs.

%package gir
Summary: GObject introspection data for the GTK+ library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GTK+ library

%package gir-devel
Summary: GObject introspection devel data for the GTK+ library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GTK+ library

%package -n libgail
Summary: Accessibility implementation for GTK+ and GNOME libraries
Group: System/Libraries
Requires: %name = %version-%release

%description -n libgail
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME libraries,
enabling accessibility technologies such as at-spi to access those GUIs.

%package -n libgail-devel
Summary: Files to compile applications that use GAIL
Group: Development/GNOME and GTK+
Requires: libgail = %version-%release
Requires: %name-devel = %version-%release

%description -n libgail-devel
This package contains the files required to develop applications against
the GAIL libraries.

%package -n libgail-devel-doc
Summary: Development documentation for GAIL
Group: Development/GNOME and GTK+
Conflicts: libgail < %version-%release
BuildArch: noarch

%description -n libgail-devel-doc
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME
libraries, enabling accessibility technologies such as at-spi to access
those GUIs.

This package contains development documentation for GAIL.

%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -n %_name-%version
install -p -m644 %_sourcedir/%name-gdk.map gdk/compat.map
install -p -m644 %_sourcedir/%name-gdk.lds gdk/compat.lds
install -p -m644 %_sourcedir/%name-gtk.map gtk/compat.map
install -p -m644 %_sourcedir/%name-gtk.lds gtk/compat.lds

%patch1 -p1
%patch6

%patch10 -p1 -b .icon-padding
%patch12 -p1 -b .tooltip-positioning
%patch20 -p1 -b .fixdso

bzip2 -9k NEWS

[ ! -d m4 ] && mkdir m4

%build
%if_enabled snapshot
NOCONFIGURE=1 ./autogen.sh
%else
%autoreconf
%endif
%configure \
    %{subst_enable xkb} \
    %{subst_enable man} \
    --with-xinput=yes \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{subst_enable introspection}

# SMP-incompatible build
%make LIBTOOL_EXPORT_OPTIONS=-Wl,--version-script=compat.map,compat.lds

%install
%make_install DESTDIR=%buildroot install
install -d %buildroot{%_sysconfdir/gtk-%api_ver,%_libdir/gtk-%api_ver/%binary_ver/engines}

touch %buildroot%_libdir/gtk-%api_ver/%binary_ver/immodules.cache

# system wide gtkrc
cat <<__RC__ > %buildroot%_sysconfdir/gtk-%api_ver/gtkrc
# This enables editing of menu accelerators by pressing
# an accelerator over the menu item.
gtk-can-change-accels = 1
__RC__

cat <<__SH__ >%name.sh
export GTK_PATH=\`getconf LIBDIR\`/gtk-%api_ver/%binary_ver
__SH__

cat <<__CSH__ >%name.csh
setenv GTK_PATH \`getconf LIBDIR\`/gtk-%api_ver/%binary_ver
__CSH__

install -pD -m755 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -pD -m755 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%find_lang --output=gtk20.lang gtk20 gtk20-properties

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version
cp -a examples/ %buildroot/%_docdir/%name-devel-%version/

# rpm posttrans filetriggers
install -pD -m755 {%_sourcedir,%buildroot%_rpmlibdir}/gtk-icon-cache.filetrigger

# rpm posttrans filetrigger to update immodules cache
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%fulllibpath/immodules
grep -qs '^'\$dir'' && %_bindir/gtk-query-immodules-%api_ver --update-cache ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger

%files
%doc AUTHORS NEWS.bz2 README
%_libdir/libgdk-x11-%api_ver.so.*
%_libdir/libgtk-x11-%api_ver.so.*
%dir %_libdir/gtk-%api_ver
%dir %_libdir/gtk-%api_ver/modules
%dir %fulllibpath
%dir %fulllibpath/engines
%fulllibpath/engines/libpixmap.so
%dir %fulllibpath/immodules
%fulllibpath/immodules/im-*.so
%dir %fulllibpath/printbackends
%fulllibpath/printbackends/libprintbackend-*.so
%exclude %fulllibpath/*/*.la
%dir %_datadir/themes
%_datadir/themes/Default
%_datadir/themes/Emacs
%_datadir/themes/Raleigh
%dir %_datadir/gtk-%api_ver
%dir %_sysconfdir/gtk-%api_ver
%config(noreplace) %_sysconfdir/gtk-%api_ver/gtkrc
%config(noreplace) %_sysconfdir/gtk-%api_ver/im-multipress.conf
%ghost %_libdir/gtk-%api_ver/%binary_ver/immodules.cache
%_bindir/gtk-query-immodules-%api_ver
%_man1dir/gtk-query-immodules*
%_rpmlibdir/gtk-%api_ver-immodules-cache.filetrigger

%files locales -f gtk20.lang

%files -n gtk-update-icon-cache
%_bindir/gtk-update-icon-cache
%_man1dir/gtk-update-icon-cache*
%_rpmlibdir/gtk-icon-cache.filetrigger

%files -n gtk-builder-convert
%_bindir/gtk-builder-convert
%_man1dir/gtk-builder-convert*

%files devel
%dir %_includedir/gtk-%api_ver
%dir %_includedir/gtk-%api_ver/gdk
%_includedir/gtk-%api_ver/gdk/*.h
%dir %_includedir/gtk-%api_ver/gtk
%_includedir/gtk-%api_ver/gtk/*.h
%dir %_includedir/gtk-unix-print-%api_ver
%dir %_includedir/gtk-unix-print-%api_ver/gtk
%_includedir/gtk-unix-print-%api_ver/gtk/*.h
%dir %_libdir/gtk-%api_ver/include
%_libdir/gtk-%api_ver/include/*.h
%_libdir/libgdk-x11-%api_ver.so
%_libdir/libgtk-x11-%api_ver.so
%_pkgconfigdir/gdk-%api_ver.pc
%_pkgconfigdir/gtk+-%api_ver.pc
%_pkgconfigdir/gtk+-unix-print-%api_ver.pc
%_pkgconfigdir/gdk-x11-%api_ver.pc
%_pkgconfigdir/gtk+-x11-%api_ver.pc
%_datadir/aclocal/gtk-%api_ver.m4

%files -n gtk-demo
%_bindir/gtk-demo
%dir %_datadir/gtk-%api_ver/demo
%_datadir/gtk-%api_ver/demo/*

%files devel-doc
%_datadir/gtk-doc/html/gdk2
%_datadir/gtk-doc/html/gtk2

%files devel-doc-examples
%doc %_docdir/%name-devel-%version/examples

%files -n libgail
%_libdir/libgailutil.so.*
%_libdir/gtk-%api_ver/modules/libferret.so
%_libdir/gtk-%api_ver/modules/libgail.so
%exclude %_libdir/gtk-%api_ver/modules/*.la

%files -n libgail-devel
%_includedir/gail-1.0
%_libdir/libgailutil.so
%_pkgconfigdir/gail.pc

%files -n libgail-devel-doc
%_datadir/gtk-doc/html/gail-libgail-util

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif

%changelog
* Tue Jan 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.24.32-alt1
- 2.24.32

* Wed Sep 07 2016 Yuri N. Sedunov <aris@altlinux.org> 2.24.31-alt1
- 2.24.31 (CVE-2013-7447)

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 2.24.30-alt1
- 2.24.30

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.29-alt1
- 2.24.29

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.28-alt1
- 2.24.28

* Tue Mar 03 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.27-alt1
- 2.24.27

* Mon Feb 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.24.26-alt1
- 2.24.26

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 2.24.25-alt1
- 2.24.25

* Tue Jun 24 2014 Yuri N. Sedunov <aris@altlinux.org> 2.24.24-alt1
- 2.24.24

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 2.24.23-alt1
- 2.24.23

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.22-alt1
- 2.24.22

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.21-alt1
- 2.24.21

* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.20-alt1
- 2.24.20

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.19-alt1
- 2.24.19

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.18-alt1
- 2.24.18

* Mon Mar 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.17-alt1
- 2.24.17

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.16-alt1
- 2.24.16

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.15-alt1
- 2.24.15

* Thu Dec 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.14-alt2
- added rpm posttrans filetrigger to update im-modules cache (ALT #28278)

* Thu Dec 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.14-alt1
- 2.24.14

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.13-alt1
- 2.24.23

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.12-alt1
- 2.24.12

* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.11-alt1
- 2.24.11 release

* Sat May 19 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.11-alt0.1
- 2.24.11 snapshot (43c9a702c7)
- linked libgtk-x11-2.0 against libgmodule-2.0 explicitly
- removed gdk_keymap_get_caps_lock_state from libgtk+2-gdk.map

* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.10-alt1
- 2.24.10

* Wed Jan 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.9-alt1
- 2.24.9

* Fri Nov 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.8-alt1
- 2.24.8

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.7-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.7-alt1
- 2.24.7

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.6-alt1
- 2.24.6

* Mon Jun 20 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt2
- fixed GNOME bug #652872 

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt1
- 2.24.5

* Sat Apr 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt2
- updated buildreqs

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Feb 16 2011 Alexey Tourbin <at@altlinux.ru> 2.24.0-alt2
- merged libgtk+2-common into libgtk+2
- merged libgtk+2-common-devel into libgtk+2-devel
- split libgtk+2-locales noarch subpackage
- disabled symbol versioning

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Wed Jun 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4
- updated buildreqs

* Mon May 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt3
- fixed some gnome bugs (## 583273, 599617, 599618, 611313)
* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt2
- rebuild with new rpm-build-gir (0.2-alt1)

* Wed Mar 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.22.0

* Wed Mar 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.18.9-alt1
- 2.18.9

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.7-alt1
- 2.19.7

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.6-alt2
- rebuild using rpm-build-gir

* Wed Feb 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.6-alt1
- 2.19.6

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.5-alt1
- 2.19.5
- updated version script for GTK_2.19.5

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.4-alt1
- 2.19.4
- updated version script for GTK_2.19.4

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.19.3-alt1
- 2.19.3
- updated version script for GTK_2.19.3

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.2-alt1
- 2.19.2
- new gir{,-devel} subpackages
- updated version script for GTK_2.19.2

* Tue Dec 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Thu Oct 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.1-alt1
- 2.18.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.17.11-alt1
- 2.17.11

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.17.9-alt1
- 2.17.9

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.17.6-alt1
- 2.17.6
- updated version script for GTK_2.17.6
- updated buildreqs

* Mon Aug 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt3
- fixed http://bugzilla.gnome.org/show_bug.cgi?id=581526

* Tue Jul 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt2
- fixed ugly bug in regexp in gdk-pixbuf-query-loaders.filetrigger

* Sat Jul 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt1
- 2.16.5

* Thu Jul 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.4-alt1
- 2.16.4

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.3-alt2
- fixed posttrans filetrigger implemented in previous release

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.3-alt1
- 2.16.3
- gdk-pixbuf-query-loaders call moved from %%post to posttrans
  filetrigger (closes #20613)

* Tue Jun 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.2-alt2
- rebuild

* Sun May 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.2-alt1
- 2.16.2

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.1-alt1
- 2.16.1

* Sat Mar 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0
- updated version script for GTK_2.16.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.15.5-alt1
- 2.15.5
- updated version script for GTK_2.15.5

* Wed Feb 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.15.4-alt1
- 2.15.4

* Wed Jan 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.15.2-alt1
- 2.15.2
- updated version script for GTK_2.15.2

* Sat Jan 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.15.1-alt1
- 2.15.1
- updated version script for GTK_2.15.1

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.15.0-alt1
- 2.15.0
- updated version scripts

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.7-alt1
- 2.14.7

* Tue Dec 16 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.6-alt1
- 2.14.6

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.5-alt1
- 2.14.5
- drop upstreamed patches

* Sat Nov 15 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt4
- use %%_rpmlibdir instead %%_libdir/rpm
- overwrite an existing icon cache, even if up to date

* Fri Nov 14 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt3
- -common subpackage requires icon-theme-hicolor
- added gtk-update-icon-cache posttrans filetrigger
- don't call ldconfig in %%post{,un}

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt2
- some fixes from upstream

* Fri Oct 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.4-alt1
- 2.14.4

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.3-alt2
- libgail-devel-doc subpackage
- don't rebuild documentation
- clean unused parts of .spec

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.14.3-alt1
- 2.14.3
- add libgail package
- drop patch5(ALT#6243,GNOME#56070 - fixed in upstream)
- updated version scripts for shared libraries
- build %name-devel-doc as noarch
- build %name-devel-doc-examples as noarch

* Tue Jul 08 2008 Yuri N. Sedunov <aris@altlinux.org> 2.12.11-alt2
- don't requires gnome-icone-theme (altbug #16244)

* Wed Jul 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.12.11-alt1
- 2.12.11 

* Tue Jul 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.12.10-alt3
- fix window positions -- patch9.

* Sat Jun 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.12.10-alt2
- examples packaged as is 
- use gnome as a default gtk-icon-theme, gnome-icon-theme required
- export GTK_PATH and GDK_PIXBUF_MODULEDIR

* Sun Jun 08 2008 Yuri N. Sedunov <aris@altlinux.org> 2.12.10-alt1
- new version
- new devel-doc-examples subpackage
- fixed files packaged twice
- updated {Build,}Requires
- %%__autoreconf is obsolete, used %%autoreconf instead
- add Packager tag

* Mon Mar 10 2008 Alexey Rusakov <ktirf@altlinux.org> 2.12.8-alt2
- Moved gtk-builder-convert to -common-devel, addressing ALT Bug 13377.

* Tue Mar 04 2008 Alexey Rusakov <ktirf@altlinux.org> 2.12.8-alt1
- New version (2.12.8).
- Updated buildreqs.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.12.3-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.3-alt1
- New version (2.12.3).

* Thu Oct 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.1-alt1
- new version 2.12.1
- use rpm-build-gnome package

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.0-alt2
- fixed Adobe Flash failures in non-GTK browsers (ALT Bug #13124).
- use rpm-build-licenses.
- removed obsolete patches and sources from the source package.

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 2.12.0-alt1
- 2.10.14 -> 2.12.0
- update version scripts

* Wed Aug 08 2007 Alexey Rusakov <ktirf@altlinux.org> 2.10.14-alt1
- new version (2.10.14)
- removed patches that fix Makefiles, they are no more needed.
- updated cursor sensitivity patch to match the sources.
- updated files list (im-thai-broken.so dropped, im-thai.so is new)
- checked version scripts (found no changes after 2.10.6)
- eliminated %%__ macros

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.10.6-alt6
- fixed double-packaging of gtk-demo sources.

* Wed Oct 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.6-alt5
- fixed libgtk+2-common-devel depending on a backend.
- made libgtk+2-common, gtk-demo, and libgtk+2-devel-doc packages compile
  only for X11 backend, as a temporary workaround to problems with binaries
  that depend on backend-specific libraries.

* Sun Oct 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.6-alt4
- added patches and missing source files to make Gtk+ compile with
  DirectFB backend.

* Fri Oct 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.6-alt3
- Fixed bad installation dependencies, now -common subpackage is PreReq'ed.

* Thu Oct 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.6-alt2
- fixed post/postun/triggerpostun scripts that appeared in a wrong package.

* Wed Oct 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.6-alt1
- new version (2.10.6)

* Mon Oct 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.4-alt1
- new version (2.10.4)
- the specfile is rewritten; now it is possible to build GTK+ either with
  X11 or with DirectFB backend. The generated packages are made as
  non-conflicting as possible, to allow installation of GTK-X11 and
  GTK-DirectFB side-by-side. -devel subpackages, however, conflict each
  other.

* Wed Sep 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.3-alt1
- new version
- removed ChangeLog.pre* files from packaging.

* Fri Aug 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.2-alt1
- new version 2.10.2 (with rpmrb script)

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.1-alt1
- new version (2.10.1)
- updated version scripts
- made the list of files more accurate

* Mon Jul 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.0-alt1
- new version
- removed Lai's patches as outdated.

* Mon May 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.18-alt1
- new version

* Sat Apr 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.17-alt1
- new version (2.8.17)

* Sat Mar 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.16-alt1
- new version 2.8.16 (with rpmrb script)

* Tue Mar 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.15-alt1
- new version (2.8.15)

* Thu Mar 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.14-alt1
- new version (2.8.14)

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.12-alt1
- new version

* Sun Jan 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.11-alt1
- new version

* Mon Jan 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.10-alt1
- new version
- updated dependencies.

* Mon Nov 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.8-alt1
- new version

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.7-alt2
- new version

* Sat Oct 08 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.6-alt2
- Restored symbol maps that were introduced in 2.8.3-alt2 and lost
  afterwards.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.6-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.5-alt1
- new version

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 2.8.3-alt2
- NMU: introduced GDK_PRIVATE ABI interface for gdk_*_libgtk_only
  functions in libgdk-x11-2.0.so.0; GDK_2.8 ABI interface for new
  functions in libgdk-x11-2.0.so.0 and libgdk_pixbuf-2.0.so.0;
  GTK_2.8 ABI interface for new functions in libgtk-x11-2.0.so.0

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Wed Apr 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.7-alt1
- 2.6.7

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.6-alt1
- 2.6.6
- updated Lai-gtkfilesel patch.
- do not run gtk-update-icon-cache in /usr/share/icons too.

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sat Feb 05 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Tue Feb 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt2
- run gtk-update-icon-cache daily.

* Sun Jan 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Dec 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Dec 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6
- documentation moved to devel-doc subpackage.

* Sat Nov 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Fri Sep 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1.1
- Fixed few potential overflows (CAN-2004-0782, CAN-2004-0783),
  patch from Matthias Clasen (RH).

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Thu Aug 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.9-alt1
- 2.4.9

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Mon Jun 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1.1
- fix #5547.

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Lai-gtkfilesel patch adopted, as usual, by Alexey Morozov.

* Fri Apr 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Apr 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1.1
- Applied Lai's GTK+ File Selector patch for 2.2.4 to 2.4.0 (Alexey Morozov)

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6
- prereqs XFree86-libs (close #3795).

* Wed Mar 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Feb 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri Jan 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Dec 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt4
- do not package .la files.
- remove fileselector patch. Some software on some systems crashes with it.

* Fri Nov 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt3
- Enhanced file selector patch
  (http://members1.chello.nl/~h.lai/gtkenhancements/).
- /etc/profile.d/gtk+.{sh,csh} setup some environment variables
   to tune fileselector.

* Mon Oct 20 2003 Rider <rider@altlinux.ru> 2.2.4-alt2
- removed val-ttf bad requires

* Thu Sep 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2
- Updated descriptions and summaries (mhz).

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Dec 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt0.5
- 2.1.4

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt0.5
- 2.1.3

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt0.5
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt0.6
- 2.1.1
- build section fixed (SMP-incompatible build).
- Run gdk-pixbuf-query-loaders in %%post
- Editing of menu accelerators enabled by default.
- %_libdir/gtk-2.0/%%binary_ver/engines directory owned by libgtk+2.

* Wed Oct 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt0.5
- 2.1.0 with Xft2 support.
- some RH patches removed (in mainstream now)

* Tue Oct 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt0.8
- lib{pango,atk}-devel added to %name-devel requires list (#1233).
- Some RH patches.

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt0.7
- 2.06
- fixed-ltmain.sh removed, not needed more.
- changed --with-xinput=yes to --with-xinput=xfree.
- post/postun scripts improved.
- cleanups.

* Sun Jun 16 2002 Igor Androsov <blake@altlinux.ru> 2.0.5-alt1
- New version
- Added ru summary
- man moved to devel package
- Added gxid daemon to package

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt2.1
- Moved *.la from static to devel package
- Fix changelog of <Wed May 29 2002>
- Removed libgtk+2-devel-static, in current time GTK+ disabled static build
- Fix BuildRequires list

* Wed May 29 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt2
- Added from AEN package "fixed-ltmain.sh" - fix not building package if host wheare building not hace libgtk+2-devel.

* Wed May 29 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt1
- New Release

* Wed May 22 2002 Igor Androsov <blake@altlinux.ru> 2.0.2-alt1
- New version
- Change SPEC, based on AEN spec
- No test program in rpm
- Buildrequires by buldreq

