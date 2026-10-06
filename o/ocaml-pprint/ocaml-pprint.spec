Name: ocaml-pprint
Version: 20230830
Release: alt1
Summary: A pretty-printing combinator library and rendering engine
Group: Development/ML
License: LGPL-2.0-only WITH OCaml-LGPL-linking-exception
Url: https://github.com/fpottier/pprint
VCS: https://github.com/fpottier/pprint
Source0: %name-%version.tar
BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml
BuildRequires: dune

%description
This library offers a set of combinators for building so-called
documents as well as an efficient engine for converting documents to a
textual, fixed-width format. The engine takes care of indentation and
line breaks, while respecting the constraints imposed by the structure
of the document and by the text width.

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
%dune_build -p pprint

%install
%dune_install pprint

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Oct 06 2026 Anton Farygin <rider@altlinux.org> 20230830-alt1
- Initial build for ALT Linux.

