%set_verify_elf_method textrel=relaxed
%define libname gen
Name: ocaml-%libname
Version: 0.5.2
Release: alt1
Summary: Simple and efficient iterators (modules Gen and GenLabels).
License: BSD
Group: Development/ML
Url: https://github.com/c-cube/sequence/
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel

%description
%name provides additional modules GenClone and GenMList for lower-level control
over persistency and duplication of iterators.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.md LICENSE CHANGELOG.md
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.cmt*
%exclude %_libdir/ocaml/%libname/*.ml
%exclude %_libdir/ocaml/%libname/*.mli
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmxs


%files devel
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.ml
%_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs

%changelog
* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- first build for ALT


