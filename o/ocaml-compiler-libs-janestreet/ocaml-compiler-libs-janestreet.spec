%define libname ocaml-compiler-libs
Name: ocaml-compiler-libs-janestreet
Version: 0.17.0
Release: alt1
Summary: OCaml compiler libraries repackaged
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/ocaml-compiler-libs
Source0: %name-%version.tar
BuildRequires: dune ocaml
BuildRequires: ocaml-compiler-libs
Obsoletes: ocaml-compiler-libs <= 0.12.4-alt2

%description
This packages exposes the OCaml compiler libraries repackages under the toplevel
names Ocaml_common, Ocaml_bytecomp, ...

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Obsoletes: ocaml-compiler-libs-devel <= 0.12.4-alt2

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
%doc README.org

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.12.4 -> 0.17.0
- renamed to ocaml-compiler-libs-janestreet

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.12.4-alt2
- fixed buildrequires 

* Mon Sep 06 2021 Anton Farygin <rider@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Mon Sep 28 2020 Anton Farygin <rider@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.12.1-alt2
- built using --release option

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with dune-1.8 

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


