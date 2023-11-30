%define libname fmt
Name:           ocaml-%libname
Version:        0.9.0
Release:        alt2
Summary:        OCaml Format pretty-printer combinators
License:        ISC
Group:          Development/ML
Url: https://erratique.ch/software/fmt
VCS: https://github.com/dbuenzli/fmt
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

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.9.0-alt2
- added support for bytecode-only version of the ocaml package

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0

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

