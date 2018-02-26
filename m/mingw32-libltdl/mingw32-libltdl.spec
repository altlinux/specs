# Define this to run tests (requires Wine, and won't work inside mock or Koji).
# Note: As of libtool-1.5.26, libltdl does not contain any tests at all.
%define run_tests 0

Summary: Runtime libraries for GNU Libtool Dynamic Module Loader
Name: mingw32-libltdl
Version: 1.5.26
Release: alt1
Group: System/Libraries
# Even though the source package contains files under
# "GPLv2+ and LGPLv2+ and GFDL", the binary RPM only ships LGPLv2+ code.
License: LGPLv2+
Group: Development/Tools

Packager: Boris Savelev <boris@altlinux.org>

Source: http://ftp.gnu.org/gnu/libtool/libtool-%version.tar.gz
Url: http://www.gnu.org/software/libtool/

# don't  read .la file in current working directory, root might get tricked
# into running a prepared binary in that directory:
Patch2: libtool-1.5.24-relativepath.patch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc

%if %run_tests
BuildRequires: wine
%endif

BuildArch: noarch

%description
The mingw32-libltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules, for the mingw32 cross compilation
environment.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%prep
%setup -n libtool-%version -q
%patch2 -p1

%build
export PATH=%_mingw32_bindir:$PATH

#./bootstrap

cd libltdl
export CXX=false
export F77=false
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
# dumb redhat-rpm-config replaces config.{sub,guess} with ancient ones in %%configure, use ./configure instead:
# %%_mingw32_configure does not make that error :)
%_mingw32_configure --enable-shared
# build not smp safe:
make

%check
%if %run_tests
cd libltdl
make check VERBOSE=yes > make_check.log 2>&1 || (cat make_check.log && false)
%endif

%install
cd libltdl
%makeinstall_std
rm -f %buildroot%_mingw32_libdir/libltdl.a

%files
%doc AUTHORS NEWS THANKS TODO ChangeLog
%doc libltdl/COPYING.LIB libltdl/README
%_mingw32_libdir/libltdl.dll.a
%_mingw32_bindir/libltdl-3.dll
%_mingw32_libdir/libltdl.la
%_mingw32_includedir/ltdl.h

%changelog
* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 1.5.26-alt1
- initial build for Sisyphus

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.26-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-12
- Make sure tests would work (if there were any)

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-11
- conditionally run tests (instead of always commenting them out)
- configure: Let implicit --host argument do its work

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-10
- fix license: only consider content of binary RPM

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-9
- remove obsolete requires(post/pre)
- remove mingw32-gcc-c++ requirement

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-8
- Call configure with --host instead of setting CC and CXX.
- Use BuildArch: noarch

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-7
- Remove unneeded %%pre and %%post
- Unify libltdl and libltdl-devel package as libltdl

* Mon Feb  2 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-6
- Fix forgotten dependency of -devel subpackage.

* Sun Feb  1 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.26-5
- Convert native libtool.spec to mingw32-libltdl.spec

* Fri Aug 29 2008 Dennis Gilmore <dennis@ausil.us> 1.5.26-4
- rebuild for gcc-4.3.2

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.26-3
- fix license tag

* Mon Jun 09 2008 Dennis Gilmore <dennis@ausil.us> 1.5.26-2
- build against gcc 4.3.1

* Tue May 20 2008 Stepan Kasal <skasal@redhat.com> 1.5.26-1
- new upstream version, requires autoconf >= 2.58

* Wed Jan 30 2008 Bill Nottingham <notting@redhat.com> 1.5.24-6
- rebuild for new gcc

* Wed Jan 23 2008 Karsten Hopp <karsten@redhat.com> 1.5.24-5
- add missing define

