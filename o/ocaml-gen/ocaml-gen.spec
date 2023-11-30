%define libname gen
Name: ocaml-%libname
Version: 1.1
Release: alt1
Summary: Simple and efficient iterators (modules Gen and GenLabels).
License: BSD-2-Clause
Group: Development/ML
Url: https://github.com/c-cube/gen
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-dune-configurator-devel ocaml-result-devel
BuildRequires: dune
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc ocaml-qtest-devel

%description
%name provides additional modules GenClone and GenMList for lower-level control
over persistency and duplication of iterators.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGELOG.md


%files devel -f ocaml-files.devel

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1

* Sun Jan 30 2022 Anton Farygin <rider@altlinux.ru> 1.0-alt1
- 0.5.3 -> 1.0

* Fri Nov 26 2021 Anton Farygin <rider@altlinux.ru> 0.5.3-alt5
- fixed homepage URL

* Mon Mar 15 2021 Anton Farygin <rider@altlinux.org> 0.5.3-alt4
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- supressed a warning 33 in tests for compatability with new dune 2.8.x

* Thu Dec 24 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- disabled check on armh due to incompatibilty -nodynlink and PIE

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- enabled tests
- migrated to rpm-build-ocaml 1.4

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 0.5.2-alt3
- rebuilt by dune-2.x

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 0.5.2-alt2
- rebuilt with ocaml-4.08

* Sat Jun 01 2019 Anton Farygin <rider@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- first build for ALT


