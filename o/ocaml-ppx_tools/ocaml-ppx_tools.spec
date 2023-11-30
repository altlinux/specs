%define libname ppx_tools
Name: ocaml-%libname
Version: 6.6
Release: alt1
Summary: Tools for authors of ppx rewriters and other syntactic tools
License: MIT
Group: Development/ML
Url: https://github.com/alainfrisch/ppx_tools
Source0: %name-%version.tar
BuildRequires: dune ocaml-cppo ocaml

%description
Tools for authors of syntactic tools (such as ppx rewriters).

This package is licensed by LexiFi under the terms of the MIT license.

The tools are installed as a findlib package called 'ppx_tools'.
Executables are thus accessible through the ocamlfind driver
(e.g.: ocamlfind ppx_tools/dumpast).

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
%dune_build --release @install

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md
%_libdir/ocaml/%libname/dumpast
%_libdir/ocaml/%libname/genlifter
%_libdir/ocaml/%libname/ppx_metaquot
%_libdir/ocaml/%libname/rewriter

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 6.6-alt1
- 6.5 -> 6.6

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 6.5-alt1
- 6.4 - 6.5

* Mon Aug 09 2021 Anton Farygin <rider@altlinux.ru> 6.4-alt1
- 6.4

* Thu Dec 31 2020 Anton Farygin <rider@altlinux.ru> 6.3-alt1
- 6.3

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 6.2-alt1
- 6.2

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 6.1-alt1
- 6.1

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 5.3-alt1
- 5.3

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- first build for ALT

