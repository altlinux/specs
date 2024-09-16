%define  modulename ppx_globalize
%def_with check

Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1
Summary: A ppx rewriter that generates functions to copy local values to the global heap
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_globalize
VCS:     https://github.com/janestreet/ppx_globalize
BuildRequires: dune ocaml-ppxlib-devel  ocaml-base-devel
BuildRequires: ocaml-ppxlib_jane-devel >= %version
BuildRequires: rpm-build-ocaml >= 1.6
Source:  %name-%version.tar

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

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- first build for ALT


