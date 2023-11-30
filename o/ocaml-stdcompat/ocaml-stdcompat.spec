%define libname stdcompat
Name: ocaml-%libname
Version: 19
Release: alt1
Summary: Compatibility module for OCaml standard library
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/thierry-martinez/stdcompat
Source0: %name-%version.tar
BuildRequires: dune ocaml

%description
Compatibility module for OCaml standard library allowing programs to use some
recent additions to the OCaml standard library while preserving the ability to
be compiled on former versions of OCaml.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

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
%doc README.md ChangeLog COPYING 

%files devel -f ocaml-files.devel

%changelog
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

