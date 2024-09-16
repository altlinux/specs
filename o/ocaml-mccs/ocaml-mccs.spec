Name: ocaml-mccs
Version: 1.1.18
Release: alt1
Summary: Multi Criteria CUDF Solver with OCaml bindings
License: LGPL-2.1-only WITH OCaml-LGPL-linking-exception and BSD-3-Clause and GPL-3.0-only
Group: Development/ML
Url: https://github.com/ocaml-opam/ocaml-mccs
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: dune
BuildRequires: gcc-c++
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-compiler-libs >= 5.2.0
BuildRequires: libglpk-devel

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem
solver developed at UNS during the European MANCOOSI project.

This project contains a stripped-down version of the mccs solver,
taken from snapshot 1.1, with a binding as an OCaml library, and
building with jbuilder.

The binding enables interoperation with binary CUDF data from the
OCaml CUDF library, and removes the native C++ parsers and printers.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md LICENCE

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 1.1.18-alt1
- 1.1+18

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.1.16-alt1
- 1.1+16

* Wed Sep 08 2021 Anton Farygin <rider@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 1.1.11-alt1
- 1.1.11

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.1.10-alt1
- 1.1.10 

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.1.9-alt3
- rebuilt with dune-1.8

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.1.9-alt2
- fixed built with dune-1.6.4

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 1.1.9-alt1
- first build for ALT

