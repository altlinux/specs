%define libname csexp
%def_without check

Name:           ocaml-%libname
Version:        1.5.2
Release:        alt1
Summary:        Canonical S-expressions for OCaml
License:        MIT
Group:          Development/ML
Url:            https://github.com/ocaml-dune/csexp
Source: %name-%version.tar

BuildRequires: ocaml dune rpm-build-ocaml
%if_with check
BuildRequires: ocaml-ppx_expect-devel
%endif

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
This library provides minimal support for Canonical S-expressions [1]. Canonical
S-expressions are a binary encoding of S-expressions that is super simple and
well suited for communication between programs.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup -q

%build
sed '3 i (version %version)' dune-project
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 02 2023 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 1.5.1-alt2
- disabled test for bootstrap ocaml 4.13

* Sat Apr 10 2021 Anton Farygin <rider@altlinux.org> 1.5.1-alt1
- 1.5.1

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 1.4.0-alt2
- temporarily disabled tests

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Oct 13 2020 Anton Farygin <rider@altlinux.ru> 1.3.2-alt2
- temporarily disabled tests

* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Thu Sep 03 2020 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- first build for ALT
