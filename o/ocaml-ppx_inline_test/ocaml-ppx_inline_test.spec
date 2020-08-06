%define ocamlmod ppx_inline_test
%set_verify_elf_method textrel=relaxed
Name: ocaml-%ocamlmod
Version: 0.14.0
Release: alt1
Summary: Syntax extension for writing in-line tests in ocaml code
Group: Development/ML
License: MIT
Url: http://ounit.forge.ocamlcore.org/
# https://github.com/gildor478/ounit
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-jane-street-headers-devel
BuildRequires: ocaml-compiler-libs-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_hash-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-time_now-devel
BuildRequires: ocaml-base-devel
BuildRequires: dune

%description
Syntax extension for writing in-line tests in ocaml code.
Part of the Jane Street's PPX rewriters collection.

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
%_libdir/ocaml/stublibs/*%{ocamlmod}*.so
%exclude %_libdir/ocaml/%ocamlmod/*.a
%exclude %_libdir/ocaml/%ocamlmod/*.cmxa
%exclude %_libdir/ocaml/%ocamlmod/*.mli

%files devel
%doc README.md CHANGES.md
%_libdir/ocaml/%ocamlmod/*.a
%_libdir/ocaml/%ocamlmod/*.cmxa
%_libdir/ocaml/%ocamlmod/*.mli

%changelog
* Thu Aug 06 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- first build for ALT

