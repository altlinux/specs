%define  modulename ppx_sexp_message
Name:    ocaml-%modulename
Version: 0.17.0
Release: alt1
Summary: A ppx rewriter for easy construction of s-expressions
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/ppx_sexp_message
BuildRequires: dune
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_here-devel

Source: %modulename-%version.tar
Patch0: %name-%version-%release.patch

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
%patch0 -p1

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 11 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt3
- added upstream patch against ppxlib 0.22

* Tue Dec 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- specfile migrated to rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
