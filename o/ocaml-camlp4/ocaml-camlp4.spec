Name: ocaml-camlp4
Version: 4.04.2
Release: alt1%ubt

Summary: Preprocessor for OCaml
License: QPL & LGPL
Group: Development/ML
Url: https://github.com/ocaml/camlp4
Source0: %name-%version.tar
BuildRequires: rpm-build-ocaml >= 1.2
BuildRequires(pre): rpm-build-ubt
BuildRequires: ocaml >= 4.04 ocaml-ocamlbuild
Provides: ocaml4-campl4
Obsoletes: ocaml4-campl4
Conflicts: camlp4

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

%package devel
Summary: Pre-Processor-Pretty-Printer for OCaml
Requires: %name = %version-%release
Group: Development/ML

%description devel
Camlp4 is a Pre-Processor-Pretty-Printer for OCaml, parsing a source
file and printing some result on standard output.

This package contains the development files.

%prep
%setup

%build
%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64
./configure --bindir=%_bindir --libdir=%_libdir/ocaml

%make all

%install
make install BINDIR=%buildroot%_bindir LIBDIR=%buildroot%_libdir/ocaml MANDIR=%buildroot%_mandir

%files
%dir %_libdir/ocaml/camlp4
%_libdir/ocaml/camlp4/*.cmi
%_libdir/ocaml/camlp4/*.cma
%_libdir/ocaml/camlp4/*.cmo
%dir %_libdir/ocaml/camlp4/Camlp4Filters
%_libdir/ocaml/camlp4/Camlp4Filters/*.cmi
%_libdir/ocaml/camlp4/Camlp4Filters/*.cmo
%dir %_libdir/ocaml/camlp4/Camlp4Parsers
%_libdir/ocaml/camlp4/Camlp4Parsers/*.cmo
%_libdir/ocaml/camlp4/Camlp4Parsers/*.cmi
%dir %_libdir/ocaml/camlp4/Camlp4Printers
%_libdir/ocaml/camlp4/Camlp4Printers/*.cmi
%_libdir/ocaml/camlp4/Camlp4Printers/*.cmo
%dir %_libdir/ocaml/camlp4/Camlp4Top
%_libdir/ocaml/camlp4/Camlp4Top/*.cmi
%_libdir/ocaml/camlp4/Camlp4Top/*.cmo

%files devel
%doc LICENSE
%_bindir/camlp4*
%_bindir/mkcamlp4
%_libdir/ocaml/camlp4/*.a
%_libdir/ocaml/camlp4/*.cmxa
%_libdir/ocaml/camlp4/*.cmx
%_libdir/ocaml/camlp4/*.o
%_libdir/ocaml/camlp4/Camlp4Filters/*.cmx
%_libdir/ocaml/camlp4/Camlp4Filters/*.o
%_libdir/ocaml/camlp4/Camlp4Parsers/*.cmx
%_libdir/ocaml/camlp4/Camlp4Parsers/*.o
%_libdir/ocaml/camlp4/Camlp4Printers/*.cmx
%_libdir/ocaml/camlp4/Camlp4Printers/*.o
%_libdir/ocaml/camlp4/Camlp4Top/*.cmx
%_libdir/ocaml/camlp4/Camlp4Top/*.o

%changelog
* Thu Jul 06 2017 Anton Farygin <rider@altlinux.ru> 4.04.2-alt1%ubt
- up to 30fc8cd  from 4.04 branch
- rebuild with ocaml-4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.04.1-alt3%ubt
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 4.04.1-alt2%ubt
- split to devel and runtime packages
- specfile cleanup

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 4.04.1-alt1%ubt
- new version

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.1-alt1
- Version update (switch to ocaml 4.03).

* Mon Apr 04 2016 Andrey Bergman <vkni@altlinux.org> 4.02.7-alt1
- Version update.

* Sun Jul 12 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt2
- Added conflict with camlp4.

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt1
- Rebuild with new rpm-build-ocaml4.

* Fri Jun 19 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1_3-alt0.1
- Version update.

* Mon Feb 02 2015 Andrey Bergman <vkni@altlinux.org> 4.02.1+2-alt0.1
- Version update. Added rpm-build-ocaml4 to buildreq.

* Sat Oct 18 2014 Andrey Bergman <vkni@altlinux.org> 4.02.0.1-alt0.1
- Initial release for Sisyphus after removal from Ocaml distribution
(see ocaml 4.02.0 changelog).

