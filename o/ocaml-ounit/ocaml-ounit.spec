#/usr/lib/ocaml/oUnit/oUnit.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-ounit
Version: 2.2.3
Release: alt1
Summary: Unit test framework for OCaml
Group: Development/ML
License: MIT
Url: http://ounit.forge.ocamlcore.org/
# https://github.com/gildor478/ounit
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-ocplib-endian-devel
BuildRequires: ocaml-result-devel
BuildRequires: libev-devel
BuildRequires: dune

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
%patch0 -p1

%build
dune build @install

%install
dune install --destdir=%buildroot

%check
dune runtest

%files
%doc LICENSE.txt
%_libdir/ocaml/ounit*
%exclude %_libdir/ocaml/ounit2-lwt/*.a
%exclude %_libdir/ocaml/ounit2-lwt/*.cmxa
%exclude %_libdir/ocaml/ounit*/*/*.a
%exclude %_libdir/ocaml/ounit*/*/*.cmxa
%exclude %_libdir/ocaml/ounit*/*/*.mli

%files devel
%doc LICENSE.txt README.md CHANGES.md
%_libdir/ocaml/ounit*/*/*.a
%_libdir/ocaml/ounit*/*/*.cmxa
%_libdir/ocaml/ounit*/*/*.mli
%_libdir/ocaml/ounit2-lwt/*.a
%_libdir/ocaml/ounit2-lwt/*.cmxa

%changelog
* Thu Jul 23 2020 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- 2.2.2
- turned on tests

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 2.0.8-alt4
- rebuilt with ocaml-4.08

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
