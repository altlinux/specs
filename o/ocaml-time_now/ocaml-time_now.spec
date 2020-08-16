%set_verify_elf_method textrel=relaxed
%define  modulename time_now

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt1

Summary: Reports the current time
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/time_now

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-jane-street-headers-devel ocaml-jst-config-devel
BuildRequires: ocaml-ppx_base-devel ocaml-ppx_optcomp-devel
BuildRequires: ocaml-ppx_js_style-devel ocaml-ppx_hash-devel
BuildRequires: ocaml-ppx_enumerate-devel ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_cold-devel ocaml-compiler-libs-devel
BuildRequires: ocaml-migrate-parsetree-devel ocaml-ppx_compare-devel
BuildRequires: ocaml-ppxlib-devel ocaml-result-devel
BuildRequires: ocaml-octavius-devel
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
%_libdir/ocaml/%{modulename}*/runtime.js
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/%{modulename}*/dune-package
%_libdir/ocaml/%{modulename}*/opam
%_libdir/ocaml/%{modulename}*/*.a
%_libdir/ocaml/%{modulename}*/*.cmt*
%_libdir/ocaml/%{modulename}*/*.cmxa
%_libdir/ocaml/%{modulename}*/*.cmx
%_libdir/ocaml/%{modulename}*/*.mli
%_libdir/ocaml/%{modulename}*/*.ml

%changelog
* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
