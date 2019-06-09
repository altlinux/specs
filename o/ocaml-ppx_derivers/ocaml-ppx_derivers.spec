%set_verify_elf_method textrel=relaxed
%define libname ppx_derivers
Name: ocaml-%libname
Version: 1.2.1
Release: alt1
Summary: ppx_type_conv/ppx_deriving interoperability library
Group: Development/ML
License: BSD
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: opam

%description
Ppx_derivers is a tiny package whose sole purpose is to allow ppx_deriving and
ppx_type_conv to inter-operate gracefully when linked as part of the same
ocaml-migrate-parsetree driver.

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
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/dune-package
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*

%changelog
* Fri Jun 07 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.2-alt2
- rebuilt with dune-1.8

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- first build for ALT

