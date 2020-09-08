%set_verify_elf_method textrel=relaxed
%define oname stdio
Name: ocaml-%oname
Version: 0.14.0
Release: alt2
Summary: Standard IO library for OCaml
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: dune >= 1.8
BuildRequires: opam
BuildRequires: ocaml-base  >= 0.14

%description
Stdio implements simple input/output functionalities for OCaml.

It re-exports the input/output functions of the OCaml standard
libraries using a more consistent API.

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
dune build --verbose -p %oname

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install
rm -rf %buildroot/usr/doc

%check
dune runtest

%files
%doc README.org LICENSE.md
%dir %_libdir/ocaml/%oname
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.cmxs

%files devel
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/*.cmt
%_libdir/ocaml/%oname/*.cmti
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.ml
%_libdir/ocaml/%oname/*.mli
%_libdir/ocaml/%oname/dune-package

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts moved to the ocaml-stdio-devel package

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt4
- fixed install with dune 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with ocaml 4.07

* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT, based on Mageia spec

