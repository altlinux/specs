%def_with check
%define modulename angstrom
Name: ocaml-%modulename
Version: 0.16.0
Release: alt1
Summary: OCaml Parser combinators built for speed and memory-efficiency
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/inhabitedtype/angstrom
VCS: https://github.com/inhabitedtype/angstrom
Source: %name-%version.tar
BuildRequires: dune ocaml-bigstringaf-devel
BuildRequires: ocaml-result-devel
%if_with check
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-ppx_let-devel
%endif

%description
Angstrom is a parser-combinator library that makes it easy to write efficient,
expressive, and reusable parsers suitable for high-performance applications. It
exposes monadic and applicative interfaces for composition, and supports
incremental input through buffered and unbuffered interfaces. Both interfaces
give the user total control over the blocking behavior of their application,
with the unbuffered interface enabling zero-copy IO. Parsers are backtracking by
default and support unbounded lookahead.

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
%dune_build -p %modulename

%install
%dune_install %modulename

%check
%dune_check -p %modulename

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.15.0 -> 0.16.0

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 0.15.0-alt1
- first build for ALT
