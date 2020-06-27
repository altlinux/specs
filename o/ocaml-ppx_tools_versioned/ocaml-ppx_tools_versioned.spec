%set_verify_elf_method textrel=relaxed

%define oname ppx_tools_versioned
Name: ocaml-%oname
Version: 5.4.0
Release: alt1
Summary: Tools for authors of ppx rewriters and other syntactic tools
License: MIT
Group: Development/ML
Url: https://opam.ocaml.org/packages/ppx_tools_versioned/
# https://github.com/let-def/ppx_tools_versioned
Source0: %name-%version.tar
BuildRequires: ocaml-findlib ocaml-migrate-parsetree-devel ocaml-result-devel opam dune

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
make all

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.md
%dir %_libdir/ocaml/%oname
%_libdir/ocaml/%oname/dune-package
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmxs
%_libdir/ocaml/%oname/metaquot_402
%_libdir/ocaml/%oname/metaquot_403
%_libdir/ocaml/%oname/metaquot_404
%_libdir/ocaml/%oname/metaquot_405
%_libdir/ocaml/%oname/metaquot_406
%_libdir/ocaml/%oname/metaquot_407
%_libdir/ocaml/%oname/metaquot_408
%_libdir/ocaml/%oname/metaquot_409
%_libdir/ocaml/%oname/metaquot_410
%_libdir/ocaml/%oname/metaquot_411

%files devel
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.cmt*
%_libdir/ocaml/%oname/*.mli
%_libdir/ocaml/%oname/*.ml

%changelog
* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 5.4.0-alt1
- 5.4.0

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- 5.3.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 5.2.3-alt2
- built by dune

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 5.2.3-alt1
- 5.2.3

* Thu Jun 06 2019 Anton Farygin <rider@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 5.2.1-alt3
- rebuild with ocaml-migrate-parsetree 1.2.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- first build for ALT, based on specfile from Mageia

