%def_with check
%define ocamlmod iostream
Name: ocaml-%ocamlmod
Version: 0.3
Release: alt1
Summary: Generic, composable IO input and output streams for OCAML
Group: Development/ML
License: MIT
Url: https://github.com/c-cube/ocaml-iostream
VCS: https://github.com/c-cube/ocaml-iostream
Source0: %name-%version.tar
BuildRequires: ocaml >= 5.2.0
BuildRequires: dune
BuildRequires: ocaml-camlzip-devel
%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
This library defines generic I/O streams of bytes. The streams should be
composable, user-definable, and agnostic to the underlying I/O mechanism; with
OCaml 5 it means that they might be backed by an effect-based scheduler.

The goal is to provide a reasonable interoperability layer that multiple
libraries and applications in the OCaml ecosystem can rely on, while providing
the modularity that standard IO channels lack. Modern statically typed
languages like Go and Rust provide this layer in their stdlib and their whole
ecosystem can build on it.

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
%dune_build --release @install

%install
%dune_install --release

%check
%dune_check --release

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md

%changelog
* Wed Sep 18 2024 Anton Farygin <rider@altlinux.ru> 0.3-alt1
- first build for ALT
