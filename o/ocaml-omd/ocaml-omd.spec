%set_verify_elf_method textrel=relaxed
%define libname omd
Name: ocaml-%libname
Version: 1.3.1
Release: alt3
Summary: OMD: extensible Markdown library and tool in OCaml
Group: Development/ML
License: ISC
Url: https://github.com/ocaml/omd
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-oasis
BuildRequires: ocaml-ocamlbuild
BuildRequires: opam

%description
This Markdown library is implemented using only pure OCaml (including
I/O operations provided by the standard OCaml compiler distribution).
OMD is meant to be as faithful as possible to the original Markdown.
Additionally, OMD implements a few Github markdown features, an extension
mechanism, and some other features. Note that the opam package installs both the
OMD library and the command line tool omd

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
oasis setup
ocaml setup.ml -configure --prefix %buildroot%prefix
ocaml setup.ml -build


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%_ocamldir
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%doc README.md ABOUT.md
%dir %_libdir/ocaml/%libname
%_bindir/*
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.annot

%files devel
%_libdir/ocaml/%libname/*.cmt
%_libdir/ocaml/%libname/*.cmti
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.ml*

%changelog
* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 1.3.1-alt3
- adaptation for rpm-build-ocaml-1.4
- devel parts moved to devel package

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2
- rebuilt with ocaml-4.08

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- first build for ALT

