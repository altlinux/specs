%set_verify_elf_method textrel=relaxed
%define  modulename bigarray-compat
Name:    ocaml-%modulename
Version: 1.1.0
Release: alt2
Summary: Compatibility library to use Stdlib.Bigarray when possible
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/bigarray-compat
BuildRequires: dune ocaml ocaml-compiler-libs >= 5.2.0
BuildRequires: rpm-build-ocaml >= 1.4
Source:  %name-%version.tar

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
%dune_build -p %{modulename}

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- add ocaml-compiler-libs build dependency to fix build with ocaml 5.2

* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- migrated to rpm-build-ocaml-1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for ALT

