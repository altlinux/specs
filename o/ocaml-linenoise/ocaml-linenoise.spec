Name: ocaml-linenoise
Version: 1.5.1
Release: alt1
Summary: Lightweight readline alternative
Group: Development/ML
License: BSD-3-clause
Url: https://github.com/ocaml-community/ocaml-linenoise
VCS: https://github.com/ocaml-community/ocaml-linenoise
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-odoc-devel

%description
Lightweight readline alternative

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
%dune_build -p linenoise

%install
%dune_install linenoise

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Jan 14 2026 Anton Farygin <rider@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux.

