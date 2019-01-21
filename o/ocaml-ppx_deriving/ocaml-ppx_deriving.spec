%set_verify_elf_method textrel=relaxed
%define libname ppx_deriving
Name: ocaml-%libname
Version: 4.2.1
Release: alt2
Summary: Type-driven code generation for OCaml >=4.02
License: MIT
Group: Development/ML
Url: https://github.com/alainfrisch/ppx_deriving
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-findlib-devel ocaml-ocamlbuild ocaml-migrate-parsetree-devel ocaml-ppx_tools-devel ocaml-result-devel ocaml-cppo_ocamlbuild-devel
BuildRequires: ocaml-ppx_derivers-devel opam dune ocaml-ounit-devel ocaml-cppo

%description
ppx_deriving provides common infrastructure for generating code based on type
definitions, and a set of useful plugins for common tasks.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
sed -i 's,%%{version}%%,%version,g' pkg/META.in
make build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %libname.install

%files
%doc README.md LICENSE.txt CHANGELOG.md
%dir %_libdir/ocaml/%libname
%dir %_libexecdir/ppx_deriving
%_libexecdir/ppx_deriving/ppx_deriving
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.mli

%changelog
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.2.1-alt2
- rebuilt with ocaml-migrate-parsetree 1.2.0

* Tue Oct 30 2018 Anton Farygin <rider@altlinux.ru> 4.2.1-alt1
- first build for ALT

