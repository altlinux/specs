Name: ocaml-cppo
Version: 1.4.1
Release: alt1%ubt
Summary: Equivalent of the C preprocessor for OCaml programs
License: BSD
Group: Development/ML
Url: http://mjambon.com/cppo.html
# https://github.com/mjambon/cppo
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-findlib
BuildRequires(pre): rpm-build-ubt
BuildArch: noarch

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
install -d %buildroot%_bindir
install -p cppo %buildroot%_bindir/cppo

%files
%doc LICENSE README.md Changes
%_bindir/cppo

%changelog
* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1%ubt
- first build for ALT

