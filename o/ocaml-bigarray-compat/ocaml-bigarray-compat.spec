%set_verify_elf_method textrel=relaxed
%define  modulename bigarray-compat

Name:    ocaml-%modulename
Version: 1.0.0
Release: alt1
Summary: Compatibility library to use Stdlib.Bigarray when possible
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/bigarray-compat
BuildRequires: dune
BuildPreReq: rpm-build-ocaml >= 1.1
Source:  %name-%version.tar

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
dune build -p %{modulename} --verbose

%install
dune install -p %{modulename} --destdir=%buildroot

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
%_libdir/ocaml/%{modulename}*/*.ml

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for ALT

