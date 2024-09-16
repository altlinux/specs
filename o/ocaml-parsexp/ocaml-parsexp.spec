%define libname parsexp
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: S-expression parsing library for ocaml
Group: Development/ML
License: Apache-2.0
Url: https://github.com/janestreet/parsexp
Source0: %name-%version.tar
BuildRequires: dune >= 3.8
BuildRequires: ocaml-sexplib0-devel >= %version
BuildRequires: ocaml-base-devel >= %version
BuildRequires: rpm-build-ocaml >= 1.6.3

%description
This library provides generic parsers for parsing S-expressions from strings or
other medium.

The library is focused on performances but still provide full generic parsers
that can be used with strings, bigstrings, lexing buffers, character streams or
any other sources effortlessly.

It provides three different class of parsers:

    the normal parsers, producing [Sexp.t] or [Sexp.t list] values
    the parsers with positions, building compact position sequences so that one
    can recover original positions in order to report properly located errors at
    little cost
    the Concrete Syntax Tree parsers, produce values of type [Parsexp.Cst.t]
    which record the concrete layout of the s-expression syntax, including
    comments

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
%dune_build -p %libname 

%install
%dune_install 
rm -rf %buildroot/usr/share/doc

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.org CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Tue Nov 30 2021 Anton Farygin <rider@altlinux.ru> 0.14.1-alt2
- fixed homepage URL

* Wed Aug 18 2021 Anton Farygin <rider@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt3
- mirated to rpm-build-ocaml 1.4
- added ocaml-base-devel dependency to devel package

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- cmxa have been moved to devel package

* Wed Jun 17 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


