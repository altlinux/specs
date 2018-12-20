Name: bc
Version: 1.07.1
Release: alt1
Serial: 1

Summary: GNU's bc (a numeric processing language) and dc (a calculator)
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://www.gnu.org/software/bc/

# https://ftp.gnu.org/gnu/bc/bc-%version.tar.gz
Source: bc-%version.tar

Patch01: 01_typo_in_bc.diff
Patch02: 02_hyphens_as_minus_in_man.diff
Patch05: 05_notice_read_write_errors.diff
Patch06: 06_read_dcrc.diff
Patch07: 07_bc_man.diff
Patch08: 08_no-make-circular-dependencies.diff

Patch11: bc-alt-texinfo.patch
Patch12: bc-owl-functions-fix.patch
Patch13: bc-rh-dc_ibase.patch

BuildRequires: bison ed flex gcc libreadline-devel makeinfo

%description
This package includes bc and dc.  bc implements a numeric processing
language with interactive execution of statements.  dc is a stack-based
calculator.  Both bc and dc support arbitrary precision arithmetic.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p1

rm doc/*.info
rm bc/{bc,scan}.c
find -type f -name getopt\* -delete
sed -i 's/getopt[1]\?\.c //g' lib/Makefile.am

%build
%add_optflags -fno-strict-aliasing -fno-strict-overflow -DDONTEXIT
autoreconf -fisv
export ac_cv_lib_termcap_tgetent=no ac_cv_lib_ncurses_tparm=no
%configure --with-readline
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc Examples AUTHORS FAQ NEWS README

%changelog
* Thu Dec 20 2018 Dmitry V. Levin <ldv@altlinux.org> 1:1.07.1-alt1
- 1.06 -> 1.07.1.

* Mon Apr 18 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.06-alt4
- Added BR: makeinfo.
- Fixed build with makeinfo 6.

* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.06-alt3
- Removed obsolete %%install_info/%%uninstall_info calls.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.06-alt2
- Disabled optimization based on strict aliasing rules.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.06-alt1.1
- Rebuilt with libreadline.so.5.

* Sun Oct 23 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.06-alt1
- Applied patch from Debian to fix build with new flex.
- Build with getopt from glibc instead of bundled aged getopt.

* Thu Apr 14 2005 Stanislav Ievlev <inger@altlinux.org> 1.06-ipl6mdk
- Fixed build with fresh autotools.

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 1.06-ipl5mdk
- fix build in new environment (autoconf)

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 1.06-ipl4mdk
- rebuild with gcc3
- fix typo in the URL.

* Sun Jun 30 2002 Dmitry V. Levin <ldv@altlinux.org> 1.06-ipl3mdk
- Patched to link with libtinfo.
- More documentation included.
- Additional convention enforcement on patch file names.

* Mon May 07 2001 Stanislav Ievlev <inger@altlinux.ru> 1.06-ipl2mdk
- Add patch from OpenWall Project. scan.l bugfix

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 1.06-ipl1mdk
- Fixed texinfo documentation.
- RE adaptions.

* Sun Nov 19 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.06-1mdk
- new and shiny bc.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.05a-12mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05a-11mdk
- readd bc :-( (gl scks)

* Tue Jul 25 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.05a-10mdk
- macros
- BM

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 1.05a-9mdk
- mandrake release.

* Wed Mar 22 2000 dam's <damien@mandrakesoft.com> 1.05a-8mdk
- Build release.

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Fri Jul 30 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Compile with readline/history support

* Fri Apr  9 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix download URLs

* Thu Jan 21 1999 Jeff Johnson <jbj@redhat.com>
- use %%configure

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.05a.

* Sun Jun 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.05 with build root.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Erik Troan <ewt@redhat.com>
- got upgrades of info entry working (I hope)

* Sun Apr 05 1998 Erik Troan <ewt@redhat.com>
- fixed incorrect info entry

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- added install-info support

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.03 to 1.04

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
