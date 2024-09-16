%define libname fiber
Name: ocaml-%libname
Version: 3.7.0
Release: alt1
Summary: Dune's monadic structured concurrency library
License: MIT
Group: Development/ML
Url: https://github.com/ocaml-dune/fiber
VCS: https://github.com/ocaml-dune/fiber
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-stdune-devel
BuildRequires: ocaml-odoc-devel


%description
%summary

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
%dune_build -p %libname

%install
%dune_install -p %libname

%check
%dune_check -p %libname

%files -f ocaml-files.runtime
%doc LICENSE.md


%files devel -f ocaml-files.devel

%changelog
* Fri Sep 13 2024 Anton Farygin <rider@altlinux.ru> 3.7.0-alt1
- first build for ALT Linux
