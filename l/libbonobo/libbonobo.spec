%define ver_major 2.32
%def_disable static
%def_disable gtk_doc

Name: libbonobo
Version: %ver_major.1
Release: alt2

Summary: Bonobo component system
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

Patch: %name-2.3.2-alt-tests_makefile.patch
Patch1: %name-2.13-fix-link-as-needed.patch
Patch2: %name-2.20.0-alt-linking.patch
Patch3: %name-2.32.1-alt-link.patch

Obsoletes: bonobo-activation
Obsoletes: libbonobo-activation
Obsoletes: libbonobo2 < 2.15.0
Provides: bonobo-activation = %version-%release
Provides: libbonobo-activation = %version-%release
Provides: libbonobo2 = %version-%release

# From configure.in
%define ORBit_ver 2.11.2
%define glib_ver 2.25.7
%define popt_ver 1.5
%define libxml2_ver 2.4.20
%define intltool_ver 0.35
%define gtk_doc_ver 1.0

BuildPreReq: gnome-common
BuildPreReq: rpm-build-gnome
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: ORBit2-devel >= %ORBit_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libpopt-devel >= %popt_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
BuildRequires: flex

# for check
BuildRequires: dbus-tools-gui

%description
Bonobo is a component system based on CORBA, used by the GNOME desktop.

%package devel
Summary: Libraries and headers for libbonobo
Group: Development/GNOME and GTK+
License: GPL/LGPL
Requires: libbonobo = %version-%release
Obsoletes: bonobo-activation-devel
Obsoletes: libbonobo2-devel < 2.15.0
Provides: bonobo-activation-devel = %version-%release
Provides: libbonobo2-devel = %version-%release
Conflicts: bonobo-devel < 1.0.8

%description devel
Bonobo is a component system based on CORBA, used by the GNOME desktop.
This package contains header files used to compile programs that
use Bonobo.

%package devel-doc
Summary: Development documentation for Bonobo
Group: Development/GNOME and GTK+
Obsoletes: libbonobo2-devel-doc < 2.15.0
Provides: libbonobo2-devel-doc = %version-%release
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
Bonobo is a component system based on CORBA, used by the GNOME desktop.
This package contains development documentation for Bonobo.

%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_bindir

%prep
%setup -q

%patch -p1
%patch1
%patch2 -p1
%patch3 -p1

%__subst 's,\${prefix}/lib,%_libdir,;s,\${prefix}/etc,%_sysconfdir,' \
    activation-server/bonobo-activation-server.1

rm -f samples/echo/Bonobo_Sample_Echo{-{common,skels,stubs}.c,.h}

%build
%autoreconf

%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

# SMP-incompatible build
%make

%check
#%%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang %name-2.0

%files -f %name-2.0.lang
%_bindir/bonobo-activation-server
%_bindir/activation-client
%_bindir/bonobo-slay
%_sbindir/bonobo-activation-sysconf
%_libdir/*.so.*
%dir %_libdir/bonobo
%dir %_libdir/bonobo/servers
%_libdir/bonobo/servers/*
%exclude %_libdir/bonobo/servers/Bonobo_Sample_Echo.server
%dir %_libdir/bonobo/monikers
%_libdir/bonobo/monikers/*.so
%_libdir/orbit-*/*.so
%_datadir/idl/*
%dir %_sysconfdir/bonobo-activation
%config %_sysconfdir/bonobo-activation/*
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README
%exclude %_libdir/bonobo/monikers/*.la
%exclude %_libdir/orbit-*/*.la

%files devel
%_bindir/bonobo-activation-run-query
%_bindir/echo-client-2
%_libdir/bonobo/servers/Bonobo_Sample_Echo.server
%_includedir/*
%_libdir/*.so
%dir %_libdir/bonobo-2.0
%dir %_libdir/bonobo-2.0/samples
%_libdir/bonobo-2.0/samples/*
%_libdir/pkgconfig/*

%files devel-doc
%_gtk_docdir/*

%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- fixed build

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- rebuilt for debuginfo

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Thu Jun 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- fixed build with automake-1.1

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed obsolete %%post{,un}_ldconfig
- don't rebuild documenation

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)
- build %name-devel-doc as noarch

* Thu Jul 03 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1.2
- %%_libdir/bonobo-2.0/samples owned by devel subpackage
- use %%autoreconf instead %%__autoreconf

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Tue Mar 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.90-alt1
- new version (2.21.90)

* Fri Sep 21 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.0 -> 2.20.0

* Wed May 16 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- updated dependencies

* Thu Sep 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.2-alt1
- new version 2.15.2 (with rpmrb script)

* Tue Aug 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.0-alt1
- new version (2.15.0)
- stripped '2' from the names of the packages
- fixed ALT bug #9850.

* Wed Mar 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sat Mar 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.93-alt1
- new version (2.13.93)

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- %%exclude .la files, rather than remove them after %%install.
- 

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.0-alt1
- new version
- removed excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0
- %%_libdir/bonobo directory owned by libbonobo2 package (close #6447).

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1.
- documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1.1
- move {broken,empty,plugin}.server to devel subpackage (close #4396)

* Sun May 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sat May 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Apr 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt2
- updated from cvs.

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sat Jan 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt2
- do not package .la files.

* Wed Nov 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sun Oct 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri Jun 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1
- merge bonobo-activation

* Sat Mar 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Dec 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.0-alt1.2
- rebuild to move to the files
- fixed URL.
- added packager Tag.
- fixed find_lang (now translations in the package)

* Mon Jun 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
-
- (inger)changed make_build to make

* Wed May 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.117.1-alt1
- 1.117.1

* Tue May 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.117.0-alt1
- 1.117

* Tue May 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.0-alt1
- Adopted for Sisyphus.

* Fri May 03 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.116.0

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- 1.113.0

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.111.0

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0
- Rebuild for dependencies
- Intltoolize, the included version has problems with our Perl

* Tue Jan 22 2002 Havoc Pennington <hp@redhat.com>
- automake-1.4

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 cvs snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- 1.107.0, glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib, new snap

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- move to 1.103.0 tarball
- call automake after patching Makefile.am
- patch for parallel install

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- add some requires

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- conflict with bonobo < 1.0.8 to avoid header conflicts
- update group

* Mon Sep 17 2001 Havoc Pennington <hp@redhat.com>
- moved IDL files into subdir
- remove smp_mflags, libbonobo does not like those

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- remove IDL files as temporary hack

* Wed Sep 12 2001 Havoc Pennington <hp@redhat.com>
- Initial build.

