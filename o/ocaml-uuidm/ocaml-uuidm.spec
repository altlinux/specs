%set_verify_elf_method textrel=relaxed
%define libname uuidm
Name: ocaml-%libname
Version: 0.9.6
Release: alt1
Summary: Universally unique identifiers (UUIDs) for OCaml
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/uuidm
# https://github.com/dbuenzli/uuidm
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-cmdliner-devel ocaml-result-devel

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Uuidm is an OCaml module implementing 128 bits universally unique identifiers
version 3, 5 (named based with MD5, SHA-1 hashing) and 4 (random based)
according to RFC 4122.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup

%build
ocaml pkg/pkg.ml build

%install
sed -i 's,%%%%VERSION%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md
%_bindir/uuidtrip
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- first build for ALT

