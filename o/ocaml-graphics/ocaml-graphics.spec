%set_verify_elf_method textrel=relaxed
%define libname graphics
Name: ocaml-%libname
Version: 5.1.0
Release: alt1
Summary: The OCaml graphics library
License: LGPLv2.1 with exceptions
Group: Development/ML
Url: https://github.com/ocaml/graphics
Source0: %name-%version.tar
BuildRequires: ocaml dune libX11-devel

%description
The graphics library provides a set of portable drawing primitives. Drawing
takes place in a separate window that is created when Graphics.open_graph is
called.

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
dune build @install

%install
dune install --destdir=%buildroot

%files
%doc README.md LICENSE CHANGES.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/stublibs/dllgraphics_stubs.so
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/dune-package
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/*.ml

%changelog
* Fri Feb 28 2020 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- first build for ALT

