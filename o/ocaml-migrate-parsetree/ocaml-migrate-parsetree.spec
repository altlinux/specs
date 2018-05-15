%set_verify_elf_method textrel=relaxed
Name: ocaml-migrate-parsetree
Version: 1.0.10
Release: alt1%ubt
Summary: Convert OCaml parsetrees between different major versions
Group: Development/ML
License: LGPLv2+ with exceptions
Url: https://github.com/ocaml-ppx/ocaml-migrate-parsetree
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: jbuilder
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-findlib
BuildRequires: opam
BuildRequires(pre): rpm-build-ubt

%description
This library converts between parsetrees of different OCaml versions.
For each version, there is a snapshot of the parsetree and conversion
functions to the next and/or previous version.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_libdir/ocaml
jbuilder install --destdir=%buildroot --libdir=%buildroot%_libdir/ocaml

# Makes *.cmxs executable such that they will be stripped.
find %buildroot -name '*.cmxs' -exec chmod 0755 {} \;

%check
%make_build test

%files
%doc README.md MANUAL.md CHANGES.md LICENSE.md
%_libdir/ocaml/*
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.ml
%exclude %_libdir/ocaml/*/*.mli
%exclude %_libdir/ocaml/*/driver-main/*.a
%exclude %_libdir/ocaml/*/driver-main/*.cmxa
%exclude %_libdir/ocaml/*/driver-main/*.cmx
%exclude %_libdir/ocaml/*/driver-main/*.ml



%files devel
%doc README.md MANUAL.md CHANGES.md LICENSE.md
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.ml
%_libdir/ocaml/*/*.mli
%_libdir/ocaml/*/driver-main/*.a
%_libdir/ocaml/*/driver-main/*.cmxa
%_libdir/ocaml/*/driver-main/*.cmx
%_libdir/ocaml/*/driver-main/*.ml

%changelog
* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.10-alt1%ubt
- first build for ALT, based on specfile from RH

