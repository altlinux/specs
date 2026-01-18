Name: ocaml-ocb
Version: 0.2
Release: alt1
Summary: SVG badge generator
Group: Development/ML
License: ISC
Url: https://ocamlpro.github.io/ocb/
VCS: https://github.com/OCamlPro/ocb
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.05
BuildRequires: dune >= 2.0
BuildRequires: ocaml-odoc-devel

%description
An OCaml library for SVG badge generation. There's also a command-line
tool provided.

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
%dune_build -p ocb

%install
%dune_install ocb

%files -f ocaml-files.runtime
%doc README.md
%_bindir/ocb

%files devel -f ocaml-files.devel

%changelog
* Sun Jan 18 2026 Anton Farygin <rider@altlinux.org> 0.2-alt1
- Initial build for ALT Linux.

