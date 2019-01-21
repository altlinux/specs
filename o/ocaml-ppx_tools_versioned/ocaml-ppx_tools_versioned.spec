%set_verify_elf_method textrel=relaxed

%define oname ppx_tools_versioned
Name: ocaml-%oname
Version: 5.2.1
Release: alt3
Summary: Tools for authors of ppx rewriters and other syntactic tools
License: MIT
Group: Development/ML
Url: https://opam.ocaml.org/packages/ppx_tools_versioned/
# https://github.com/let-def/ppx_tools_versioned
Source0: %name-%version.tar
BuildRequires: ocaml-findlib ocaml-migrate-parsetree-devel ocaml-result-devel jbuilder opam

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
mkdir -p %buildroot/%_libdir/ocaml
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install


%files
%doc README.md
%dir %_libdir/ocaml/%oname
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

%files devel
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.cmt*
%_libdir/ocaml/%oname/*.mli
%_libdir/ocaml/%oname/*.ml

%changelog
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 5.2.1-alt3
- rebuild with ocaml-migrate-parsetree 1.2.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 5.1-alt1
- first build for ALT, based on specfile from Mageia

