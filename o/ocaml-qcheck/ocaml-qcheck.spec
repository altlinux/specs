%set_verify_elf_method textrel=relaxed
%define libname qcheck
Name: ocaml-%libname
Version: 0.12
Release: alt1
Summary: QuickCheck inspired property-based testing for OCaml
Group: Development/ML
License: BSD
Url: https://github.com/c-cube/qcheck/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires: ocaml-ounit
BuildRequires: ocaml-alcotest-devel

%description
This module allows to check invariants (properties of some types) over randomly
generated instances of the type. It provides combinators for generating
instances and printing them.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
make

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
rm -rf %buildroot/usr/doc

# Makes *.cmxs executable such that they will be stripped.
find %buildroot -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest

%files
%doc README.adoc
%dir %_libdir/ocaml/%{libname}*
%dir %_libdir/ocaml/%{libname}-core/runner
%_libdir/ocaml/%{libname}*/META
%_libdir/ocaml/%{libname}*/*.cmi
%_libdir/ocaml/%{libname}*/*.cma
%_libdir/ocaml/%{libname}*/*.a
%_libdir/ocaml/%{libname}*/*/*.cmi
%_libdir/ocaml/%{libname}*/*/*.cma
%_libdir/ocaml/%{libname}*/*/*.a

%files devel
%_libdir/ocaml/%{libname}*/opam
%_libdir/ocaml/%{libname}*/dune-package
%_libdir/ocaml/%{libname}*/*.cmt
%_libdir/ocaml/%{libname}*/*.cmti
%_libdir/ocaml/%{libname}*/*.cmx
%_libdir/ocaml/%{libname}*/*.ml*
%_libdir/ocaml/%{libname}*/*.cmxa
%_libdir/ocaml/%{libname}*/*.cmxs
%_libdir/ocaml/%{libname}*/*/*.cmt
%_libdir/ocaml/%{libname}*/*/*.cmti
%_libdir/ocaml/%{libname}*/*/*.cmx
%_libdir/ocaml/%{libname}*/*/*.ml*
%_libdir/ocaml/%{libname}*/*/*.cmxa
%_libdir/ocaml/%{libname}*/*/*.cmxs

%changelog
* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 0.12-alt1
- 0.12

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.10-alt1
- 0.10

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.9-alt2
- rebuilt with dune-1.8

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.9-alt1
- first build for ALT

