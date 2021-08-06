%define libname fix
Name: ocaml-%libname
Version: 20201120
Release: alt1
Summary: Facilities for memoization and fixed points
License: LGPLv2 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/c-cube/sequence/
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml

%description
Facilities for memoization and fixed points.

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

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Fri Aug 06 2021 Anton Farygin <rider@altlinux.ru> 20201120-alt1
- first build for ALT
