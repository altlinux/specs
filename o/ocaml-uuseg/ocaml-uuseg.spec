%define libname uuseg
Name: ocaml-%libname
Version: 16.0.0
Release: alt3
Summary: Unicode text segmentation for OCaml
License: ISC
Group: Development/ML
Url: https://erratique.ch/software/uuseg
VCS: https://github.com/dbuenzli/uuseg
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.14.0
BuildRequires: opam
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-topkg-devel
BuildRequires: ocaml-uucp-devel >= 15.1.0
BuildRequires(pre): rpm-build-ocaml >= 1.6

%description
Uucp is an OCaml library providing efficient access to a selection of
character properties of the Unicode character database
(http://www.unicode.org/reports/tr44/).

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
# findreq can't find this dependency via cmt/cmti files on bytecode ocaml
Requires: ocaml-uucp-devel

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
ocaml pkg/pkg.ml build --dev-pkg false --with-cmdliner false

%install
sed -i 's,%%%%VERSION%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Jan 27 2025 Anton Farygin <rider@altlinux.ru> 16.0.0-alt3
- added ocaml-uucp-devel dependency to ocaml-uuseg-devel package

* Wed Jan 22 2025 Anton Farygin <rider@altlinux.ru> 16.0.0-alt2
- changed BR - use ocaml-findlib-devel instead of the ocaml-findlib

* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 16.0.0-alt1
- 16.0.0

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 15.1.0-alt1
- first build for ALT
