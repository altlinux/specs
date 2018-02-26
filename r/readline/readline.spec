Name: readline
%define rl_version 5.2
%define rl_patch 14
%define srcname readline-%rl_version
Version: %rl_version.%rl_patch
Release: alt3

Summary: A library for editing typed in command lines
License: GPLv2+
Group: System/Libraries
Url: http://www.gnu.org/software/readline/

# ftp://ftp.gnu.org/gnu/readline/readline-%rl_version.tar.gz
# ftp://ftp.gnu.org/gnu/readline/readline-%rl_version-patches/
Source: readline-%version.tar

Patch: readline-%version-%release.patch

# Automatically added by buildreq on Mon Sep 02 2002
BuildRequires: libtinfo-devel

%define compat_list %nil
%define lib_suffix %nil
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}

%package -n lib%name
Summary: A library for editing typed in command lines
Group: System/Libraries
Obsoletes: readline
Provides: readline = %version-%release
%if "%compat_list" != ""
Provides: %(for n in %compat_list; do echo -n "libhistory.so.$n%lib_suffix libreadline.so.$n%lib_suffix "; done)
%endif

%package -n lib%name-devel
Summary: Files needed to develop programs which use the readline library
Group: Development/C
Provides: readline-devel = %version-%release
Obsoletes: readline-devel
PreReq: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: Files needed to develop statically linked programs which use the readline library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
The readline library reads a line from the terminal and returns it,
allowing the user to edit the line with standard emacs editing keys.

%description -n lib%name
The readline library reads a line from the terminal and returns it,
allowing the user to edit the line with standard emacs editing keys.

%description -n lib%name-devel
The readline library reads a line from the terminal and returns it,
allowing the user to edit the line with standard emacs editing keys.

This package contains the files needed to develop programs which use
the readline library to provide an easy to use and more intuitive
command line interface for users.

%description -n lib%name-devel-static
The readline library reads a line from the terminal and returns it,
allowing the user to edit the line with standard emacs editing keys.

This package contains the files needed to develop statically linked
programs which use the readline library to provide an easy to use
and more intuitive command line interface for users.

%prep
%setup -q
%patch -p1

%build
# This is required to fix some "implicit declaration" warnings.
%add_optflags -D_GNU_SOURCE

# Link with libtinfo unconditionally.
export bash_cv_termcap_lib=libtinfo

# Workaround for buildreq/strace.
%{?__buildreqs:export bash_cv_must_reinstall_sighandlers=no}

# Fix temporary file handling.
sed -i 's,/tmp/,,g' *.m4
autoconf

%configure
rm doc/*.info

%make_build all examples documentation

%install
%makeinstall_std

# Relocate shared libraries from %_libdir/ to /%_lib/.
soname=$(readlink "%buildroot%_libdir/libreadline.so")
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

for v in %compat_list; do
	for n in readline history; do
		t=$(readlink "%buildroot%_libdir/lib$n.so")
		ln -s "../../%_lib/$t" "%buildroot%_libdir/lib$n.so.$v"
	done
done

# Replace libreadline.so symlink with a linker script.
rm %buildroot%_libdir/libreadline.so
cat >%buildroot%_libdir/libreadline.so <<__EOF__
/* GNU ld script */
GROUP(/%_lib/$soname AS_NEEDED(-lhistory))
__EOF__

# Relocate and fix documentation.
%define docdir %_docdir/readline-%version
mkdir -p %buildroot%docdir
cp -a README CHANGE* USAGE examples \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/CHANGE*
cp -p config.h posixstat.h xmalloc.h \
	%buildroot%docdir/examples/
pushd %buildroot%docdir/examples
	sed -i 's,\.\./shlib/lib\([^.]\+\)\.so,-l\1,' Makefile
	sed -i 's,^\(top_srcdir *=\).*,\1 %_includedir/readline,g;s,^\(LDFLAGS *=\).*,\1,g' Makefile
	make clean
popd

%set_verify_elf_method strict

