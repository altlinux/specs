%set_verify_elf_method textrel=relaxed
%define libname ppxlib
Name: ocaml-%libname
Version: 0.5.0
Release: alt1
Summary: Base library and tools for ppx rewriters.
License: MIT
Group: Development/ML
Url: https://github.com/ocaml-ppx/ppxlib
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam  ocaml-compiler-libs-devel cinaps ocaml-result-devel
BuildRequires: ocaml-sexplib0-devel ocaml-migrate-parsetree-devel ocaml-stdio-devel ocaml-ppx_derivers-devel

%description
A comprehensive toolbox for ppx development. It features:

 * a OCaml AST / parser / pretty-printer snapshot,to create a full frontend independent of the version of OCaml;
 * a library for library for ppx rewriters in general, and type-driven code generators in particular;
 * a feature-full driver for OCaml AST transformers;
 * a quotation mechanism allowing to write values representing the OCaml AST in the OCaml syntax;
 * a generator of open recursion classes from type definitions.

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
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install

%files
%doc README.md LICENSE.md CHANGES.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.cmt*
%exclude %_libdir/ocaml/%libname/*.ml
%exclude %_libdir/ocaml/%libname/*.mli
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmxs
%exclude %_libdir/ocaml/%libname/*/*.cmx
%exclude %_libdir/ocaml/%libname/*/*.cmt*
%exclude %_libdir/ocaml/%libname/*/*.ml
%exclude %_libdir/ocaml/%libname/*/*.mli
%exclude %_libdir/ocaml/%libname/*/*.cmxa
%exclude %_libdir/ocaml/%libname/*/*.cmxs


%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.ml
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/*/*.cmx
%_libdir/ocaml/%libname/*/*.cmt*
%_libdir/ocaml/%libname/*/*.ml
%_libdir/ocaml/%libname/*/*.mli
%_libdir/ocaml/%libname/*/*.cmxa
%_libdir/ocaml/%libname/*/*.cmxs

%changelog
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- first build for ALT


