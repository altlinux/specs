%define libname uucd
Name: ocaml-%libname
Version: 16.0.0
Release: alt1
Summary: Unicode character database decoder for OCaml
License: ISC
Group: Development/ML
Url: https://erratique.ch/software/uucd
VCS: https://github.com/dbuenzli/uucd
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.14.1 opam
BuildRequires: ocaml-cmdliner-devel ocaml-result-devel ocaml-xmlm-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Uucd is an OCaml module to decode the data of the Unicode character database
from its XML representation. It provides high-level (but not
necessarily efficient) access to the data so that efficient representations
can be extracted.

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

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 16.0.0-alt1
- 16.0.0 

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 15.1.0-alt1
- first build for ALT

