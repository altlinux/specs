%set_verify_elf_method textrel=relaxed
%define libname sequence
Name: ocaml-%libname
Version: 1.1
Release: alt1
Summary: Simple and lightweight sequence abstract data type for OCaml
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/sequence/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel

%description
Simple sequence abstract datatype, intended to iterate efficiently on
collections while performing some transformations.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%check
jbuilder runtest --no-buffer --force --verbose

%files
%doc README.adoc LICENSE CHANGELOG.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.cmt*
%exclude %_libdir/ocaml/%libname/*.ml
%exclude %_libdir/ocaml/%libname/*.mli
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmxs
%exclude %_libdir/ocaml/%libname/*/*.cmx
%exclude %_libdir/ocaml/%libname/*/*.cmt*
%exclude %_libdir/ocaml/%libname/*/*.ml
%exclude %_libdir/ocaml/%libname/*/*.mli
%exclude %_libdir/ocaml/%libname/*/*.a
%exclude %_libdir/ocaml/%libname/*/*.cmxa
%exclude %_libdir/ocaml/%libname/*/*.cmxs


%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.ml
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/*/*.cmx
%_libdir/ocaml/%libname/*/*.cmt*
%_libdir/ocaml/%libname/*/*.ml
%_libdir/ocaml/%libname/*/*.mli
%_libdir/ocaml/%libname/*/*.a
%_libdir/ocaml/%libname/*/*.cmxa
%_libdir/ocaml/%libname/*/*.cmxs

%changelog
* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT


