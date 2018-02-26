%define _unpackaged_files_terminate_build 1
%define oldname libgnomeprint2
%define ver_major 2.18
%def_disable static
%def_disable gtk_doc

%def_with cups

Name: libgnomeprint
Version: %ver_major.8
Release: alt3

Summary: Printing library for GNOME
License: LGPL
Group: System/Libraries

Provides: %oldname = %version-%release
Obsoletes: %oldname < 2.12.1-alt3

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Patch: %name-2.18.6-alt-configure.patch
Patch1: %name-2.18.8-include.patch

%define glib_ver 2.6.3
%define libxml2_ver 2.6.17
%define pango_ver 1.8.1
%define libart_lgpl_ver 2.3.17
%define libbonobo_ver 2.8.1
%define fontconfig_ver 2.2.1-alt2
%define gtk_doc_ver 1.3
%define cups_ver 1.1.20

Requires: fontconfig >= %fontconfig_ver

BuildPreReq: rpm-build-gnome
BuildPreReq: intltool >= 0.35.0
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: libart_lgpl-devel >= %libart_lgpl_ver
BuildPreReq: libbonobo2-devel >= %libbonobo_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
BuildPreReq: libfreetype-devel >= 2.0.5
%if_with cups
BuildPreReq: libssl-devel
BuildPreReq: libgnomecups-devel >= 0.2.0
BuildPreReq: libcups-devel >= %cups_ver
%endif

BuildRequires: docbook-utils flex gcc-c++ libgnutls-devel perl-XML-Parser bison zlib-devel

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-print package contains
libraries needed by GNOME applications for printing.

You should install the %name package if you intend to use any of
the GNOME applications that can print. If you would like to develop
GNOME applications that can print you will also need to install the
%name-devel package.

%package devel
Summary: Libraries and include files for developing GNOME applications
Group: Development/GNOME and GTK+
Provides: %oldname-devel = %version-%release
Obsoletes: %oldname-devel < 2.12.1-alt3
Requires: %name = %version-%release

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The %name-devel package
includes the libraries and include files needed for developing
applications that use the GNOME printing capabilities.

You should install the %name-devel package if you would like to
develop GNOME applications that will use the GNOME print capabilities.
You do not need to install the %name-devel package if you just
want to use the GNOME desktop environment.

%package devel-doc
Summary: Libraries and include files for developing GNOME applications
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The %name-devel-doc package
includes the documenation needed for developing
applications that use the GNOME printing capabilities.

%package devel-static
Summary: static libraries and objects for gnomeprint
Group: Development/GNOME and GTK+
Provides: %oldname-devel-static = %version-%release
Obsoletes: %oldname-devel-static < 2.12.1-alt3
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libraries for the GNOME printing infrastructure.

