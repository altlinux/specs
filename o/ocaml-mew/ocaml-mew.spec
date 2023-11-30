%def_with check
Name: ocaml-mew
Version: 0.1.0
Release: alt3
Summary: Modal Editing Witch

Group: Development/ML
License: MIT
Url: https://github.com/kandu/mew
Source: %name-%version.tar

BuildRequires: dune ocaml-trie-devel ocaml-result-devel
%if_with check
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_compare-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_hash-devel
%endif
BuildPreReq: rpm-build-ocaml >= 1.4

%description
This is the core module of mew, a general modal editing engine generator.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-result-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build

%check
%dune_check

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 0.1.0-alt3
- updated BuildRequires

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.1.0-alt2
- cleanup spec and buildrequires
- enabled check

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
