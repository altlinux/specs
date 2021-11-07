%define libname fmt
Name:           ocaml-%libname
Version:        0.8.10
Release:        alt1
Summary:        OCaml Format pretty-printer combinators
License:        ISC
Group:          Development/ML
Url:            http://erratique.ch/software/fmt
# https://github.com/dbuenzli/fmt
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-cmdliner

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Fmt exposes combinators to devise Format pretty-printing functions.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q
%patch0 -p1

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
* Tue Oct 12 2021 Anton Farygin <rider@altlinux.ru> 0.8.10-alt1
- 0.8.10

* Thu Dec 31 2020 Anton Farygin <rider@altlinux.ru> 0.8.9-alt1
- 0.8.9

* Mon Jan 27 2020 Anton Farygin <rider@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- first build for ALT

