%set_verify_elf_method textrel=relaxed
%define libname parsexp
Name: ocaml-%libname
Version: 0.14.0
Release: alt2
Summary: S-expression parsing library for ocaml
Group: Development/ML
License: Apache-2.0
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune >= 1.8
BuildRequires: ocaml
BuildRequires: ocaml-findlib 
BuildRequires: ocaml-sexplib0-devel >= 0.12.0
BuildRequires: ocaml-base-devel >= 0.12.0
BuildRequires: opam

%description
This library provides generic parsers for parsing S-expressions from strings or
other medium.

The library is focused on performances but still provide full generic parsers
that can be used with strings, bigstrings, lexing buffers, character streams or
any other sources effortlessly.

It provides three different class of parsers:

    the normal parsers, producing [Sexp.t] or [Sexp.t list] values
    
    the parsers with positions, building compact position sequences so that one
    can recover original positions in order to report properly located errors at
    little cost
    
    the Concrete Syntax Tree parsers, produce values of type [Parsexp.Cst.t]
    which record the concrete layout of the s-expression syntax, including 
    comments

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
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
rm -rf %buildroot/usr/share/doc

%check
dune runtest

%files
%doc README.org CHANGES.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxs

%files devel
%_libdir/ocaml/%libname/dune-package
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.ml*

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- cmxa have been moved to devel package

* Wed Jun 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


