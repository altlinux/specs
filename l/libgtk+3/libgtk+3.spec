%define _name gtk+
%define ver_major 3.4
%define api_ver 3.0
%define binary_ver 3.0.0

%def_enable xkb
%def_disable static
%def_disable gtk_doc
%def_enable man
%def_enable introspection
%def_enable colord
%def_disable wayland

Name: libgtk+3
Version: %ver_major.4
Release: alt1

Summary: The GIMP ToolKit (GTK+)
Group: System/Libraries
License: %lgpl2plus
Url: http://www.gtk.org
Icon: gtk+-logo.xpm
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
Patch: gtk+-2.16.5-alt-stop-spam.patch

%define glib_ver 2.32.2
%define cairo_ver 1.10
%define pango_ver 1.30.0
%define atk_ver 1.30
%define pixbuf_ver 2.26.0
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.6
%define colord_ver 0.1.9

# We need to prereq these so we can run gtk-query-immodules-%api_ver in post
PreReq: glib2 >= %glib_ver
PreReq: libpango >= %pango_ver
PreReq: libatk >= %atk_ver

Requires: gtk-update-icon-cache
Requires: icon-theme-hicolor
%{?_enable_colord:Requires: colord}

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildPreReq: glib2-devel >= %glib_ver libgio-devel
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libcairo-gobject-devel >= %cairo_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libatk-devel >= %atk_ver
BuildPreReq: libgdk-pixbuf-devel >= %pixbuf_ver
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
BuildRequires: gtk-update-icon-cache docbook-utils libcups-devel zlib-devel

BuildRequires: libXdamage-devel libXcomposite-devel libX11-devel libXcursor-devel
BuildRequires: libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel
BuildRequires: libXrender-devel libXt-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libpango-gir-devel libatk-gir-devel >= %atk_ver libgdk-pixbuf-gir-devel}
%{?_enable_colord:BuildRequires: libcolord-devel >= %colord_ver}
%{?_enable_wayland:BuildRequires: libwayland-client-devel libEGL-devel libwayland-egl-devel libxkbcommon-devel}

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains X11 part of GTK+. It is required for GNOME 3 desktop
and programs.

%package devel
Summary: Development files and tools for GTK+ applications
Group: Development/GNOME and GTK+
Icon: gtk+-devel-logo.xpm
Requires: %name = %version-%release
Requires: gtk-builder-convert

%description devel
This package contains development files for GTK+, X11 version. Use this to
build programs that use GTK+.

%package -n gtk3-demo
Summary: GTK+ widgets demonstration program
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gtk3-demo
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains a program, along with its source code, that
demonstrates GTK+ variety of all its widgets.

%package -n %name-devel-doc
Summary: Development documentation for GTK+
Group: Development/Documentation
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description -n %name-devel-doc
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains documentation needed for developing GTK+ applications.

%package -n %name-devel-doc-examples
Summary: Examples for developing applications which will use GTK+
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description -n %name-devel-doc-examples
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains sources for example programs.

%package -n %name-devel-static
Summary: Static libraries for GTK+ (GIMP ToolKit) applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n %name-devel-static
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
This package contains the static libraries for GTK+.

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

%description gir-devel
GObject introspection devel data for the GTK+ library

%package -n libgail3
Summary: Accessibility implementation for GTK+ and GNOME libraries
Group: System/Libraries
Requires: %name = %version-%release

%description -n libgail3
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME libraries,
enabling accessibility technologies such as at-spi to access those GUIs.

%package -n libgail3-devel
Summary: Files to compile applications that use GAIL
Group: Development/GNOME and GTK+
Requires: libgail3 = %version-%release
Requires: %name-devel = %version-%release

%description -n libgail3-devel
This package contains the files required to develop applications against
the GAIL libraries.

%package -n libgail3-devel-static
Summary: Static libraries of GAIL
Group: Development/GNOME and GTK+
Requires: libgail3-devel = %version-%release

%description -n libgail3-devel-static
This package contains the libraries required to compile applications
statically linked against the GAIL libraries.

%package -n libgail3-devel-doc
Summary: Development documentation for GAIL
Group: Development/Documentation
Conflicts: libgail3-devel < %version-%release
BuildArch: noarch

%description -n libgail3-devel-doc
GAIL implements the abstract interfaces found in ATK for GTK+ and GNOME
libraries, enabling accessibility technologies such as at-spi to access
those GUIs.

This package contains development documentation for GAIL.


%define fulllibpath %_libdir/gtk-%api_ver/%binary_ver

%prep
%setup -q -n %_name-%version
%patch -p1

%build
%{?_disable_static:export lt_cv_prog_cc_static_works=no}
%{?_enable_static:export lt_cv_prog_cc_static_works=yes}

export CFLAGS="$CFLAGS $(freetype-config --cflags)"
export LDLIBS="$LDLIBS $(freetype-config --libs)"

%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable man} \
    --enable-x11-backend \
    %{subst_enable xkb} \
    --disable-schemas-compile \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --enable-gtk2-dependency \
    %{subst_enable colord} \
    %{?_enable_wayland:--enable-wayland-backend}

