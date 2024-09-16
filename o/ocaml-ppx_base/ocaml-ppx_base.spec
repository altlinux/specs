%define  modulename ppx_base
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1

Summary: Base set of ppx rewriters
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_base
BuildRequires: dune ocaml-ppx_js_style-devel ocaml-ppx_hash-devel
BuildRequires: ocaml-ppx_enumerate-devel ocaml-ppx_cold-devel
BuildRequires: ocaml-base-devel ocaml-ppxlib-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-ppx_compare-devel
BuildRequires: ocaml-octavius-devel
BuildRequires: ocaml-ppx_globalize-devel >= %version

Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-ppxlib-devel
Requires: ocaml-ppx_globalize-devel
Requires: ocaml-ppx_cold-devel
Requires: ocaml-ppx_sexp_conv-devel
Requires: ocaml-ppx_compare-devel
Requires: ocaml-ppx_enumerate-devel
Requires: ocaml-ppx_hash-devel
Requires: ocaml-ppx_js_style-devel

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
%_bindir/ppx-base

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Sun Jan 09 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt3
- specfile BR: cleanup

* Thu Sep 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- added requires to devel subpackage from dune file
- migrated to rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
