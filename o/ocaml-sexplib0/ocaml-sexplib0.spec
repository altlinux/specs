%set_verify_elf_method textrel=relaxed
%define oname sexplib0
Name: ocaml-%oname
Version: 0.11.0
Release: alt4
Summary: OCaml library for converting OCaml values to S-expressions
License: Apache 2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: jbuilder
BuildRequires: ocaml
BuildRequires: ocaml-num
BuildRequires: opam

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
%_libdir/ocaml/sexplib0/*.dune
%_libdir/ocaml/sexplib0/*.cmt
%_libdir/ocaml/sexplib0/*.cmti
%_libdir/ocaml/sexplib0/*.cmx
%_libdir/ocaml/sexplib0/*.mli
%_libdir/ocaml/sexplib0/*.ml

%changelog
* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt4
- fixed build with dune 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with ocaml-4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT, based on specfile from Mageia

