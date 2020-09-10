%set_verify_elf_method textrel=relaxed
%define  modulename cstruct

# TODO: async
%define opamodules cstruct,cstruct-unix,cstruct-lwt,cstruct-sexp,ppx_cstruct

Name:    ocaml-%modulename
Version: 5.3.0
Release: alt1
Summary: access C-like structures directly from OCaml
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-cstruct
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-bigarray-compat-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-sexplib-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-ppx_tools_versioned-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-alcotest-devel
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Cstruct is a library and syntax extension to make it easier to access C-like
structures directly from OCaml.  It supports both reading and writing to these
structures, and they are accessed via the `Bigarray` module.

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
dune build -p %opamodules --verbose

%install
dune install `echo "%opamodules"|tr ',' ' '` --destdir=%buildroot

%check
dune runtest

%files
%doc README.md
%dir %_libdir/ocaml/%modulename
%dir %_libdir/ocaml/ppx_%modulename
%_libdir/ocaml/stublibs/dllcstruct_stubs.so
%_libdir/ocaml/%{modulename}/*.js
%_libdir/ocaml/*%{modulename}*/META
%_libdir/ocaml/*%{modulename}*/*.cma
%_libdir/ocaml/*%{modulename}*/*.cmi
%_libdir/ocaml/*%{modulename}*/*.cmxs

%files devel
%_libdir/ocaml/*%{modulename}*/dune-package
%_libdir/ocaml/*%{modulename}*/opam
%_libdir/ocaml/*%{modulename}*/*.exe
%_libdir/ocaml/*%{modulename}*/*.a
%_libdir/ocaml/*%{modulename}*/*.cmt*
%_libdir/ocaml/*%{modulename}*/*.cmxa
%_libdir/ocaml/*%{modulename}*/*.cmx
%_libdir/ocaml/*%{modulename}*/*.mli
%_libdir/ocaml/*%{modulename}*/*.ml

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- first build for ALT
