Name: libpng
Version: 1.2.49
Release: alt1

Summary: A library of functions for manipulating PNG image format files
License: OSI certified
Group: System/Libraries
Url: http://www.libpng.org/pub/png/libpng.html

# ftp://swrinde.nde.swri.edu/pub/png/src
Source: http://prdownloads.sourceforge.net/libpng/libpng-%version.tar
Patch: libpng-%version-%release.patch

# Automatically added by buildreq on Tue Feb 08 2011
BuildRequires: zlib-devel

%package -n libpng12
Summary: PNG runtime library
Group: System/Libraries
Provides: libpng = %version
Conflicts: libpng3 < 1.2.13-alt1

%package -n libpng3
Summary: PNG runtime library
Group: System/Libraries
Requires: libpng12 = %version-%release
Provides: libpng = %version

%package devel
Summary: PNG development library
Group: Development/C
Requires: libpng12 = %version-%release, zlib-devel
Provides: libpng3-devel = %version
Obsoletes: libpng3-devel < %version
Conflicts: libpng2-devel

%package devel-static
Summary: PNG static library
Group: Development/C
Requires: %name-devel = %version-%release, zlib-devel-static
Provides: libpng3-devel-static = %version
Obsoletes: libpng3-devel-static < %version
Conflicts: libpng2-devel-static

%description
libpng is a library implementing an interface for reading and writing
PNG (Portable Network Graphics) format files.

%description -n libpng12
libpng is a library implementing an interface for reading and writing
PNG (Portable Network Graphics) format files.

This package contains the runtime library files needed to run software
using libpng.

%description -n libpng3
libpng is a library implementing an interface for reading and writing
PNG (Portable Network Graphics) format files.

This package is superseded by libpng12, and is provided only for
transitional purposes.

%description devel
libpng is a library implementing an interface for reading and writing
PNG (Portable Network Graphics) format files.

This package contains the header and development files needed to build
programs and packages using libpng.

%description devel-static
This package contains static library necessary for developing statically
linked programs using the PNG (Portable Network Graphics) library.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
rm %buildroot%_libdir/lib*.la

