%define libname postgresql
Name: ocaml-%libname
Version: 5.0.0
Release: alt1
Summary: PostgreSQL Bindings for OCaml
Group: Development/ML
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Url: https://github.com/mmottl/postgresql-ocaml
Source0: %name-%version.tar
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: postgresql-devel
BuildRequires: chrpath

%description
OCAML Postgresql offers library functions for accessing PostgreSQL databases.

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
%dune_build -p %libname 

%install
%dune_install
rm -rf %buildroot/usr/share/doc
chrpath -d %buildroot%_libdir/ocaml/stublibs/dllpostgresql_stubs.so

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE.md CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 5.0.0-alt1
- 5.0.0
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- spec: use SPDX for ocaml linking exception in license tag
- simplified specfile with macros from rpm-build-ocaml 1.4

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 4.5.2-alt1
- 4.5.2

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Fri Nov 02 2018 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- first build for ALT
