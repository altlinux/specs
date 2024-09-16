%define  modulename ppx_hash
%def_with check

Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1
Summary: A ppx rewriter that generates hash functions from type expressions and definitions
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_hash
VCS:     https://github.com/janestreet/ppx_hash
BuildRequires: dune ocaml-ppx_compare-devel ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-base-devel ocaml-ppxlib-devel 
BuildPreReq: rpm-build-ocaml >= 1.4
Source:  %modulename-%version.tar

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
%setup -n %modulename-%version

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml 1.4
- cleaned up spec

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
