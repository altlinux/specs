%define ver_major 3.4
%def_disable debug
%def_disable lzma

Name: yelp
Version: %ver_major.2
Release: alt1

Summary: Lightweight help browser for GNOME
License: %gpl2plus
Group: Graphical desktop/GNOME
URL: http://live.gnome.org/yelp
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.in
%define gio_ver 2.28.5
%define gtk_ver 3.0.5
%define xslt_ver 1.1.4
%define webkit_ver 1.3.2
%define yelpxsl_ver 3.3.92
%define intltool_ver 0.41.0

Requires: lib%name = %version-%release
Requires: yelp-xsl >= %yelpxsl_ver

BuildPreReq: rpm-build-licenses rpm-build-gnome gnome-common intltool >= %intltool_ver itstool gtk-doc
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libxslt-devel >= %xslt_ver
BuildPreReq: libwebkitgtk3-devel >= %webkit_ver
BuildPreReq: yelp-xsl >= %yelpxsl_ver
BuildRequires: zlib-devel bzlib-devel libsqlite3-devel
%{?_enable_lzma:BuildRequires: liblzma-devel}

%description
Yelp is a help browser for the GNOME desktop. Yelp provides
a simple graphical interface for viewing DocBook, HTML, man, and info
formatted documentation. The name Yelp was suggested by Daniel Lundin.
Yelp is pronounced the same as the swedish word for 'help'.

%package -n lib%name
Summary: Shared library for Yelp
Group: System/Libraries

%description -n lib%name
Yelp is a help browser for the GNOME desktop. Yelp provides
a simple graphical interface for viewing DocBook, HTML, man, and info
formatted documentation.

This package provides shared library required for dconf to work

%package -n lib%name-devel
Summary: Development files for Yelp library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Yelp is a help browser for the GNOME desktop. Yelp provides
a simple graphical interface for viewing DocBook, HTML, man, and info
formatted documentation.

This is a Yelp development package. Contains files needed for doing
development using Yelp.

%package -n lib%name-devel-doc
Summary: Development documentation for Yelp library
Group: Development/C
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
Yelp is a help browser for the GNOME desktop. Yelp provides
a simple graphical interface for viewing DocBook, HTML, man, and info
formatted documentation.

This package contains documentation needed for doing development using
Yelp.


%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-schemas-compile \
	%{subst_enable debug} \
	%{subst_enable lzma}

%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name
%_datadir/yelp-xsl/xslt/common/domains/yelp.xml
%config %_datadir/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%doc AUTHORS README NEWS TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
#%_libdir/pkgconfig/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Sep 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.3-alt1
- 3.1.3

* Sat Jun 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt4
- build against xulrunner-2.0.1

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt3
- use g_build_filename to avoid missing slash problem
- added schemehandler information to the desktop file

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- fixed for xulrunner-2.0

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt4
- beagle support disabled

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.2-alt1
- 2.29.2

* Wed Jan 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- 2.29.1

* Sat Nov 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt2
- removed broken pregenerated yelp.schemas from source

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- lzma support disabled

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5

* Sun Mar 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt2
- updated buildreqs
- removed obsolete %%post{,un} calls

* Mon Sep 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- new version

* Wed Sep 03 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.91-alt1
- new version
- Used man-show-source implemented by legion@ in man-1.6f-alt5 package to
  fix reopened #15648 (patch10)
- patch3 from Fedora (gnome bug #497559)

* Sun Aug 31 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt3
- hack to fix man encoding -- patch9 (altbugs ##15648, 16795).

* Thu Aug 07 2008 Alexey Rusakov <ktirf@altlinux.org> 2.23.1-alt2.1
- Plugged the security hole (see https://bugs.launchpad.net/bugs/254860 for
  details).

* Tue Jul 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt2
- fixed %%build, many thanks legion@

* Sun Jul 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- jump to 2.23
- built against xulrunner
- removed Patch10 (yelp-2.22.0-beagle-0.3.0.patch) - ready to beagle-0.3.0

* Tue Jun 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt2
- Require docbook-dtds (#15943)
- Require gnome-doc-utils-xslt (#15734)
- change online url search to search.altlinux.org

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- remove requires beagle-crawl-system (#15167)
- add update/clean menus

* Sun Mar 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Sat Dec 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.21.1-alt2
- Removed explicit (and unnecessary) runtime dependency on gnome-doc-utils.
- Use a license macro.
- Spec cleanup around %%makeinstall invocation.

* Wed Dec 12 2007 Alexey Shabalin <shaba@altlinux.ru> 2.21.1-alt1
- new version (2.21.1) (for 2.20.0 need rarian-0.6.0, but ALTLinux have rarian-0.7.0)
- update buildreq
- register docbook mime type for yelp (patch2)
- strip newline from title (patch4)
- patch to define langs before using (patch6)
- fix build with beagle-0.3.0 (patch10)

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- use macros from rpm-build-gnome
- yelp-pregenerate is not needed for as long as 3 years, so is removed.

* Tue Feb 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version (2.16.2)

* Sat Oct 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt2
- fixed building on x86_64.

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version 2.16.1
- switched to xulrunner

* Fri Sep 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt2
- rebuild with new Firefox.

* Tue Sep 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0 (with rpmrb script)

* Sat Aug 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)

* Tue Aug 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.5-alt1
- new version 2.15.5 (GNOME 2.16 beta)
- switched from Mozilla to Firefox (does it build?)

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Tue Apr 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Fri Mar 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)

* Wed Mar 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt2
- Fixed Gecko provider macros.

* Fri Feb 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt1
- new version (2.13.5)
- removed Debian stuff
- added Beagle switch (does nothing yet)
- added Gecko provider switch.

* Mon Jan 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Nov 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Mon Nov 21 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Added rpath hack to the build due to Bug #8530.

* Sat Sep 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- 2.12.1

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.

* Mon Sep 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Fri Apr 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.3-alt1.1
- build current cvs snapshot.

* Fri Jan 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Mon Jan 03 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Aug 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Jul 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1.1
- updated buildreqs to make buildable.

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Tue Nov 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Sep 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt1
- 1.0.6
- Group changed.

* Fri Jun 21 2002 Igor Androsov <blake@altlinux.ru> 1.0.1-alt1
- New version
- Fix Requires and BuildPreReq section
- Fix files section
- Cosmetic changes spec

* Wed Jun 19 2002 Igor Androsov <blake@altlinux.ru> 1.0-alt1
- Initial build for AltLinux
- Added make_build
- Added Icons for Menu
- Added menu file

* Sun May 19 2002 Igor Androsov <blace@mail.ru> 0.7.0-blk1
- New version from CVS
- Created spec
