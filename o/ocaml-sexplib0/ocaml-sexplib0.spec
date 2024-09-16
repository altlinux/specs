%define oname sexplib0
Name: ocaml-%oname
Version: 0.17.0
Release: alt1
Summary: OCaml library for converting OCaml values to S-expressions
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/%oname
Source0: %name-%version.tar
BuildRequires: dune
BuildRequires: ocaml

%description
This library contains functionality for parsing and pretty-printing
S-expressions. In addition to that it contains an extremely useful
preprocessing module for Camlp4, which can be used to automatically
generate code from type definitions for efficiently converting
OCaml-values to S-expressions and vice versa. In combination with the
parsing and pretty-printing functionality this frees users from having
to write their own I/O-routines for datastructures they
define. Possible errors during automatic conversions from
S-expressions to OCaml-values are reported in a very human-readable
way. Another module in the library allows you to extract and replace
sub-expressions in S-expressions.

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

%check
%dune_check

%install
%dune_install

%files -f ocaml-files.runtime
%doc LICENSE.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 03 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- cmxa moved to the devel package

* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt2
- removed opam build requires

* Tue Jan 28 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0 

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt4
- fixed build with dune 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt2
- rebuilt with ocaml-4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT, based on specfile from Mageia

