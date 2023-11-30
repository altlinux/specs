%set_verify_elf_method textrel=relaxed
%define libname ppx_derivers
Name: ocaml-%libname
Version: 1.2.1
Release: alt2
Summary: ppx_type_conv/ppx_deriving interoperability library
Group: Development/ML
License: BSD
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml

%description
Ppx_derivers is a tiny package whose sole purpose is to allow ppx_deriving and
ppx_type_conv to inter-operate gracefully when linked as part of the same
ocaml-migrate-parsetree driver.

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

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- cleanup specfile

* Fri Jun 07 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.2-alt2
- rebuilt with dune-1.8

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- first build for ALT

