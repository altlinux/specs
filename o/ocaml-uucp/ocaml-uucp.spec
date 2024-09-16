%define libname uucp
Name: ocaml-%libname
Version: 16.0.0
Release: alt1
Summary: Unicode character properties for OCaml
License: ISC
Group: Development/ML
Url: https://erratique.ch/software/uucp
VCS: https://github.com/dbuenzli/uucp
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.14.0
BuildRequires: opam
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-compiler-libs
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-topkg-devel
BuildRequires: ocaml-uucd-devel >= 15.1.0
BuildRequires: ocaml-uunf-devel >= 15.1.0
BuildRequires(pre): rpm-build-ocaml >= 1.6

%description
Uucp is an OCaml library providing efficient access to a selection of
character properties of the Unicode character database
(http://www.unicode.org/reports/tr44/).

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
ocaml pkg/pkg.ml build --dev-pkg false  --with-uunf true  --with-cmdliner true --tests true

%install
sed -i 's,%%%%VERSION%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md
%_bindir/ucharinfo

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 16.0.0-alt1
- 16.0.0

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 15.1.0-alt1
- first build for ALT
