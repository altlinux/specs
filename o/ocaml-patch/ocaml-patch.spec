%def_with check
Name: ocaml-patch
Version: 3.1.1
Release: alt1
Summary: Patch library purely in OCaml
Group: Development/ML
License: ISC
Url: https://github.com/hannesm/patch
VCS: https://github.com/hannesm/patch
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.08
BuildRequires: dune >= 3.0

%if_with check
BuildRequires: ocaml-alcotest-devel >= 1.7.0
BuildRequires: ocaml-crowbar-devel
%endif

%description
This is a library which parses unified diff and git diff output, and can
apply a patch in memory.

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
%dune_build -p patch

%install
%dune_install patch

%check
%dune_check -p patch

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Wed May 06 2026 Anton Farygin <rider@altlinux.org> 3.1.1-alt1
- 3.1.0 -> 3.1.1

* Thu Dec 25 2025 Anton Farygin <rider@altlinux.org> 3.1.0-alt1
- Initial build for ALT Linux.

