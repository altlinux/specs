%define libname ppx_stable
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: OCAML ppx extension for stable types conversions generator
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_stable
VCS: https://github.com/janestreet/ppx_stable
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel >= 0.28.0
BuildRequires: ocaml-base-devel >= %version

%description
A ppx extension for easier implementation of conversion functions
between almost identical types.

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
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT Linux
