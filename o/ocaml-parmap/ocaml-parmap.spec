%set_verify_elf_method textrel=relaxed
Name: ocaml-parmap
Version: 1.1.1
Release: alt2
Summary: small OCaml library allowing to exploit multicore architectures
Group: Development/ML
License: LGPLv2+ with exceptions

Url: http://rdicosmo.github.io/parmap/
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: dune
BuildRequires(pre): rpm-build-ocaml

%description
Parmap is a minimalistic library allowing to exploit multicore
architectures for OCaml programs with minimal modifications.

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
make

%install
dune install --destdir=%buildroot

%check
# `dune runtests' actually are very CPU intensive benchmarks ('scale' tests),
# and we don't need to run benchmarks for integration testing. Run single and
# fastest test just to be sure parmap is working at all.
dune exec tests/simplescalefold.exe

%files
%doc CHANGES README.md
%doc LICENSE
%_libdir/ocaml/parmap/*.cmi
%_libdir/ocaml/parmap/*.cma
%_libdir/ocaml/parmap/*.cmxs
%_libdir/ocaml/stublibs/dllparmap_stubs.so*

%files devel
%doc LICENSE
%_libdir/ocaml/parmap/META
%_libdir/ocaml/parmap/opam
%_libdir/ocaml/parmap/dune-package
%_libdir/ocaml/parmap/*.a
%_libdir/ocaml/parmap/*.cmxa
%_libdir/ocaml/parmap/*.cmti
%_libdir/ocaml/parmap/*.cmt
%_libdir/ocaml/parmap/*.cmx
%_libdir/ocaml/parmap/*.mli
%_libdir/ocaml/parmap/*.ml

%changelog
* Thu May 14 2020 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt2
- spec: Fix beekeeper rebuild kill by removing benchmark tests in %%check.

* Fri Feb 07 2020 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 1.0-alt3.rc10
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.rc10
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt1.rc10
- up to 1.0-rc10
- rebuilt with ocaml 4.07

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1.rc9
- First build of ocaml-parmap for ALT.

