%define  modulename version
%def_with check

Name:    ocaml-%modulename
Version: 3.6.8
Release: alt1
Summary: Manipulate, parse and generate OCaml compiler version strings
License: ISC
Group:   Development/ML
URL:     https://github.com/ocurrent/ocaml-version
VCS: https://github.com/ocurrent/ocaml-version
BuildRequires: dune ocaml-alcotest-devel ocaml-odoc-devel
Source:  %name-%version.tar

%description
This library provides facilities to parse version numbers of the OCaml compiler,
and enumerates the various official OCaml releases and configuration variants.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 3.6.8-alt1
- 3.6.2 -> 3.6.8

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 3.6.2-alt1
- first build for ALT
