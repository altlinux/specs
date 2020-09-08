%define ocamlmod ppx_expect
%set_verify_elf_method textrel=relaxed
Name: ocaml-%ocamlmod
Version: 0.14.0
Release: alt2
Summary: a cram like framework for OCaml
Group: Development/ML
License: MIT
Url: http://ounit.forge.ocamlcore.org/
# https://github.com/gildor478/ounit
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: ocaml-jane-street-headers-devel
BuildRequires: ocaml-compiler-libs-devel
BuildRequires: ocaml-ppx_inline_test-devel
BuildRequires: ocaml-ppx_here-devel
BuildRequires: ocaml-time_now-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_hash-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-sexplib0-devel
BuildRequires: dune

%description
Expect-test is a framework for writing tests in OCaml, similar to Cram.
Expect-tests mimic the existing inline tests framework with the let%%expect_test
construct. The body of an expect-test can contain output-generating code,
interleaved with %%expect extension expressions to denote the expected output.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
dune build @install

%install
dune install --destdir=%buildroot

# tests is broken in upstream
#%check
#dune runtest

%files
%doc LICENSE.md
%_libdir/ocaml/%{ocamlmod}*
%_libdir/ocaml/stublibs/*test_collector*.so
%exclude %_libdir/ocaml/%ocamlmod/*.a
%exclude %_libdir/ocaml/%ocamlmod/*.cmx
%exclude %_libdir/ocaml/%ocamlmod/*.cmxa
%exclude %_libdir/ocaml/%ocamlmod/*.mli
%exclude %_libdir/ocaml/%ocamlmod/*/*.a
%exclude %_libdir/ocaml/%ocamlmod/*/*.cmx
%exclude %_libdir/ocaml/%ocamlmod/*/*.cmxa
%exclude %_libdir/ocaml/%ocamlmod/*/*.mli

%files devel
%doc README.org CHANGES.md
%_libdir/ocaml/%ocamlmod/*.a
%_libdir/ocaml/%ocamlmod/*.cmxa
%_libdir/ocaml/%ocamlmod/*.cmx
%_libdir/ocaml/%ocamlmod/*.mli
%_libdir/ocaml/%ocamlmod/*/*.a
%_libdir/ocaml/%ocamlmod/*/*.cmx
%_libdir/ocaml/%ocamlmod/*/*.cmxa
%_libdir/ocaml/%ocamlmod/*/*.mli

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts have been moved from the main package

* Fri Sep 04 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- first build for ALT
