%define pkgname swhid_core
Name: ocaml-%pkgname
Version: 0.1
Release: alt1
Summary: OCaml library to work with swhids
License: ISC
Group: Development/ML
Url: https://github.com/ocamlpro/swhid_core
VCS: https://github.com/ocamlpro/swhid_core
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-odoc-devel

%description
swhid_core is an OCaml library to with with Software Heritage persistent
identifiers (swhids). This is the core library, for most use cases you should
use the swhid library instead.

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
* Tue Sep 17 2024 Anton Farygin <rider@altlinux.ru> 0.1-alt1
- first build for ALT Linux
