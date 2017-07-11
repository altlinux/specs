#ERROR: ./usr/lib/ocaml/easy-format/easy_format.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed

Name: ocaml-easy-format
Version: 1.2.0
Release: alt1%ubt
Summary: High-level and functional interface to the Format module
License: BSD
Group: Development/ML
Url: https://opam.ocaml.org/packages/easy-format/
# https://github.com/mjambon/easy-format
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ubt

%description
This module offers a high-level and functional interface to the Format
module of the OCaml standard library. It is a pretty-printing
facility, i.e. it takes as input some code represented as a tree and
formats this code into the most visually satisfying result, breaking
and indenting lines of code where appropriate.

Input data must be first modeled and converted into a tree using 3
kinds of nodes:

    atoms
    lists
    labeled nodes

Atoms represent any text that is guaranteed to be printed as-is. Lists
can model any sequence of items such as arrays of data or lists of
definitions that are labeled with something like "int main", "let x
=" or "x:".

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
sed -i.add-debuginfo 's/ocamlopt/ocamlopt -g/;s/ocamlc \(-[co]\)/ocamlc -g \1/' Makefile

%build
make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc LICENSE
%_libdir/ocaml/easy-format
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.o
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc LICENSE README.md Changes
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.o
%_libdir/ocaml/*/*.mli

%changelog
* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1%ubt
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.2-alt2%ubt
- rebuild with ocaml 4.04.1

* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1%ubt
- first build for ALT, based on RH spec
