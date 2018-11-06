%set_verify_elf_method textrel=relaxed
%define libname stringext
Name: ocaml-%libname
Version: 1.5.0
Release: alt1
Summary: Extra string functions for OCaml
Group: Development/ML
License: BSD
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-qcheck-devel

%description
Extra string functions for OCaml. Mainly splitting. All functions are in
the Stringext module.

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
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.dune
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%changelog
* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- first build for ALT

