Name: m4
Version: 1.4.16
Release: alt2

Summary: The GNU macro processor
License: GPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/m4/

# ftp://ftp.gnu.org/gnu/m4/%name-%version.tar.xz
Source: m4-%version.tar
Source1: m4.m4
Patch: gnulib-up-tests-readlink.patch

%description
A GNU implementation of the traditional UNIX macro processor.  m4 is
useful for writing text files which can be logically parsed, and is
used by many programs as part of their build process.  m4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts,
but not for running configure scripts.

%prep
%setup
%patch -p1

%build
rm doc/*.info*
%configure --without-included-regex
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std
install -pD -m644 %_sourcedir/m4.m4 %buildroot%_datadir/aclocal/m4.m4

%check
%make_build -k check

%files
%_bindir/*
%_infodir/*.info*
%_man1dir/*
%_datadir/aclocal/*
%doc AUTHORS BACKLOG NEWS README THANKS TODO

%changelog
* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt2
- Fixed build on linux kernel >= 2.6.39.

* Wed Mar 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt1
- Updated to 1.4.16.

* Thu Sep 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.15-alt1
- Updated to 1.4.15.

* Sat Feb 27 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.14-alt1
- Updated to 1.4.14.
- Updated m4.m4 from autoconf-v2.65-6-g4a814e4.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt2
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt1
- Updated to 1.4.13.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Wed Oct 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- Updated to 1.4.6.
- Removed obsolete patches.

* Fri Oct 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Fri Apr 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.
- Updated patches.

* Mon Jan 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt3
- Updated to released tarball.
- Merged upstream patches: alt-format.
- Updated patches: alt-glibc.

* Fri Oct 04 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt2
- Explicitly use autoconf-2.13 for build.
- Use getopt, error, libintl, obstack implementations from
  glibc rather then build them statically here
- Added m4.m4 from autoconf-2.54 (Alexey Morozov).
- Additional convention enforcement on patch file names.

* Thu Oct 25 2001 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl20mdk
- Fixed format string bug.

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl19mdk
- RE adaptions.
- Patched siginfo stuff.
- Fixed texinfo documentation.

* Thu Dec  7 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 1.4-19mdk
- Run automated tests at build time
- Use RPM_OPT_FLAGS.  Damn, who forgot that one.

* Fri Nov 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-18mdk
- build for gcc-2.96

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-17mdk
- BM

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-16mdk
- spechelper fixes
- group fix

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.
- Fix building as user.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added info file handling and BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

