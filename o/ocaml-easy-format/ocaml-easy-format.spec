%define ocamlmod easy-format
Name: ocaml-%ocamlmod
Version: 1.3.4
Release: alt1
Summary: High-level and functional interface to the Format module
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/ocaml-community/easy-format
Source: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-ocamldoc
BuildRequires: dune

%description
This module offers a high-level and functional interface to the Format
module of the OCaml standard library. It is a pretty-printing
facility, i.e. it takes as input some code represented as a tree and
formats this code into the most visually satisfying result, breaking
and indenting lines of code where appropriate.

Input data must be first modeled and converted into a tree using 3
kinds of nodes:

    atoms
    lists
    labeled nodes

Atoms represent any text that is guaranteed to be printed as-is. Lists
can model any sequence of items such as arrays of data or lists of
definitions that are labeled with something like "int main", "let x
=" or "x:".

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
%dune_build -p %ocamlmod

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc LICENSE README.md CHANGES.md

%changelog
* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 1.3.2-alt2
- migrated to rpm-build-ocaml 1.4

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.2
- added patch from suse to fix build with dune-2.x and ocaml 4.08

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt3
- rebuilt for ocaml-4.07.1

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2
- rebuilt for ocaml-4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Thu Dec 21 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- rebuilt for ocaml 4.06

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.2-alt2
- rebuild with ocaml 4.04.1

* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- first build for ALT, based on RH spec
