Name: ocaml-migrate-parsetree
Version: 2.4.0
Release: alt1
Summary: Convert OCaml parsetrees between different major versions
Group: Development/ML
License: LGPLv2+ with OCaml-LGPL-linking-exception
Url: https://github.com/ocaml-ppx/ocaml-migrate-parsetree
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: dune cinaps

%description
This library converts between parsetrees of different OCaml versions.
For each version, there is a snapshot of the parsetree and conversion
functions to the next and/or previous version.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
%dune_build -p %name

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md CHANGES.md LICENSE.md

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Fri Dec 10 2021 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.2.0 -> 2.3.0

* Wed Jul 28 2021 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Dec 09 2020 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.7.3-alt2
- built in verbose mode
- fixed requires in devel package (by change BR from
  ocaml-ppx_derivers to ocaml-ppx_derivers-devel)

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Jun 07 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.10-alt1
- first build for ALT, based on specfile from RH

