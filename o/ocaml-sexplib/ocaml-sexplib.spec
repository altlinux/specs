%set_verify_elf_method textrel=relaxed
%define oname sexplib
Name: ocaml-%oname
Version: 0.14.0
Release: alt2
Summary: OCaml library for converting OCaml values to S-expressions
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: dune >= 2.0
BuildRequires: ocaml
BuildRequires: ocaml-num
BuildRequires: ocaml-parsexp-devel >= 0.14.0

%description
This library contains functionality for parsing and pretty-printing
S-expressions. In addition to that it contains an extremely useful
preprocessing module for Camlp4, which can be used to automatically
generate code from type definitions for efficiently converting
OCaml-values to S-expressions and vice versa. In combination with the
parsing and pretty-printing functionality this frees users from having
to write their own I/O-routines for datastructures they
define. Possible errors during automatic conversions from
S-expressions to OCaml-values are reported in a very human-readable
way. Another module in the library allows you to extract and replace
sub-expressions in S-expressions.

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
dune build --verbose -p %oname

%check
dune runtest

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
rm -rf %buildroot/usr/share/doc

%files
%doc LICENSE.md LICENSE-Tywith.txt
%dir %_libdir/ocaml/sexplib
%dir %_libdir/ocaml/sexplib/num
%dir %_libdir/ocaml/sexplib/unix
%_libdir/ocaml/sexplib/META
%_libdir/ocaml/sexplib/*.a
%_libdir/ocaml/sexplib/*.cmi
%_libdir/ocaml/sexplib/*.cma
%_libdir/ocaml/sexplib/*.cmxs
%_libdir/ocaml/sexplib/*/*.a
%_libdir/ocaml/sexplib/*/*.cmi
%_libdir/ocaml/sexplib/*/*.cma
%_libdir/ocaml/sexplib/*/*.cmxs

%files devel
%doc COPYRIGHT.txt README.org CHANGES.md CHANGES.txt
%_libdir/ocaml/sexplib/opam
%_libdir/ocaml/sexplib/*.cmt
%_libdir/ocaml/sexplib/*.cmti
%_libdir/ocaml/sexplib/*.cmx
%_libdir/ocaml/sexplib/*.cmxa
%_libdir/ocaml/sexplib/*.mli
%_libdir/ocaml/sexplib/*.ml
%_libdir/ocaml/sexplib/dune-package
%_libdir/ocaml/sexplib/*/*.cmt
%_libdir/ocaml/sexplib/*/*.cmti
%_libdir/ocaml/sexplib/*/*.cmx
%_libdir/ocaml/sexplib/*/*.cmxa
%_libdir/ocaml/sexplib/*/*.mli
%_libdir/ocaml/sexplib/*/*.ml

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- cmxa moved to the devel package

* Wed Jun 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.10.0-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 0.10.0-alt2
- rebuilt with ocaml 4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.10.0-alt1
- first build for ALT, based on specfile from Mageia

