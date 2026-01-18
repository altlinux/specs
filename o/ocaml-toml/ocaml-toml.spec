%def_with check
Name: ocaml-toml
Version: 7.1.0
Release: alt1
Summary: Library for TOML with a parser, a serializer and a printer
Group: Development/ML
License: LGPL3
Url: https://ocaml-toml.github.io/To.ml/
VCS: https://github.com/ocaml-toml/To.ml
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.08
BuildRequires: dune >= 3.0

BuildRequires: ocaml-menhir
BuildRequires: ocaml-odoc-devel
BuildRequires: ocaml-ISO8601-devel >= 0.2

%if_with check
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-mdx-devel >= 2.1
BuildRequires: ocaml-bisect_ppx-devel >= 2.5
BuildRequires: ocaml-ocb-devel >= 0.1
%endif

%description
toml is an OCaml library providing a parser, a serializer and a printer
for TOML, a minimal configuration file format. Helpful getters to
retrieve data as OCaml primitive types are also supplied.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p toml

%install
%dune_install toml

%check
%dune_check -p toml

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Jan 18 2026 Anton Farygin <rider@altlinux.org> 7.1.0-alt1
- Initial build for ALT Linux.

