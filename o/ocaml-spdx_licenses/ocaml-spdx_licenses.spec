%define pkgname spdx_licenses
Name: ocaml-%pkgname
Version: 1.2.0
Release: alt1
Summary: A library providing a strict SPDX License Expression parser for OCAML
License: MIT
Group: Development/ML
Url: https://github.com/kit-ty-kate/spdx_licenses
VCS: https://github.com/kit-ty-kate/spdx_licenses
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-alcotest-devel

%description
An OCaml library aiming to provide an up-to-date and strict SPDX License
Expression parser.
It implements the format described in: https://spdx.github.io/spdx-spec/appendix-IV-SPDX-license-expressions/
See https://spdx.org/licenses/ for more details.

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
%dune_install --release

%check
%dune_check --release

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 17 2024 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- first build for ALT Linux
