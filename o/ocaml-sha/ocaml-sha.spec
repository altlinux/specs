%define pkgname sha
Name: ocaml-%pkgname
Version: 1.15.4
Release: alt1
Summary: OCAML binding to the SHA cryptographic functions
License: ISC
Group: Development/ML
Url: https://github.com/djs55/ocaml-sha
VCS: https://github.com/djs55/ocaml-sha
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-odoc-devel

%description
This is the binding for SHA interface code in OCaml. Offering the same interface
than the MD5 digest included in the OCaml standard library. It's currently
providing SHA1, SHA256 and SHA512 hash functions.

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
* Tue Sep 17 2024 Anton Farygin <rider@altlinux.ru> 1.15.4-alt1
- first build for ALT Linux
