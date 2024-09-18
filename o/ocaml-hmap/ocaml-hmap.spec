%define libname hmap
Name: ocaml-%libname
Version: 0.8.1
Release: alt1
Summary: Heterogeneous value maps for OCaml
License: ISC
Group: Development/ML
Url: https://github.com/dbuenzli/hmap
VCS: https://github.com/dbuenzli/hmap
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.14.1 opam
BuildRequires(pre): rpm-build-ocaml >= 1.6

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Hmap provides heterogeneous value maps for OCaml. These maps bind keys to values
with arbitrary types. Keys witness the type of the value they are bound to which
allows to add and lookup bindings in a type safe manner.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup

%build
sed -i 's,%%%%VERSION%%%%,%version,g' pkg/META src/* README.md
sed -i 's,%%%%NAME%%%%,%libname,g' src/*
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 18 2024 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- first build for Sisyphus
