Name: rpmtools
Version: 3.1
Release: alt6.2

Summary: Contains various rpm command-line tools
License: GPL
Group: System/Configuration/Packaging

Source: %name-%version.tar.bz2
Patch0: rpmtools-3.1-alt.patch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: bzlib-devel librpm-devel perl-devel zlib-devel

%description
Various tools needed by urpmi and drakxtools for handling rpm files.

%prep
%setup -q
%patch -p1

%build
perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor
%make_build -f Makefile_core OPTIMIZE="$RPM_OPT_FLAGS"
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%make_build install PREFIX=$RPM_BUILD_ROOT
%make_build -f Makefile_core install PREFIX=$RPM_BUILD_ROOT%prefix

%files
%_bindir/*
%perl_vendor_archlib/rpmtools*
%perl_vendor_archlib/packdrake*
%perl_vendor_autolib/rpmtools*

%changelog
* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 3.1-alt6.2
- rebuilt for perl-5.14

* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.1-alt6.1.qa1
- NMU (by repocop): the following fixes applied:
  * specfile-macros-get_dep-is-deprecated for rpmtools
  * postclean-03-private-rpm-macros for ([not specified])

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.1-alt6.1
- rebuilt with perl 5.12

* Tue Aug 03 2004 Anton Farygin <rider@altlinux.ru> 3.1-alt6
- rebuild

* Thu Jul 10 2003 Rider <rider@altlinux.ru> 3.1-alt5
- change Mandrake directories to ALTLinux

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1-alt4
- rebuild with new perl

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.1-alt3
- Rebuilt in new environment

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1-alt2
- Rebuilt with new rpm

* Wed Nov 08 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.1-alt1
- First build for Sisyphus

* Thu Sep 20 2001 François Pons <fpons@mandrakesoft.com> 3.1-4mdk
- build release.

* Thu Aug  9 2001 Pixel <pixel@mandrakesoft.com> 3.1-3mdk
- rebuild for new rpm

* Wed Jul 25 2001 François Pons <fpons@mandrakesoft.com> 3.1-2mdk
- use rpmvercmp for version_compare.

* Mon Jul 23 2001 François Pons <fpons@mandrakesoft.com> 3.1-1mdk
- allow provides on full package name.
- fixed multiple version, release or arch of the same
  package in the same hdlist.

* Sat Jul 21 2001 Warly <warly@mandrakesoft.com> 3.0-10mdk
- add sourcerpm tag.

* Wed Jul 18 2001 François Pons <fpons@mandrakesoft.com> 3.0-9mdk
- changed rpm requires by including release with test.
- allow bootstrap with current version and not installed one.
- build release for new rpm.

* Thu Jul  5 2001 François Pons <fpons@mandrakesoft.com> 3.0-8mdk
- added compute_id function.

* Mon Jul  2 2001 François Pons <fpons@mandrakesoft.com> 3.0-7mdk
- added arch check support for parsehdlist.

* Thu Jun 28 2001 François Pons <fpons@mandrakesoft.com> 3.0-6mdk
- removed some specific urpm code to urpm package.
- removed obsoleted methods.

* Wed Jun 27 2001 François Pons <fpons@mandrakesoft.com> 3.0-5mdk
- fix problem interpreting serial.

* Wed Jun 27 2001 François Pons <fpons@mandrakesoft.com> 3.0-4mdk
- take care of epoch (serial) for version comparison.

* Tue Jun 26 2001 François Pons <fpons@mandrakesoft.com> 3.0-3mdk
- improved arch management and relocation code.
- fix bad arch parsing when building hdlist.
- fix bad evalution of bad rpm filename.

* Mon Jun 25 2001 François Pons <fpons@mandrakesoft.com> 3.0-2mdk
- fixed version_compare to match rpm behaviour on some cases,
  needed for Garbage Collector cases.
- fixed use of : by @ in provides file.

* Thu Jun 21 2001 François Pons <fpons@mandrakesoft.com> 3.0-1mdk
- changed depslist format to fix support multi-arch.
- changed depslist format to add serial support.
- changed hdlist format to add non standard rpm filename.
- added support to build rpmtools with various rpm.
- added serial, size, summary and description tags.

* Wed Jun 13 2001 François Pons <fpons@mandrakesoft.com> 2.3-25mdk
- really fix with newer rpm (rpmtools.so was missing).
- update distribution tag.

* Wed Jun 13 2001 François Pons <fpons@mandrakesoft.com> 2.3-24mdk
- fix with newer rpm (added -lrpmdb).

* Wed Jun  6 2001 François Pons <fpons@mandrakesoft.com> 2.3-23mdk
- added require on perl-base version used for build.
- fix ordering package to choose libXXX before XXX.

* Tue May 22 2001 François Pons <fpons@mandrakesoft.com> 2.3-22mdk
- added arch support.

* Mon Apr 16 2001 François Pons <fpons@mandrakesoft.com> 2.3-21mdk
- added back anti-lock patch.

* Sat Apr 14 2001 François Pons <fpons@mandrakesoft.com> 2.3-20mdk
- fixed wrong version comparison.

* Sat Apr 14 2001 François Pons <fpons@mandrakesoft.com> 2.3-19mdk
- fixed parsehdlist to print what is needed in synthesis file
  of hdlists.

* Thu Apr 12 2001 François Pons <fpons@mandrakesoft.com> 2.3-18mdk
- added quiet support for packdrake module (for DrakX).

* Tue Apr  3 2001 François Pons <fpons@mandrakesoft.com> 2.3-17mdk
- fixed error code management for parsehdlist.
- fixed read_hdlists return value.

* Mon Mar 26 2001 François Pons <fpons@mandrakesoft.com> 2.3-16mdk
- modified libtermcap to libtermcap2 for VIP.

* Mon Mar 26 2001 François Pons <fpons@mandrakesoft.com> 2.3-15mdk
- fixed depslist sort algorithm to fix Aurora problems.

* Fri Mar 23 2001 François Pons <fpons@mandrakesoft.com> 2.3-14mdk
- reverted rpmtools.xs modification.
- simplified cleaner (include support for sense flag).

* Fri Mar 23 2001 François Pons <fpons@mandrakesoft.com> 2.3-13mdk
- semi-fixed hashes subscript error (workaround).
- added --compact option to parsehdlist.

* Mon Mar 12 2001 François Pons <fpons@mandrakesoft.com> 2.3-12mdk
- added support for LD_LOADER in packdrake module and
  parsehdlist executable.
- removed explicit requires of db2 and db3.
- added BuildRequires for db[123]-devel and libbzip2-devel.

* Fri Mar 09 2001 Francis Galiegue <fg@mandrakesoft.com> 2.3-11mdk
- BuildRequires: perl-devel db2-devel

* Thu Mar  8 2001 François Pons <fpons@mandrakesoft.com> 2.3-10mdk
- fixed duplicate choices in depslist.ordered file.
- fixed missing choices on some deps.

* Wed Mar  7 2001 François Pons <fpons@mandrakesoft.com> 2.3-9mdk
- make sure parsehdlist exit correctly.

* Mon Mar  5 2001 François Pons <fpons@mandrakesoft.com> 2.3-8mdk
- added requires on db2 and db3.

* Thu Mar  1 2001 François Pons <fpons@mandrakesoft.com> 2.3-7mdk
- added compression ratio to build_hdlist.

* Tue Feb 27 2001 François Pons <fpons@mandrakesoft.com> 2.3-6mdk
- fixed gendistrib with multi source of same number as
  media listed in hdlists file.

* Mon Feb 26 2001 François Pons <fpons@mandrakesoft.com> 2.3-5mdk
- improved base flag usage so obsoleted use_base_flag.

* Mon Feb 19 2001 François Pons <fpons@mandrakesoft.com> 2.3-4mdk
- _parse_ returns now fullname of package read.

* Mon Feb 19 2001 François Pons <fpons@mandrakesoft.com> 2.3-3mdk
- fixed version_compare to return number.
- fixed relocate_depslist for package with source to keep.

* Fri Feb 16 2001 François Pons <fpons@mandrakesoft.com> 2.3-2mdk
- fixed invocation of parsehdlist with full package name
  including version and release. make sure to write only one
  description if using the full description.

* Wed Feb 14 2001 François Pons <fpons@mandrakesoft.com> 2.3-1mdk
- changed db_traverse_name to more generic db_traverse_tag
  with support of name, whatprovides, whatrequires, triggeredby,
  group and path.
- added conffiles tag.
- rpmtools.pm to 2.3 to match package version.

* Sat Feb 10 2001 François Pons <fpons@mandrakesoft.com> 2.2-1mdk
- added faster method to access rpm db to rpmtools.xs
  as in DrakX.
- rpmtools.pm to 0.04.

* Tue Jan 30 2001 François Pons <fpons@mandrakesoft.com> 2.1-10mdk
- fixed bug of NOTFOUND_6 in depslist computation.
- fixed depslist relocation bug.

* Tue Jan 23 2001 François Pons <fpons@mandrakesoft.com> 2.1-9mdk
- packdrake.pm to 0.03, added source directory for building an archive.
- changed build_archive to use a specific directory.
- removed bug of gendistrib with relative pathname of distrib.

* Wed Jan 17 2001 François Pons <fpons@mandrakesoft.com> 2.1-8mdk
- removed obsoleted genhdlists, genhdlist_cz2, genbasefiles by gendistrib.
- new tools gendistrib which integrate all the obsoleted tools.
- fixed volative cwd in rpmtools.pm when building hdlist, added noclean support.

* Tue Jan 16 2001 François Pons <fpons@mandrakesoft.com> 2.1-7mdk
- fixed white char in packdrake archive.
- added output mode for parsehdlist.
- added build_hdlist to rpmtools.
- rpmtools.pm to 0.03.

* Fri Jan 05 2001 François Pons <fpons@mandrakesoft.com> 2.1-6mdk
- fixed dependancy in parsehdlist against packdrake.
- fixed packdrake.pm against DrakX usage.

* Fri Dec 08 2000 François Pons <fpons@mandrakesoft.com> 2.1-5mdk
- split packdrake into packdrake.pm, updated version to 0.02.
- rpmtools.pm to 0.02 too.
- added man pages.

* Thu Nov 23 2000 François Pons <fpons@mandrakesoft.com> 2.1-4mdk
- fixed deadlock with version_compare().
- fixed memory leaks in parsehdlist.

* Mon Nov 20 2000 François Pons <fpons@mandrakesoft.com> 2.1-3mdk
- removed ugly log in stdout in parsehdlist.

* Mon Nov 20 2000 François Pons <fpons@mandrakesoft.com> 2.1-2mdk
- fixed abusive -ldb2 and -ldb1 in Makefile.
- fixed deadlock with DrakX by using fflush.
- fixed big bug on execvl (thanks to francis).

* Mon Nov 20 2000 François Pons <fpons@mandrakesoft.com> 2.1-1mdk
- removed rpmtools-compat which is now obsoleted.
- obsoleted genfilelist is removed from rpmtools-devel package.
- removed rpmtools-devel which will be obsoleted by merge on genhdlist*.
- add more complete parsehdlist tools, to be used by DrakX
  in interactive mode.

* Thu Nov 16 2000 François Pons <fpons@mandrakesoft.com> 2.0-6mdk
- updated order of 9 first package to be installed.
- removed memory consuming code in perl.

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 2.0-5mdk
- add requires for -devel

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 2.0-4mdk
- fix compability spelling error

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 2.0-3mdk
- capitalize summaries

* Thu Oct 19 2000 François Pons <fpons@mandrakesoft.com> 2.0-2mdk
- fixed speed problem of rpmtools depslist computation, now 10x faster!

* Thu Oct 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0-1mdk
- updated for rpm 4.

* Fri Sep 15 2000 Pixel <pixel@mandrakesoft.com> 1.2-11mdk
- genhdlist_cz2, packdrake, build_archive: use TMPDIR if exists

* Mon Sep 04 2000 François Pons <fpons@mandrakesoft.com> 1.2-10mdk
- fixed management of basesystem, so that it always keeps all
  its dependancies in order to keep ability to update base packages
  when dobles on basesystem exists.

* Sun Sep 03 2000 François Pons <fpons@mandrakesoft.com> 1.2-9mdk
- fixed write_depslist to avoid resorting, fixes dobles.
- fixed compute_depslist to use only remove dobles in provides.
- fixed genbasefiles to do 3 pass instead of 2, because provides is no more
  used in such a case.
- moved version_compare in rpmtools perl package.
- added relocation of packages to match the best ones (so that urpmi install
  the most up-to-date version it finds).

* Fri Sep 01 2000 François Pons <fpons@mandrakesoft.com> 1.2-8mdk
- fixed read_provides with unresolved dependancies.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.2-7mdk
- fixed rpmtools.pm depslist.ordered reading code on gendepslist2 produced
  file.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.2-6mdk
- fixed hdlist2groups with wrong invocations of parsehdlist.

* Mon Aug 28 2000 François Pons <fpons@mandrakesoft.com> 1.2-5mdk
- fixed packdrake to not use absolute pathname by default for uncompression
  method, else this breaks DrakX as software are not in same place.

* Mon Aug 28 2000 François Pons <fpons@mandrakesoft.com> 1.2-4mdk
- moved genbasefiles to rpmtools as it is used by urpmi.

* Mon Aug 28 2000 François Pons <fpons@mandrakesoft.com> 1.2-3mdk
- fixed ugly arch specific optimization in Makefile.PL.

* Fri Aug 25 2000 François Pons <fpons@mandrakesoft.com> 1.2-2mdk
- added rpmtools perl module.
- added genbasefiles to build compss, depslist.ordered and provides files
  in one (or two) pass.

* Wed Aug 23 2000 François Pons <fpons@mandrakesoft.com> 1.2-1mdk
- 1.2 of rpmtools.
- new tools packdrake and parsehdlist.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1-30mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Pixel <pixel@mandrakesoft.com> 1.1-29mdk
- skip "rpmlib(..." dependencies

* Thu Jul 27 2000 Pixel <pixel@mandrakesoft.com> 1.1-28mdk
- fix handling of choices in basesystem (hdlist -1)

* Wed Jul 12 2000 Pixel <pixel@mandrakesoft.com> 1.1-27mdk
- add version require for last bzip2 and last rpm

* Tue Jun 13 2000 Pixel <pixel@mandrakesoft.com> 1.1-25mdk
- fix a bug in gendepslist2 (thanks to diablero)

* Thu Jun 08 2000 François Pons <fpons@mandrakesoft.com> 1.1-24mdk
- fixed bug in genhdlist_cz2 for multi arch management.

* Thu May 25 2000 François Pons <fpons@mandrakesoft.com> 1.1-23mdk
- adding multi arch management (sparc and sparc64 need).

* Tue May 02 2000 François Pons <fpons@mandrakesoft.com> 1.1-22mdk
- fixed bug for extracting file if some of them are unknown.

* Fri Apr 28 2000 Pixel <pixel@mandrakesoft.com> 1.1-21mdk
- more robust gendepslist2

* Thu Apr 20 2000 François Pons <fpons@mandrakesoft.com> 1.1-20mdk
- dropped use strict in some perl script, for rescue.

* Wed Apr 19 2000 François Pons <fpons@mandrakesoft.com> 1.1-19mdk
- rewrite description.

* Wed Apr 19 2000 François Pons <fpons@mandrakesoft.com> 1.1-18mdk
- update with CVS.

* Fri Apr 14 2000 Pixel <pixel@mandrakesoft.com> 1.1-17mdk
- fix buggy extract_archive

* Fri Apr 14 2000 Pixel <pixel@mandrakesoft.com> 1.1-16mdk
- updated genhdlists

* Fri Mar 31 2000 François PONS <fpons@mandrakesoft.com> 1.1-15mdk
- add genfilelist

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 1.1-14mdk
- fix silly bug

* Mon Mar 27 2000 Pixel <pixel@mandrakesoft.com> 1.1-13mdk
- add hdlist2groups

* Sun Mar 26 2000 Pixel <pixel@mandrakesoft.com> 1.1-12mdk
- gendepslist2: add ability to handle files (was only hdlist.cz2's), and to
output only the package dependencies for some hdlist's/packages (use of "--")

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 1.1-11mdk
- new group

* Fri Mar 24 2000 Pixel <pixel@mandrakesoft.com> 1.1-10mdk
- gendepslist2 bug fix again

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 1.1-9mdk
- gendepslist2 now put filesystem and setup first

* Thu Mar 23 2000 Pixel <pixel@mandrakesoft.com> 1.1-8mdk
- gendepslist2 now handles virtual basesystem requires

* Wed Mar 22 2000 Pixel <pixel@mandrakesoft.com> 1.1-7mdk
- add require rpm >= 3.0.4
- gendepslist2 now puts basesystem first in depslist.ordered
- gendepslist2 orders better

* Mon Mar 20 2000 Pixel <pixel@mandrakesoft.com> 1.1-5mdk
- fix a bug in gendepslist2 (in case of choices)

* Tue Mar  7 2000 Pixel <pixel@mandrakesoft.com> 1.1-1mdk
- new version (gendepslist2 instead of gendepslist, hdlist2prereq)
- host build_archive/extract_archive until francois put them somewhere else :)

* Fri Feb 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-9mdk
- Really fix with rpm-3.0.4 (Fredl).

* Thu Feb 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-8mdk
- rpmtools.spec (BuildRequires): rpm-3.0.4.
- gendepslist.cc: port to rpm-3.0.4.
- Makefile: cvs support, add -lpopt.

* Tue Jan  4 2000 Pixel <pixel@mandrakesoft.com>
- renamed hdlist2files in hdlist2names
- added hdlist2files

* Sun Dec 19 1999 Pixel <pixel@mandrakesoft.com>
- added ability to read from stdin to hdlist2files

* Sat Dec 18 1999 Pixel <pixel@mandrakesoft.com>
- modified gendepslist to accept hdlist's from stdin

* Thu Nov 25 1999 Pixel <pixel@linux-mandrake.com>
- removed rpm-find-leaves (now in urpmi)

* Sun Nov 21 1999 Pixel <pixel@mandrakesoft.com>
- now installed in /usr/bin
- added rpm-find-leaves
- replaced -lrpm by /usr/lib/librpm.so.0 to make it dynamic
(why is this needed?)

* Mon Nov 15 1999 Pixel <pixel@mandrakesoft.com>

- first version

# end of file
