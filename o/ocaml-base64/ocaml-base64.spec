%set_verify_elf_method textrel=relaxed
%define  modulename base64

Name:    ocaml-%modulename
Version: 3.4.0
Release: alt1
Summary: Base64 encoding for OCaml
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-base64
Source:  %name-%version.tar

BuildRequires: dune 
BuildRequires: ocaml-bos-devel
BuildRequires: ocaml-rresult-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-result-devel
BuildPreReq: rpm-build-ocaml >= 1.1


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
%setup

%build
dune build -p %modulename

%install
dune install --destdir=%buildroot

%check
dune runtest

%files
%doc README.md
%dir %_libdir/ocaml/%modulename
%dir %_libdir/ocaml/%modulename/rfc2045
%_libdir/ocaml/%{modulename}*/META
%_libdir/ocaml/%{modulename}*/*.cma
%_libdir/ocaml/%{modulename}*/*.cmi
%_libdir/ocaml/%{modulename}*/*.cmxs
%_libdir/ocaml/%{modulename}*/*/*.cma
%_libdir/ocaml/%{modulename}*/*/*.cmi
%_libdir/ocaml/%{modulename}*/*/*.cmxs

%files devel
%_libdir/ocaml/%{modulename}*/dune-package
%_libdir/ocaml/%{modulename}*/opam
%_libdir/ocaml/%{modulename}*/*.a
%_libdir/ocaml/%{modulename}*/*.cmt*
%_libdir/ocaml/%{modulename}*/*.cmxa
%_libdir/ocaml/%{modulename}*/*.cmx
%_libdir/ocaml/%{modulename}*/*.mli
%_libdir/ocaml/%{modulename}*/*.ml
%_libdir/ocaml/%{modulename}*/*/*.a
%_libdir/ocaml/%{modulename}*/*/*.cmt*
%_libdir/ocaml/%{modulename}*/*/*.cmxa
%_libdir/ocaml/%{modulename}*/*/*.cmx
%_libdir/ocaml/%{modulename}*/*/*.mli
%_libdir/ocaml/%{modulename}*/*/*.ml

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 3.4.0-alt1
- first build for ALT
