%define  modulename ppx_optional
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: Pattern matching on flat options
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_optional
BuildRequires: dune
BuildRequires: ocaml-base-devel ocaml-ppxlib-devel
BuildRequires: ocaml-ppxlib_jane-devel >= %version
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
* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt2
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
