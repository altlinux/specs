Name: ocaml-stdlib-random
Version: 1.1.0
Release: alt1
Summary: Ocaml Compatibility library for Random number generation
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/ocaml/stdlib-random
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.14
BuildRequires: dune ocaml-cppo

%description
This library provides access to the various implementation of the Random module
from the OCaml standard library independently of the compiler version.

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
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md Changelog.md 

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- first build for ALT
