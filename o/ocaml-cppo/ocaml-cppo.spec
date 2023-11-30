%define libname cppo_ocamlbuild
Name: ocaml-cppo
Version: 1.6.9
Release: alt1
Summary: Equivalent of the C preprocessor for OCaml programs
License: BSD
Group: Development/ML
Url: http://mjambon.com/cppo.html
# https://github.com/mjambon/cppo
Source0: %name-%version.tar
BuildRequires: dune ocaml ocaml-ocamlbuild-devel ocaml-findlib

%description
Cppo is an equivalent of the C preprocessor targeted at the OCaml
language and its variants.

The main purpose of cppo is to provide a lightweight tool for simple
macro substitution (\#define) and file inclusion (\#include) for the
occasional case when this is useful in OCaml. Processing specific
sections of files by calling external programs is also possible via
\#ext directives.

The implementation of cppo relies on the standard library of OCaml and
on the standard parsing tools Ocamllex and Ocamlyacc, which contribute
to the robustness of cppo across OCaml versions.

%package -n ocaml-%libname
Summary: ocamlbuild support for cppo, OCaml-friendly source preprocessor
Group: Development/ML
%description -n ocaml-%libname
ocamlbuild support for cppo, OCaml-friendly source preprocessor

%package -n ocaml-%libname-devel
Summary: Development files for %name-ocamlbuild
Group: Development/ML
Requires: ocaml-%libname = %EVR
%description -n ocaml-%libname-devel
The %name-ocamlbuild-devel package contains libraries and signature files for
developing applications that use %name-ocamlbuild.

%prep
%setup 

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files
%doc LICENSE.md README.md
%_bindir/cppo
%_libdir/ocaml/cppo

%files -n ocaml-%libname -f ocaml-files.runtime
%exclude %_libdir/ocaml/cppo/META

%files -n ocaml-%libname-devel -f ocaml-files.devel
%exclude %_libdir/ocaml/cppo/opam
%exclude %_libdir/ocaml/cppo/dune-package

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 1.6.9-alt1
- 1.6.9

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Mon Mar 22 2021 Anton Farygin <rider@altlinux.org> 1.6.7-alt1
- 1.6.7

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.6.6-alt1
- 1.6.6

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.6.5-alt4
- rebuilt with dune-1.8

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 1.6.5-alt3
- added findlib META and opam files

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 1.6.5-alt2
- build cppo_ocamlbuild library
- build system changed to dune

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.6.4-alt2
- rebuilt with ocaml 4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.5.0-alt2
- rebuild with ocaml 4.04.2

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- first build for ALT

