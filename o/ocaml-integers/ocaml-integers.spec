%define  modulename integers

Name:    ocaml-%modulename
Version: 0.7.0
Release: alt2
Summary: Various signed and unsigned integer types for OCaml
License: MIT
Group:   Development/ML
URL:     https://github.com/ocamllabs/ocaml-integers
VCS:     https://github.com/ocamllabs/ocaml-integers
BuildRequires: dune
BuildRequires: ocaml rpm-build-ocaml
BuildRequires: ocaml-compiler-libs
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
sed -i 's,stdlib-shims,,' src/dune
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
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.7.0-alt2
- added ocaml-compiler-libs to BuildRequires

* Thu Mar 24 2022 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.5.1 -> 0.7.0

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 0.4.0-alt3
- added ocaml to BuildRequires

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.4.0-alt2
- migrated to rpm-build-ocaml 1.4

* Fri Jul 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
