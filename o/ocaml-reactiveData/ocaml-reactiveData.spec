%set_verify_elf_method textrel=relaxed
%define libname reactiveData
Name:           ocaml-%libname
Version:        0.2.2
Release:        alt1
Summary:        Functional reactive programming with incremental changes in data structures
License:        LGPLv3 with OCaml linking exception
Group:          Development/ML
Url:            https://github.com/ocsigen/reactiveData
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-react

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
ReactiveData is an OCaml module for functional reactive programming (FRP) based on React.
It adds support to incremental changes in data structures by reasoning on patches instead of absolute values.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q

%build
ocaml pkg/build.ml native=true native-dynlink=true

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE CHANGES README.md
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
* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- first build for ALT

