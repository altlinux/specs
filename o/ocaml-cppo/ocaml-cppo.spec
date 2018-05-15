%set_verify_elf_method textrel=relaxed
Name: ocaml-cppo
Version: 1.6.4
Release: alt1%ubt
Summary: Equivalent of the C preprocessor for OCaml programs
License: BSD
Group: Development/ML
Url: http://mjambon.com/cppo.html
# https://github.com/mjambon/cppo
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-findlib jbuilder opam ocaml-ocamlbuild
BuildRequires(pre): rpm-build-ubt

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

%prep
%setup 
%build
make all

%install
mkdir -p %buildroot%prefix %buildroot%_libdir/ocaml
jbuilder install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md README.md Changes
%_bindir/cppo

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1%ubt
- 1.6.4

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.5.0-alt2%ubt
- rebuild with ocaml 4.04.2

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1%ubt
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2%ubt
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1%ubt
- first build for ALT

