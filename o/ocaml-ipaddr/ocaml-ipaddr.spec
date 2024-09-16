%define  modulename ipaddr
Name:    ocaml-%modulename
Version: 5.6.0
Release: alt1
Summary: An OCaml library for manipulation of IP (and MAC) address representations 
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-ipaddr
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-domain-name-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-cstruct-devel
BuildPreReq: rpm-build-ocaml >= 1.4

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
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 5.6.0-alt1
- 5.6.0

* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 5.5.0-alt1
- 5.5.0

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- 5.3.0

* Wed Sep 15 2021 Anton Farygin <rider@altlinux.ru> 5.2.0-alt1
- 5.2.0

* Wed Aug 18 2021 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- 5.1.0 (Fixes: CVE-2021-29921)

* Wed Sep 30 2020 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 5.0.0-alt1
- first build for ALT
