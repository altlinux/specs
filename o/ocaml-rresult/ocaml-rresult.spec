%define libname rresult
Name:           ocaml-%libname
Version:        0.7.0
Release:        alt1
Summary:        Result value combinators for OCaml
License:        ISC
Group:          Development/ML
Url:            http://erratique.ch/software/rresult
# https://github.com/dbuenzli/rresult
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Rresult is an OCaml module for handling computation results and errors in an explicit
and declarative manner, without resorting to exceptions. It defines combinators to
operate on the result type available from OCaml 4.03 in the standard library.

Rresult depends on the compatibility result package and is distributed under the ISC license.

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
* Mon Jan 03 2022 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 0.6.0-alt3
- added ocaml-result to BR

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 0.6.0-alt2
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- first build for ALT

