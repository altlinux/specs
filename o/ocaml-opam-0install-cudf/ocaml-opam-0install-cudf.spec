%define pkgname opam-0install-cudf
Name: ocaml-%pkgname
Version: 0.5.0
Release: alt1
Summary: Opam solver using 0install backend using the CUDF interface
License: ISC
Group: Development/ML
Url: https://github.com/ocaml-opam/opam-0install-cudf
VCS: https://github.com/ocaml-opam/opam-0install-cudf
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-0install-solver-devel

%description
Opam's default solver is designed to maintain a set of packages over time,
minimising disruption when installing new programs and finding a compromise
solution across all packages.

In many situations (e.g. CI, local roots or duniverse builds) this is not
necessary, and we can get a solution much faster by using a different algorithm.

This package provides a generic solver library which uses 0install's solver
library. The library uses the CUDF library in order to interface with opam as
it is the format common used to talk to all the supported solvers.

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
%dune_build --release @install

%install
%dune_install --release

%check
%dune_check --release

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 17 2024 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- first build for ALT Linux
