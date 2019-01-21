%set_verify_elf_method textrel=relaxed
%define libname ppx_sexp_conv
Name: ocaml-%libname
Version: 0.11.2
Release: alt2
Summary: Generation of S-expression conversion functions from type definitions
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/ppx_sexp_conv
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam ocaml-result-devel
BuildRequires: ocaml-sexplib0-devel ocaml-ppxlib-devel ocaml-migrate-parsetree-devel

%description
ppx_sexp_conv is a PPX syntax extension that generates code for converting OCaml
types to and from s-expressions, as defined in the =sexplib= library.

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
%doc README.org LICENSE.txt CHANGES.md
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
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.11.2-alt2
- rebuilt with ocaml-ppxlib 0.5.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.2-alt1
- first build for ALT


