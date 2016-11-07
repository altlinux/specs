%def_enable introspection
%define ver_major 9.0
%define api_ver 2.90
%define unicode_ver 9.0.0

Name: gucharmap
Version: %ver_major.2
Release: alt1

Summary: gucharmap is a featureful Unicode character map
License: %gpl3plus
Group: Text tools

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
#http://www.unicode.org/Public/%unicode_ver/ucd/

# From configure.ac
%define glib_ver 2.32.0
%define gtk_ver 3.4.0

Requires: lib%name = %version-%release
Requires: dconf gnome-icon-theme

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.ac
BuildPreReq: intltool >= 0.40.0
BuildPreReq: unicode-ucd >= %unicode_ver unzip
BuildRequires: gnome-common desktop-file-utils appdata-tools
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: yelp-tools itstool
BuildPreReq: gtk-doc >= 1.0
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+3-gir-devel}

%description
This package provides a featureful Unicode character map for GNOME.

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
%setup

%build
%configure \
    --disable-static \
    --disable-schemas-compile \
    %{subst_enable introspection} \
    --with-unicode-data=%_datadir/unicode/ucd
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%config %_datadir/glib-2.0/schemas/org.gnome.Charmap.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.Charmap.enums.xml
%_datadir/appdata/%name.appdata.xml
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
* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.2-alt1
- 9.0.2

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.1-alt1
- 9.0.1

* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 8.0.1-alt1
- 8.0.1

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- 8.0.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Aug 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.13.90-alt1
- 3.13.90

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.99-alt1
- 3.9.99

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.99-alt1
- 3.5.99

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

