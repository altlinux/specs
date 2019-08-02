%set_verify_elf_method textrel=relaxed
%define libname astring
Name:           ocaml-%libname
Version:        0.8.5
Release:        alt1
Summary:        Alternative String module for OCaml
License:        ISC
Group:          Development/ML
Url:            http://erratique.ch/software/astring
# https://github.com/dbuenzli/astring
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Astring exposes an alternative String module for OCaml. This module tries to 
balance minimality and expressiveness for basic, index-free, string processing
and provides types and functions for substrings, string sets and string maps.

Remaining compatible with the OCaml String module is a non-goal. The String module
exposed by Astring has exception safe functions, removes deprecated and rarely used
functions, alters some signatures and names, adds a few missing functions and
fully exploits OCaml's newfound string immutability.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Thu Sep 03 2020 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Wed Aug 05 2020 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.8.3-alt2
- rebuilt with ocaml 4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.8.3-alt1
- first build for ALT

