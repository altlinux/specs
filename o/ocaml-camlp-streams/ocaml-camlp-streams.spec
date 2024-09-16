Name: ocaml-camlp-streams
Version: 5.0.1
Release: alt2
Summary: The Stream and Genlex libraries for use with Camlp4 and Camlp5
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/ocaml/camlp-streams
Source0: %name-%version.tar
BuildRequires: ocaml >= 5.2.0 ocaml-compiler-libs >= 5.2.0
BuildRequires: dune

%description
This package provides two library modules:
 Stream: imperative streams, with in-place update and memoization of the latest
 element produced.
 Genlex: a small parameterized lexical analyzer producing streams of tokens from
 streams of characters.

The two modules are designed for use with Camlp4 and Camlp5:
 The stream patterns and stream expressions of Camlp4/Camlp5 consume and produce
 data of type 'a Stream.t.
 The Genlex tokenizer can be used as a simple lexical analyzer for
 Camlp4/Camlp5-generated parsers.

The Stream module can also be used by hand-written recursive-descent parsers,
but is not very convenient for this purpose.

The Stream and Genlex modules have been part of the OCaml standard library for
a long time, and have been distributed as part of the core OCaml system.
They will be removed from the OCaml standard library at some future point,
but will be maintained and distributed separately in this camlpstreams package.

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
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md CHANGES.md 

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 5.0.1-alt2
- added ocaml-compiler-libs to BuildRequires against ocaml 5.2.0

* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- first build for ALT
