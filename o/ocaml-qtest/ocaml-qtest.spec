%define libname qtest
Name: ocaml-%libname
Version: 2.11.2
Release: alt3
Summary: Inline (Unit) Tests for OCaml
License: GPLv3
Group: Development/ML
Url: https://github.com/vincent-hugot/qtest
VCS: https://github.com/vincent-hugot/qtest
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires:  dune 
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-base-devel 

%description
qtest extracts inline unit tests written using a special syntax in comments.
Those tests are then run using the oUnit framework and the qcheck library. The
possibilities range from trivial tests -- extremely simple to use -- to
sophisticated random generation of test cases.

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
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.adoc HOWTO.adoc
%_bindir/qtest

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 2.11.2-alt3
- removed "bytes" dependency to fix build with ocaml 5.2

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 2.11.2-alt2
- fixed URL

* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 2.11.2-alt1
- 2.11.2

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 2.11.1-alt1
- 2.11.1

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 2.11-alt1
- 2.11

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt3
- oUnit to ounit2 replace has been moved to specfile

* Mon Feb 17 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt2
- update build requires for new ounit2 and qcheck packages

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 2.9-alt1
- first build for ALT


