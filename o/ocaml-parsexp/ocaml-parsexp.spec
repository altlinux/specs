%set_verify_elf_method textrel=relaxed
%define libname parsexp
Name: ocaml-%libname
Version: 0.11.0
Release: alt1
Summary: S-expression parsing library for ocaml
Group: Development/ML
License: Apache-2.0
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-findlib ocaml-sexplib0-devel
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
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install
rm -rf %buildroot/usr/doc

%check
dune runtest

%files
%doc README.org CHANGES.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.dune
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*

%changelog
* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


