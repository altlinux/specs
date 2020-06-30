%set_verify_elf_method textrel=relaxed
%define pkgname ocplib-endian
Name: ocaml-%pkgname
Version: 1.1
Release: alt1
Summary: Functions to read/write int16/32/64 from strings, bigarrays
License: LGPLv2+
Group: Development/ML
Url: https://github.com/OCamlPro/ocplib-endian
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-cppo
BuildRequires: ocaml-ocamldoc
BuildRequires: dune

%description
Optimised functions to read and write int16/32/64 from strings,
bytes and bigarrays, based on primitives added in version 4.01.

The library implements three modules:

EndianString works directly on strings, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBytes works directly on bytes, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBigstring works on bigstrings (Bigarrays of chars),
and provides submodules BigEndian and LittleEndian, with their
unsafe counter-parts;

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and
signature files for developing applications that use %name.

%prep
%setup

%build
dune build --profile=release

%install
dune install --destdir=%buildroot --profile=release

%check
dune runtest --profile=release

%files
%doc COPYING.txt README.md CHANGES.md
%_libdir/ocaml/%pkgname
%exclude %_libdir/ocaml/%pkgname/*.a
%exclude %_libdir/ocaml/%pkgname/*.cmxa
%exclude %_libdir/ocaml/%pkgname/*.cmx
%exclude %_libdir/ocaml/%pkgname/*.mli

%files devel
%_libdir/ocaml/%pkgname/*.a
%_libdir/ocaml/%pkgname/*.cmxa
%_libdir/ocaml/%pkgname/*.cmx
%_libdir/ocaml/%pkgname/*.mli

%changelog
* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.1

* Thu Feb 13 2020 Anton Farygin <rider@altlinux.ru> 1.0-alt1
- first build for Sisyphus

