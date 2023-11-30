%def_with check
%define docdir %_docdir/%name-%version
%define module sqlite3
Name: ocaml-%module
Version: 5.1.0
Release: alt2
Summary: OCaml library for accessing SQLite3 databases
License: MIT
Group: Development/ML
Url: https://mmottl.github.io/sqlite3-ocaml/
# https://github.com/mmottl/sqlite3-ocaml
Source: %name-%version.tar

BuildRequires: libsqlite3-devel ocaml-dune-configurator-devel rpm-build-ocaml
%if_with check
BuildRequires: ocaml-ppx_inline_test-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_compare-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_hash-devel
%endif
Provides: ocaml4-%module
Obsoletes: ocaml4-%module
Obsoletes: ocaml-%module-runtime < %EVR

%description
SQLite 3 database library wrapper for OCaml.

%package devel
Summary: Development files for %name 
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q 

%build
%dune_build -p %module

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md TODO.md

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 5.1.0-alt2
- fix BuildRequires

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- 5.1.0

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 5.0.2-alt2
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- simplified specfile with macros from rpm-build-ocaml 1.4
- enabled tests

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 5.0.2-alt1
- 5.0.2
- added devel package
- runtime package merged to %name

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Wed Feb 13 2019 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt2
- rebuilt with ocaml-4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 4.1.3-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt3
- rebuild with ocaml 4.04.1

* Wed Mar 29 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt2
- updated to new version

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.2.0-alt1
- updated to new version

* Thu Mar 06 2008 Veaceslav Grecea <slavutich@altlinux.org> 0.23.0-alt1
- Adapted for ALTLinux

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-2
- Added BR ocaml-camlp4-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-1
- Initial RPM release.
