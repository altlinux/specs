%define libname iter
Name: ocaml-%libname
Version: 1.4
Release: alt1
Summary: Simple and lightweight iterator abstract data type for OCaml
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/iter/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel ocaml-dune-configurator-devel ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel
Provides: ocaml-sequence = %EVR
Obsoletes: ocaml-sequence

%description
Simple abstraction over `iter` functions, intended to iterate efficiently
on collections while performing some transformations.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Provides: ocaml-sequence-devel = %EVR
Obsoletes: ocaml-sequence-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
rm -f dune
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGELOG.md

%files devel -f ocaml-files.devel

%changelog
* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- 1.3 -> 1.4

* Fri Nov 26 2021 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- 1.2.1 -> 1.3

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 1.2.1-alt3
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- simplified specfile with macros from rpm-build-ocaml 1.4

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- fixed build by dune-2.x

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1
- renamed to iter by upstream

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT


