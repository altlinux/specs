%define libname postgresql
Name: ocaml-%libname
Version: 5.4.0
Release: alt1
Summary: PostgreSQL Bindings for OCaml
Group: Development/ML
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Url: https://github.com/mmottl/postgresql-ocaml
Source0: %name-%version.tar
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: libpq-devel
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
%doc README.md LICENSE.md CHANGELOG.md

%files devel -f ocaml-files.devel

%changelog
* Sun Apr 19 2026 Anton Farygin <rider@altlinux.org> 5.4.0-alt1
- 5.3.2 -> 5.4.0

* Sun Mar 01 2026 Anton Farygin <rider@altlinux.org> 5.3.2-alt1
- 5.1.3 -> 5.3.2

* Sat Sep 27 2025 Alexei Takaseev <taf@altlinux.org> 5.1.3-alt1.3
- NMU: change BR libpq5-devel -> libpq-devel

* Mon Mar 03 2025 Alexei Takaseev <taf@altlinux.org> 5.1.3-alt1.2
- Change BR libpq5-17-devel -> libpq5-devel

* Wed Feb 12 2025 Alexei Takaseev <taf@altlinux.org> 5.1.3-alt1.1
- Temporary change BR postgresql-devel -> libpq5-17-devel

* Fri Jan 17 2025 Anton Farygin <rider@altlinux.ru> 5.1.3-alt1
- 5.1.3

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
