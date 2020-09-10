%set_verify_elf_method textrel=relaxed
%define oname base
Name: ocaml-%oname
Version: 0.14.0
Release: alt2
Summary: Full standard library replacement for OCaml
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune-devel
BuildRequires: ocaml-sexplib0-devel  >= 0.12

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
dune build --verbose -p %oname %_smp_mflags

%install
dune install --destdir=%buildroot

%check
dune runtest

%files
%doc README.org LICENSE.md
%dir %_libdir/ocaml/%oname
%dir %_libdir/ocaml/%oname/md5
%dir %_libdir/ocaml/%oname/caml
%dir %_libdir/ocaml/%oname/shadow_stdlib
%dir %_libdir/ocaml/%oname/base_internalhash_types
%_libdir/ocaml/%oname/META
%_libdir/ocaml/%oname/*.cmi
%_libdir/ocaml/%oname/*.cma
%_libdir/ocaml/%oname/*.cmxs
%_libdir/ocaml/%oname/*/*.cmi
%_libdir/ocaml/%oname/*/*.cma
%_libdir/ocaml/%oname/*/*.cmxs
%_libdir/ocaml/stublibs/dllbase_stubs.so
%_libdir/ocaml/stublibs/dllbase_internalhash_types_stubs.so
%_libdir/ocaml/%oname/runtime.js
%_libdir/ocaml/%oname/base_internalhash_types/runtime.js

%files devel
%_libdir/ocaml/%oname/opam
%_libdir/ocaml/%oname/dune-package
%_libdir/ocaml/%oname/*.cmt
%_libdir/ocaml/%oname/*.a
%_libdir/ocaml/%oname/*.cmxa
%_libdir/ocaml/%oname/*.cmti
%_libdir/ocaml/%oname/*.cmx
%_libdir/ocaml/%oname/*.ml
%_libdir/ocaml/%oname/*.mli
%_libdir/ocaml/%oname/*/*.cmt
%_libdir/ocaml/%oname/*/*.cmti
%_libdir/ocaml/%oname/*/*.cmx
%_libdir/ocaml/%oname/*/*.a
%_libdir/ocaml/%oname/*/*.cmxa
%_libdir/ocaml/%oname/*/*.ml
%_libdir/ocaml/%oname/*/*.mli
%_libdir/ocaml/%oname/base_internalhash_types/internalhash.h

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts moved to ocaml-base-devel package

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Sat Feb 22 2020 Anton Farygin <rider@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt3
- fixed build with dune 1.4

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for Sisyphus, based on specfile from Mageia 

