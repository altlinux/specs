%define ver_major 2.3
%def_disable static

Name: libart_lgpl
Version: %ver_major.21
Release: alt3

Summary: Library of graphics routines used by libgnomecanvas
Group: System/Libraries
License: LGPLv2+
Url: http://www.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Source: ftp://ftp.gnome.org/pub/gnome/sources/libart_lgpl/%ver_major/libart_lgpl-%version.tar.bz2

%description
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.

%package devel
Summary: Libraries and headers for libart_lgpl
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.
This package it`s a development package, need for writing and compile
software using libart_lgpl

%package devel-static
Summary: Static libraries for libart_lgpl
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.
This package it`s static libraries

%prep
%setup

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.21-alt3
- Updated license information.
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.3.21-alt2
- rebuild for set-version

* Fri Apr 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.3.21-alt1
- 2.3.21
- remove useless buildreqs

* Tue Sep 22 2009 Alexey Shabalin <shaba@altlinux.ru> 2.3.20-alt2
- drop obsoleted post scripts
- add Packager

* Thu Oct 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.3.20-alt1
- 2.3.20

* Fri Apr 06 2007 Victor Forsyuk <force@altlinux.org> 2.3.19-alt1
- 2.3.19

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.17-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sat Jan 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.3.17-alt1
- 2.3.17.
- do not build devel-static subpackage by default.

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.16-alt2
- don't package .la files.

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.16-alt1
- 2.3.16

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.15-alt1
- 2.3.15

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.14-alt1
- 2.3.14

* Fri Jul 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.13-alt1
- 2.3.13

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.12-alt1
- 2.3.12

* Mon Nov 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.3.11-alt1
- 2.3.11

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.3.10-alt1
- 2.3.10

* Thu Jun 27 2002 Igor Androsov <blake@altlinux.ru> 2.3.9-alt1
- New release

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 2.3.8-alt1.1
- Moved *.la from static to devel package

* Thu May 23 2002 Igor Androsov <blake@altlinux.ru> 2.3.8-alt1
- Build for AltLinux

* Wed May 09 2002 Igor Androsov <blace@mail.ru> 2.3.8-blk0.2
- New version from CVS

* Wed May 08 2002 Igor Androsov <blace@mail.ru> 2.3.8-blk0.1
- New sources from CVS
- Changes for AltLinux
- Moved static libs to devel-static

* Tue Jan 22 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- removed conflicts line from devel package
- disable libtoolize, as it's on crack
- added %%doc files
- replaced files sections with the ones from elsewhere
- removed tabs from header

* Sat Jan 19 2002 Chris Chabot <chabotc@reviewboard.com>
- Imported into gnome 2.0 alpha
- Changed versions accordingly
- Minor cleanups

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.7.91 snap

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild with new glib

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- 2.3.6

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new CVS snap with upstream changes merged

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- Initial build.

