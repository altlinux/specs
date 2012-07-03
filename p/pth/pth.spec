Name: pth
Version: 2.0.7
Release: alt6

Summary: The GNU Portable Threads library
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnu.org/software/%name/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

%define libname lib%name
%def_disable static

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

%package -n %libname
Summary: The GNU Portable Threads runtime library
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: %name

%package -n %libname-devel
Summary: The GNU Portable Threads developement files
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%package -n %libname-devel-static
Summary: The GNU Portable Threads static library
Group: Development/C
Requires: %libname-devel = %version-%release
Provides: %name-devel-static = %version-%release

%description -n %libname
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

This package includes Pth runtime library.

%description -n %libname-devel
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

This package includes headers and other development files necessary
to build applications that use Pth.

%description -n %libname-devel-static
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

This package includes Pth static library.

%prep
%setup

%build
%configure --enable-shared %{subst_enable static}
# SMP-incompatible build
make

%install
%makeinstall_std

%check
make -k check

%files -n %libname
%doc ANNOUNCE AUTHORS COPYING NEWS README SUPPORT TESTS THANKS
%_libdir/*.so.*

%files -n %libname-devel
%_bindir/*
%_libdir/*.so
%_includedir/*
%_man1dir/*
%_man3dir/*
%_datadir/aclocal/*

%if_enabled static
%files -n %libname-devel-static
%_libdir/*.a
%endif	# enabled static

%changelog
* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt6
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt5
- Rebuilt for soname set-versions.

* Thu Aug 20 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt4
- Cleaned up specfile.
- Fixed build.

* Sun Dec 28 2008 Led <led@altlinux.ru> 2.0.7-alt3
- Cleaned up spec

* Sat Aug 09 2008 Led <led@altlinux.ru> 2.0.7-alt2
- Fixed and cleaned up spec

* Sat Jul 26 2008 Led <led@altlinux.ru> 2.0.7-alt1
- Updated to 2.0.7
- Fixed License

* Sun Dec 11 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.6-alt1
- Updated to 2.0.6

* Thu Jan 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.0-alt1
- Updated to 2.0.0
- License is LGPL

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt4
- Removed libtool files

* Wed Sep 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt3
- mdk-pth-config.in patch sucked

* Tue Sep 24 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt2
- static build disabled by default
- included the pth.m4 file for aclocal
- bzipped ChangeLog
- sanitized descriptions

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.1-alt1
- 1.4.1
- some little spec improvements

* Tue Mar 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Jan 15 2001 Dmitry V. Levin <ldv@fandra.org> 1.3.7-ipl1mdk
- RE adaptions.

* Thu Jan 04 2001 Francis Galiegue <fg@mandrakesoft.com> 1.3.7-1mdk
- New lib policy:
  * s,pth,lib&,g
  * Obsoletes: pth (and -devel)
  * no need for serial anymore
- Don't use macros when not needed

* Sun Jul 30 2000 Geoffrey Lee <snailtalk@mnandrakesoft.com> 1.3.7-1mdk
- new version

* Thu Jul 27 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.6-1mdk
- 1.3.6
- BMacros
- numerous spec file changes - why has the Makefile gone so screwy?

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.3.1-4mdk
- makeinstall macro
- macroszifications

* Thu Apr 13 2000 Francis Galiegue <fg@mandrakesoft.com> 1.3.1-3mdk
- Changed group for -devel

* Thu Mar 16 2000 Francis Galiegue <francis@mandrakesoft.com>
- Some spec file changes
- Changed group to match 7.1 specs
- Let spec-helper do its job

* Tue Feb 22 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.3.1-1mdk
- v1.3.1

* Wed Feb  9 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.3-2mdk
- bzip man pages and make rpmlint happy.

* Tue Feb  8 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.3-1mdk
- version 1.2.3

* Fri Jul 30 1999 Ryan Weaver <ryanw@infohwy.com>
  [pth-1.0.3-1]
- Fixed inconsistent and wrong API value: PTH_ATTR_NULL existed and was
  documented as PTH_ATTR_NONE. But actually the intended and intuitive
  value was PTH_ATTR_DEFAULT. !BE CAREFUL: This is an API change and
  requires adjustments in Pth applications!
  [Ralf S. Engelschall, Eric Newton <ecn@smart.net>]
- Make sure pthread.h.in doesn't redefine the poll(2) environment
  under built-time because it's already defined by the included pth.h.
  [Kriton Kyrimis <kyrimis@cti.gr>]
- Add readv/writev environment fallback definitions to pthread.h.in.
  [Ralf S. Engelschall]
- Support for AmigaOS in pthreads.c: timespec attributes have (correct)
  ts_ prefix under AmigaOS and not the (bogus) POSIX tv_ prefix
  [Kriton Kyrimis <kyrimis@cti.gr>]
- Add `#include <time.h>' for struct timespec to pthread.h.in
  and removed timespec references in pth.h.in.
  [Ralf S. Engelschall]
- Fixed documentation for pth_spawn() and pth_wait().
  [Ralf S. Engelschall, Eric Newton <ecn@smart.net>]
