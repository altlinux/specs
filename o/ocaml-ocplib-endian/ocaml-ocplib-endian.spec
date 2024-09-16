%ifarch %ocaml_native_arch
%def_with check
%else
%def_without check
%endif

%define pkgname ocplib-endian
Name: ocaml-%pkgname
Version: 1.2
Release: alt3
Summary: Functions to read/write int16/32/64 from strings, bigarrays
License: LGPLv2+
Group: Development/ML
Url: https://github.com/OCamlPro/ocplib-endian
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-cppo
BuildRequires: ocaml-ocamldoc
BuildRequires: dune
BuildRequires: rpm-build-ocaml >= 1.6

%description
Optimised functions to read and write int16/32/64 from strings,
bytes and bigarrays, based on primitives added in version 4.01.

The library implements three modules:

EndianString works directly on strings, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBytes works directly on bytes, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBigstring works on bigstrings (Bigarrays of chars),
and provides submodules BigEndian and LittleEndian, with their
unsafe counter-parts;

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and
signature files for developing applications that use %name.

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
%doc COPYING.txt README.md CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 12 2024 Anton Farygin <rider@altlinux.ru> 1.2-alt3
- removed the module "bytes" dependence to fix build with ocaml 5.2

* Fri Nov 17 2023 Anton Farygin <rider@altlinux.ru> 1.2-alt2
- disabled tests for non-native ocaml architectures

* Fri Dec 10 2021 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- 1.2

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.1

* Thu Feb 13 2020 Anton Farygin <rider@altlinux.ru> 1.0-alt1
- first build for Sisyphus

