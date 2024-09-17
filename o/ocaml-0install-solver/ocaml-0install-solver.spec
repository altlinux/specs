%def_with check
%define ocamlmod 0install-solver
Name: ocaml-%ocamlmod
Version: 2.17
Release: alt1
Summary: Package dependency solver
Group: Development/ML
License: LGPL-2.1
Url: https://github.com/0install/0install
VCS: https://github.com/0install/0install
Source0: %name-%version.tar
BuildRequires: ocaml >= 5.2.0
BuildRequires: ocaml-compiler-libs >= 5.2.0
BuildRequires: dune

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
A package dependency resolver based on a SAT solver. This was originally
written for the 0install package manager, but is now generic and is also used
as a solver backend for opam.
The SAT solver is based on MiniSat (http://minisat.se/Papers.html) and
the application to package management is based on OPIUM (Optimal Package
Install/Uninstall Manager). 0install-solver uses a (novel?) strategy to find
the optimal solution extremely quickly (even for a SAT-based solver).

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
%dune_build -p %ocamlmod

%install
%dune_install %ocamlmod

%check
%dune_check -p %ocamlmod

%files -f ocaml-files.runtime
%doc COPYING

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md

%changelog
* Tue Sep 17 2024 Anton Farygin <rider@altlinux.ru> 2.17-alt1
- first build for ALT
