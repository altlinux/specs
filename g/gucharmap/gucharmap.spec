%def_enable introspection
%define ver_major 3.4
%define api_ver 2.90

Name: gucharmap
Version: %ver_major.1.1
Release: alt1

Summary: gucharmap is a featureful Unicode character map
License: %gpl3plus
Group: Text tools

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.ac
%define glib_ver 2.28.0
%define gtk_ver 3.0.5

Requires: lib%name = %version-%release
Requires(post,preun): GConf

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.ac
BuildPreReq: intltool >= 0.40.0
BuildPreReq: gnome-common
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gnome-doc-utils >= 0.9.0
BuildPreReq: gtk-doc >= 1.0
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+3-gir-devel}

%description
This package provides a featureful Unicode character map for GNOME2.

%package -n lib%name
Summary: Shared library needed to run %name
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

%prep
%setup -q

%build
%configure \
    --disable-scrollkeeper \
    --disable-static \
    --disable-schemas-compile \
    %{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%config %_datadir/glib-2.0/schemas/org.gnome.Charmap.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.Charmap.enums.xml
%doc AUTHORS NEWS README TODO COPYING.UNICODE

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Gucharmap-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Gucharmap-%api_ver.gir
%endif

%changelog
* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1.1-alt1
- 3.4.1.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Fri Jan 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- updated buildreqs

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Mar 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- introspection support
- new python-module-gucharmap subpackage

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3.1-alt1
- 2.26.3.1

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Thu Oct 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- New version (2.24.0).

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gucharmap

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- New version (2.22.1).

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- New version (2.22.0).

* Wed Dec 19 2007 Alexey Rusakov <ktirf@altlinux.org> 1.10.1-alt1
- New version (1.10.1).
- Use license macro.
- Added license files to the packages (notably, COPYING.UNICODE).

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 1.10.0-alt1
- new version (1.10.0)
- updated dependencies
- spec cleanup

* Fri Sep 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.8.0-alt1
- new version 1.8.0
- updated dependencies
- removed ALL_LINGUAS fix, as it's not needed anymore.
- removed scrollkeeper workaround in the specfile.

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.0-alt2
- new version
- fixed ALL_LINGUAS initialization.
- should also build on x86_64.

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Mon Feb 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.3-alt1
- new version (1.5.3)
- updated dependencies, cleaned up the spec
- removed Debian menu stuff

* Tue Jan 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.1-alt1
- new version

* Sun Jan 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.0-alt2
- updated dependencies due to X.org 7.0.
- use %%__autoreconf instead of auto-bundle.

* Sat Jan 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.5.0-alt1
- new version

* Fri Oct 07 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.4-alt2
- Fixed a group of the menu item (Bug #4426).

* Sun Sep 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt0.5
- 1.4.1

* Thu Mar 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.1-alt0.5
- 1.3.1

* Sun Dec 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt0.5
- 1.2.0
- do not package .la files.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt0.5
- 1.0.0

* Fri Aug 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt0.5
- 0.9.0

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt0.5
- 0.8.0

* Sun May 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt0.5
- First build for Sisyphus.

