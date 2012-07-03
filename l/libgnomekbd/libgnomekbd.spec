%define ver_major 3.4
%def_enable introspection

Name: libgnomekbd
Version: %ver_major.0.1
Release: alt2

Summary: GNOME keyboard shared library
License: %lgpl2plus
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch: %name-3.4.0.1-drop_wrong_free_calls.patch
Patch1: %name-3.4.0-install.patch

Obsoletes: gnome-kbd-indicator < 2.22.0
Provides: gnome-kbd-indicator = %version-%release

%define glib_ver 2.28.0
%define gtk_ver 2.91.6
%define libxklavier_ver 5.2.1

BuildPreReq: rpm-build-gnome >= 0.4
BuildPreReq: rpm-build-licenses

# from configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libxklavier-devel >= %libxklavier_ver
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libX11-devel libXt-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+3-gir-devel libxklavier-gir-devel}

%description
GNOME keyboard shared library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
GNOME keyboard shared library.

This is package contain development files for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GNOME keyboard library

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GNOME keyboard library

%prep
%setup -q
%patch
%patch1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%check
%make check

%files -f %name.lang
%_libdir/lib*.so.*
%doc AUTHORS NEWS

%_bindir/gkbd-keyboard-display
%_desktopdir/gkbd-keyboard-display.desktop
%_datadir/%name
%config %_datadir/glib-2.0/schemas/org.gnome.libgnomekbd.desktop.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.libgnomekbd.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.libgnomekbd.keyboard.gschema.xml
%_datadir/GConf/gsettings/%name.convert

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir
%endif

%changelog
* Thu Apr 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt2
- fixed install

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- used %%autoreconf to fix RPATH problem

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.1-alt1
- 3.0.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt1
- 2.91.92

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Jun 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sat Apr 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sun Mar 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt2
- don't use flags in keyboard indicator by default

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Jan 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Sun Dec 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.4-alt1
- 2.27.4
- updated buildreqs

* Sat Mar 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete %%post{,un}_ldconfig
- updated buildreqs

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)
- libgnomekbd contain gnome-kbd-indicator(#14112)

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.4.1-alt1.1
- build for Sisyphus
- build with libxklavier-0.35

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.4.1-alt1
- new version (2.21.4.1)

* Tue Sep 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt1
- new version (2.20.0)
- use macros from rpm-build-gnome and rpm-build-licenses
- gnome-kbd-indicator now depends on a specific version-release of
  libgnomekbd
- updated dependencies
- changed group of libgnomekbd (it is more of GNOME, than system libraries)

* Thu Jul 05 2007 Igor Zubkov <icesik@altlinux.org> 2.18.2-alt2
- apply fixes from ktirf@

* Tue Jun 05 2007 Igor Zubkov <icesik@altlinux.org> 2.18.2-alt1
- 2.18.1 -> 2.18.2
- add proper build requires with versions from configure.in

* Wed May 09 2007 Igor Zubkov <icesik@altlinux.org> 2.18.1-alt1
- build for Sisyphus


