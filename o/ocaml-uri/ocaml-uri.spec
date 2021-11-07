%define libname uri
Name: ocaml-%libname
Version: 4.2.0
Release: alt1
Summary: An RFC3986 URI/URL parsing library for OCaml
Group: Development/ML
License: BSD
Url: https://github.com/ocaml-ppx/ppx_derivers
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune >= 1.8
BuildRequires: ocaml
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-angstrom-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-stringext-devel
BuildRequires: ocaml-migrate-parsetree-devel

%description
his is an OCaml implementation of the RFC3986 specification for parsing URI
or URLs.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
sed -si 's,oUnit,ounit2,' lib_test/dune
%dune_build --release @install

%install
%dune_install

# Makes *.cmxs executable such that they will be stripped.
find %buildroot -name '*.cmxs' -exec chmod 0755 {} \;

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Tue Mar 23 2021 Anton Farygin <rider@altlinux.org> 4.1.0-alt1
- 4.1.0
- cleanup spec

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 3.1.0-alt2
- enabled sexp variant

* Sat Feb 01 2020 Anton Farygin <rider@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- first build for ALT

