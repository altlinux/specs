%define oname base
Name: ocaml-%oname
Version: 0.16.3
Release: alt1
Summary: Full standard library replacement for OCaml
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-sexplib0-devel  >= 0.16

%description
Base is a complete and portable alternative to the OCaml standard
library. It provides all standard functionalities one would expect
from a language standard library. It uses consistent conventions
across all of its module.

Base aims to be usable in any context. As a result system dependent
features such as I/O are not offered by Base. They are instead
provided by companion libraries such as stdio.

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
%dune_build -p %oname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.org LICENSE.md
%_libdir/ocaml/%oname/runtime.js
%_libdir/ocaml/%oname/base_internalhash_types/runtime.js

%files devel -f ocaml-files.devel
%_libdir/ocaml/%oname/base_internalhash_types/internalhash.h

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.3-alt1
- 0.16.3

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 0.14.1-alt1
- 0.14.1
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- simplified specfile with macros from rpm-build-ocaml 1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts moved to ocaml-base-devel package

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Sat Feb 22 2020 Anton Farygin <rider@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt3
- fixed build with dune 1.4

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for Sisyphus, based on specfile from Mageia 

