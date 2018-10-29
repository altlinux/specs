%set_verify_elf_method textrel=relaxed
%define libname cppo_ocamlbuild
Name: ocaml-cppo
Version: 1.6.5
Release: alt2
Summary: Equivalent of the C preprocessor for OCaml programs
License: BSD
Group: Development/ML
Url: http://mjambon.com/cppo.html
# https://github.com/mjambon/cppo
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-findlib dune opam ocaml-ocamlbuild

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
make all

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md README.md Changes
%_bindir/cppo

%files -n ocaml-%libname
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files -n ocaml-%libname-devel
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.dune
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/*.ml

%changelog
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

