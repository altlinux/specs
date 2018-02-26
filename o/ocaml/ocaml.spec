# TEXTREL on i386
#/usr/lib/ocaml/unix.cmxs
#/usr/lib/ocaml/str.cmxs
#/usr/lib/ocaml/nums.cmxs
#/usr/lib/ocaml/bigarray.cmxs
#/usr/lib/ocaml/graphics.cmxs
#/usr/lib/ocaml/dbm.cmxs
%set_verify_elf_method textrel=relaxed

Name: ocaml
Version: 3.12.1
Release: alt1

Summary: The Objective Caml compiler and programming environment
License: QPL & LGPL
Group: Development/ML

Url: http://caml.inria.fr/
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source0: %name-%version.tar
Source1: ocaml-refman.html.tar
Source2: ocaml-3.12-refman.pdf
Source4: %name.menu
Source5: http://caml.inria.fr/oreilly-book/ocaml-ora-book.pdf
Source6: ocaml-reqprov.ml

Patch1: ocaml-3.04+7-threadhack.patch
Patch2: ocaml-3.12.1-alt-stdlib-pdf.patch
Patch3: ocaml-3.09.1-tinfo.patch
Patch4: ocaml-3.12.1-alt-tcltk8.5.patch
Patch5: ocaml-3.04-pld-objinfo.patch
Patch6: ocaml-3.12.1-alt-mk-reqprov.patch
Patch7: ocaml-3.10.0-pld-db4.patch
Patch8: ocaml-3.12.1-alt-mk-odoc_info-toplevellib_cmxa.patch
Patch9: ocaml-3.10.2-alt-tags-camlp4lib-no-use_dynlink.patch
Patch10: ocaml-3.12.0-rpath.patch
Patch11: ocaml-3.12.1-deb-ocamlopt-arm-add-.type-directive-for-code-symbols.patch

Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

# Automatically added by buildreq on Tue Apr 01 2008
BuildRequires: libdb4-devel libtinfo-devel tetex-latex tk-devel

# Better keep those deps explicit, just in case
BuildRequires: libX11-devel

Requires: %name-runtime = %version-%release

%package runtime
Summary: Runtime part of the OCaml system
Group: Development/ML
Provides: %name-runtime = %(v=%version; IFS=.; set $v; echo "$1.$2")
# For some reason, this is Requires, not Provides.
Requires: %_rpmlibdir/ocaml-reqprov

%package -n camlp4
Summary: Preprocessor for OCaml
Group: Development/ML
Requires: %name = %version-%release

%package dbm
Summary: Interface to DBM databases
Group: Development/ML
Requires: %name = %version-%release

%package -n labltk
Summary: Tk toolkit bindings for OCaml
Group: Development/ML
Requires: %name = %version-%release
Requires: labltk-runtime = %version-%release
Provides: ocamltk = %version, camltk = %version
Obsoletes: ocamltk < %version , camltk < %version

%package -n labltk-runtime
Summary: Tk toolkit bindings for OCaml
Group: Development/ML
Requires: %name-runtime = %version-%release

%package -n ocamlbrowser
Summary: OCaml interface browser
Group: Development/ML
Requires: %name = %version-%release

%package graphics
Summary: Graphics primitives
Group: Development/ML
Requires: %name = %version-%release
Requires: %name-graphics-runtime = %version-%release

%package graphics-runtime
Summary: Graphics primitives
Group: Development/ML
Requires: %name-runtime = %version-%release

%package -n ocamldoc
Summary: The Objective Caml documentation generator
Group: Development/ML
Requires: %name = %version-%release

%package -n ocamlbuild
Summary: The Objective Caml project compilation tool
Group: Development/ML
Requires: %name = %version-%release

%package doc
Summary: Documentation for OCaml
Group: Development/ML
BuildArch: noarch
Conflicts: %name < %version, %name > %version

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler and an
optimizing native-code compiler), an interactive toplevel system, Lex&Yacc
tools, a replay debugger, and a comprehensive library.

%description runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package contains the runtime environment needed to run Objective
Caml bytecode.

