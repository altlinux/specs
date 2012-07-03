%define ver_major 2.30
%def_disable static
%def_disable gtk_doc
%def_enable glade

Name: libgnomecanvas
Version: %ver_major.3
Release: alt2

Summary: GnomeCanvas widget
License: %lgpl2plus
Group: System/Libraries
Url: http://www.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

BuildPreReq: rpm-build-gnome rpm-build-licenses intltool

# From configure.in
BuildPreReq: libgtk+2-devel >= 2.6.4
BuildPreReq: libart_lgpl-devel >= 2.3.17
BuildPreReq: libpango-devel >= 1.8.1
%{?_enable_glade:BuildPreReq: libglade-devel >= 2.5.1}

BuildRequires: gtk-doc libgail-devel perl-XML-Parser
BuildRequires: docbook-dtds docbook-style-xsl gtk-doc xsltproc

%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary: Libraries and headers for libgnomecanvas
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

This package contains development libraries and headers files for %name.

%package devel-doc
Summary: Development documentation for GNOME Canvas Widget
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

This package provides development documentation for %name.

%package devel-static
Summary: Static libraries for libgnomecanvas
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%prep
%setup -q

%build
#export gnomelocaledir="%_datadir/locale"
%configure \
	%{subst_enable static} \
	%{subst_enable glade} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall

%find_lang %name-2.0

%files -f %name-2.0.lang
%_libdir/*.so.*
%_libdir/libglade/2.0/*.so
%doc AUTHORS ChangeLog README NEWS

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/libglade/2.0/*.a
%endif

%exclude %_libdir/libglade/2.0/*.la

%changelog
* Thu Feb 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt2
- rebuild for update debuginfo dependencies

* Mon Jan 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- rebuild for update dependencies

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Fri Apr 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1
- glade2 support is optional now

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sat Jan 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90
- removed obsolete %%post{,un}_ldconfig
- removed upstreamed patch
- don't rebuild documentation
- documentation packaged as noarch
- updated buildreqs

* Sat Dec 27 2008 Alexey Rusakov <ktirf@altlinux.org> 2.20.1.1-alt2
- spec cleanup
- removed Requires that are added automatically by findreq
- added a patch that makes repainting smoother
- fixed License tag (LGPL -> %lgpl2plus)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1.1-alt1
- new version 2.20.1.1
- add Packager

* Fri Mar 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sat Feb 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.0-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.2-alt1
- 2.11.2

* Tue Jun 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.1-alt1
- 2.9.1
- documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1
- 2.6.1.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sat Nov 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build devel-static subpackage.

* Mon Sep 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Fri Feb 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt1
- 2.2.0.2

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Dec 03 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.1-alt2
- change dep on libart_lgpl-devel to libart_lgpl

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Jun 07 2002 Igor Androsov <blake@altlinux.ru> 2.0.0-alt1
- New Version
- Fix Group (Thanks Yuri Sedunov)

* Tue Jun 04 2002 Igor Androsov <blake@altlinux.ru> 1.117.0-alt1.1
- Return *.la from static to devel package

* Tue May 14 2002 Igor Androsov <blake@altlinux.ru> 1.1.117-alt1
- New version

* Thu May 09 2002 Igor Androsov <blace@mail.ru> 1.1.116-blk0.2
- New version from CVS

* Wed May 08 2002 Igor Androsov <blace@mail.ru> 1.1.116-blk0.1
- Changes for AltLinux
- Moved static libs to libgnomecanvas-devel-static

* Mon Feb 25 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.112.0-1
- new version

* Sun Feb 17 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.111.0-1
- new version
- disabled gtk-doc
- fixed permissions
- disabled binary stripping

* Mon Jan 28 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.109.0-4
- changed some depdendencies

* Tue Jan 22 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- removed tabs from header
- turn off libtoolize, as it breaks lots of things (and fixes nothing, so far as I can see)
- replaced %files section

* Sat Jan 19 2002 Chris Chabot <chabotc@reviewboard.com>
- Imported into gnome 2.0 alpha
- Changed versions accordingly
- Minor cleanups

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- cvs snap 1.105.0.90, gtk 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, rebuild for gtk 1.3.10,
  add libglade dep, fix libart dep

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- rebuild cvs snap for new glib/gtk

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap with upstream changes

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- Initial build.

