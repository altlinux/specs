Name: gdbm
Version: 1.8.3
Release: alt9

Summary: A GNU set of database routines which use extensible hashing
License: GPLv2+
Group: System/Libraries
Url: http://www.gnu.org/software/gdbm/

# ftp://ftp.gnu.org/pub/gnu/gdbm/gdbm-%version.tar.gz
Source: gdbm-%version.tar
Patch1: gdbm-1.8.3-alt-texinfo.patch
Patch2: gdbm-1.8.3-alt-makefile.patch
Patch3: gdbm-1.8.3-alt-configure.patch
Patch4: gdbm-1.8.3-alt-read_loop.patch
Patch11: gdbm-1.8.3-deb-texinfo.patch
Patch12: gdbm-1.8.3-deb-zero-headers.patch
Patch13: gdbm-1.8.3-deb-man.patch
Patch14: gdbm-1.8.3-rh-GDBM_FILE.patch

%def_disable static

%package -n lib%name
Summary: A GNU set of database routines which use extensible hashing
Group: System/Libraries
Provides: %name = %version-%release
#Obsoletes: %name

%package -n lib%name-devel
Summary: Development libraries and header files for the gdbm library
Group: Development/Databases
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: The gdbm static library
Group: Development/Databases
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static
Requires: lib%name-devel = %version-%release

%description
gdbm is a GNU database indexing library, including routines which use
extensible hashing.  gdbm works in a similar way to standard Unix dbm
routines.  gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%description -n lib%name
gdbm is a GNU database indexing library, including routines which use
extensible hashing.  gdbm works in a similar way to standard Unix dbm
routines.  gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%description -n lib%name-devel
This package contains the development libraries and header files for
gdbm, the GNU database system.  These libraries and header files are
necessary if you plan to do development using the gdbm database.

%description -n lib%name-devel-static
This package contains the GDBM development static library necessary
if you plan to do development of statically linked software using
the gdbm database.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
rm aclocal.m4

%build
export ac_cv_lib_dbm_main=no
export ac_cv_lib_ndbm_main=no
%autoreconf
%configure %{subst_enable static} --includedir=%_includedir/gdbm
%make_build

%install
%makeinstall_std install-compat \
	INSTALL_ROOT=%buildroot \
	BINOWN=`id -u` \
	BINGRP=`id -g` \
	#
ln -s gdbm/gdbm.h %buildroot%_includedir/

%files -n lib%name
%_libdir/*so.*
%doc README NEWS

%files -n lib%name-devel
%_libdir/*so
%_includedir/*
%_infodir/*.info*
%_mandir/man?/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Feb 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt9
- Imported a fix for a g++ 4.5 warning from Fedora.
- Rebuilt for debuginfo.

* Mon Oct 18 2010 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt8
- Rebuilt for soname set-versions.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt7
- Removed obsolete %%install_info/%%uninstall_info calls.

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt6
- Fixed build with fresh autotools.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt5
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt4
- Cleaned up specfile.
- Fixed short read error handling.
- Imported patches from Debian gdbm package.

* Fri May 14 2004 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt3
- Fixed compat library linkage.
- Do not build static libraries by default.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt2
- Do not package .la files.
- Corrected URLs.

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt1
- Updated to 1.8.3
- Libificated.

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1.8.0-ipl9mdk
- Rebuilt

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.8.0-ipl8mdk
- RE adaptions.

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix building as non root.
- Merge with redhat patchs.
- make sure created database header is initialized (r).
- repackage to include /usr/include/gdbm/*dbm.h compatibility includes(r)
- make sure created database header is initialized (r).

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.8.0

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- gdbm-devel moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- buildroot and built for Manhattan

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