%define docdir %_docdir/libpng-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -p -m644 CHANGES KNOWNBUG LICENSE README TODO example.c libpng*.txt \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/*.txt %buildroot%docdir/CHANGES

%check
%make_build -k check

%files -n libpng12
%_libdir/libpng12.so.*
%_man5dir/*

%files -n libpng3
%_libdir/libpng.so.*

%files devel
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*
%docdir

%files devel-static
%_libdir/*.a

%changelog
* Thu Apr 05 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.49-alt1
- Updated to 1.2.49 (fixes CVE-2011-3048).

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.48-alt1
- Updated to 1.2.48 (fixes CVE-2011-3045).

* Mon Feb 20 2012 Dmitry V. Levin <ldv@altlinux.org> 1.2.47-alt1
- Updated to 1.2.47 (fixes CVE-2011-3026).

* Wed Jul 13 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.46-alt1
- Updated to 1.2.46 (fixes: CVE-2011-2690, CVE-2011-2691, CVE-2011-2692).

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 1.2.44-alt3
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.44-alt2
- Rebuilt for soname set-versions.

* Tue Jun 29 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.44-alt1
- Updated to 1.2.44 (fixes: CVE-2010-1205, CVE-2010-2249).

* Tue Mar 09 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.43-alt1
- Updated to 1.2.43 (fixes CVE-2010-0205).

* Fri Sep 18 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.40-alt2
- libpng12: Swapped PNG_12 and PNG12_0 interfaces again (closes: #21559).

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.40-alt1
- Updated to 1.2.40.
- Moved "make check" to %%check section.

* Thu Jul 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.38-alt1
- Updated to 1.2.38.

* Tue Jun 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.37-alt3
- libpng12: Added compatibility interface with previous library
  versioning (by Sergey Vlasov; closes: #12886).

* Mon Jun 22 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.37-alt2
- libpng12: Changed versioning to match upstream versioning (closes: #12886).

* Sat Jun 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.37-alt1
- Updated to 1.2.37 (closes: #20339).

* Wed Feb 18 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.35-alt1
- Updated to 1.2.35.

* Fri Feb 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.34-alt1
- Updated to 1.2.34.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.33-alt1
- Updated to 1.2.33.

* Sun Sep 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.32-alt1
- Updated to 1.2.32.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.31-alt1
- Updated to 1.2.31.

* Tue Apr 29 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.27-alt1
- Updated to 1.2.27.

* Thu Apr 03 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.26-alt1
- Updated to 1.2.26.

* Sat Feb 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.25-alt1
- Updated to 1.2.25.

* Mon Nov 26 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.23-alt1
- Updated to 1.2.23 (CVE-2007-526[6789]).
- Enhanced comment in pngconf.h about setjmp.h (#8498).
- Added PNG12_0 versioning interface for compatibility (#12886).

* Wed May 16 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.13-alt3
- Imported upstream fix for png_handle_tRNS() bug (CVE-2007-2445:
  a grayscale PNG image with a malformed tRNS chunk may crash
  some libpng applications).

* Fri Dec 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.13-alt2
- libpng12: Added conflict with old libpng3 (#10341).

* Fri Nov 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.13-alt1
- Updated to 1.2.13 release.
- Imported FC patch for pngconf.h to disable asm code
  on non-x86 architectures (RH#196580).
- Imported Debian patch from 1.2.13-4 package.
- Moved libpng12 library to separate subpackage.
- Removed "3" suffix from -devel* subpackages.
- Switched to upstream versioning (introduced in 1.2.9) with minimal changes.
  As result, libpng12.so.0 no longer provides PNG_INTERNAL interface,
  and PNG_12 interface was changed: 22 old data names removed,
  8 old function names removed, 8 new function names added.

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt3
- Fixed build with --as-needed.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.8-alt2.1
- Rebuilt for new pkg-config dependencies.

* Tue Dec 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt2
- Updated interpackage dependencies.
- Updated patch.

* Mon Dec 06 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt1
- Updated to 1.2.8 release.
- Fixed libpng.pc (#5632).
- Updated interpackage dependencies.

* Thu Nov 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.8-alt0.1
- Updated to 1.2.8beta3.

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt1
- Updated to 1.2.7.

* Tue Sep 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt2
- Applied pngwutil bugfix from upstream.

* Wed Sep 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt1
- Updated to 1.2.6.
- Added multilib support (#5094).

* Mon Aug 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt5
- Applied patch from upstream maintainer,
  to fix CAN-2004-0597, CAN-2004-0598 and CAN-2004-0599.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt4
- Updated patch for the buffer overflow in
  png_do_read_filler() function (CAN-2002-1363).

* Tue May 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt3
- Changed shared library:
  + introduced versioning;
  + export legacy symbols on PNG_INTERNAL interface;
  + export normal symbols on PNG_12 interface.

* Sat May 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt2
- Applied patch to pngerror.c by Steve Grubb to fix unintended
  memory access that could result in a crash of the application
  linking against libpng [CAN-2004-0421].
- Changed shared library: restricted list of exported symbols
  to those which are mentioned in png.h and libpng(3).

* Mon Feb 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5

* Tue Jan 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt5
- Applied patch to pngrtran.c by Glenn Randers-Pehrson to fix
  a buffer overrun.

* Thu Oct 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt4
- Cleanup %%build.
- Rebuilt to fix config files in devel subpackage.

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.4-alt3
- rebuild with gcc3

* Tue Aug 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt2
- Refined trigger once more.

* Sat Jul 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sat Jun 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt3
- Fixed latest fix.

* Fri May 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt2
- Fixed libpng.so.3 upgrade problem.

* Thu May 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Feb 28 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.2.1-alt2
- Renamed to libpng3.
- Added buildreq substitution rules.

* Fri Dec 14 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.2.1-alt1
- 1.2.1

* Fri Oct 26 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt2
- Prevented libpng.so.3 from being installed in man3dir.

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.12-alt1
- 1.0.12
- Updated requires on zlib-*.

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Tue Apr 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.10-alt1
- 1.0.10
- Moved static libraries to devel-static subpackage.

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.9-ipl1mdk
- 1.0.9

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.8-ipl2mdk
- Fixed Url.
- Specfile cleanup (since we have brp-adjust_libraries).

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.8-ipl1mdk
- 1.0.8

* Wed Jul 05 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.7-ipl1mdk
- 1.0.7
- RE and Fandra adaptions.

* Mon Jun 26 2000 Alexandre Dussart <adussart@mandrakesoft.com> 1.0.6-1mdk
- 1.0.6
- Patch 1.0.6a(official)
- Patch 1.0.6b(official)
- Patch 1.0.6c(official)
- Updated mdkconf patch(some parts was obsoletes)

* Fri May 19 2000 Pixel <pixel@mandrakesoft.com> 1.0.5-3mdk
- fix *ugly* install of man pages
- add soname

* Mon Mar 27 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.5-2mdk
- fix group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.0.5
- redo patch with perl (yay perl)
- SMP check/build

* Mon Jul 12 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- libpng.so.2.1.0.3 is not a man pages lets not put it in usr/man/man3

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Sun Feb 07 1999 Michael Johnson <johnsonm@redhat.com>
- rev to 1.0.3

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- we are Serial: 1 now because we are reverting the 1.0.2 version from 5.2
  beta to this prior one
- install man pages; set defattr defaults

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel subpackage moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.0.1
- added buildroot

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- updated to new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
