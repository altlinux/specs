Name: ocaml-monolith
Version: 20250922
Release: alt1
Summary: A framework for strong random testing of OCaml libraries
Group: Development/ML
License: LGPL-3.0-or-later
Url: https://gitlab.inria.fr/fpottier/monolith/
VCS: https://gitlab.inria.fr/fpottier/monolith
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.12
BuildRequires: dune >= 3.11

BuildRequires: ocaml-afl-persistent-devel >= 1.3
BuildRequires: ocaml-pprint-devel >= 20200410
BuildRequires: ocaml-odoc-devel

%description
A framework for strong random testing of OCaml libraries

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
%dune_build -p monolith

%install
%dune_install monolith

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel
%_libdir/ocaml/monolith/Makefile.monolith

%changelog
* Tue Oct 06 2026 Anton Farygin <rider@altlinux.org> 20250922-alt1
- initial build for ALT Linux
