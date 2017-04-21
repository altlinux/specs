# ./usr/lib/ocaml/yojson/yojson.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-yojson
%define libname %(sed -e 's/^ocaml-//' <<< %name)
Version: 1.3.3
Release: alt1%ubt
Summary: An optimized parsing and printing library for the JSON format
Group: Development/ML
License: BSD
Url: http://opam.ocaml.org/packages/yojson/
# https://github.com/mjambon/yojson.git
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-easy-format-devel
BuildRequires(pre): rpm-build-ubt

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make META all
make opt

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_bindir
mkdir -p $OCAMLFIND_DESTDIR
make install BINDIR=%buildroot%_bindir

%files
%doc LICENSE
%_libdir/ocaml/%libname/
%_bindir/ydump
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.o
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc LICENSE README.md Changes examples
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.o
%_libdir/ocaml/*/*.mli

%changelog
* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1%ubt
- first build for ALT, based on RH spec
