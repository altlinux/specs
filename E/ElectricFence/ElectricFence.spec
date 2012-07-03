Name: ElectricFence
Version: 2.2.2
Release: alt3

Summary: A debugger which detects memory allocation violations

License: GPL
Group: Development/Other
Url: http://perens.com/FreeSoftware/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

# restricted ftp?
Source: ftp://ftp.perens.com/pub/ElectricFence/beta/%name-%version.tar
Patch1: ElectricFence-2.0.5-longjmp.patch
Patch2: ElectricFence-2.1-vaarg.patch
Patch3: ElectricFence-2.2.2-pthread.patch
Patch4: ElectricFence-2.2.2-madvise.patch
Patch5: ElectricFence-2.2.2-strerror.patch
Patch6: ElectricFence-mmap-size.patch
Patch7: ElectricFence-2.2.2-ef.patch
Patch8: ElectricFence-2.2.2-builtins.patch

%description
ElectricFence is a utility for C programming and
debugging. ElectricFence uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by
free(). ElectricFence will then stop the program on the first
instruction that caused a bounds violation and you can use your
favorite debugger to display the offending statement.

Install ElectricFence if you need a debugger to find malloc()
violations.

%prep
%setup
%patch1 -p1 -b .longjmp
%patch2 -p1 -b .vaarg
%patch3 -p1 -b .pthread
%patch4 -p1 -b .madvise
%patch5 -p2 -b .strerror
%patch6 -p1
%patch7 -p1
%patch8 -p1
%__subst "s|/lib\$|/%_lib|g" Makefile

%build
%make_build CFLAGS='${RPM_OPT_FLAGS} -DUSE_SEMAPHORE -fpic'

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_man3dir}
%makeinstall MAN_INSTALL_DIR=%buildroot%_man3dir
echo ".so man3/efence.3" > %buildroot%_mandir/man3/libefence.3

%files
%_bindir/ef
%_libdir/libefence.*
%_man3dir/*
%doc README CHANGES

%changelog
* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt3
- use strerror instead obsoleted str_error variable
- add patches from Fedora

* Sat Nov 14 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt2
- remove obsoleted post/postun section

* Fri Mar 30 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- cleanup spec

* Wed Aug 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt0.2
- fix build on x86_64

* Tue Aug 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt0.1
- resurrected from orphaned
- update spec, add URL, update Source URL
- sync with package from FC5

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 2.2.2-ipl2mdk
- rebuild

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.2-ipl1mdk
- RE adaptions.

* Sat Dec 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.2.2-1mdk
- new and shiny source.
- fix the build on x86 architecture.

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.0-11mdk
- BM, macros, _spechelper_

* Mon Apr 17 2000 Christopher Molnarc <molnarc@mandrakesoft.com> 2.2.0-10mdk
- new post and postun sections, call ldconfig
- split into ElectricFence and ElectricFence-devel

* Tue Apr 11 2000 Christopher Molnarc <molnarc@mandrakesoft.com> 2.2.0-9mdk
- new group Development/Other

* Wed Apr  5 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 2.2.0-8mdk
- updated BuildRoot
- new group Development/Debuggers

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 2.2.0-7mdk
- Added va patch for PPC

* Fri Jan 21 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.0-6mdk
- don't use broken Excludearch but use Exclusivearch to exclude alpha.

* Fri Nov 26 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- fix lib perms

* Thu Oct  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Rewrite the spec to be usuable (#279).

* Sat Jul 17 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
- 2.2.0

* Sun Jul  4 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip2 manpage

* Tue May 04 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
- add de locale

* Sat Apr 10 1999 Matt Wilson <msw@redhat.com>
- version 2.1

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 13)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- create efence.3 (problem #830)

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- need to use sigsetjmp() and siglongjmp() for proper testing

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExcludeArch instead of Exclude

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
