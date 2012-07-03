%define ver_major 2.24
%def_disable static

Name: libbonoboui
Version: %ver_major.5
Release: alt1

Summary: Bonobo user interface components
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

# From configure.in
%define libgnomecanvas_ver 1.116.0
%define libbonobo_ver 2.13.0
%define libgnome_ver 2.13.7
%define libxml2_ver 2.4.20
%define gconf_ver 1.1.9
%define gtk_ver 2.6.0
%define glib_ver 2.6.0
%define glade_ver 1.99.11
%define gtk_doc_ver 1.0

BuildPreReq: rpm-build-gnome gnome-common

# From configure.in
BuildPreReq: intltool >= 0.40.0
BuildPreReq: libpango-devel libpopt-devel
BuildPreReq: libXt-devel libX11-devel
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libbonobo-devel >= %libbonobo_ver
BuildPreReq: libgnomecanvas-devel >= %libgnomecanvas_ver
BuildPreReq: libgnome-devel >= %libgnome_ver
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libglade-devel >= %glade_ver
BuildPreReq: libGConf-devel >= %gconf_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver

%description
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%package devel
Summary: Develompment libraries and headers for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
Bonobo is a component system based on CORBA, used by the GNOME desktop.
libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that use
libbonoboui.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Bonobo is a component system based on CORBA, used by the GNOME desktop.
libbonoboui contains GUI components that come with Bonobo.

This package contains development documentation for %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
Bonobo is a component system based on CORBA, used by the GNOME desktop.
libbonoboui contains GUI components that come with Bonobo.

This package contains libraries used to compile statically linked
programs that use %name.
%endif

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q

%build
%configure \
	%{subst_enable static}

%make

%install
%make_install DESTDIR=%buildroot install

bzip2 -9f ChangeLog NEWS

# development diocumentation.
mkdir -p %buildroot%_docdir/%name-devel-%version
cp doc/{*.txt,*.dtd,*.html,*.xml} %buildroot%_docdir/%name-devel-%version/

%find_lang %name-2.0

%files -f %name-2.0.lang
%_libdir/*.so.*
%_libdir/libglade/*/*.so
%dir %_datadir/gnome-2.0
%dir %_datadir/gnome-2.0/ui
%doc AUTHORS ChangeLog* NEWS* README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
# TODO: Maybe move bonobo-browser into a separate package?
%_bindir/bonobo-browser
%_bindir/test-moniker
%_datadir/gnome-2.0/ui/bonobo-browser.xml
%_desktopdir/*
# TODO: And samples, too
%_libdir/bonobo-2.0/samples/*
%bonobo_serversdir/*.server
%_datadir/gnome-2.0/ui/Bonobo_Sample*.xml

%files devel-doc
%_gtk_docdir/*
%_docdir/%name-devel-%version

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/libglade/*/*.a
%endif

%exclude %_libdir/libglade/2.0/*.la

%changelog
* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt1
- 2.24.5

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed obsolete %%post{,un} scripts

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)
- build devel-doc as noarch

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for libbonoboui-devel

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Tue Mar 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.90-alt1
- new version (2.21.90)

* Fri Sep 21 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.0 -> 2.20.0

* Mon May 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- spec cleanup, updated dependencies, removed %%__ macros

* Fri Dec 29 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.0-alt2
- ChangeLog and NEWS files are no more duplicated (bug #10330)
- added /usr/share/gnome-2.0{,/ui} directories to the files list
- files list reordered a bit.

* Thu Sep 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0.
- added intltool minimal version requirement.

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.1-alt1
- new version 2.15.1 (with rpmrb script)

* Tue Aug 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.0-alt1
- new version (2.15.0)
- minor spec cleanup

* Fri Mar 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- spec cleanup, dependencies revised.
- removed Debian menu stuff.

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.0-alt1
- new version
- removed excess buildreqs

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1.
- documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon May 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Mar 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sat Mar 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt2
- updated from cvs.

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Wed Jan 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Fri Jan 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Tue Dec 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Thu Oct 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Tue May 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Mar 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3.2-alt1
- 2.0.3.2

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt2
- rebuild with new pango, gtk+

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Fri Jun 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Jun 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.118.0-alt1
- Adopted for Sisyphus
- 1.118.0
- devel-static package.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- 1.117.0

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.116.0

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- 1.113.0

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.111.0

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0
- Reintoolize to fix DBM problems

* Mon Jan 28 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.108.1.90 cvs snap

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- 1.107.0.90 snap, explicit requires lines for dependencies
- add libtool hack to avoid relinking

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- add glade dependency, add glade module to file list

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- rebuild with glib 1.3.10, new cvs snap

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- rebuild, hoping build root is fixed

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- grumble, build require newer gtk
- require libart_lgpl-devel not the non-devel package

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- cvs snap with menu stuff fixed so gnome-terminal works

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- new tarball, rebuild for new glib

* Mon Sep 24 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, fix up prereqs/requires a bit

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.

