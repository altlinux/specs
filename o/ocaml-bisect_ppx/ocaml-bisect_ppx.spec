%define libname bisect_ppx
Name: ocaml-%libname
Version: 2.8.3
Release: alt1
Summary: Code coverage for OCaml
Group: Development/ML
License: MPL-2.0
Url: https://github.com/aantron/bisect_ppx
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.07.1
BuildRequires: dune
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-cmdliner-devel

%description
Bisect_ppx helps you test thoroughly. It is a small preprocessor that inserts
instrumentation at places in your code, such as if-then-else and match
expressions. After you run tests, Bisect_ppx gives a nice HTML report
showing which places were visited and which were missed.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-ocamlbuild

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md LICENSE.md
%_bindir/bisect-ppx-report


%files devel -f ocaml-files.devel

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 2.8.3-alt1
- 2.8.1 -> 2.8.3

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 2.8.1-alt1
- 2.7.1 -> 2.8.1

* Fri Feb 04 2022 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Sun Nov 28 2021 Anton Farygin <rider@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Fri Aug 06 2021 Anton Farygin <rider@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu May 13 2021 Anton Farygin <rider@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Jan 15 2021 Anton Farygin <rider@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Mon Sep 21 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt2
- migrated to rpm-build-ocaml 1.4

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuilt with ocaml-4.08

* Fri Jun 07 2019 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.4.0-alt2
- rebuilt with dune-1.8

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- first build for ALT


