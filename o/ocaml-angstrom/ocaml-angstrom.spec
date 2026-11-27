%def_with check
%define modulename angstrom
Name: ocaml-%modulename
Version: 0.16.1
Release: alt2
Summary: OCaml Parser combinators built for speed and memory-efficiency
License: BSD-3-Clause
Group: Development/ML
Url: https://github.com/inhabitedtype/angstrom
VCS: https://github.com/inhabitedtype/angstrom
Source: %name-%version.tar
BuildRequires: dune ocaml-bigstringaf-devel ocaml-lwt-devel
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
%__subst -p '/package "async" (/,/^)/d' META.angstrom.template

%build
%dune_build -p %modulename,%modulename-unix,%modulename-lwt-unix

%install
%dune_install_multi %modulename %modulename-unix %modulename-lwt-unix
cat ocaml-files.runtime.* > ocaml-files.runtime
cat ocaml-files.devel.* > ocaml-files.devel

%check
%dune_check -p %modulename

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Aug 12 2026 Anton Farygin <rider@altlinux.org> 0.16.1-alt2
- built Unix and Lwt_unix support libraries

* Fri Sep 20 2024 Anton Farygin <rider@altlinux.ru> 0.16.1-alt1
- 0.16.0 -> 0.16.1

* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.15.0 -> 0.16.0

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 0.15.0-alt1
- first build for ALT
