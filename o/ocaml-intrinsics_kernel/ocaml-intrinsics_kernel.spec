%define oname  ocaml_intrinsics_kernel
Name: ocaml-intrinsics_kernel
Version: 0.17.1
Release: alt1
Summary: a library of intrinsics for OCaml
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml >= 5.2.0
BuildRequires: dune

%description
Provides functions to invoke amd64 instructions (such as cmov, min/maxsd, popcnt
when available, or compatible software implementation on other targets.

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
%dune_build -p %oname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 03 2024 Anton Farygin <rider@altlinux.ru> 0.17.1-alt1
- first build for ALT Linux
