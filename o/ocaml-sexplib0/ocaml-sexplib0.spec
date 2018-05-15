%set_verify_elf_method textrel=relaxed
%define oname sexplib0
Name: ocaml-%oname
Version: 0.11.0
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
%doc LICENSE.txt 
%dir %_libdir/ocaml/sexplib0
%_libdir/ocaml/sexplib0/META
%_libdir/ocaml/sexplib0/*.a
%_libdir/ocaml/sexplib0/*.cmi
%_libdir/ocaml/sexplib0/*.cma
%_libdir/ocaml/sexplib0/*.cmxa
%_libdir/ocaml/sexplib0/*.cmxs

%files devel
%_libdir/ocaml/sexplib0/opam
%_libdir/ocaml/sexplib0/*.cmt
%_libdir/ocaml/sexplib0/*.cmti
%_libdir/ocaml/sexplib0/*.cmx
%_libdir/ocaml/sexplib0/*.mli
%_libdir/ocaml/sexplib0/*.ml
%_libdir/ocaml/sexplib0/*.ml-gen

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1%ubt
- first build for ALT, based on specfile from Mageia

