%define libname stringext
Name: ocaml-%libname
Version: 1.6.0
Release: alt3
Summary: Extra string functions for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/rgrinberg/stringext
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: rpm-build-ocaml > 1.4
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-qcheck-devel

%description
Extra string functions for OCaml. Mainly splitting. All functions are in
the Stringext module.

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
sed -i 's,oUnit,ounit2,' lib_test/dune
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 1.6.0-alt3
- fixed URL and License tag
- cleanup specfile

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 1.6.0-alt2
- fixed build with ounit-2.2.2

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.5.0-alt2
- rebuilt with dune-1.8

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- first build for ALT

