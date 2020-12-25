%set_verify_elf_method textrel=relaxed
%define  modulename integers

Name:    ocaml-%modulename
Version: 0.4.0
Release: alt3
Summary: Various signed and unsigned integer types for OCaml
License: MIT
Group:   Development/ML
URL:     https://github.com/ocamllabs/ocaml-integers
BuildRequires: dune
BuildRequires: ocaml rpm-build-ocaml
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
%_libdir/ocaml/%{modulename}*/*.h

%changelog
* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 0.4.0-alt3
- added ocaml to BuildRequires

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.4.0-alt2
- migrated to rpm-build-ocaml 1.4

* Fri Jul 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
