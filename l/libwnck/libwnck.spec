%define ver_major 2.31
%def_enable introspection
%def_disable static
%def_disable debug

Name: libwnck
Version: %ver_major.0
Release: alt1

Summary: libwnck is a Window Navigator Construction Kit
License: %lgpl2plus
Group: System/Libraries
URL: ftp://ftp.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Provides: %{name}2.22 = %version-%release
Provides: %{name}2.20 = %version-%release
Obsoletes: %{name}2.22
Obsoletes: %{name}2.20

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.in
BuildPreReq: intltool >= 0.40.0
BuildPreReq: gnome-common
BuildPreReq: libstartup-notification-devel >= 0.4
BuildPreReq: libX11-devel libXres-devel libXext-devel libXt-devel
BuildPreReq: libgtk+2-devel >= 2.19.7
BuildPreReq: glib2-devel >= 2.16.0
BuildPreReq: gtk-doc >= 1.9
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libcairo-gobject-devel libgtk+2-gir-devel}

%description
libwnck is Window Navigator Construction Kit, i.e. a library to use for
writing pagers and taskslists and stuff.

This library is a part of the GNOME 2 platform.

%package devel
Summary: Header and development libraries for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: %{name}2.22-devel = %version-%release
Provides: %{name}2.20-devel = %version-%release
Obsoletes: %{name}2.22-devel
Obsoletes: %{name}2.20-devel

%description devel
This package contains header and development libraries for %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Window Navigator Construction Kit library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Window Navigator Construction Kit library

%if_enabled static
%package devel-static
Summary: Static libraries and objects for %name
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
This package contains the General Window Manager interfacing static
libraries and objects.
%endif

%prep
%setup -q

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable introspection}

%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/wnck-urgency-monitor
%_bindir/wnckprop
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*

%files gir-devel
%_datadir/gir-1.0/*
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Mar 05 2012 Yuri N. Sedunov <aris@altlinux.org> 2.31.0-alt1
- 2.31.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.7-alt2
- used %%autoreconf to fix RPATH problem

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.7-alt1
- 2.30.7

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt2
- rebuild for debuginfo

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt1
- 2.30.6

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt2
- rebuild for update dependencies

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- updated rotate-windowlist patch
- introspection support

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Feb 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5

* Sun Jan 04 2009 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt3
- Re-updating the patch from the previous build (-alt2 contained the older
  version of the patch, that still was buggy).
- Added Packager tag (thanks to repocop for reminding).

* Mon Dec 08 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt2
- Updated the patch for a tasklist on vertical panels; hopefully, the
  issue is finally fixed.
- Added debug switch, disabled by default.
- Minor cleanup (using macros from rpm-build-compat).

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- New version (2.24.0).
- Rename from lib%name%%ver_major to %name
- build devel-doc as noarch

* Tue Apr 08 2008 Alexey Rusakov <ktirf@altlinux.org> 2.22.1-alt1
- New version (2.22.1).

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 2.22.0-alt1
- New version (2.22.0).
- Added a patch for a tasklist on vertical panels (GNOME Bug 86382).

* Mon Oct 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- new version (2.20.1)
- updated dependencies, use a license macro
- try to conform to DSO packages naming policy

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)

* Sat Jun 30 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt2
- added a patch for GNOME Bug 412887.

* Thu Jun 28 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- mention gtk-doc files in the files list more correctly.
- add gtk-doc to Requires of -devel, since it contains gtk-doc files.

* Wed Jun 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt2
- fixed building on x86_64.

* Wed Jun 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- spec cleanup, updated dependencies

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Sun Aug 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Tue Mar 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Thu Feb 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- updated dependencies

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92.1-alt1
- 2.9.92.1.

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90.

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0.1-alt1
- 2.8.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2.1-alt1
- 2.6.2.1

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Feb 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Tue Dec 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.17-alt1
- fix changelog entry

* Thu Jun 20 2002 Igor Androsov <blake@altlinux.ru> 0.14-alt1
- Initial build for AltLinux
- Many fixes spec

* Wed May 15 2002 Igor Androsov <blace@mail.ru> 0.11-blk0.1
- New source from CVS
- Added BuildRequires

* Sat May 11 2002 Igor Androsov <blace@mail.ru> 0.9-blk0.1
- New source from CVS
- Minor fixes .spec file
- Moved static libraries to devel-static

* Mon Jan 28 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 0.2-3
- cleaned up dependancies, according to docs that Chris sent me.
- disabled libtoolize

* Sat Jan 19 2002 Chris Chabot <chabotc@reviewboard.com>
- Changed description from 'atk' to 'libwnck' ;)
- Modified configure, make, make install and clean parts
- Added a lot of Requires and BuildRequires (as defined by ./configure)
- Changed description from 'windowmanager thingies' to something more usefull
- Modified change log entry below from 'Jun 16 2002' to 'Jan 16', duh
- Minor cleanups

* Tue Jan 16 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- created new spec file

