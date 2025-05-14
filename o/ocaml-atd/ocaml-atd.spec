%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: ocaml-atd
Version: 2.16.0
Release: alt1

Summary: Static Types for Json APIs
Group: Development/ML
License: BSD-3-Clause
Url: https://github.com/ahrefs/atd
Vcs: https://github.com/ahrefs/atd

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ocaml
BuildRequires: dune
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-menhir
BuildRequires: ocaml-odoc
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-easy-format-devel
%if_with check
BuildRequires: /proc rpm-build-java
BuildRequires: java-11-openjdk-devel
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-flake8
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pytest
BuildRequires: ocaml-alcotest-devel
%endif

%description
ATD stands for Adaptable Type Definitions. It is a syntax for defining
cross-language data types. It is used as input to generate efficient
and type-safe serializers, deserializers and validators.

Target languages currently supported:
* Java: [atdj](atdj)
* OCaml, Bucklescript: [atdgen](atdgen)
* Python: [atdpy](atdpy)
* Scala: [atds](atds)
* TypeScript: [atdts](atdts)

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Requires: ocaml-easy-format-devel
Requires: ocaml-re-devel
Requires: ocaml-yojson-devel
Requires: ocaml-biniou-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install @doc 

%install
%dune_install

%check
dune test atd{,gen,j,py}/test

%files -f ocaml-files.runtime
%doc CHANGES.md README.md LICENSE.md
%_bindir/*

%files devel -f ocaml-files.devel
%doc %{_docdir}/*/*.md
%doc CODEOWNERS

%changelog
* Tue May 13 2025 Denis Rastyogin <gerben@altlinux.org> 2.16.0-alt1
- Initial build for ALT Sisyphus.
