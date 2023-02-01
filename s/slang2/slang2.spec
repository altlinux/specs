%set_verify_elf_method strict
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1
%def_enable static

Name: slang2
Version: 2.3.3
Release: alt1

Summary: The shared library for the S-Lang extension language
License: GPL-2.0-or-later
Group: System/Libraries
Url: http://www.jedsoft.org/slang/

# https://www.jedsoft.org/releases/slang/slang-2.3.2.tar.bz2
Source: slang-%version.tar

Patch2: slang-2.3.3-owl-alt-fixes.patch
Patch3: slang-2.2.4-alt-doc.patch

Patch11: slang-2.2.4-deb-demos-make.patch
Patch12: slang-2.2.4-deb-hostent-haddr.patch

# Automatically added by buildreq on Tue Sep 25 2012
# optimized out: gnu-config pkg-config xorg-xproto-devel zlib-devel
BuildRequires: libICE-devel libX11-devel libncurses-devel libpcre-devel libpng-devel

# for src/test/posixio.sl
BuildRequires: /dev/pts

%package slsh
Summary: S-Lang shell
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name
Summary: The shared library for the S-Lang extension language
Group: System/Libraries
Provides: slang = %version

%package -n lib%name-devel
Summary: The development environment for S-Lang
Group: Development/C
Requires: lib%name = %version-%release
Provides: libslang-devel = %version
Obsoletes: libslang-devel < %version

%if_enabled static
%package -n lib%name-devel-static
Summary: The static library for development using S-Lang
Group: Development/C
Requires: lib%name-devel = %version-%release
%endif

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%description slsh
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

This package contains a stand-alone interpreter for scripts written
in the S-Lang language.

%description -n lib%name
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%description -n lib%name-devel
This package contains the S-Lang extension language development libraries
and header files which you'll need if you want to develop S-Lang based
applications.

%if_enabled static
%description -n lib%name-devel-static
This package contains the S-Lang extension language static libraries
which you'll need if you want to develop S-Lang based statically linked
applications.
%endif

%prep
%setup -n slang-%version
%patch2 -p1
%patch3 -p1

%patch11 -p1
%patch12 -p1

%build
%add_optflags %(getconf LFS_CFLAGS)

export ac_cv_func_snprintf=yes ac_cv_func_vsnprintf=yes
%configure \
	--includedir=%_includedir/slang \
	--with-{pcre,png,z}lib=%_libdir \
	--with-pcreinc=$(pkg-config libpcre --cflags |sed 's/^[^/]*//') \
	--with-pnginc=$(pkg-config libpng --cflags |sed 's/^[^/]*//') \
	--with-zinc=%_includedir \
	#
mkdir -p modules/objs slsh/objs src/elfobjs src/objs
%make_build RPATH= SLANG_LIB="-L$PWD/src/elfobjs -lslang"
%{?_enable_static:%make_build -C src static}

%install
%makeinstall_std RPATH= %{?_enable_static:install-static}
%define docdir %_docdir/slang-%version
mv %buildroot%_docdir/slang/v2 %buildroot%docdir
rmdir %buildroot%_docdir/slang
mv %buildroot%_docdir/slsh/html %buildroot%docdir/slsh
rmdir %buildroot%_docdir/slsh

%check
# for test_slsmg.sl
export TERM=xterm
%make check