%description -n camlp4
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

%description dbm
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

The dbm library provides access to DBM-like databases (Berkeley DB).

%description -n labltk
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to develop OCaml programs using LablTk.

%description -n labltk-runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to run bytecode OCaml programs using LablTk.

%description -n ocamlbrowser
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides OCamlBrowser, a source and compiled interface
browser, written using LablTk.

%description graphics
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides machine-independent graphics primitives
and additional graphics primitives for the X Windows system.

%description graphics-runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides machine-independent graphics primitives
and additional graphics primitives for the X Windows system.

%description -n ocamldoc
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides OCamldoc, a tool that generates documentation
from special comments embedded in source files.

%description -n ocamlbuild
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides ocamlbuild, a tool automating the compilation
of OCaml projects.

%description doc
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package contains Ocaml documentation and "Developing applications
with Objective Caml" O'Reilly book translation.

%prep
%setup -q -T -b 0 
%setup -q -T -D -a 1

#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch9 -p1
%patch10 -p1
%patch11 -p1

# grrr ...
#%__cat <<EOF |ed - emacs/Makefile
#%%s|\(--batch \)|\1--no-site-file |
#wq
#EOF

cp %SOURCE5 ./

cp %SOURCE2   ./ocaml-refman.pdf

## replace a bootstrap compiler 
#(cd boot; bzcat %%SOURCE6 | tar -xvvf -)

%build

sed -i 's@/usr/X11R6/lib\>@%_x11libdir@g' configure

%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64
./configure -with-pthread -bindir %_bindir -libdir %_libdir/ocaml -mandir %_mandir
make BYTECCCOMPOPTS="%optflags" NATIVECCCOMPOPTS="%optflags" world
make BYTECCCOMPOPTS="%optflags" NATIVECCCOMPOPTS="%optflags" ocamlopt
make BYTECCCOMPOPTS="%optflags" NATIVECCCOMPOPTS="%optflags" opt opt.opt
make -C ocamldoc stdlib.pdf

install -pD -m644 %SOURCE6 tools/reqprov.ml
make -C tools reqprov

%install
make install BINDIR=%buildroot%_bindir LIBDIR=%buildroot%_libdir/ocaml MANDIR=%buildroot%_mandir
mkdir -p %buildroot%_libdir/ocaml/site-lib/

# (cd emacs; make install install-ocamltags BINDIR=%buildroot%_bindir EMACSDIR=%buildroot%_datadir/emacs/site-lisp)

perl -pi -e "s|%buildroot||" %buildroot%_libdir/ocaml/ld.conf

install -p -m644 parsing/asttypes.{mli,cmi} %buildroot%_libdir/ocaml/
install -p -m644 parsing/parsetree.{mli,cmi} %buildroot%_libdir/ocaml/
install -p -m644 bytecomp/cmo_format.{mli,cmi} %buildroot%_libdir/ocaml/
install -p -m644 typing/annot.{mli,cmi} %buildroot%_libdir/ocaml/
install -p -m644 asmcomp/clambda.{mli,cmi,cmo,cmx,o} %buildroot%_libdir/ocaml/
install -p -m644 asmcomp/cmx_format.{mli,cmi} %buildroot%_libdir/ocaml/
install -p -m644 asmcomp/debuginfo.{mli,cmi,cmx} %buildroot%_libdir/ocaml/

install -p -m644 toplevel/toplevellib.{cmxa,a} %buildroot%_libdir/ocaml/
install -p -m644 tools/depend.{mli,cmi,cmo,cmx,o} %buildroot%_libdir/ocaml/

ln -snf ocamlc.opt %buildroot%_bindir/ocamlc
ln -snf ocamlopt.opt %buildroot%_bindir/ocamlopt
ln -snf ocamldep.opt %buildroot%_bindir/ocamldep
ln -snf ocamllex.opt %buildroot%_bindir/ocamllex
rm %buildroot%_bindir/ocamlbuild.{byte,native}
# Option -g not available in native code version.
#ln -snf ocamldoc.opt %buildroot%_bindir/ocamldoc

