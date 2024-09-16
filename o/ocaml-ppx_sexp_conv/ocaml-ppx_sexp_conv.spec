%define libname ppx_sexp_conv
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Generation of S-expression conversion functions from type definitions
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/ppx_sexp_conv
VCS: https://github.com/janestreet/ppx_sexp_conv
Source0: %name-%version.tar
BuildRequires: dune 
BuildRequires: ocaml-sexplib0-devel
BuildRequires: ocaml-ppxlib-devel >= %version
BuildRequires: ocaml-base-devel >= %version
BuildRequires: ocaml-ppxlib_jane >= %version

%description
ppx_sexp_conv is a PPX syntax extension that generates code for converting OCaml
types to and from s-expressions, as defined in the =sexplib= library.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.org LICENSE.md CHANGES.md


%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.3-alt1
- 0.14.3
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- built as release (dune build -p) against incomplete dependencies
  in devel package

* Wed Jun 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Mon Mar 02 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt2
- added ocaml-compiler-libs-devel to Build Requires

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.11.2-alt2
- rebuilt with ocaml-ppxlib 0.5.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.2-alt1
- first build for ALT


