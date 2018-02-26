Name: slang
Version: 1.4.9
Release: alt1.3

Summary: The shared library for the S-Lang extension language
License: GPLv2+
Group: System/Libraries
Url: http://www.s-lang.org/
Packager: Ilya Mashkin <oddity@altlinux.ru>

# ftp://ftp.jedsoft.org/pub/davis/%name/v1.4/%name-%version.tar.bz2
Source: %name-%version.tar
Source1: README.UTF-8

Patch1: %name-1.4.6-alt-makefile.patch
Patch2: %name-1.4.7-owl-alt-fixes.patch
Patch3: %name-1.4.7-alt-doc.patch
Patch4: %name-1.4.4-deb-utf8.patch
Patch5: %name-1.4.5-utf8-acs.patch
Patch6: %name-1.4.5-utf8-fix.patch
Patch7: %name-1.4.5-utf8-segv.patch
Patch8: %name-1.4.9-mdk-utf8-revert_soname.patch

%package -n lib%name
Summary: The shared library for the S-Lang extension language
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name

%package -n lib%name-devel
Summary: The development environment for S-Lang
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%package -n lib%name-devel-static
Summary: The static library for development using S-Lang
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static

%package -n lib%name-doc
Summary: Extra documentation for S-Lang libraries
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-doc = %version
Obsoletes: %name-doc

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

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

%description -n lib%name-devel-static
This package contains the S-Lang extension language static libraries
which you'll need if you want to develop S-Lang based statically linked
applications.

%description -n lib%name-doc
This package contains documentation which may help you write S-Lang based
applications.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%__subst 's/\(ELF_CFLAGS="[^"]*\)-O2\([^"]*".*\)/\1'"$RPM_OPT_FLAGS"'\2/g' configure

%build
%{expand: %%define _includedir %_includedir/%name}
export ac_cv_func_snprintf=yes ac_cv_func_vsnprintf=yes
%configure --enable-warnings
%make_build elf all

%install
mkdir -p %buildroot%_includedir
%makeinstall install-elf

chmod a+x %buildroot%_libdir/*.so.*

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
cp -pRL changes.txt COPYRIGHT NEWS %SOURCE1 doc/{README,grammar.txt,text,internal} \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/changes.txt

mkdir -p %buildroot%_datadir/%name
ln -s `relative %docdir/text %_datadir/%name/help` %buildroot%_datadir/%name/help


%files -n lib%name
%_libdir/*.so.*
%dir %docdir
%docdir/[CNc]*

%files -n lib%name-devel
%_libdir/*.so
%_includedir

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-doc
%doc %_datadir/%name
%dir %docdir
%docdir/[Rgti]*

%changelog
* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt1.3
- Rebuilt for debuginfo.

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.9-alt1.2
- Rebuilt for soname set-versions

* Sat Dec 20 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.9-alt1.1
- remove deprecated post/postun_ldconfig

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
