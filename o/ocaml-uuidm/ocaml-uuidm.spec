%define libname uuidm
Name: ocaml-%libname
Version: 0.9.8
Release: alt2
Summary: Universally unique identifiers (UUIDs) for OCaml
License: ISC
Group: Development/ML
Url: https://erratique.ch/software/uuidm
VCS: https://github.com/dbuenzli/uuidm
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-cmdliner-devel ocaml-result-devel
BuildRequires: rpm-build-ocaml >= 1.6

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

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md
%_bindir/uuidtrip

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.9.8-alt2
- added support for bytecode-only version of the ocaml package

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- first build for ALT

