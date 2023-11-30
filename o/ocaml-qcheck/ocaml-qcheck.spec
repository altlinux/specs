# tests broken on 32-bit platforms and ppc64le
%ifarch %ix86 armh ppc64le
%def_disable check
%endif

%define libname qcheck
Name: ocaml-%libname
Version: 0.21.2
Release: alt1
Summary: QuickCheck inspired property-based testing for OCaml
Group: Development/ML
License: BSD
Url: https://github.com/c-cube/qcheck/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-alcotest-devel

%description
This module allows to check invariants (properties of some types) over randomly
generated instances of the type. It provides combinators for generating
instances and printing them.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

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
rm -rf %buildroot/usr/doc

%check
#sed -i '19d' example/alcotest/output.txt.expected
%dune_check

%files -f ocaml-files.runtime
%doc README.adoc

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 0.21.2-alt1
- 0.21.2

* Mon Feb 21 2022 Anton Farygin <rider@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 0.18-alt1
- 0.18

* Mon Mar 15 2021 Anton Farygin <rider@altlinux.org> 0.17-alt1
- 0.17

* Thu Dec 31 2020 Anton Farygin <rider@altlinux.ru> 0.16-alt1
- 0.16

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.15-alt1
- 0.15

* Wed Aug 26 2020 Anton Farygin <rider@altlinux.ru> 0.14-alt1
- 0.14

* Mon Feb 17 2020 Anton Farygin <rider@altlinux.ru> 0.13-alt1
- 0.13

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 0.12-alt1
- 0.12

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.10-alt1
- 0.10

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.9-alt2
- rebuilt with dune-1.8

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.9-alt1
- first build for ALT

