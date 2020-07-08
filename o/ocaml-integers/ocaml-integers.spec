%set_verify_elf_method textrel=relaxed
%define  modulename integers

Name:    ocaml-%modulename
Version: 0.4.0
Release: alt1

Summary: Various signed and unsigned integer types for OCaml
License: MIT
Group:   Development/ML
URL:     https://github.com/ocamllabs/ocaml-integers

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune
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

%files
%doc README.md
%dir %_libdir/ocaml/%modulename
%_libdir/ocaml/%{modulename}*/META
%_libdir/ocaml/%{modulename}*/*.cma
%_libdir/ocaml/%{modulename}*/*.cmi
%_libdir/ocaml/%{modulename}*/*.cmxs
%_libdir/ocaml/stublibs/*.so
%dir %_libdir/ocaml/%modulename/top
%_libdir/ocaml/%{modulename}*/top/*.cmi
%_libdir/ocaml/%{modulename}*/top/*.cma

%files devel
%_libdir/ocaml/%{modulename}*/dune-package
%_libdir/ocaml/%{modulename}*/opam
%_libdir/ocaml/%{modulename}*/*.a
%_libdir/ocaml/%{modulename}*/*.cmt*
%_libdir/ocaml/%{modulename}*/*.cmxa
%_libdir/ocaml/%{modulename}*/*.cmx
%_libdir/ocaml/%{modulename}*/*.mli
%_libdir/ocaml/%{modulename}*/*.ml
%_libdir/ocaml/%{modulename}*/*.h
%_libdir/ocaml/%{modulename}*/top/*.cmt*
%_libdir/ocaml/%{modulename}*/top/*.mli
%_libdir/ocaml/%{modulename}*/top/*.ml

%changelog
* Fri Jul 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
