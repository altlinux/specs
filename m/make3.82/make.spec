%define ver 3.82
Name: make%ver
Version: 3.82
Release: alt2
Epoch:   2

Summary: A GNU tool which simplifies the build process for users
License: GPLv3
Group: Development/Other
Url: http://www.gnu.org/software/make/
Packager: Alexey Gladkov <legion@altlinux.org>

# ftp://ftp.gnu.org/gnu/make/make-%version.tar.bz2
Source: make-%version.tar
Patch1: make-3.82-err-reporting.patch
Patch2: make-3.82-getcwd.patch
Patch3: make-3.82-j8k.patch
Patch4: make-3.82-jobserver.patch
Patch5: make-3.82-newlines.patch
Patch6: make-3.82-weird-shell.patch
Patch7: make-3.82-bugfixes.patch
Patch8: make-3.82-sort-blank.patch


%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files.
Make allows users to build and install packages without any significant
knowledge about the details of the build process.  The details about
how the program should be built are provided for make in the program's
makefile.

%prep
%setup -q -n make-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
bzip2 -9k NEWS ChangeLog
rm doc/*.info*

%build
%autoreconf

# Enable mkstemp explicitly, not rely on configure (Owl).
export ac_cv_func_mkstemp=yes
%configure --program-suffix=-%ver
%make_build

%install
%makeinstall
ln -sf make-%ver %buildroot%_bindir/gmake-%ver

find %buildroot%_infodir -name 'make.info*' |
while read fn; do
	name="${fn##*/}"
	new_fn="${fn%%/*}/make-%ver.${name#make.}"
	mv -f -- "$fn" "$new_fn"
done

find %buildroot%_datadir/locale -name '*.mo' |
while read fn; do
	new_fn="${fn%%/*}/make-%ver.mo"
	mv -f -- "$fn" "$new_fn"
done

%find_lang make-%ver

%check
%make_build -k check

%files -f make-%ver.lang
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS ChangeLog.bz2 NEWS.bz2 README

%changelog
* Thu Feb 24 2011 Alexey Gladkov <legion@altlinux.ru> 2:3.82-alt2
- Add upstream fixes.
- Add fedora patches.

* Sat Aug 21 2010 Alexey Gladkov <legion@altlinux.ru> 2:3.82-alt1
- Updated to 3.82.
- Package was renamed because of incompatibility with the previous version.

* Sat Jun 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2:3.81-alt5
- Fixed tests/scripts/features/recursion.
- Updated fixes from Debian make-3.81-8.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2:3.81-alt4
- Moved "make check" to %%check section.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2:3.81-alt3
- Removed obsolete %%install_info/%%uninstall_info calls.
- Imported fixes from Debian make-3.81-5.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 2:3.81-alt2
- Backported upstream fix to ENULLLOOP macro.
- Fixed getcwd() redeclaration.
- Added -jN sanity check.

* Sat Apr 01 2006 Dmitry V. Levin <ldv@altlinux.org> 2:3.81-alt1
- Updated to 3.81 release.

* Mon Mar 20 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.81rc2-alt1
- Updated to 3.81rc2.

* Mon Mar 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.81rc1-alt3
- Updated to cvs snapshot 20060310.

* Tue Feb 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.81rc1-alt2
- Updated to cvs snapshot 20060221.

* Mon Feb 20 2006 Dmitry V. Levin <ldv@altlinux.org> 1:3.81rc1-alt1
- Updated to 3.81rc1.

* Wed Dec 14 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta4-alt1
- Updated to 3.81beta4.

* Tue Jun 28 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta3-alt4
- Updated to 3.81beta3.

* Fri Jun 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta3-alt3
- Updated to cvs snapshot 20050609.

* Thu May 12 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta3-alt2
- Updated to cvs snapshot 20050510.

* Sun May 08 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta3-alt1
- Updated to cvs snapshot 20050503.

* Wed Apr 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt7
- Updated to cvs snapshot 20050413.
- Vain attempt to workaround reap_children bug
  while upstream is working on the fix.

* Fri Apr 08 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt6
- Updated to cvs snapshot 20050408 (fixes Savannah bug #12331
  and allows to workaround Savannah bug #12260).

* Tue Mar 15 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt5
- Updated to cvs snapshot 20050315 (fixes Savannah bug #12320).

* Thu Mar 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt4
- Updated to cvs snapshot 20050310 (fixes Savannah bug #12267).

* Sat Mar 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt3
- Updated to cvs snapshot 20050303 (fixes Savannah bug #12202).

* Thu Mar 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt2
- Updated to cvs snapshot 20050301 (fixes #6153).
- Merged upstream patch removed: alt-func_shell-filenm.

* Wed Feb 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta2-alt1
- Updated to 3.81beta2.

* Fri Apr 16 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.81beta1-alt1
- Updated to 3.81beta1.
- Updated patches.

* Mon Apr 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1:3.80-alt1
- Updated to 3.80.
- Almost all patches merged upstream.

* Mon Sep 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.79.1-ipl6mdk
- Merged in debian patches, including:
  + fixed the problem in expansion of target specific variables (#0000791);
  + fixed the problem with make not echoing commands correctly;
  + fixed the command execution problem.

* Tue Feb 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:3.79.1-ipl5mdk
- Disabled linking with -lrt.
- Fixed i18n support.
- Fixed buildreq support.
- Fixed build.

* Wed Dec 06 2000 Dmitry V. Levin <ldv@fandra.org> 3.79.1-ipl4mdk
- Undefine _configure_gettext to fix building.
- Fixed texinfo documentation.

* Thu Sep 21 2000 Dmitry V. Levin <ldv@fandra.org> 3.79.1-ipl3mdk
- Automatically added BuildRequires.

* Sat Sep 09 2000 Dmitry V. Levin <ldv@fandra.org> 3.79.1-ipl2mdk
- FHS rebuild.

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org>
- update to 3.79.1.

* Fri Apr 14 2000 Dmitry V. Levin <ldv@fandra.org>
- update to 3.79.

* Tue Sep 30 1999 Dmitry V. Levin <ldv@fandra.org>
- update to 3.78.1.
- make test
- Fandra adaptions

* Tue Jul 27 1999 Dmitry V. Levin <ldv@fandra.org>
- update to 3.77.91

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- added a serial tag so it upgrades right

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for large file support in glob

* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.77

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- udpated from 3.75 to 3.76
- various spec file cleanups
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
