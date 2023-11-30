Name: ocaml-ounit
Version: 2.2.7
Release: alt1
Summary: Unit test framework for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/gildor478/ounit
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: libev-devel
BuildRequires: dune ocaml

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p ounit2

%install
%dune_install ounit2

%check
%dune_check -p ounit2

%files -f ocaml-files.runtime
%doc LICENSE.txt

%files devel -f ocaml-files.devel
%doc LICENSE.txt README.md CHANGES.md

%changelog
* Thu Nov 02 2023 Anton Farygin <rider@altlinux.ru> 2.2.7-alt1
- 2.2.7

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 2.2.4-alt3
- disabled lwt variant of the ounit2

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 2.2.4-alt2
- added --release option for dune in build and check sections
- simplified specfile with macros from rpm-build-ocaml 1.4
- cleanup build requires

* Mon Mar 15 2021 Anton Farygin <rider@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Jul 23 2020 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- 2.2.2
- turned on tests

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 2.0.8-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- rebuild with ocaml 4.04.1

* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- first build for ALT, based on RH spec
