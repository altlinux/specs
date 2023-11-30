%define libname reactiveData
Name: ocaml-%libname
Version: 0.3
Release: alt1
Summary: Functional reactive programming with incremental changes in data structures
License: LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/ocsigen/reactiveData
Source: %name-%version.tar
BuildRequires: dune ocaml >= 4.07.1
BuildRequires: ocaml-react-devel

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description
ReactiveData is an OCaml module for functional reactive programming (FRP) based on React.
It adds support to incremental changes in data structures by reasoning on patches instead of absolute values.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup

%build
%dune_build

%install
%dune_install

%files -f ocaml-files.runtime
%doc LICENSE CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 0.3-alt1
- 0.3

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- first build for ALT

