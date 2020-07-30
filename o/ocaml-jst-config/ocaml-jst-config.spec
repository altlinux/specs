%set_verify_elf_method textrel=relaxed
%define  modulename jst-config

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt1

Summary: Compile-time configuration for Jane Street libraries
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/jst-config

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-ppx_assert-devel ocaml-result-devel
BuildRequires: ocaml-ppxlib-devel ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ppx_compare-devel ocaml-ppx_here-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-compiler-libs-devel
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
%dir %_libdir/ocaml/%modulename
%_libdir/ocaml/%{modulename}*/META
%_libdir/ocaml/%{modulename}*/*.cma
%_libdir/ocaml/%{modulename}*/*.cmi
%_libdir/ocaml/%{modulename}*/*.cmxs

%files devel
%_libdir/ocaml/%{modulename}*/dune-package
%_libdir/ocaml/%{modulename}*/opam
%_libdir/ocaml/%{modulename}*/*.a
%_libdir/ocaml/%{modulename}*/*.cmt*
%_libdir/ocaml/%{modulename}*/*.cmxa
%_libdir/ocaml/%{modulename}*/*.cmx
%_libdir/ocaml/%{modulename}*/*.ml
%_libdir/ocaml/%{modulename}*/*.h
%_libdir/ocaml/%{modulename}*/rt-flags

%changelog
* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
