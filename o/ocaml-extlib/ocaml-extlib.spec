Name: ocaml-extlib
Version: 1.7.9
Release: alt1
Summary: extended standard library for OCaml
License: LGPLv2 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/ygrek/ocaml-extlib
Source: %name-%version.tar
BuildRequires: rpm-build-ocaml ocaml-cppo dune ocaml

%description
ExtLib is a project aiming at providing a complete - yet small - standard
library for the OCaml programming language.

The purpose of this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances or more
safety (tail-recursive) but also to provide new modules which should be useful
for the average OCaml programmer.

ExtLib contains modules implementing: enumeration over abstract collection of
elements, efficient bit sets, dynamic arrays, references on lists, Unicode
characters and UTF-8 encoded strings, additional and improved functions for
hashtables, strings, lists and option types.

%define extlibdir %_libdir/ocaml/extlib

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE

%files devel -f ocaml-files.devel
%doc CHANGES

%changelog
* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 1.7.9-alt1
- 1.7.9

* Wed May 19 2021 Anton Farygin <rider@altlinux.ru> 1.7.8-alt2
- fixed typo in install section

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 1.7.8-alt1
- 1.7.8

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 1.7.7-alt1
- 1.7.7

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 1.7.6-alt3
- fixed License tag

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.7.6-alt2
- rebuilt with ocaml-4.08

* Thu May 16 2019 Anton Farygin <rider@altlinux.ru> 1.7.6-alt1
- 1.7.6

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.7.5-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt5
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt4
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt3
- split to devel and runtime packages

* Sat Apr 15 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt2
- do not use site-lib

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt1
- new version

* Thu Dec 22 2011 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Wed Jul 02 2008 Alexander Myltsev <avm@altlinux.ru> 1.5.1-alt2
- Fix build error (buildrequire ocamldoc).

* Mon Jan 21 2008 Alex V. Myltsev <avm@altlinux.ru> 1.5.1-alt1
- New version.
- Use rpm-build-ocaml.

* Mon Jul 09 2007 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt1
- Initial build for Sisyphus.

