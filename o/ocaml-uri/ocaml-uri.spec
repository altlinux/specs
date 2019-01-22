%set_verify_elf_method textrel=relaxed
%define libname uri
Name: ocaml-%libname
Version: 2.1.0
Release: alt1
Summary: An RFC3986 URI/URL parsing library for OCaml
Group: Development/ML
License: BSD
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-sexplib0-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-stringext-devel
BuildRequires: ocaml-migrate-parsetree-devel

%description
his is an OCaml implementation of the RFC3986 specification for parsing URI
or URLs.

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
dune build -p %libname 

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install
rm -rf %buildroot/usr/doc

# Makes *.cmxs executable such that they will be stripped.
find %buildroot -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest

%files
%doc README.md
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
* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- first build for ALT