* Wed Jan 23 2008 Karsten Hopp <karsten@redhat.com> 1.5.24-4
- require specific gcc version as that path is hardcoded in libtool
  (#429880)

* Wed Aug 29 2007 Karsten Hopp <karsten@redhat.com> 1.5.24-3
- fix license tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.5.24-2
- Rebuild for selinux ppc32 issue.

* Tue Jul 24 2007 Karsten Hopp <karsten@redhat.com> 1.5.24-1
- update to libtool 1.5.24

* Thu Apr 05 2007 Karsten Hopp <karsten@redhat.com> 1.5.22-11
- use ./configure so that config.{sub,guess} will not be replaced with ancient
  version of those files (#234778)

* Wed Mar 14 2007 Karsten Hopp <karsten@redhat.com> 1.5.22-10
- add disttag (#232204)

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 1.5.22-10
- fix libtool-ltdl post/postun requirements

* Thu Feb 08 2007 Karsten Hopp <karsten@redhat.com> 1.5.22-9
- fix ltdl file open (#225116)
- fix lt_unset usage (#227454)
- spec file cleanups for merge review

* Mon Jan 22 2007 Karsten Hopp <karsten@redhat.com> 1.5.22-8
- don't abort (un)install scriptlets when _excludedocs is set (#223708)

* Thu Dec 07 2006 Karsten Hopp <karsten@redhat.com> 1.5.22-7
- update config.guess, config.sub with newer files from automake-1.10
- skip over lines in %_sysconfdir/ld.so.conf.d/* which don't look like absolute paths
  (p.e. files from kernel-xen). This avoids having unwanted relative paths in
  lib_search_path

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.5.22-6.1
- rebuild

* Thu Jun 29 2006 Karsten Hopp <karsten@redhat.de> 1.5.22-6
- detect gcc path at runtime instead of requiring one specific version

* Thu Jun 29 2006 Karsten Hopp <karsten@redhat.de> 1.5.22-5
- miscellaneous upstream fixes

* Tue Jun 06 2006 Karsten Hopp <karsten@redhat.de> 1.5.22-4
- don't warn when %_sysconfdir/ld.so.conf.d/*.conf doesn't exist (p.e. in mock)

* Fri May 26 2006 Jakub Jelinek <jakub@redhat.com> 1.5.22-3
- rebuilt with GCC 4.1.0

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.5.22-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.5.22-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb 06 2006 Karsten Hopp <karsten@redhat.de> 1.5.22-2
- libtool-ltdl-devel is LGPL (#168075)

* Tue Dec 20 2005 Karsten Hopp <karsten@redhat.de> 1.5.22-1
- update to 1.5.22, most prominent fixes are:
  - Fix 1.5 regression that caused linking a program `-static' to also
    link statically against installed libtool libraries, contrary to
    documented (and actual 1.4.x) behavior.
  - Fix silent failure of `libtoolize --ltdl' if libltdl files not present.

* Wed Nov 30 2005 Warren Togami <wtogami@redhat.com> 1.5.20-5
- rebuilt with GCC 4.1.0

* Thu Sep 29 2005 Jakub Jelinek <jakub@redhat.com> 1.5.20-4
- rebuilt with GCC 4.0.2

* Wed Sep 14 2005 Karsten Hopp <karsten@redhat.de> 1.5.20-3
- rebuilt

* Mon Sep 12 2005 Karsten Hopp <karsten@redhat.de> 1.5.20-2
- add ltdl license, minor spec-file cleanups (#168075, Ville Skyttä)

* Fri Sep 09 2005 Karsten Hopp <karsten@redhat.de> 1.5.20-1
- update

* Thu Sep 08 2005 Florian La Roche <laroche@redhat.com>
- add version-release to the Provides: and fix our own
  Requires: line to the current naming scheme

* Sat Jul  9 2005 Jakub Jelinek <jakub@redhat.com> 1.5.18-3
- rebuilt with GCC 4.0.1.

* Tue May 17 2005 Alexandre Oliva <aoliva@redhat.com> 1.5.18-2
- Update patch file.

* Tue May 17 2005 Alexandre Oliva <aoliva@redhat.com> 1.5.18-1
- 1.5.18.  Removed .multilib2 suffix.

* Tue Apr 26 2005 Alexandre Oliva <aoliva@redhat.com> 1.5.16.multilib2-1
- 1.5.16 fixes #132435.

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar  1 2005 Alexandre Oliva <aoliva@redhat.com> 1.5.14.multilib2-5
- use gfortran instead of g77.
- rebuild with GCC 4.

* Tue Feb 15 2005 Joe Orton <jorton@redhat.com> 1.5.14.multilib2-4
- revert to the old multilib patch (#138742)

* Sun Feb 13 2005 Florian La Roche <laroche@redhat.com>
- 1.5.14 bugfix release

* Sun Feb  6 2005 Daniel Reed <djr@redhat.com> 1.5.12.multilib2-3.4.3
- update to the 1.5.12 bugfix release
  - Makes use of $datarootdir, which is necessary for Autoconf >= 2.60.
  - Correctly skip hppa, x86_64, and s390* in tests/demo-nopic.test.
  - Interpret `include' statements in toplevel ld.so.conf file.
  - While "parsing" %_sysconfdir/ld.so.conf, skip comments.
- add dependency on gcc version; %_bindir/libtool hardcodes paths into gcc's internal directories
- replace "libtool-libs" with "libtool-ltdl" and "libtool-ltdl-devel"

* Tue Oct 26 2004 Daniel Reed <djr@redhat.com> 1.5.10-1
- update to the 1.5.10 bugfix release
  - obsoletes libtool-1.4-nonneg.patch
  - obsoletes libtool-1.5-libtool.m4-x86_64.patch
  - obsoletes libtool-1.4.2-multilib.patch
  - obsoletes libtool-1.4.2-demo.patch
  - obsoletes libtool-1.5-testfailure.patch

* Tue Jul  6 2004 Jens Petersen <petersen@redhat.com> - 1.5.6-4
- improve buildrequires and prereqs
- buildrequire texinfo (Dawid Gajownik, 126950)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 13 2004 Thomas Woerner <twoerner@redhat.com> - 1.5.6-2
- compile libltdl.a PIC

* Mon Apr 12 2004 Jens Petersen <petersen@redhat.com> - 1.5.6-1
- update to 1.5.6 bugfix release

* Sun Apr  4 2004 Jens Petersen <petersen@redhat.com> - 1.5.4-1
- 1.5.4 bugfix release
- improve libtool-1.4.2-multilib.patch (Albert Chin) and only apply to
  libtool.m4
- use bootstrap instead of autoreconf to update configuration
- update libtool-1.4.3-ltmain-SED.patch to libtool-1.5.4-ltmain-SED.patch

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 26 2004 Jens Petersen <petersen@redhat.com> - 1.5.2-1
- update to 1.5.2 bugfix release
- update libtool-1.5-libtool.m4-x86_64.patch
- nolonger need libtool-1.5-mktemp.patch, libtool-1.5-expsym-linux.patch,
  libtool-1.5-readonlysym.patch, libtool-1.5-relink-libdir-order-91110.patch,
  libtool-1.5-AC_PROG_LD_GNU-quote-v-97608.patch and libtool-1.5-nostdlib.patch

* Tue Oct 28 2003 Jens Petersen <petersen@redhat.com> - 1.5-8
- update libtool-1.4.2-multilib.patch to also deal with powerpc64 (#103316)
  [Joe Orton]

* Sun Oct 26 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild again, Jakub has done a new compiler version number

* Thu Oct 02 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Thu Jul 17 2003 Jens Petersen <petersen@redhat.com> - 1.5-5
- bring back libtool-1.4.2-demo.patch to disable nopic tests on amd64
  and s390x again

* Tue Jul 15 2003 Owen Taylor <otaylor@redhat.com>
- Fix misapplied chunk for expsym-linux patch

* Tue Jul  8 2003 Jens Petersen <petersen@redhat.com> - 1.5-4
- remove the quotes around LD in AC_PROG_LD_GNU (#97608)
  [reported by twaugh]
- use -nostdlib also when linking with g++ and non-GNU ld in
  _LT_AC_LANG_CXX_CONFIG [reported by fnasser, patch by aoliva]
- use %%configure with CC and CXX set

* Thu Jun 12 2003 Jens Petersen <petersen@redhat.com> - 1.5-3
- don't use %%configure since target options caused libtool to assume
  i386-redhat-linux-gcc instead of gcc for CC (reported by Joe Orton)
- add libtool-1.5-relink-libdir-order-91110.patch to fix order of lib dirs
  searched when relinking (#91110) [patch from Joe Orton]

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May  1 2003 Jens Petersen <petersen@redhat.com> - 1.5-1
- update to 1.5
- no longer override config.{guess,sub} for rpmbuild %%configure,
  redhat-rpm-config owns those now
- update and rename libtool-1.4.2-s390_x86_64.patch to
  libtool-1.5-libtool.m4-x86_64.patch since s390 now included
- buildrequire autoconf and automake, no longer automake14
- skip make check on s390 temporarily
- no longer skip demo-nopic.test on x86_64, s390 and s390x
- from Owen Taylor
  - add libtool-1.4.2-expsym-linux.patch (#55607) [from James Henstridge]
  - add quoting in mktemp patch
  - add libtool-1.5-readonlysym.patch
  - add libtool-1.5-testfailure.patch workaround
  - no longer need libtool-1.4.2-relink-58664.patch

* Sat Feb 08 2003 Florian La Roche <Florian.LaRoche@redhat.de> - 1.4.3-5
- add config.guess and config.sub, otherwise old versions of
  these files can creep into %_datadir/libtool/

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Jens Petersen <petersen@redhat.com> 1.4.3-3
- fix mktemp to work when running mktemp fails (#76602)
  [reported by (Oron Peled)]
- remove info dir file, don't exclude it
- fix typo in -libs description (#79619)
- use buildroot instead of RPM_BUILD_ROOT

* Tue Jan 07 2003 Karsten Hopp <karsten@redhat.de> 1.4.3-2.2
- use lib64 on s390x, too.

* Thu Dec  5 2002 Jens Petersen <petersen@redhat.com>
- add comment to explain why we use an old Automake for building
- buildrequire automake14

* Sat Nov 23 2002 Jens Petersen <petersen@redhat.com>
- add --without check build option to allow disabling of "make check"
- exclude info dir file rather than removing

* Sat Nov 23 2002 Jens Petersen <petersen@redhat.com> 1.4.3-2
- define SED in ltmain.sh for historic ltconfig files
- define macro AUTOTOOLS to hold automake-1.4 and aclocal-1.4, and use it
- leave old missing file for now
- general spec file cleanup
  - don't copy install files to demo nor mess with installed ltdl files
  - don't need to run make in doc
  - force removal of info dir file
  - don't need to create install prefix dir
  - don't bother gzipping info files ourselves

* Mon Nov 18 2002 Jens Petersen <petersen@redhat.com> 1.4.3-1
- update to 1.4.3
- remove obsolete patches (test-quote, dup-deps, libtoolize-configure.ac)
- apply the multilib patch to just the original config files
- update x86_64/s390 patch and just apply to original config files
- use automake-1.4 in "make check" for demo-make.test to pass!
- remove info dir file that is not installed
- make autoreconf update missing

* Mon Oct 07 2002 Phil Knirsch <pknirsch@redhat.com>  1.4.2-12.2
- Added s390x and x64_64 support.

* Fri Oct  4 2002 Nalin Dahyabhai <nalin@redhat.com> 1.4.2-12.1
- rebuild

* Fri Sep 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- patch to find the proper libdir on multilib boxes

* Mon Aug 19 2002 Jens Petersen <petersen@redhat.com> 1.4.2-12
- don't include demo in doc, specially now that we "make check" (#71609)

* Tue Aug 13 2002 Jens Petersen <petersen@redhat.com> 1.4.2-11
- don't hardcode "configure.in" in libtoolize (#70864)
  [reported by bastiaan@webcriminals.com]
- make check, but not on ia64

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.4.2-10
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 1.4.2-9
- automated rebuild

* Fri Apr 26 2002 Jens Petersen <petersen@redhat.com> 1.4.2-8
- add old patch from aoliva to fix relinking when installing into a buildroot
- backport dup-deps fix from cvs stable branch

* Wed Mar 27 2002 Jens Petersen <petersen@redhat.com> 1.4.2-7
- run ldconfig in postin and postun

* Thu Feb 28 2002 Jens Petersen <petersen@redhat.com> 1.4.2-6
- rebuild in new environment

* Tue Feb 12 2002 Jens Petersen <petersen@redhat.com> 1.4.2-5
- revert filemagic and archive-shared patches following cvs (#54887)
- don't change "&& test" to "-a" in ltmain.in

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.4.2-4
- automated rebuild

* Mon Dec  3 2001 Jens Petersen <petersen@redhat.com> 1.4.2-3
- test quoting patch should be on ltmain.in not ltmain.sh (#53276)
- use file_magic for Linux ELF (#54887)
- allow link against an archive when building a shared library (#54887)
- include ltdl.m4 in manifest (#56671)

* Wed Oct 24 2001 Jens Petersen <petersen@redhat.com> 1.4.2-2
- added URL to spec

* Tue Sep 18 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.4.2-1
- 1.4.2 - sync up with autoconf...

* Thu Jul  5 2001 Bernhard Rosenkraenzer <bero@redhat.de> 1.4-8
- extend s390 patch to 2 more files
- s/Copyright/License/

* Wed Jul 04 2001 Karsten Hopp <karsten@redhat.de>
- add s390 patch for deplibs_check_method=pass_all

* Tue Jun 12 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add patches from Tim Waugh #42724

* Mon Jun 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add patches from cvs mainline

* Thu Jun 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix a "test" bug in ltmain.sh

* Sun Jun 03 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- disable the post commands to modify %_docdir/

* Sat May 12 2001 Owen Taylor <otaylor@redhat.com>
- Require automake 1.4p1

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to libtool 1.4
- adjust or remove patches

* Thu Jul 13 2000 Elliot Lee <sopwith@redhat.com>
- Fix recognition of ^0[0-9]+$ as a non-negative integer.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch to use mktemp to create the tempdir
- use %%configure after defining __libtoolize to /bin/true

* Mon Jul  3 2000 Matt Wilson <msw@redhat.com>
- subpackage libltdl into libtool-libs

* Sun Jun 18 2000 Bill Nottingham <notting@redhat.com>
- running libtoolize on the libtool source tree ain't right :)

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.3.5.

* Fri Mar  3 2000 Jeff Johnson <jbj@redhat.com>
- add prereqs for m4 and perl inorder to run autoconf/automake.

* Mon Feb 28 2000 Jeff Johnson <jbj@redhat.com>
- functional /usr/doc/libtool-*/demo by end-user %%post procedure (#9719).

* Wed Dec 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.4.

* Mon Dec  6 1999 Jeff Johnson <jbj@redhat.com>
- change from noarch to per-arch in order to package libltdl.a (#7493).

* Thu Jul 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.3.

* Mon Jun 14 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.2.

* Tue May 11 1999 Jeff Johnson <jbj@redhat.com>
- explicitly disable per-arch libraries (#2210)
- undo hard links and remove zero length file (#2689)

* Sat May  1 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- disable the --cache-file passing to ltconfig; this breaks the older
  ltconfig scripts found around.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.2f

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- completed arm patch
- added patch to make it more arm-friendly
- upgrade to version 1.2d

* Thu May 07 1998 Donnie Barnes <djb@redhat.com>
- fixed busted group

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- Update to 1.0h
- added install-info support

* Tue Nov 25 1997 Elliot Lee <sopwith@redhat.com>
- Update to 1.0f
- BuildRoot it
- Make it a noarch package
