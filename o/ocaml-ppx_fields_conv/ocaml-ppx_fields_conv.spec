%set_verify_elf_method textrel=relaxed
%define  modulename ppx_fields_conv

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt2

Summary: Generation of accessor and iteration functions for ocaml records
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_fields_conv

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-fieldslib-devel ocaml-ppxlib-devel
BuildRequires: ocaml-compiler-libs-devel ocaml-migrate-parsetree-devel
BuildRequires: ocaml-result-devel ocaml-base-devel
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
dune build -p %modulename

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
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- built as release (dune build -p) against incomplete dependencies
  in devel package

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
