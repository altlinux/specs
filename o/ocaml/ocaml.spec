# enabled LTO leads to a  slowdown
%define optflags_lto %nil
# with enabled WAll two tests fall
%define optflags_warnings %nil

%ifarch %ocaml_native_arch
%def_with nativeocaml
%def_with check
%else
%def_without nativeocaml
%def_without check
%endif

# https://github.com/ocaml/ocaml/issues/9050
%filter_from_requires /Backend_intf/d
%filter_from_requires /Inlining_decision_intf/d
%filter_from_requires /Simplify_boxed_integer_ops_intf/d

Name: ocaml
Version: 4.14.1
Release: alt1

Summary: The Objective Caml compiler and programming environment
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML

Url: http://caml.inria.fr/
Source0: %name-%version.tar
Source1: ocaml-reqprov.ml

Patch1: ocaml-3.12.1-alt-stdlib-pdf.patch
Patch2: ocaml-4.14-alt-mk-reqprov.patch
Patch3: ocaml-4.14.1-more-source-artifacts.patch
Patch4: ocaml-4.11.1-RH-configure-Allow-user-defined-C-compiler-flags.patch
Patch5: ocaml-4.14.1-alt-ocamldoc-install-all-cmti.patch

Requires: rpm-build-ocaml >= 1.6.1
BuildRequires(pre): rpm-build-ocaml >= 1.6.1

Conflicts: ocaml4
Obsoletes: ocaml4
Provides: ocaml4

# Automatically added by buildreq on Mon Sep 23 2013
BuildRequires: texlive-latex-base texlive-latex-recommended

BuildRequires: binutils-devel

Requires: %name-runtime = %EVR

%package runtime
Summary: Runtime part of the OCaml system
Group: Development/ML
Obsoletes: ocaml4-runtime

%package ocamldoc
Summary: The Objective Caml documentation generator
Group: Development/ML
Requires: %name = %EVR
Provides: ocaml4-ocamldoc
Obsoletes: ocaml4-ocamldoc

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler and
an optimizing native-code compiler), an interactive toplevel system,
Lex&Yacc tools, a replay debugger, and a comprehensive library.

%description runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package contains the runtime environment needed to run Objective
Caml bytecode.

%description ocamldoc
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides OCamldoc, a tool that generates documentation
from special comments embedded in source files.

%prep
%setup -T -b 0

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
install -pD -m644 %SOURCE1 tools/reqprov.ml
%add_optflags -D_FILE_OFFSET_BITS=64
./configure \
	CFLAGS="%optflags" \
	-bindir %_bindir \
	-libdir %_libdir/ocaml \
	-mandir %_mandir \
%if_without nativeocaml
	--disable-native-compiler \
%endif
%if_with check
        --enable-ocamltest \
%endif
	%nil

%make_build world

%if_with nativeocaml
%make_build opt
%make_build opt.opt
%endif

%install
make install DESTDIR=%buildroot
perl -pi -e "s|%buildroot||" %buildroot%_libdir/ocaml/ld.conf

install -pD -m755 tools/ocamlreqprov %buildroot%_rpmlibdir/ocaml-reqprov

%check
pushd testsuite
make -j1 all
popd

