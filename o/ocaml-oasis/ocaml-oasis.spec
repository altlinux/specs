%set_verify_elf_method textrel=relaxed

Name: ocaml-oasis
Version: 0.4.11
Release: alt1
Summary: Architecture for building OCaml libraries and applications
License: LGPL-2.1
Group: Development/ML
Url: http://oasis.forge.ocamlcore.org/
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-findlib-devel ocaml-ocamlbuild ocamlmod ocamlify ocaml-ocamldoc ocaml-ocamlbuild-devel

%description
OASIS is a tool to integrate a configure, build and install system in your OCaml project.
It helps to create standard entry points in your build system and allows external tools to
analyse your project easily.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml setup.ml -configure \
    --destdir %buildroot \
    --prefix %_prefix
ocaml setup.ml -build

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%doc COPYING.txt
%_bindir/*
%dir %_libdir/ocaml
%dir %_libdir/ocaml/*
%_libdir/ocaml/*/*.cmxs

%files devel
%dir %_libdir/ocaml
%dir %_libdir/ocaml/*
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.annot
%_libdir/ocaml/*/*.cma
%_libdir/ocaml/*/*.cmi
%_libdir/ocaml/*/*.cmt
%_libdir/ocaml/*/*.cmti
%_libdir/ocaml/*/*.ml
%_libdir/ocaml/*/*.mli
%_libdir/ocaml/*/META
%changelog
* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 0.4.11-alt1
- first build for ALT

