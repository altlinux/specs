%def_with check
Name: ocaml-re
Version: 1.11.0
Release: alt1
Summary: A regular expression library for OCaml
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Url: https://github.com/ocaml/ocaml-re
Source0: ocaml-re-%version.tar
Patch0: %name-%version-alt.patch
Group: Development/ML
BuildRequires: ocaml
BuildRequires: dune
%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p re

%install
%dune_install

%check 
sed -si 's,oUnit,ounit2,' lib_test/fort_unit/dune
%dune_check -p re

%files -f ocaml-files.runtime
%doc CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Fri Nov 03 2023 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 1.10.3-alt2
- disabled tests for bootstrap ocaml-4.13

* Mon Oct 04 2021 Anton Farygin <rider@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Thu May 20 2021 Anton Farygin <rider@altlinux.ru> 1.9.0-alt3
- simplified specfile with rpm-build-ocaml 1.4

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.9.0-alt2
- built as release (dune build -p) against incomplete dependencies
  in devel packages

* Thu Aug 08 2019 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.8.0-alt5
- fixed built with dune-1.6.4

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt4
- fixed install section with dune-1.4.0

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt3
- all development stuff were moved to the devel package

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt2
- rebuilt with ocaml-4.07.1

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2
- rebuilt for ocaml 4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- first build for ALT, based on RH spec

