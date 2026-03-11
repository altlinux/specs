%define libname stdcompat
Name: ocaml-%libname
Version: 21.1
Release: alt1
Summary: Compatibility module for OCaml standard library
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/thierry-martinez/stdcompat
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch2: ocaml-stdcompat-ocaml5.4.patch
BuildRequires: dune ocaml

%description
Compatibility module for OCaml standard library allowing programs to use some
recent additions to the OCaml standard library while preserving the ability to
be compiled on former versions of OCaml.

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
%patch2 -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md COPYING 

%files devel -f ocaml-files.devel

%changelog
* Fri Mar 06 2026 Anton Farygin <rider@altlinux.org> 21.1-alt1
- 19 -> 21.1

* Fri Jan 17 2025 Anton Farygin <rider@altlinux.ru> 19-alt4.gitd53390d
- added ocaml 5.3 compatibility patches

* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 19-alt3.gitd53390d
- added ocaml 5.2 compatibility patches from upstream git d53390d

* Mon Dec 04 2023 Anton Farygin <rider@altlinux.ru> 19-alt2
- added a lost header to the development package (Closes: #48671)

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 19-alt1
- 17 -> 19

* Mon Oct 04 2021 Anton Farygin <rider@altlinux.ru> 17-alt1
- 15 -> 17

* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 15-alt1
- 14 -> 15

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 14-alt1
- 13 -> 14

* Thu Mar 05 2020 Anton Farygin <rider@altlinux.ru> 13-alt1
- first build for ALT

