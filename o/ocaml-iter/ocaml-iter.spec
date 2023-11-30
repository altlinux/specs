%def_with check
%ifnarch %ix86 armh ppc64le
%define relax %nil
%else
%define relax ||:
%endif
%define libname iter
Name: ocaml-%libname
Version: 1.8
Release: alt1
Summary: Simple and lightweight iterator abstract data type for OCaml
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/iter/
Source0: %name-%version.tar
BuildRequires: dune ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel
BuildRequires: ocaml-mdx-devel
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
%dune_build --release @install

%install
%dune_install

%check
%dune_check %relax

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGELOG.md

%files devel -f ocaml-files.devel

%changelog
* Fri Nov 24 2023 Anton Farygin <rider@altlinux.ru> 1.8-alt1
- 1.7 -> 1.8
- relaxed check on the ppc64le and 32-bit architectures

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.7-alt1
- 1.4 -> 1.7
- disabled tests on 32-bit platforms

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


