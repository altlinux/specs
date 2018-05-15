%set_verify_elf_method textrel=relaxed
%define oname stdio
Name: ocaml-%oname
Version: 0.11.0
Release: alt1%ubt
Summary: Standard IO library for OCaml
License: Apache 2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: jbuilder
BuildRequires: opam
BuildRequires: ocaml-base  >= 0.11
BuildRequires(pre): rpm-build-ubt

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
jbuilder build --verbose -p %oname

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install
rm -rf %buildroot/usr/doc

%check
jbuilder runtest

%files
%doc README.org LICENSE.txt
%dir %_libdir/ocaml/%oname
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmxs

%files devel
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/*.cmt
%_libdir/ocaml/%oname/*.cmti
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.ml
%_libdir/ocaml/%oname/*.ml-gen
%_libdir/ocaml/%oname/*.mli

%changelog
* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1%ubt
- first build for ALT, based on Mageia spec