install -pD -m755 tools/objinfo %buildroot%_bindir/ocamlobjinfo
install -pD -m755 tools/reqprov %buildroot%_rpmlibdir/ocaml-reqprov

install -pD -m644 camlp4/man/camlp4.1.tpl %buildroot%_man1dir/camlp4.1

find %buildroot%_libdir/ocaml -type f -name '*.cmx' |
while read f; do [ -f "${f%%.cmx}.o" ] || rm "$f"; done

#install -d %buildroot%_sysconfdir/emacs/site-start.d
#cat <<EOF >%buildroot%_sysconfdir/emacs/site-start.d/%name.el
#(require 'caml-font)
#(autoload 'caml-mode "caml" "Caml editing mode" t)
#(add-to-list 'auto-mode-alist '("\\\\.mli?$" . caml-mode))
#EOF

install -pD -m644 %SOURCE4 %buildroot%_menudir/%name

%files
%doc Changes LICENSE README 
%_bindir/ocaml*
%exclude %_bindir/ocamlrun
%exclude %_bindir/ocamlbrowser
%exclude %_bindir/ocamlbuild
%exclude %_bindir/ocamldoc*
%_man1dir/ocaml*
%exclude %_man1dir/ocamlbuild*
%exclude %_man1dir/ocamldoc*
%_man3dir/*.3o*
%_menudir/ocaml
%_libdir/ocaml/camlheader
%_libdir/ocaml/camlheader_ur
%_libdir/ocaml/expunge
%_libdir/ocaml/extract_crc
%_libdir/ocaml/*.*
%_libdir/ocaml/objinfo_helper
%exclude %_libdir/ocaml/ld.conf
%exclude %_libdir/ocaml/*graphics*
%exclude %_libdir/ocaml/*dbm*
%_libdir/ocaml/caml/
%exclude %_libdir/ocaml/ocamlbuild/
%exclude %_libdir/ocaml/ocamldoc/
%_libdir/ocaml/threads/
%_libdir/ocaml/vmthreads/
# %_datadir/emacs/site-lisp/*
# %config(noreplace) %_sysconfdir/emacs/site-start.d/*

%files runtime
%_bindir/ocamlrun
%dir %_libdir/ocaml
%config %_libdir/ocaml/ld.conf
%dir %_libdir/ocaml/stublibs
%_libdir/ocaml/stublibs/dllbigarray.so
%_libdir/ocaml/stublibs/dllmldbm.so
%_libdir/ocaml/stublibs/dllnums.so
%_libdir/ocaml/stublibs/dllcamlstr.so
%_libdir/ocaml/stublibs/dllthreads.so
%_libdir/ocaml/stublibs/dllunix.so
%_libdir/ocaml/stublibs/dllvmthreads.so
%dir %_libdir/ocaml/site-lib
%_rpmlibdir/ocaml-reqprov

%files -n camlp4
%_bindir/camlp4*
%_bindir/mkcamlp4
%_man1dir/camlp4.1*
%_libdir/ocaml/camlp4/

%files dbm
%_libdir/ocaml/*dbm*

%files -n labltk
%doc otherlibs/labltk/README otherlibs/labltk/examples_labltk otherlibs/labltk/examples_camltk
%_bindir/labltk
%_libdir/ocaml/labltk/

%files -n labltk-runtime
%_libdir/ocaml/stublibs/dlllabltk.so

%files -n ocamlbrowser
%_bindir/ocamlbrowser

%files graphics
%_libdir/ocaml/*graphics*

%files graphics-runtime
%_libdir/ocaml/stublibs/dllgraphics.so

%files -n ocamldoc
%_bindir/ocamldoc*
%_man1dir/ocamldoc*
%_libdir/ocaml/ocamldoc/

%files -n ocamlbuild
%_bindir/ocamlbuild
%_man1dir/ocamlbuild*
%_libdir/ocaml/ocamlbuild/

%files doc
%doc htmlman/* ocamldoc/stdlib.pdf ocaml-refman.pdf ocaml-ora-book.pdf

%changelog
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

