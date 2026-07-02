%define libname ppx_deriving
Name: ocaml-%libname
Version: 6.1.1
Release: alt1
Summary: Type-driven code generation for OCaml >=4.02
License: MIT
Group: Development/ML
Url: https://github.com/ocaml-ppx/ppx_deriving
VCS: https://github.com/ocaml-ppx/ppx_deriving.git
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-findlib-devel ocaml-ocamlbuild 
BuildRequires: ocaml-ppx_derivers-devel opam dune ocaml-ounit-devel ocaml-cppo ocaml-ppxlib-devel

%description
ppx_deriving provides common infrastructure for generating code based on type
definitions, and a set of useful plugins for common tasks.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md LICENSE.txt CHANGELOG.md

%files devel -f ocaml-files.devel

%changelog
* Thu Jul 02 2026 Anton Farygin <rider@altlinux.org> 6.1.1-alt1
- 4.4.1 -> 6.1.1

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Tue Feb 04 2020 Anton Farygin <rider@altlinux.ru> 4.4-alt2
- used the dune to install

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 4.4-alt1
- 4.4

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 4.3-alt1
- 4.3

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.2.1-alt2
- rebuilt with ocaml-migrate-parsetree 1.2.0

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 4.2.1-alt1
- first build for ALT

