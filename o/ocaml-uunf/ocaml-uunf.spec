%define libname uunf
Name: ocaml-%libname
Version: 15.1.0
Release: alt1
Summary: Unicode text normalization for OCaml
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/uunf
VCS: https://github.com/dbuenzli/uunf
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.14.1 opam
BuildRequires: ocaml-cmdliner-devel ocaml-result-devel ocaml-uucd-devel ocaml-uutf-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6


%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Uunf is an OCaml library for normalizing Unicode text. It supports all Unicode
normalization forms. The library is independent from any IO mechanism or Unicode
text data structure and it can process text without a complete
in-memory representation.

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
%_bindir/unftrip

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 15.1.0-alt1
- first build for ALT

