%define  modulename base64
Name:    ocaml-%modulename
Version: 3.5.1
Release: alt1
Summary: Base64 encoding for OCaml
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-base64
Source:  %name-%version.tar

BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-bos-devel
BuildRequires: ocaml-rresult-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-result-devel
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

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check --release

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 3.5.0-alt2
- added --release in the check section to igrnore the alerts about deprecation

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 3.5.0-alt1
- 3.5.0

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 3.4.0-alt2
- fixed build with dune 2.7

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 3.4.0-alt1
- first build for ALT
