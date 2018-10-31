%set_verify_elf_method textrel=relaxed
%define libname ppx_tools
Name: ocaml-%libname
Version: 5.1
Release: alt1
Summary: Tools for authors of ppx rewriters and other syntactic tools
License: MIT
Group: Development/ML
Url: https://github.com/alainfrisch/ppx_tools
Source0: %name-%version.tar
BuildRequires: ocaml-findlib

%description
Tools for authors of syntactic tools (such as ppx rewriters).

This package is licensed by LexiFi under the terms of the MIT license.

The tools are installed as a findlib package called 'ppx_tools'.
Executables are thus accessible through the ocamlfind driver
(e.g.: ocamlfind ppx_tools/dumpast).

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
make all

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p %buildroot/%_libdir/ocaml
make install

%files
%doc README.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/dumpast
%_libdir/ocaml/%libname/genlifter
%_libdir/ocaml/%libname/ppx_metaquot
%_libdir/ocaml/%libname/rewriter

%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.mli

%changelog
* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- first build for ALT

