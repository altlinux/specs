#/usr/lib/ocaml/oUnit/oUnit.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-ounit
Version: 2.0.8
Release: alt3
Summary: Unit test framework for OCaml
Group: Development/ML
License: MIT
Url: http://ounit.forge.ocamlcore.org/
# https://github.com/gildor478/ounit
Source: %name-%version.tar

BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

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
./configure --destdir %buildroot
make all
make doc
make test

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc LICENSE.txt
%_libdir/ocaml/oUnit
%exclude %_libdir/ocaml/oUnit/*.a
%exclude %_libdir/ocaml/oUnit/*.cmxa
%exclude %_libdir/ocaml/oUnit/*.mli

%files devel
%doc LICENSE.txt README.txt
%doc _build/src/api-ounit.docdir/*
%_libdir/ocaml/oUnit/*.a
%_libdir/ocaml/oUnit/*.cmxa
%_libdir/ocaml/oUnit/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- rebuild with ocaml 4.04.1

* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- first build for ALT, based on RH spec
