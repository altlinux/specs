%set_verify_elf_method textrel=relaxed
Name: ocaml-num
Version: 1.3
Release: alt1
Summary: Legacy Num library for arbitrary-precision integer and rational arithmetic
Group: Development/ML
License: LGPLv2+ with exceptions

Url: https://github.com/ocaml/num
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel dune

%description
This library implements arbitrary-precision arithmetic on big integers
and on rationals.

This is a legacy library. It used to be part of the core OCaml
distribution (in otherlibs/num) but is now distributed separately. New
applications that need arbitrary-precision arithmetic should use the
Zarith library (https://github.com/ocaml/Zarith) instead of the Num
library, and older applications that already use Num are encouraged to
switch to Zarith. Zarith delivers much better performance than Num and
has a nicer API.

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
dune build @install

%check
dune runtest

%install
dune install --destdir=%buildroot

%files
%doc Changelog README.md
%doc LICENSE
%_libdir/ocaml/num
%_libdir/ocaml/num_top
%_libdir/ocaml/stublibs/dll*.so
%exclude %_libdir/ocaml/num/*.a
%exclude %_libdir/ocaml/num/*.cmxa
%exclude %_libdir/ocaml/num/*/*.a
%exclude %_libdir/ocaml/num/*/*.cmxa
%exclude %_libdir/ocaml/num/*/*.cmx
%exclude %_libdir/ocaml/num/*/*.mli

%files devel
%doc LICENSE
%_libdir/ocaml/num/*/*.a
%_libdir/ocaml/num/*/*.cmxa
%_libdir/ocaml/num/*/*.cmx
%_libdir/ocaml/num/*/*.mli
%_libdir/ocaml/num/*.a
%_libdir/ocaml/num/*.cmxa

%changelog
* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- 1.3

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- 1.2

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt2
- rebuilt with ocaml 4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT, based on Mageia spec

