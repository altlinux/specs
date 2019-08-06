%set_verify_elf_method textrel=relaxed
%define libname iter
Name: ocaml-%libname
Version: 1.2.1
Release: alt1
Summary: Simple and lightweight iterator abstract data type for OCaml
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/sequence/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel
Provides: ocaml-sequence = %EVR
Obsoletes: ocaml-sequence

%description
Simple abstraction over `iter` functions, intended to iterate efficiently
on collections while performing some transformations.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Provides: ocaml-sequence-devel = %EVR
Obsoletes: ocaml-sequence-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
rm -f dune
make

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%check
make test

%files
%doc README.md LICENSE CHANGELOG.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.cmt*
%exclude %_libdir/ocaml/%libname/*.ml
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmxs
# compatability package with sequence
%dir %_libdir/ocaml/sequence
%_libdir/ocaml/sequence/*
%exclude %_libdir/ocaml/sequence/*.cmx
%exclude %_libdir/ocaml/sequence/*.cmt*
%exclude %_libdir/ocaml/sequence/*.ml
%exclude %_libdir/ocaml/sequence/*.a
%exclude %_libdir/ocaml/sequence/*.cmxa
%exclude %_libdir/ocaml/sequence/*.cmxs


%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.ml
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/sequence/*.cmx
%_libdir/ocaml/sequence/*.cmt*
%_libdir/ocaml/sequence/*.ml
%_libdir/ocaml/sequence/*.a
%_libdir/ocaml/sequence/*.cmxa
%_libdir/ocaml/sequence/*.cmxs

%changelog
* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1
- renamed to iter by upstream

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT


