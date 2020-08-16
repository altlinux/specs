%set_verify_elf_method textrel=relaxed
%define  modulename ppx_assert

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt1

Summary: Assert-like extension nodes that raise useful errors on failure
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_assert

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-ppxlib-devel ocaml-ppx_cold-devel ocaml-result-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-ppx_compare-devel
BuildRequires: ocaml-compiler-libs-devel ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ppx_here-devel
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -n %modulename-%version

%build
dune build

%install
dune install --destdir=%buildroot

%check
dune runtest

%files
%doc README.md
%dir %_libdir/ocaml/%modulename
%_libdir/ocaml/%{modulename}*/META
%_libdir/ocaml/%{modulename}*/*.cma
%_libdir/ocaml/%{modulename}*/*.cmi
%_libdir/ocaml/%{modulename}*/*.cmxs
%dir %_libdir/ocaml/%modulename/runtime-lib
%_libdir/ocaml/%{modulename}/runtime-lib/*.cma
%_libdir/ocaml/%{modulename}/runtime-lib/*.cmi
%_libdir/ocaml/%{modulename}/runtime-lib/*.cmxs

%files devel
%_libdir/ocaml/%{modulename}*/dune-package
%_libdir/ocaml/%{modulename}*/opam
%_libdir/ocaml/%{modulename}*/*.a
%_libdir/ocaml/%{modulename}*/*.cmt*
%_libdir/ocaml/%{modulename}*/*.cmxa
%_libdir/ocaml/%{modulename}*/*.cmx
%_libdir/ocaml/%{modulename}*/*.mli
%_libdir/ocaml/%{modulename}*/*.ml
%_libdir/ocaml/%{modulename}*/*.exe
%_libdir/ocaml/%{modulename}/runtime-lib/*.a
%_libdir/ocaml/%{modulename}/runtime-lib/*.cmt*
%_libdir/ocaml/%{modulename}/runtime-lib/*.cmxa
%_libdir/ocaml/%{modulename}/runtime-lib/*.cmx
%_libdir/ocaml/%{modulename}/runtime-lib/*.ml
%_libdir/ocaml/%{modulename}/runtime-lib/*.mli

%changelog
* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