%files slsh
%_sysconfdir/slsh.rc
%_bindir/slsh
%_datadir/slsh
%_man1dir/*
%dir %docdir/
%docdir/slsh/

%files -n lib%name
%_libdir/*.so.*
%_libdir/slang
%docdir/
%exclude %docdir/slsh/

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Feb 01 2023 Anton Farygin <rider@altlinux.ru> 2.3.3-alt1
- 2.3.3
- removed -fno-strict-overflow from %%optflags and slang-2.3.2-slarray-ub.patch
  (not need anymore)

* Sat Oct 16 2021 Anton Farygin <rider@altlinux.ru> 2.3.2-alt5
- fixed build with LTO

* Wed Jan 01 2020 Sergey Y. Afonin <asy@altlinux.org> 2.3.2-alt4
- enabled LFS support
- updated %%License to SPDX syntax
- improvements in spec-file:
 + added "%%define _unpackaged_files_terminate_build 1"
 + properly quoted "%%optflags" in changelog
 + fixed using "%%def_enable static"

* Tue Apr 09 2019 Sergey Y. Afonin <asy@altlinux.ru> 2.3.2-alt3
- added slang-2.3.2-slarray-ub.patch (fixed UB in slarray, ALT #36424#c25)
- added -fno-strict-overflow to %%optflags (ALT #36424#c17)

* Mon Apr 08 2019 Sergey Y. Afonin <asy@altlinux.ru> 2.3.2-alt2
- fixed gcc8 optimization on i586 (ALT #36424)

* Fri Aug 17 2018 Sergey Y. Afonin <asy@altlinux.ru> 2.3.2-alt1
- Updated to 2.3.2 (ALT #33982)
- Adapted alt-makefile.patch for slang 2.3.2
- Used %%make check instead %%make_build in %%check section

* Wed Sep 26 2012 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt2
- Changed libslang2-devel dependencies to replace libslang-devel.

* Tue Sep 25 2012 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt1
- Updated to 2.2.4 (ALT #24882).
- Fixed packaging (ALT #15151).

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2.1
- Removed bad RPATH

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2
- Rebuilt for debuginfo

* Wed Dec 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1
- Version 2.2.3 (ALT #24759)

* Tue May 26 2009 Nick S. Grechukh <gns@altlinux.org> 2.1.4-alt2
- new version

* Wed Mar 26 2008 Nick S. Grechukh <gns@altlinux.org> 2.1.3-alt2
- slang2, slightly based on debian package

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.9-alt1.0
- Automated rebuild.

* Wed May 18 2005 Kachalov Anton <mouse@altlinux.ru> 1.4.9-alt1
- 1.4.9
- UTF8 support

* Sun Dec 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7, rediffed patches.
- Repackaged documentation (#0001587).

* Mon Oct 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- 1.4.6
- Moved static library to -devel-static subpackage.
- Merged Owl changes (1.4.6-owl1):
  * Sat Oct 12 2002 Solar Designer <solar@owl.openwall.com>
  - Reviewed all of the library code for environment variable uses and
    restricted those which would be unsafe in SUID/SGID programs.
  - Corrected the examples to not use temporary files unsafely.
  - Enable snprintf() and vsnprintf() explicitly.

* Wed Feb 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.4.5-alt1
- 1.4.5

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.4-ipl1mdk
- 1.4.4.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.4.3-ipl1mdk
- 1.4.3.
- Libification.

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 1.4.2-ipl1mdk
- RE adaptions.

* Sun Aug 20 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.4.2-1mdk
- s|1.4.0|1.4.2|.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.0-6mdk
- automatically added BuildRequires

* Mon May 29 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.4.0-5mdk
- Move libslang.so from -devel to normal.

* Fri May 19 2000 Pixel <pixel@mandrakesoft.com> 1.4.0-4mdk
- move .so to devel
- add soname

* Tue May 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.4.0-3mdk
- Add link for alpha.

* Mon Mar 27 2000 Warly <warly@mandrakesoft.com> 1.4.0-2mdk
- fix doc path

* Sun Mar 26 2000 Warly <warly@mandrakesoft.com> 1.4.0-1mdk
- 1.4.0
- new package doc

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Jul 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.8.

* Mon Jun 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.7.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Oct 21 1998 Bill Nottingham <notting@redhat.com>
- libslang.so goes in -devel

* Sun Jun 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de

* Sat Jun  6 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.2.2 with buildroot.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 18 1998 Erik Troan <ewt@redhat.com>
- rebuilt to find terminfo in /usr/share

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 0.99.38 (will it EVER go 1.0???)
- all patches removed (all appear to be in this version)

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