%prep
%setup
%patch
%patch1 -p1

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_with cups} \
    %{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%find_lang %name-2.2

%files -f %name-2.2.lang
%_libdir/*.so.*
%dir %_libdir/%name
%dir %_libdir/%name/%version
%dir %_libdir/%name/%version/modules
%dir %_libdir/%name/%version/modules/transports
%dir %_libdir/%name/%version/modules/filters
%_libdir/%name/%version/modules/transports/*.so
%_libdir/%name/%version/modules/filters/*.so
%_libdir/%name/%version/modules/libgnomeprintlpd.so
%if_with cups
%_libdir/%name/%version/modules/libgnomeprintcups.so
%endif
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/models
%dir %_datadir/%name/%version/printers
%_datadir/%name/%version/models/*
%_datadir/%name/%version/printers/*
%_datadir/%name/%version/*.xml
%doc AUTHORS ChangeLog NEWS README

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%dir %_libdir/%name/%version/modules/transports/*.a
%endif

%exclude %_libdir/%name/%version/modules/transports/*.la
%exclude %_libdir/%name/%version/modules/filters/*.la
%exclude %_libdir/%name/%version/modules/*.la

%changelog
* Wed Aug 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.18.8-alt3
- fixed build against libcups-1.5

* Wed Jul 06 2011 Dmitry V. Levin <ldv@altlinux.org> 2.18.8-alt2
- Rebuilt for debuginfo.

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.18.8-alt1
- 2.18.8

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.18.7-alt1
- 2.18.7

* Mon Dec 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.6-alt2
- fixed build with new gtk-doc

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.6-alt1
- 2.18.6
- removed obsolete %post{,un}_ldconfig
- new noarch devel-doc subpackage
- don't rebuild documentation

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.18.4-alt1
- new version (2.18.4)

* Tue Jun 26 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- use rpm-build-gnome and its cool gnome_ftp macro
- updated dependencies, removed excess ones.
- updated files list to be more correct, use macros instead of paths.
- don't allow unpackaged files

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt3
- removed '2' from the name of the package.
- reduced too greedy dependencies.

* Sun Feb 26 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- removed urw-fonts from Requires list
- spec cleanup

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- 2.12.1

* Tue Sep 13 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt2
- Added /usr/share/libgnomeprint to %files

* Mon Sep 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.0-alt1
- 2.11.0

* Fri Jul 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.3-alt1
- 2.10.3

* Thu Mar 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Wed Mar 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0.1-alt1
- 2.8.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Sat Sep 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.90-alt1
- 2.7.90

* Thu Sep 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Wed Jun 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Mar 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Feb 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt2
- enabled cups support.

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Tue Dec 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2
- do not package .la files.
- do not build devel-static subpackage by default.

* Fri Nov 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt1
- 2.4.1.1

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Jun 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.3-alt1
- 2.2.1.3

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.2-alt1
- 2.2.1.2

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.1-alt1
- 2.2.1.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Mon Dec 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Wed Dec 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Dec 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Thu Dec 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Dec 03 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.1-alt3
- removed unnesessary dep on perl
- ressurected drivers again (was orphaned symlinks)
- .so files from drivers must live in main package (this is plug-in's)

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2
- fixed paths to media, printers etc.

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.1-alt1
- 1.116.1
- RH patches removed (in mainstream now)
- %%_libdir/gnome-print-2.0/{drivers,transports} dirs owned by main package.

* Thu Oct 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1.116.0-alt3
- don't use %%makeinstall macros. It's redefine libexec variable
  now all drivers and transports on it's right places
- .so files in the transports must live in the library (not in the devel subpackage)

* Tue Oct 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.0-alt2
- RH patches
- improved %%post.

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.116.0-alt1.1
- fix buildreqs (remove colorgcc and update)

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.116.0-alt1
- 1.116.0

* Wed Jun 12 2002 Igor Androsov <blake@altlinux.ru> 1.115.0-alt1
- New version

* Thu May 30 2002 Igor Androsov <blace@mail.ru> 1.114.0-blk1
- New version

* Fri May 24 2002 Igor Androsov <blace@mail.ru> 1.113.0-blk1
- Release build

* Wed May 15 2002 Igor Androsov <blace@mail.ru> 1.113.0-blk0.2
- New version from CVS
- Added patch for dir

* Thu May 09 2002 Igor Androsov <blace@mail.ru> 1.113.0-blk0.1
- new version from CVS
- changes for AltLinux
- libs moved to libgnomeprint2
- static libs moved to libgnomeprint2-devel

* Sun Feb 17 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.111.0-1
- new version
- split packages
- lots of files cleanups
- removed cruft from %%setup line
- disabled binary stripping

* Mon Jan 28 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.109.1-4
- fixed some dependencies

* Tue Jan 22 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- s/prereq/Requires/
- turned off libtoolize
- ran cowering in fear from %post scriptletts
- made main package not require itself

* Sat Jan 19 2002 Chris Chabot <chabotc@reviewboard.com>
- Imported into gnome 2.0 alpha
- Changed versions accordingly
- Minor cleanups

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.109.0.90 snap
- remove .options patch which is upstream
- remove .nofontmaps patch, upstream uses sysconfdir sometimes now
  and has --disable-font-install configure option
- remove .fontmapdir, now fixed upstream

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- rebuild due to build system fuckup

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- cvs snap 1.106.0.90, glib 1.3.11

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, rebuild for glib 1.3.10, remove bogus gtk dep

* Tue Oct  9 2001 Havoc Pennington <hp@redhat.com>
- remove epoch screwup

* Mon Oct  8 2001 Havoc Pennington <hp@redhat.com>
- libgnomeprint package based on the gnome-print package

* Mon Oct  8 2001 Havoc Pennington <hp@redhat.com>
- use 0.30 tarball

* Sat Sep 22 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, with headers moved

* Wed Aug 15 2001 Owen Taylor <otaylor@redhat.com>
- Back out freetype change, for now, until we can get it in upstream.
- Move gnome-print/<ver>/profiles back to datadir, and remove the %%config.
  Making them %%config doesn't seem compatible with locating them
  in gnome-print/<ver>.

* Mon Aug 13 2001 Akira TAGOH <tagoh@redhat.com> 0.29-5
- no replace profiles.

* Mon Aug 13 2001 Akira TAGOH <tagoh@redhat.com> 0.29-4
- Move profiles directory to /etc/gnome-print/<ver>/profiles/

* Mon Aug 13 2001 Akira TAGOH <tagoh@redhat.com> 0.29-3
- Add freetype support patch. (Bug#50360)

* Sat Jul 21 2001 Owen Taylor <otaylor@redhat.com>
- Add missing directory

* Fri Jul 20 2001 Owen Taylor <otaylor@redhat.com>
- Upgrade to 0.29
- Don't install run-gnome-font-install (#48466), run gnome-font-install directly.
- Add BuildPrereq and make -devel package require gdk-pixbuf-devel
- Make libgnomeprint package require gnome-print package; otherwise
  packages requiring libgnomeprint might not get a runtime environment
- Add Prereq on ghostscript, since run-gnome-font-install parses output of 'gs -h'

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Kill output from run-gnome-font-install
- s/Copyright/License/
- Add post/postun scripts for the libgnomeprint subpackage

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Apr 20 2001 Jonathan Blandford <jrb@redhat.com>
- new version (0.28)

* Thu Mar 01 2001 Owen Taylor <otaylor@redhat.com>
- Rebuild for GTK+-1.2.9 include paths

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- patch it to compile (didn't include locale.h when needed)
- use %%{_tmppath}

* Fri Feb 23 2001 Akira TAGOH <tagoh@redhat.com>
- Fixed font problem for Japanese.
- Fixed library dependency on VFlib (Bug#28331)

* Wed Feb 21 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed bugzilla bug #27417, simple specfile %post fix.

* Sun Feb 18 2001 Akira TAGOH <tagoh@redhat.com>
- Fixed PostScript broken.
- Added autoheader,automake,autoconf stuff.

* Thu Feb 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add libtoolize to make porting to new archs easy

* Tue Feb 06 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese patch for Gnumeric.
  Created dummy .afm.

* Mon Feb 05 2001 Akira TAGOH <tagoh@redhat.com>
- Fixed gdk_fontset_load().
- Added Japanese patch for Gnumeric.

* Fri Feb 02 2001 Akira TAGOH <tagoh@redhat.com>
- Added Japanese patch.
  Fixed Print and Preview with Japanese.

* Fri Dec 29 2000 Matt Wilson <msw@redhat.com>
- 0.25

* Sat Aug 19 2000 Preston Brown <pbrown@redhat.com>
- added "|| true" to %%post so that if font-install screws up we don't get a
  bad exit status.  gnome-font-install expects that the directory specified by
  HOME env. var is writable, but it isn't always if you install with 'sudo'
  or the equivalent.  bad. bad. bad.

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Fri Jul 14 2000 Matt Wilson <msw@redhat.com>
- redirect %%post script output to /dev/null

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 29 2000 Owen Taylor <otaylor@redhat.com>
- Spec file fixes
