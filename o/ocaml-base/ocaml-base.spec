%set_verify_elf_method textrel=relaxed
%define oname base
Name: ocaml-%oname
Version: 0.11.0
Release: alt1%ubt
Summary: Full standard library replacement for OCaml
License: Apache 2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: jbuilder
BuildRequires: opam
BuildRequires: ocaml-sexplib0-devel  >= 0.11
BuildRequires(pre): rpm-build-ubt

%description
Base is a complete and portable alternative to the OCaml standard
library. It provides all standard functionalities one would expect
from a language standard library. It uses consistent conventions
across all of its module.

Base aims to be usable in any context. As a result system dependent
features such as I/O are not offered by Base. They are instead
provided by companion libraries such as stdio.

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
jbuilder build --verbose -p %oname %_smp_mflags

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml %oname.install
rm -rf %buildroot/usr/doc

%check
jbuilder runtest

%files
%doc README.org LICENSE.txt
%dir %_libdir/ocaml/%oname
%dir %_libdir/ocaml/%oname/md5
%dir %_libdir/ocaml/%oname/caml
%dir %_libdir/ocaml/%oname/shadow_stdlib
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmxs
%_libdir/ocaml/%oname/*/*.cmi
%_libdir/ocaml/%oname/*/*.cma
%_libdir/ocaml/%oname/*/*.a
%_libdir/ocaml/%oname/*/*.cmxa
%_libdir/ocaml/%oname/*/*.cmxs
%_libdir/ocaml/stublibs/dllbase_stubs.so
%_libdir/ocaml/%oname/runtime.js

%files devel
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/*.cmt
%_libdir/ocaml/%oname/*.cmti
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.ml
%_libdir/ocaml/%oname/*.ml-gen
%_libdir/ocaml/%oname/*.mli
%_libdir/ocaml/%oname/*/*.cmt
%_libdir/ocaml/%oname/*/*.cmti
%_libdir/ocaml/%oname/*/*.cmx
%_libdir/ocaml/%oname/*/*.ml
%_libdir/ocaml/%oname/*/*.mli
%_libdir/ocaml/%oname/internalhash.h

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1%ubt
- first build for Sisyphus, based on specfile from Mageia 

