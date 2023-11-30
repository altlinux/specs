%define  modulename ppx_sexp_value
Name:    ocaml-%modulename
Version: 0.16.0
Release: alt1
Summary: A ppx rewriter that simplifies building s-expressions from ocaml values
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_sexp_value
BuildRequires: dune ocaml-base-devel ocaml-ppx_here-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-ppx_sexp_conv-devel

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
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt2
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
