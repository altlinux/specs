Name: ORBit
Version: 0.5.17
Release: alt3.qa2

Summary: High-performance CORBA Object Request Broker
License: LGPL/GPL
Group: System/Libraries
Url: http://orbit-resource.sourceforge.net/

Source: %url/%name-%version.tar.bz2
Patch0: %name-0.5.5-texinfo.patch
Patch1: %name-%version-libs-alt.patch

Prefix: %prefix

Requires: lib%name = %version-%release

# Automatically added by buildreq on Sun Nov 10 2002
BuildRequires: flex glib-devel glibc-devel libwrap-devel

%description
%name is a high-performance CORBA ORB (object request broker).
It allows programs to send requests and  receive replies from
other programs, regardless of the locations of the two programs.
ORBit features CORBA bindings for the C language.

You will need to install this package and the related header files,
libraries and utilities if you want to write programs that use CORBA
technology.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
%name is a high-performance CORBA ORB (object request broker).
It allows programs to send requests and  receive replies from
other programs, regardless of the locations of the two programs.

This package contains the shared libraries required for ORBit
and components using it to function.

%package devel
Summary: Development libraries, header files and utilities for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release, glib-devel, indent
Provides: lib%name-devel = %version
Obsoletes: lib%name-devel
Conflicts: lib%name-devel-static <= 0.5.11-alt1
# indent is called by orbit-idl

%description devel
%name is a high-performance CORBA ORB (object request broker).
It allows programs to send requests and  receive replies from
other programs, regardless of the locations of the two programs.

This package contains the header files, libraries and utilities
necessary to write programs that use CORBA technology.

%package devel-static
Summary: Development static libraries for %name
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release
Provides: lib%name-devel-static = %version
Obsoletes: lib%name-devel-static

%description devel-static
%name is a high-performance CORBA ORB (object request broker).
It allows programs to send requests and  receive replies from
other programs, regardless of the locations of the two programs.

This package contains the static libraries necessary to write
statically linked programs that use CORBA technology.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
touch .now
find -type f -newer .now -print0 |xargs -r0 touch
rm -f .now
%set_automake_version 1.4
#needed by patch #1
%__automake

%build
%configure
#NO SMP
%make

%install
mkdir -p $RPM_BUILD_ROOT%prefix
%makeinstall

%files
%doc AUTHORS NEWS README TODO
%_bindir/*-server
%_bindir/name-client
%_bindir/orbit-ird
%_bindir/ior-decode
%_datadir/idl/*

%files -n lib%name
%_libdir/*.so.*

%files devel
%_bindir/orbit-idl
%_bindir/*-config
%_libdir/*.sh
%_libdir/*.so
%_libdir/libname-server.a
%_libdir/liborbit-c-backend.a
%_libdir/pkgconfig/*
%_includedir/*
%_infodir/*.info*
%_datadir/aclocal/*
%doc ChangeLog docs/*.txt docs/IDEA1

%files devel-static
%_libdir/libIDL.a
%_libdir/libIIOP.a
%_libdir/libORBit*.a

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.17-alt3.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.17-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libORBit
  * postun_ldconfig for libORBit
  * obsolete-call-in-post-install-info for ORBit-devel
  * postclean-05-filetriggers for spec file

* Sun Apr 30 2006 Yury Aliaev <mutabor@altlinux.org> 0.5.17-alt3
- fix build with --as-needed option

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 0.5.17-alt2
- rebuild without *.la files

* Sun Nov 10 2002 AEN <aen@altlinux.ru> 0.5.17-alt1
- new version

* Tue Mar 26 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.15-alt2
- ORBit-devel depends on ORBit because the IDL files are placed there

* Mon Mar 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.15-alt1
- 0.5.15
- Expanded /usr/lib/pkgconfig in the file list (bug 748)

* Fri Nov 02 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.12-alt1
- New version
- -devel conflicts with -devel-static pre 0.5.11-alt2

* Wed Oct 31 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.11-alt2
- Static libraries not duplicated with .so are moved into -devel
- Got rid of libORBit-devel naming stupidity

* Fri Oct 26 2001 AEN <aen@logic.ru> 0.5.11-alt1
- new version

* Mon Jul 9 2001 AEN <aen@logic.ru> 0.5.8-alt3
- snapshot 0522

* Tue May 22 2001 Stanislav Ievlev <inger@altlinux.ru> 0.5.8-alt2
- Librification. Statification.

* Mon May 14 2001 AEN <aen@logic.ru> 0.5.8-alt1
- 0.5.8

* Thu Feb 22 2001 AEN <aen@logic.ru> 0.5.7-ipl1mdk
- 0.5.7

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 0.5.6-ipl2mdk
- Fixed group tag in devel subpackage.

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 0.5.6-ipl1mdk
- 0.5.6

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 0.5.5-ipl1mdk
- 0.5.5
- Fixed texinfo documentation.

* Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 0.5.4-ipl1mdk
- 0.5.4

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 0.5.3-ipl1mdk
- 0.5.3

* Wed Jul 05 2000 Dmitry V. Levin <ldv@fandra.org> 0.5.2-ipl1mdk
- 0.5.2
- FHSification.

* Thu Jun 22 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Wed May 31 2000 AEN <aen@logic.ru>
- build official GNOME version for RE

* Thu Oct 4 1999 AEN <aen@logic.ru>
- build for RE

* Fri Oct 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 0.5.1

* Tue Sep 07 1999 Daouda LO <daouda@mandrakesoft.com>
- 0.4.94

* Wed Aug 18 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add defattr for devel package

* Wed Aug 18 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added dependency for ORBit-devel

* Tue Aug 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.4.93

* Wed Aug 04 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- upgraded to 0.4.92

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Last CVS version from Mon Jun 28 1999.

* Sat Jun  5 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Add libIDL-config to ORBit-devel

* Sun May  1 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sat Apr 10 1999 Michael Fulbright <drmike@redhat.com>
- version 0.4.3

* Tue Apr 06 1999 Michael Fulbright <drmike@redhat.com>
- fixed some user permissions in the tarball

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 0.4.1 and 0.4.2 in one day, woohoo!

* Mon Feb 22 1999 Michael Fulbright <drmike@redhat.com>
- unlibtoolize

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.98

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.97

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.96

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- updated to version 0.3.91

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze, version 0.3.90

* Mon Nov 23 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>
- improved %files section, and added use of %prefix and install-info
  (well,... no. The info file has not dir info inside, commented out)
