%set_verify_elf_method textrel=relaxed
%define libname qtest
Name: ocaml-%libname
Version: 2.9
Release: alt1
Summary: Inline (Unit) Tests for OCaml
License: GPLv3
Group: Development/ML
Url: https://github.com/c-cube/ocaml-containers/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam  ocaml-compiler-libs-devel ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc 

%description
qtest extracts inline unit tests written using a special syntax in comments.
Those tests are then run using the oUnit framework and the qcheck library. The
possibilities range from trivial tests -- extremely simple to use -- to
sophisticated random generation of test cases.

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
make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.adoc HOWTO.adoc
%dir %_libdir/ocaml/%libname
%_bindir/qtest
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*/*.cmx
%exclude %_libdir/ocaml/%libname/*/*.cmt*
%exclude %_libdir/ocaml/%libname/*/*.ml
%exclude %_libdir/ocaml/%libname/*/*.a
%exclude %_libdir/ocaml/%libname/*/*.cmxa
%exclude %_libdir/ocaml/%libname/*/*.cmxs


%files devel
%_libdir/ocaml/%libname/*/*.cmx
%_libdir/ocaml/%libname/*/*.cmt*
%_libdir/ocaml/%libname/*/*.ml
%_libdir/ocaml/%libname/*/*.a
%_libdir/ocaml/%libname/*/*.cmxa
%_libdir/ocaml/%libname/*/*.cmxs

%changelog
* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 2.9-alt1
- first build for ALT


