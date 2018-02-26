Name: ed
Version: 0.2
Release: alt9
Epoch: 1

Summary: The GNU line-oriented text editor
License: GPLv2+
Group: Text tools
Url: http://www.gnu.org/software/ed/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.gnu.org/gnu/ed/ed-%version.tar.gz
Source: ed-%version.tar

Patch1: ed-0.2-alt-configure.patch
Patch2: ed-0.2-alt-error.patch
Patch3: ed-0.2-deb-makefile.patch
Patch4: ed-0.2-deb-parentheses.patch
Patch5: ed-0.2-alt-tmp.patch
Patch6: ed-0.2-alt-progname.patch
Patch7: ed-0.2-deb-owl-man.patch
Patch8: ed-0.2-alt-man-tmp.patch
Patch9: ed-0.2-alt-texinfo.patch
Patch10: ed-0.2-alt-glibc.patch
Patch11: ed-0.2-alt-warnings.patch
Patch12: ed-0.2-alt-bound.patch

%description
ed is a line-oriented text editor, used to create, display, and modify
text files (both interactively and via shell scripts).
For most purposes, ed has been replaced in normal usage by full-screen
editors such as vi and emacs.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

find -type f -name \*.orig -delete
rm getopt.h regex.h

%build
# ed lives in /bin.
%define _bindir	/bin
# Disable rscid information.
%add_optflags -Dlint
# glibc does have sigsetjmp, it's just a macro, which confuses autoconf.
export ac_cv_func_sigsetjmp=yes
autoreconf -fisv
%configure

%make_build

%check
%make_build -k check

%install
%makeinstall mandir=%buildroot%_man1dir

%files
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc ChangeLog NEWS POSIX README THANKS TODO

%changelog
* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt9
- Moved "make check" to %%check section.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt8
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Aug 31 2008 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt7
- Fixed potential heap buffer overflow in strip_escapes(),
  reported by Alfredo Ortega from Core Security Technologies.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt6
- Fixed compilation warnings.

* Sun Jul 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt5
- Updated URL, summary, description and texinfo entry.

* Thu Apr 07 2005 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt4
- Migrated to new autotools.
- Disabled build of code provided by glibc.

* Thu Jul 10 2003 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt3
- Updated documentation notes about buffer file location.
- Deal with info dir entries such that the menu looks pretty.
- Reverted change made in 1:0.2-alt2.2 (fixed librpm instead).

* Wed Jun 25 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2-alt2.2
- __install_info now PreReq (problems during package installation).

* Tue Jun 17 2003 Stanislav Ievlev <inger@altlinux.ru> 1:0.2-alt2.1
- fix building in bte.

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt2
- Added "alt-error" portability patch (for non-glibc platforms).

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.2-alt1
- Minor specfile cleanup; changed release numbering.
- Replaced "security-tempfile" patch with "alt-tmp" patch.
- Fixed program_name initialization.
- Applied fixes for compilation warnings (deb).
- Applied fixes for ed(1) manpage (deb).
- Explicitly build with sigsetjmp.
- Disabled rcsid information.
- Added run of testcase after build.

* Thu Jan 24 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-ipl23mdk
- patch #3

* Thu Nov 30 2000 Dmitry V. Levin <ldv@fandra.org> 0.2-ipl22mdk
- Fixed texinfo documentation.

* Mon Nov 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2-22mdk
- Optimisations.
- Add security patch for tempfile open.

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-21mdk
- fix bad script

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-20mdk
- minor fix

* Tue Jul 25 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.2-19mdk
- macroszifications
- BM
* Wed Jun 07 2000 Etienne Faure <etienne@mandrakesoft.com> 0.2-18mdk
- rebuild on kenobi

* Thu Apr 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.2-17mdk
- Clean-up specs.
- * Sun Apr 23 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- let the spechelper handle compressing man / info pages

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 0.2-16mdk
- move to Text tools group

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add defattr

* Wed May 19 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- fix typo in %preun
- fix download URL

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added install-info support
- added BuildRoot
- correct URL in Source line

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
