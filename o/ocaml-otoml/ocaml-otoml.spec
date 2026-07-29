%def_with check
Name: ocaml-otoml
Version: 1.0.5
Release: alt1
Summary: TOML parsing, manipulation, and pretty-printing library (1.0.0-compliant)
Group: Development/ML
License: MIT
Url: https://github.com/dmbaturin/otoml
VCS: https://github.com/dmbaturin/otoml
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml
BuildRequires: dune

BuildRequires: ocaml-menhir
BuildRequires: ocaml-uutf-devel >= 1.0.0
BuildRequires: ocaml-odoc-devel

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
OTOML is a library for parsing, manipulating, and pretty-printing TOML
files.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p otoml

%install
%dune_install otoml

%check
%dune_check -p otoml

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed Jul 29 2026 Anton Farygin <rider@altlinux.org> 1.0.5-alt1
- Initial build for ALT Linux.

