Name: ocaml-javalib
Version: 3.2.2
Release: alt1.gitae04c6b3

Summary: Parses Java .class files into OCaml data structures
Group: Development/ML
License: LGPL-2.1
Url: https://github.com/javalib-team/javalib
Vcs: https://github.com/javalib-team/javalib

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ocaml
BuildRequires: dune
BuildRequires: ocaml-camlzip-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-ppx_inline_test-devel

%description
Javalib is a library that parses Java .class files into OCaml data structures.
Javalib offers primitives to extract information from, manipulate,
and generate valid .class files.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build

%install
%dune_install

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc LICENSE CHANGELOG README.md

%changelog
* Tue Apr 29 2025 Denis Rastyogin <gerben@altlinux.org> 3.2.2-alt1.gitae04c6b3
- Initial build for ALT Sisyphus.