%make_build

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

# The license
ln -sf %_licensedir/LGPL-2 COPYING

%find_lang --output=gtk30.lang gtk30 gtk30-properties
%find_lang --output=gail.lang gail

bzip2 -9f NEWS

mkdir %buildroot%_libdir/gtk-%api_ver/modules

# examples
mkdir -p %buildroot/%_docdir/%name-devel-%version/examples
cp examples/*.c examples/Makefile* %buildroot/%_docdir/%name-devel-%version/examples/

%post
%_bindir/gtk-query-immodules-%api_ver --update-cache

%files -f gtk30.lang
%_bindir/gtk-query-immodules-%api_ver
%_libdir/libgdk-3.so.*
%_libdir/libgtk-3.so.*
%dir %_libdir/gtk-%api_ver/modules
%dir %fulllibpath
%dir %fulllibpath/engines
%dir %fulllibpath/immodules
%fulllibpath/immodules/im-am-et.so
%fulllibpath/immodules/im-cedilla.so
%fulllibpath/immodules/im-cyrillic-translit.so
%fulllibpath/immodules/im-inuktitut.so
%fulllibpath/immodules/im-ipa.so
%fulllibpath/immodules/im-thai.so
%fulllibpath/immodules/im-ti-er.so
%fulllibpath/immodules/im-ti-et.so
%fulllibpath/immodules/im-viqr.so
%fulllibpath/immodules/im-multipress.so
%fulllibpath/immodules/im-xim.so
%dir %fulllibpath/printbackends
%fulllibpath/printbackends/libprintbackend-*.so
%dir %_datadir/themes/*/gtk-%{api_ver}*
%_datadir/themes/*/gtk-%{api_ver}/*.css
%dir %_sysconfdir/gtk-%api_ver
%config(noreplace) %_sysconfdir/gtk-%api_ver/gtkrc
%config(noreplace) %_sysconfdir/gtk-%api_ver/im-multipress.conf
#%config(noreplace) %_sysconfdir/profile.d/*
%ghost %_libdir/gtk-%api_ver/%binary_ver/immodules.cache
%_man1dir/gtk-query-immodules*
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%doc --no-dereference COPYING
%doc AUTHORS NEWS.bz2 README

%files devel
%_includedir/gtk-%api_ver/
%_libdir/libgdk-3.so
%_libdir/libgtk-3.so
%_pkgconfigdir/gtk+-%api_ver.pc
%_pkgconfigdir/gtk+-x11-%api_ver.pc
%_pkgconfigdir/gdk-%api_ver.pc
%_pkgconfigdir/gdk-x11-%api_ver.pc
%_pkgconfigdir/gtk+-unix-print-%api_ver.pc
%dir %_datadir/gtk-%api_ver
%_datadir/gtk-%api_ver/gtkbuilder.rng
%_datadir/aclocal/gtk-%api_ver.m4
%exclude %_datadir/gtk-%api_ver/demo

%if_enabled wayland
#%_includedir/gtk-%api_ver/gdk/gdkwayland.h
%_pkgconfigdir/gtk+-wayland-%api_ver.pc
%_pkgconfigdir/gdk-wayland-%api_ver.pc
%endif

%files -n gtk3-demo
%_bindir/gtk3-demo
%_bindir/gtk3-demo-application
%_bindir/gtk3-widget-factory
%dir %_datadir/gtk-%api_ver/demo
%_datadir/gtk-%api_ver/demo/*
%_datadir/glib-2.0/schemas/org.gtk.Demo.gschema.xml

%files devel-doc
%_datadir/gtk-doc/html/*
%exclude %_datadir/gtk-doc/html/gail-libgail-util3

%files devel-doc-examples
%doc %_docdir/%name-devel-%version/examples

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%fulllibpath/*/*.a

%files -n libgail3-devel-static
%_libdir/libgailutil.a
%endif

%files -n libgail3 -f gail.lang
%_libdir/libgailutil-3.so.*

%files -n libgail3-devel
%_includedir/gail-%api_ver
%_libdir/libgailutil-3.so
%_pkgconfigdir/gail-%api_ver.pc

%files -n libgail3-devel-doc
%_datadir/gtk-doc/html/gail-libgail-util3

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%exclude %fulllibpath/*/*.la

%changelog
* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.4-alt1
- 3.4.4 release

* Wed May 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt2
- updated from upsream git

* Sat May 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.20-alt2
- rebuilt against newest libX11/libXi/cairo

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.20-alt1
- 3.3.20

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.4-alt1
- 3.2.4

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Sat Nov 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sat Oct 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.12-alt1
- 3.0.12

* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.11-alt1
- 3.0.11

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.10-alt1
- 3.0.10

* Fri Apr 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.9-alt1
- 3.0.9

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Sun Apr 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt2
- applied some fixes from upstream git

* Sat Apr 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.7-alt1
- 3.0.7

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5
- updated buildreqs

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon Mar 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Feb 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.3-alt1
- 2.99.3

* Wed May 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.1-alt1
- 2.90.1

* Tue May 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.0-alt1
- first build for Sisyphus

