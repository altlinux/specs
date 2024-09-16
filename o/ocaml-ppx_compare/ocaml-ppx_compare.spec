%define  modulename ppx_compare
%def_with check

Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1
Summary: Generation of comparison functions from types
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_compare
VCS:     https://github.com/janestreet/ppx_compare
BuildRequires: dune ocaml-base-devel ocaml-ppxlib-devel
BuildRequires: ocaml-ppxlib_jane-devel >= %version
Source:  %modulename-%version.tar

%description
Generation of fast comparison and equality functions from type
expressions and definitions.

Ppx_compare is a ppx rewriter that derives comparison and equality functions
from type representations. The scaffolded functions are usually much faster
than ocaml's Pervasives.compare and Pervasives.(=). Scaffolding functions also
gives you more flexibility by allowing you to override them for a specific
type and more safety by making sure that you only compare comparable values.

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

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