%files
%doc Changes LICENSE README.adoc
%_bindir/ocaml*
%exclude %_bindir/ocamlrun
%exclude %_bindir/ocamldoc*
%_man1dir/ocaml*
%exclude %_man1dir/ocamldoc*
%_man3dir/*.3o*
%_libdir/ocaml/camlheader
%_libdir/ocaml/camlheader_ur
%_libdir/ocaml/expunge
%_libdir/ocaml/*.*
%exclude %_libdir/ocaml/ld.conf
%_libdir/ocaml/caml/
%exclude %_libdir/ocaml/ocamldoc/
%_libdir/ocaml/threads/
%dir %_libdir/ocaml/compiler-libs
%_libdir/ocaml/compiler-libs/*.mli
%_libdir/ocaml/compiler-libs/*.cmt
%_libdir/ocaml/compiler-libs/*.cmti
%_libdir/ocaml/compiler-libs/*.cmi
%_libdir/ocaml/compiler-libs/*.cmo
%_libdir/ocaml/compiler-libs/*.cma
%if_with nativeocaml
%_libdir/ocaml/compiler-libs/*.a
%_libdir/ocaml/compiler-libs/*.cmxa
%_libdir/ocaml/compiler-libs/*.cmx
%_libdir/ocaml/compiler-libs/*.o
%endif

%files runtime
%_bindir/ocamlrun
%dir %_libdir/ocaml
%config %_libdir/ocaml/ld.conf
%dir %_libdir/ocaml/stublibs
%_libdir/ocaml/stublibs/dllcamlstr.so
%_libdir/ocaml/stublibs/dllthreads.so
%_libdir/ocaml/stublibs/dllunix.so
%_libdir/ocaml/camlheaderd
%_libdir/ocaml/camlheaderi
%dir %_libdir/ocaml/stublibs
%_rpmlibdir/ocaml-reqprov

%files ocamldoc
%_bindir/ocamldoc*
%_man1dir/ocamldoc*
%_libdir/ocaml/ocamldoc/

%changelog
* Fri Nov 03 2023 Anton Farygin <rider@altlinux.ru> 4.14.1-alt1
- 4.14.1
- new implementaion of the ocaml-reqprov
- added support for bytecode-only build of the ocaml

* Mon Oct 25 2021 Anton Farygin <rider@altlinux.ru> 4.13.1-alt1
- 4.13.1

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 4.12.0-alt1
- 4.12.0

* Thu Oct 08 2020 Anton Farygin <rider@altlinux.ru> 4.11.1-alt1
- 4.11.1

* Wed Sep 09 2020 Anton Farygin <rider@altlinux.ru> 4.10.0-alt2
- built with binutils-devel to add cmxs support to ocamlobjinfo

* Sat Feb 22 2020 Anton Farygin <rider@altlinux.ru> 4.10.0-alt1
- 4.10.0 release
- removed ocaml-graphics subpackage (available from separate package
  in opam)
- fixed License tag: ocaml from version 4.03 is distributed under
  LGPLv2.1 with linking exceptions

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 4.08.1-alt1
- 4.08.1 release

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 4.08.1-alt0.rc3
- 4.08.1-rc3

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 4.08.0-alt1
- 4.08.0

* Wed Feb 13 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.07.1-alt3
- Removed erroneous %%ifarch (ocaml builds dllraw_spacetime_lib.so
  on all architectures with 64 bit pointers).

* Fri Nov 09 2018 Anton Farygin <rider@altlinux.ru> 4.07.1-alt2
- disabled mark as config file for ocaml/ld.conf

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 4.07.1-alt1
- 4.07.1

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 4.07.0-alt1
- 4.07.0

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 4.06.1-alt1
- 4.06.1

* Mon Dec 18 2017 Anton Farygin <rider@altlinux.ru> 4.06.0-alt1
- new version

* Tue Jul 04 2017 Anton Farygin <rider@altlinux.ru> 4.04.2-alt1
- new version with security fixes:
   + CVE-2017-9772 Local privilege escalation issue with ocaml binaries

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.04.1-alt1
- new version

* Sat Apr 15 2017 Anton Farygin <rider@altlinux.ru> 4.04.0-alt1
- build from upstream git
- added %%ubt tag
- renamed back to ocaml

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.12.1-alt4
- NMU: adopted and rebuilt against Tcl/Tk 8.6

* Sat Dec 17 2016 Andrey Bergman <vkni@altlinux.org> 4.04.0-alt1
- Update to version 4.04.0

* Sat Jun 25 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0-alt2
- Added stdlib cmx files to disable warning 58.

* Sat Jun 18 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0-alt1
- Update to version 4.03.0. Splitted out ocamlbuild.

* Fri Aug 07 2015 Andrey Bergman <vkni@altlinux.org> 4.02.3-alt1
- Update to version 4.02.3

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 4.02.2-alt3
- Rebuild with new rpm-build-ocaml4.

* Tue Jun 23 2015 Andrey Bergman <vkni@altlinux.org> 4.02.2-alt2
- Corrected ocaml-reprov program to print zeroes if md5 sum is missing.

* Fri Jun 19 2015 Andrey Bergman <vkni@altlinux.org> 4.02.2-alt1
- Update to version 4.02.2

* Tue Mar 31 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1-alt2
- Added conflicts (with ocaml 3.x).

* Sat Jan 31 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1-alt1
- Added rpm-build-ocaml4 to build pre requires.

* Sat Oct 18 2014 Andrey Bergman <vkni@altlinux.org> 4.02.1-alt0.1
- Update to version 4.02.1

* Thu Oct 16 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0-alt0.3
- Removed rpm-build-ocaml from build pre requires.

* Wed Oct 08 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0-alt0.2
- Removed wrong Requires.

* Tue Oct 07 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0-alt0.1
- Update to version 4.02.
- Removed camlp4, labltk from base package (upstream).
- Also removed external documentation (refman and ocaml-ora-book).

* Thu Sep 26 2013 Andrey Bergman <vkni@altlinux.org> 4.01.0-alt0.3
- Corrected Provides and libs.

* Mon Sep 23 2013 Andrey Bergman <vkni@altlinux.org> 4.01.0-alt0.2
- Corrected BuildReq.

* Sun Aug 18 2013 Andrey Bergman <vkni@altlinux.org> 4.01.0-alt0.1
- Update to version 4.01.0.

* Fri Jun 14 2013 Andrey Bergman <vkni@altlinux.org> 3.12.1-alt2
- Removed deprecated patches.
- Removed .menu, added .desktop.
- Corrected BuildReq for using TeXLive instead of teTeX.

* Fri Dec 16 2011 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 3.10.2-alt3.1
- Automated rebuild with libdb-4.7.so.

* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 3.10.2-alt3
- new subpackages ocamldoc and ocamlbuild (now with units)
- hacked odoc_info.cmxa to link with toplevellib.cmxa
- hacked camlp4lib.cma not link in a copy of dynlink.cma

* Thu Apr 03 2008 Alexey Tourbin <at@altlinux.ru> 3.10.2-alt2
- implemented ocaml-reqprov.ml, based on tools/objinfo.ml and
  tools/dumpobj.ml, for use with rpm-build-ocaml
- built with new rpm-build-ocaml, added dependency on rpm-build-ocaml
- compiled dbm unit with libdb4.4 (previously compiled with libgdbm)
- new subpackage ocaml-dbm, which now requires libdb4.4-devel
- new subpackages labltk-runtime, graphics-runtime, and ocamlbrowser
- ocamldoc/ and ocamlbuild/ units not packaged
- dropped man3o.patch (man3o/*.3o* -> man3/*.3o*)
- removed *.cmx files which do not have corresponding *.o files

* Fri Mar 14 2008 Grigory Batalov <bga@altlinux.ru> 3.10.2-alt1
- New upstream release.

* Thu Nov 15 2007 Alex V. Myltsev <avm@altlinux.ru> 3.10.0-alt0.1
- New version: backtraces in native code, new CamlP4, ocamlbuild.

* Sat Dec 09 2006 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 3.09.3-alt0.1
- NMU.
- bugfix release.

* Sun Nov 12 2006 Grigory Batalov <bga@altlinux.ru> 3.09.1-alt3
- Built with Large File System support.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 3.09.1-alt2
- Added patch to use system-wide libtinfo (fixes findlib build).

* Wed Mar 01 2006 Pavlov Konstantin <thresh@altlinux.ru> 3.09.1-alt1
- Adopted package.
- Fixed #8944.
- New version.

* Thu Dec 22 2005 Pavlov Konstantin <thresh@altlinux.ru> 3.08.1-alt1.1
- NMU.
- %%'ed unused macroses.
- fixed %%_libdir/menu to %%_menudir.
- changed usr/lib in %%files section to usr/%%_lib.

* Tue Oct 26 2004 Vitaly Lugovsky <vsl@altlinux.ru> 3.08.1-alt1
- bugfix release

* Sat Jul 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 3.08.0-alt0.2
- 3.08.0 officially released

* Wed Jul 07 2004 Vitaly Lugovsky <vsl@altlinux.ru> 3.08-alt0.1
- current cvs

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 3.07-alt6.1
- Non-Maintainer upload
- Rebuild with glibc 2.3.x
- Add packager to spec (Vitaly Lugovsky <vsl@altlinux.ru>)
- Gone build dependency on db2 (replace with libgdbm)

* Wed Mar 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt6
- CVS 3.07+14 with a current shared patch

* Tue Jan 20 2004 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt5
- CVS 3.07+13 with a modified shared patch

* Wed Dec 17 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt4.2
Bugfix

* Tue Dec 16 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt4.1b
- Current CVS version merged.

* Mon Oct 13 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt2
A bugfix release

* Wed Oct 08 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.07-alt1
- Final 3.07 with a shared libs patch

* Wed Aug 27 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.07bs-alt0.1
- New version (3.07 beta CVS).

* Thu Jul 03 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.06s-alt5
- rebuild with a new binutils (now undefined symbols should be weak)

* Wed Mar 26 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.06s-alt4.2
- a bit of .spec cleanup
- merge with 3.1 (I'm *sorry*)
- russian description added
- a small bugfix patch (related to the bytecode profiling)

* Sat Mar 15 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.06s-alt4
- bugfix (ocaml-shared4fix.patch)

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 3.06s-alt3.1
- unmet fix: added provides to stdlib.so in runtime subpackage

* Tue Feb 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.06s-alt3
- stdlib.so now in the ocaml-runtime package

* Fri Jan 31 2003 Vitaly Lugovsky <vsl@altlinux.ru> 3.06s-alt1
- Malc's patch is here again. Ready for testing.
- X11 dependent module is in the separate package now
- Some .spec cleanups

* Tue Oct 22 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.06-alt4
- O'Relly book included in the docs package
- Some minor cleanups

* Fri Oct  4 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.06-alt3
- rebuilt with tcl 8.4

* Thu Sep 26 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.06-alt2
- tcllibdir in RPATH problem fixed
- now camltk library interface is emulated by labltk

* Tue Aug 20 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.06-alt1
- Bugfix release 3.06
- We have bytecode binaries again

* Mon Aug 12 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.05-alt3
- Ocaml package splitted: now we have runtime and
- development parts separated

* Wed Jul 31 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.05-alt2
- critical bugfix (in the bytecode runtime)

* Mon Jul 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.05-alt1
- New Objective Caml released: 3.05.
- Camlp4 manpages hack is obsolete now.

* Mon Jul 15 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.04_15-alt4
- rebuilt with new tcl layout

* Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04_15-alt2
- CVS version 3.04+15
- no more emacs mode installed.

* Tue May 14 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04_10-alt5
- CVS version of OCaml (3.04+10)
- naive patch about stdlib manuals (odoc bug?)
- pdf and postscript stdlib manual
- pdf ocaml reference manual moved to the ocaml-doc subpackage
- ldconf patch (to simplify installation of packages with dynamic libraries)

* Tue Apr 16 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04+9-alt8
- CVS version of OCaml (3.04+9),
- bytecode versions of compilers now included (due to the problem
   with threads).
- Threadhack patch from vsu <vsu@mivlgu.murom.ru>

* Wed Apr 3 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04+8-alt1
- CVS version of OCaml (3.04+8), with ocamldoc officialy included

* Sat Mar 2 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04+7-alt1
- CVS version of OCaml (3.04+7), shared patch and patch_record
  completely disabled.

* Mon Feb 4 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04-alt4
- Shared patch commented out (can't fix a bug with string_of_int)...
- make opt is now disabled for camlp4
- ocamltk renamed to labltk

* Wed Jan 23 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.04-alt3
- patch_record added

* Thu Jan 10 2002 Vitaly Lugovsky <warlock@skeptik.net> 3.04-vsl2
- Shared patch
- GCC 2.96 bug workaround patch
- -with-pthread
- PDF documentation included
- no-opt for debug and profile patch removed (what is it for?!?)
- installation/uninstallation of INFO removed

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 3.04-alt1
- 3.04. MDK merges

* Wed Aug 08 2001 Stanislav Ievlev <inger@altlinux.ru> 3.02-alt1
- 3.02

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 3.01-alt1
new version

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 3.00-23mdk
- fix silly #define clashing with new glibc

* Tue Oct 10 2000 Pixel <pixel@mandrakesoft.com> 3.00-22mdk
- add ocamltags (needs emacs)

* Mon Sep  4 2000 Pixel <pixel@mandrakesoft.com> 3.00-21mdk
- rebuild with spec-helper fixed

* Tue Aug 29 2000 Pixel <pixel@mandrakesoft.com> 3.00-20mdk
- fix info pages

* Tue Aug 29 2000 Pixel <pixel@mandrakesoft.com> 3.00-19mdk
- remove menu entry

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 3.00-18mdk
- add packager

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 3.00-17mdk
- add obsolete %name-emacs

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 3.00-16mdk
- nicer site-start.d/ocaml.el (use add-to-list)

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 3.00-15mdk
- fix missing %%config, add install info

* Tue Aug 22 2000 Pixel <pixel@mandrakesoft.com> 3.00-14mdk
- use %_sysconfdir/emacs/site-start.d for the caml-mode.el
- merge %name and %name-emacs

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.00-13mdk
- automatically added BuildRequires

* Tue Aug 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 3.00-12mdk
- relink with the new and shiny tcltk

* Wed Jul 26 2000 Pixel <pixel@mandrakesoft.com> 3.00-11mdk
- use %%optflags with omit-frame-buffer removed

* Tue Jul 25 2000 Pixel <pixel@mandrakesoft.com> 3.00-10mdk
- use %%optflags (so that there is -mieee on alpha)

* Sat Jul 22 2000 Pixel <pixel@mandrakesoft.com> 3.00-9mdk
- patch for camldebug.el to workaround the silly ocamldebug command not looking
in cwd

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 3.00-7mdk
- more macro (use clean clean_menus)

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 3.00-6mdk
- macroization
- BM

* Sun Jun 04 2000 David BAUDENS <baudens@mandrakesoft.com> 3.00-5mdk
- Fix %%doc
- Use %%_tmppath for BuildRoot

* Thu Jun  1 2000 Pixel <pixel@mandrakesoft.com> 3.00-4mdk
- change copyright

* Thu Jun  1 2000 Pixel <pixel@mandrakesoft.com> 3.00-3mdk
- takes care of ocamlbrowser and ocamldebug (these must not be stripped)

* Tue May 16 2000 Pixel <pixel@mandrakesoft.com> 3.00-2mdk
- add README to ocaml-emacs

* Mon May  1 2000 Pixel <pixel@mandrakesoft.com> 3.00-1mdk
- new version

* Mon Apr 10 2000 Pixel <pixel@mandrakesoft.com> 2.04-9mdk
- fix groups

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 2.04-8mdk
- really add menu

* Mon Mar 27 2000 Pixel <pixel@mandrakesoft.com> 2.04-7mdk
- add menu

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 2.04-6mdk
- new group + cleanup

* Mon Dec  6 1999 Pixel <pixel@linux-mandrake.com>
- 2.04

* Fri Nov 26 1999 Pixel <pixel@linux-mandrake.com>
- 2.03 + cleanup

* Tue Nov 23 1999 Pixel <pixel@linux-mandrake.com>
- build root added

* Tue Jun 01 1999 Pixel <pixel@linux-mandrake.com>
- Hacked to package properly ocamltk

* Tue Dec 29 1998 Alexey Nogin <ayn2@cornell.edu>
- Do not include any /usr/lib/ocaml/*.ml files

* Fri Dec 11 1998 Alexey Nogin <ayn2@cornell.edu>
- Updated to ocaml-2.01

* Sun Nov 29 1998 Alexey Nogin <ayn2@cornell.edu>
- Divided ocaml RPM into ocaml and ocaml-emacs RPMs
  to make it easier to have both ocaml and caml installed
  on the same machine

* Wed Nov 10 1998 Alexey Nogin <ayn2@cornell.edu>
- Changed SRPM according to RHCN Package Requirements
- Added LICENSE, Changelog and README files to the doc directory

