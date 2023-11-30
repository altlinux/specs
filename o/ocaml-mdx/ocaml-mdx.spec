%define libname mdx
Name: ocaml-%libname
Version: 2.3.1
Release: alt1
Summary: Executable code blocks inside markdown files
Group: Development/ML
License: ISC
Url: https://github.com/realworldocaml/mdx
Source0: %name-%version.tar
BuildRequires: dune >= 3.0
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-logs-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-version-devel
BuildRequires: ocaml-csexp-devel

%description
mdx allows to execute code blocks inside markdown files.
There are (currently) two sub-commands, corresponding to two modes of
operations: pre-processing (mdx pp) and tests (mdx test).

The pre-processor mode allows to mix documentation and code, and to practice
"literate programming" using markdown and OCaml.

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
%dune_install %libname

%files -f ocaml-files.runtime
%doc README.md
%_bindir/*


%files devel -f ocaml-files.devel

%changelog
* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

