%set_verify_elf_method textrel=relaxed
Name: ocaml-mccs
Version: 1.1.13
Release: alt1
Summary: Multi Criteria CUDF Solver with OCaml bindings
# Original C/C++ code is BSD, OCaml bindings are LGPL.
# Linking exception, see included COPYING file.
License: BSD and LGPLv3+ with exceptions
Group: Development/ML
Url: https://github.com/AltGr/ocaml-mccs
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: dune
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-cudf-devel
BuildRequires: libglpk-devel

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem
solver developed at UNS during the European MANCOOSI project.

This project contains a stripped-down version of the mccs solver,
taken from snapshot 1.1, with a binding as an OCaml library, and
building with jbuilder.

The binding enables interoperation with binary CUDF data from the
OCaml CUDF library, and removes the native C++ parsers and printers.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
dune build -p mccs

%install
dune install --destdir=%buildroot 

%files
%doc README.md LICENCE
%dir %_libdir/ocaml/mccs/
%_libdir/ocaml/mccs/META
%_libdir/ocaml/mccs/opam
%_libdir/ocaml/mccs/*.cma
%_libdir/ocaml/mccs/*.cmi
%_libdir/ocaml/mccs/*.cmx
%_libdir/ocaml/mccs/*.cmxs
%_libdir/ocaml/stublibs/*.so
%dir %_libdir/ocaml/mccs/glpk/
%dir %_libdir/ocaml/mccs/glpk/internal/
%_libdir/ocaml/mccs/glpk/internal/*.cma
%_libdir/ocaml/mccs/glpk/internal/*.cmi
%_libdir/ocaml/mccs/glpk/internal/*.cmx
%_libdir/ocaml/mccs/glpk/internal/*.cmxs

%files devel
%_libdir/ocaml/mccs/*.a
%_libdir/ocaml/mccs/*.cmxa
%_libdir/ocaml/mccs/dune-package
%_libdir/ocaml/mccs/*.cmt
%_libdir/ocaml/mccs/*.cmti
%_libdir/ocaml/mccs/*.ml
%_libdir/ocaml/mccs/*.mli
%_libdir/ocaml/mccs/glpk/internal/*.a
%_libdir/ocaml/mccs/glpk/internal/*.cmxa
%_libdir/ocaml/mccs/glpk/internal/*.cmt
%_libdir/ocaml/mccs/glpk/internal/*.ml

%changelog
* Wed Sep 08 2021 Anton Farygin <rider@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 1.1.11-alt1
- 1.1.11

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.1.10-alt1
- 1.1.10 

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.1.9-alt3
- rebuilt with dune-1.8

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.1.9-alt2
- fixed built with dune-1.6.4

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 1.1.9-alt1
- first build for ALT

