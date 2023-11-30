%define  modulename ppx_fixed_literal
Name:    ocaml-%modulename
Version: 0.16.0
Release: alt1
Summary: Simpler notation for fixed point literals
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_fixed_literal
BuildRequires: dune ocaml-ppxlib-devel
BuildRequires: ocaml-base-devel

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

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt3
- specfile BR: cleanup

* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrate to rpm-build-ocaml 1.4
- added ocaml-base-devel to BuildRequires

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
