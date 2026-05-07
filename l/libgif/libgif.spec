%define sover 7

Name: libgif
Version: 6.1.3
Release: alt2

Summary: A library for manipulating GIF format image files
Group: System/Libraries
License: MIT
Url: https://giflib.sourceforge.net
Vcs: https://git.code.sf.net/p/giflib/code

BuildRequires: xmlto

Source: %name-%version-%release.tar

%def_disable static

%package -n libgif%sover
Summary: A library for manipulating GIF format image files
Group: System/Libraries
Provides: libgiflib_7 = %EVR
Obsoletes: libgiflib_7 < %EVR

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name%sover = %EVR
Provides: libungif-devel = %EVR
Provides: giflib-devel = %EVR

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %EVR

%package utils
Summary: Programs for manipulating GIF format image files
Group: Graphics
Requires: %name%sover = %EVR

%description
This package contains a shared library of functions for loading and
saving GIF format image files.

%description -n libgif%sover
This package contains a shared library of functions for loading and
saving GIF format image files.

%description devel
This package contains development files and documentation necessary for
development of programs that will use the %name library to load and save
GIF format image files.

%description devel-static
This package contains static %name library necessary for development of
statically linked programs that will use the %name library to load and
save GIF format image files.

%description utils
This package contains various programs for manipulating GIF format
image files.

%prep
%setup -n %name-%version-%release
bzip2 -9fk ChangeLog

%build
%add_optflags -fPIC
%make_build CFLAGS='%optflags'

%install
make install-bin install-include install-shared-lib install-man \
	DESTDIR=%buildroot LIBDIR=%_libdir PREFIX=%_prefix

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 ChangeLog.bz2 \
	COPYING NEWS TODO \
	doc/*.html \
	%buildroot%docdir/

%check
%make_build check

%files -n libgif%sover
%_libdir/*.so.%{sover}*
%dir %docdir
%docdir/[A-Z][A-Z]*
%docdir/*.bz2

%files utils
%_bindir/*
%_man1dir/*
%dir %docdir
%docdir/*.html

%files devel
%_libdir/*.so
%_includedir/*
%dir %docdir
%_man7dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu May 07 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.1.3-alt2
- libgif7: fixed Obsolete: for libgiflib_7 (ALT#59020).

* Thu Apr 30 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.1.3-alt1
- 4.1.6 -> 6.1.3.

* Mon May 05 2025 Constantin Sunzow <protvin@altlinux.org> 4.1.6-alt4
- Fix FTBFS: implicit declaration of function (compatibility with GCC 14).

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 4.1.6-alt3
- Rebuilt for debuginfo.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 4.1.6-alt2
- Synced with giflib-4.1.6-9 from Debian.

* Fri Mar 20 2009 Dmitry V. Levin <ldv@altlinux.org> 4.1.6-alt1
- Updated to giflib-4.1.6 (closes: #15974).

* Thu Nov 03 2005 Dmitry V. Levin <ldv@altlinux.org> 4.1.4-alt1
- Updated to 4.1.4 (fixes CVE-2005-2974 and CVE-2005-3350 but
  the code remains far from clean yet).

* Wed Mar 02 2005 Stanislav Yadykin <tosick@altlinux.ru> 4.1.3-alt1
- Updated to 4.1.3

* Sun Nov 30 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.0b1-alt2
- Do not package .la files.
- Do not build static library by default.
- Do not build gif2rle and rle2gif utilities by default.

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.0b1-alt1
- Updated to 4.1.0b1
- Added "stdarg" and "cvs" patches from RH.
- Dropped compatibility library.
- Updated buildrequires.

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.1.0-ipl14mdk
- Updated buildrequires again.

* Sat Aug 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.1.0-ipl13mdk
- Moved static library to devel-static subpackage.
- Corrected package requires and buildrequires.

* Thu Aug 16 2001 AEN <aen@logic.ru> 4.1.0-ipl12mdk
- rebuild with netpbm

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 4.1.0-ipl11mdk
- Split into %name, %name-utils, %name-devel, %name-compat subpackages.
- RE adaptions.

* Wed Dec 13 2000 Yves Duret <yduret@mandrakesoft.com> 4.1.0-10mdk
- fix mode 0644 to some files (patches)
- fix URL: to the new home
- macroization

* Mon Oct  2 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.1.0-9mdk
- removed build dependency on libungif-devel.

* Thu Sep  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 4.1.0-8mdk
- BM

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.1.0-7mdk
- automatically added BuildRequires

* Mon Mar 27 2000 Daouda Lo <daouda@mandrakesoft.com> 4.1.0-6mdk
- fix group

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed May 12 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- fix up provides (original didn't provide libgif.so.4 :/ )
- create missing link for libungif.so.4

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Sun Mar 14 1999 Preston Brown <pbrown@redhat.com>
- include libungif 4.1.0 as standard library, with 3.1.0 backwards compat.

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- call libtoolize to make sure it will build on the arm

* Sat Oct 31 1998 Jeff Johnson <jbj@redhat.com>
- package for RH 5.2.

* Mon Sep 14 1998 Arne Coucheron <arneco@online.no>
  [3.1.0-3]
- major cleanups and changes to the spec file

* Mon Sep 7 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Upgrade to version 3.1.0 (which incorporates the patches in 3.0-4)
- Updated Source: and URL: to reflect change in directories/pages.

* Tue May 26 1998 Dick Porter <dick@cymru.net>
- Fixed some "warning: cast to pointer from integer of different size" on Alpha

* Tue May 5 1998 Marc Ewing <marc@redhat.com>
- Made it obsolete giflib and provide libgif.so and giflib (previous
  giflib packages were built incorrectly and packages built against
  it require libgif.so but work fine with this package)
- cleaned buildroot
- Removed Toshio as packager so he doesn't get yelled at when Red Hat
  breaks it :-)

* Fri Apr 24 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Initial revision of libungif, a giflib derivative modified to not use LZW
  compression.
