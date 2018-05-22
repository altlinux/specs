%set_verify_elf_method textrel=relaxed
%define oname sexplib
Name: ocaml-%oname
Version: 0.10.0
Release: alt1%ubt
Summary: OCaml library for converting OCaml values to S-expressions
License: Apache 2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: jbuilder
BuildRequires: ocaml
BuildRequires: ocaml-num
BuildRequires: opam
BuildRequires(pre):rpm-build-ubt

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
jbuilder build --verbose -p %oname

%check
jbuilder runtest

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install
rm -rf %buildroot/usr/doc

%files
%doc LICENSE.txt LICENSE-Tywith.txt
%dir %_libdir/ocaml/sexplib
%_libdir/ocaml/sexplib/META
%_libdir/ocaml/sexplib/*.a
%_libdir/ocaml/sexplib/*.cmi
%_libdir/ocaml/sexplib/*.cma
%_libdir/ocaml/sexplib/*.cmxa
%_libdir/ocaml/sexplib/*.cmxs
%dir %_libdir/ocaml/sexplib/*/
%_libdir/ocaml/sexplib/*/*.a
%_libdir/ocaml/sexplib/*/*.cmi
%_libdir/ocaml/sexplib/*/*.cma
%_libdir/ocaml/sexplib/*/*.cmxa
%_libdir/ocaml/sexplib/*/*.cmxs

%files devel
%doc COPYRIGHT.txt README.org CHANGES.md CHANGES.txt
%_libdir/ocaml/sexplib/opam
%_libdir/ocaml/sexplib/*.cmt
%_libdir/ocaml/sexplib/*.cmti
%_libdir/ocaml/sexplib/*.cmx
%_libdir/ocaml/sexplib/*.mli
%_libdir/ocaml/sexplib/*.ml
%_libdir/ocaml/sexplib/*.ml-gen
%_libdir/ocaml/sexplib/*/*.cmt
%_libdir/ocaml/sexplib/*/*.cmti
%_libdir/ocaml/sexplib/*/*.cmx
%_libdir/ocaml/sexplib/*/*.mli
%_libdir/ocaml/sexplib/*/*.ml
%_libdir/ocaml/sexplib/*/*.ml-gen

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.10.0-alt1%ubt
- first build for ALT, based on specfile from Mageia