%files -n lib%name
/%_lib/*
%if "%compat_list" != ""
%_libdir/*.so.*
%endif

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%_infodir/*.info*
%docdir

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Feb 10 2011 Dmitry V. Levin <ldv@altlinux.org> 5.2.14-alt3
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 5.2.14-alt2
- Rebuilt for soname set-versions.

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 5.2.14-alt1
- Updated to 5.2 patchlevel 14.
- Backported upstream fix for completion bug.

* Fri Jun 05 2009 Dmitry V. Levin <ldv@altlinux.org> 5.2.13-alt1
- Updated to 5.2 patchlevel 13.
- Imported redisplay-sigint.patch from FC.
- Imported audit.patch from FC (RH#476216).
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 5.2.11-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Tue Mar 25 2008 Dmitry V. Levin <ldv@altlinux.org> 5.2.11-alt1
- Updated to 5.2 patchlevel 11.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 5.1.4-alt3
- Synced with readline-5.1-owl1.

* Thu Mar 23 2006 Dmitry V. Levin <ldv@altlinux.org> 5.1.4-alt2
- Applied specfile enhancements from 4.3-alt8.

* Fri Mar 17 2006 Dmitry V. Levin <ldv@altlinux.org> 5.1.4-alt1
- Updated to 5.1 patchlevel 4.

* Mon Feb 06 2006 Dmitry V. Levin <ldv@altlinux.org> 5.1.2-alt1
- Updated to 5.1 patchlevel 2.

* Wed Dec 28 2005 Dmitry V. Levin <ldv@altlinux.org> 5.1.1-alt1
- Updated to 5.1 patchlevel 1.
- Reviewed and updated patches.
- Dropped compatibility symlinks because new libhistory
  breaks backwards binary compatibility.
- Restricted list of global symbols exported by libraries
  to the list of symbols mentioned in the public API.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt7
- Fixed multilib (closes #4895).

* Wed Apr 28 2004 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt6
- Rebuilt with glibc-2.3.x.

* Sun Mar 21 2004 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt5
- Applied 3 more official patches.
- Merged to official patches:
  + chet-mbyte
  + alt-mbutil-fixes
- Applied 3 more debian patches:
  + include stdio.h in readline.h and history.h;
  + speedup long lines processing in multibyte locales;
  + fix typo in readline(3) manpage.
- Linked readline library with -lhistory -ltinfo.

* Tue Dec 24 2002 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt4
- mbutil.c (_rl_get_char_len,_rl_adjust_point):
  Fixed several potential null dereferences.

* Sat Dec 14 2002 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt3
- Fixed histexpand utf8 problem (rh).
- nls.c (_rl_init_eightbit): Instead of setting the LC_CTYPE
  locale category from environment variables, query it from
  the program's current locale.
- Prevent prompt overwriting output for multibyte locales,
  patch from Chet Ramey.

* Sun Sep 29 2002 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt2
- Applied two "official" patches from
  ftp://ftp.cwru.edu/pub/bash/readline-4.3-patches/.
- Merged two debian patches:
  + handle key sequence sent by the Delete key, if any;
  + support for /etc/inputrc in addition to ~/inputrc.

* Sun Sep 15 2002 Dmitry V. Levin <ldv@altlinux.org> 4.3-alt1
- 4.3
- Patch out rpath.
- Fixed most of compilation warnings.
- Added 4.2 shlib symlink for compatibility.
- Relocated documentation, fixed examples.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 4.2a-alt3
- Fixed library symlinks generation.
- Use subst instead of perl for build.
- Relocated compatibility symlinks from /%_lib/ to %_libdir/.
- Updated devel-static requirements.

* Sat Jun 29 2002 Dmitry V. Levin <ldv@altlinux.org> 4.2a-alt2
- Updated buildrequires.

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.2a-alt1
- 4.2a, dropped outdated patches.

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-alt5
- Use strpbrk implementation from glibc (rh).

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-alt4
- Make sure headers can be included from C++ applications.

* Thu May 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-alt3
- Dropped buggy resize patch.
- Updated requires according to new policy.

* Tue May 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-alt2
- Fixed requires.

* Wed Apr 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-alt1
- 4.2
- Libification.

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.1-ipl9mdk
- Fixed provides list.

* Mon Oct 30 2000 Dmitry V. Levin <ldv@fandra.org> 4.1-ipl8mdk
- Check for arithmetic overflow (by RH).
- FHSification.

* Tue Jun 13 2000 Dmitry V. Levin <ldv@fandra.org> 4.1-ipl7mdk
* RE and Fandra adaptions.

* Mon Jun 12 2000 Pixel <pixel@mandrakesoft.com> 4.1-7mdk
- add .so's in /usr/lib for -devel
- move .a's in /usr/lib

* Mon Jun 12 2000 Pixel <pixel@mandrakesoft.com> 4.1-6mdk
- move doc to -devel (was partially done, hurk), that way, no more prerequisite
on shell.

* Fri Jun  9 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.1-5mdk
- move libraries in /lib.

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.1-4mdk
- s|/usr/local/bin/perl|/usr/bin/perl|;

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.1-3mdk
- add documentation, support and examples

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 4.1-2mdk
- remove rluserman install-info

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 4.1-1mdk
- new version
- much cleanup
- patch for strange buggy Makefile
- remove the trigger, i prefer require

* Tue Feb  8 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.0-8mdk
- Make sure to have the *so in the %files(>#751).

* Sun Feb  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.0-7mdk
- Librairies in /usr/lib no binaries on /bin/ or /sbin need
  libreadline.(#751).

* Sun Feb 06 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Leave libraries in /usr/lib/

* Tue Nov 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong link (#426).

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build Release.

* Sun Jul 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
- move dynamic libraries to /lib rather than /usr/lib - a dynamically linked
  primary shell depends on them to run...
- Install info pages in %trigger -- info - readline has to be installed
  before info because bash depends on it.

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adptation.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- set compatibility links + provides for older versions, like those
  used in Red Hat 6.0
- add de locale

* Wed Mar 10 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- relink with ncurses 5.0

* Sat Dec  5 1998 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- bzip2 info/man pages
- use ncurses rather than termcap

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.2.1

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- added proper sonames

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- updated to readline 2.1

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
