%def_with check
%define pkgname charInfo_width
Name: ocaml-%pkgname
Version: 2.0.0
Release: alt2
Summary: Determine column width for a character
Group: Development/ML
License: MIT
Url: https://github.com/kandu/charinfo_width/
VCS: https://github.com/kandu/charinfo_width/
Source: %name-%version.tar

BuildRequires: dune
BuildRequires: ocaml-camomile-devel
BuildRequires: ocaml-result-devel
BuildPreReq: rpm-build-ocaml >= 1.4
%if_with check
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_compare-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_hash-devel
BuildRequires: ocaml-camlp-streams-devel
%endif

%description
This module is implemented purely in OCaml and the width function follows the
prototype of POSIX's wcwidth.

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
%dune_build -p %pkgname

%install
%dune_install %pkgname

%check
%dune_check -p %pkgname

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- fixed URL

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
