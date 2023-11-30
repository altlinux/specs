%define  modulename cairo2
%def_with check
Name:    ocaml-%modulename
Version: 0.6.4
Release: alt1
Summary: Ocaml binding to Cairo, a 2D Vector Graphics Library
License: LGPL-3.0-only
Group:   Development/ML
URL:     https://github.com/Chris00/ocaml-cairo
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-base-devel
BuildRequires: libcairo-devel
BuildRequires: libfreetype-devel
Source: %name-%version.tar

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
%dune_install %modulename

%check
%dune_check -p %modulename

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel
%_ocamldir/%modulename/*.h

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Mon Mar 22 2021 Anton Farygin <rider@altlinux.org> 0.6.2-alt1
- 0.6.2

* Wed Mar 17 2021 Anton Farygin <rider@altlinux.org> 0.6.1-alt3
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.6.1-alt2
- fixed build with dune 2.7

* Fri Sep 25 2020 Anton Farygin <rider@altlinux.ru> 0.6.1-alt1
- first build for ALT

