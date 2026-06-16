%define  modulename version
%def_with check

Name:    ocaml-%modulename
Version: 4.1.2
Release: alt1
Summary: Manipulate, parse and generate OCaml compiler version strings
License: ISC
Group:   Development/ML
URL:     https://github.com/ocurrent/ocaml-version
VCS: https://github.com/ocurrent/ocaml-version
BuildRequires: dune ocaml-alcotest-devel ocaml-odoc-devel
Source:  %name-%version.tar

%description
This library provides facilities to parse version numbers of the OCaml compiler,
and enumerates the various official OCaml releases and configuration variants.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Jun 16 2026 Anton Farygin <rider@altlinux.org> 4.1.2-alt1
- 4.1.1 -> 4.1.2

* Tue May 26 2026 Anton Farygin <rider@altlinux.org> 4.1.1-alt1
- 4.1.0 -> 4.1.1

* Tue Apr 21 2026 Anton Farygin <rider@altlinux.org> 4.1.0-alt1
- 4.0.4 -> 4.1.0

* Mon Mar 30 2026 Anton Farygin <rider@altlinux.org> 4.0.4-alt1
- 4.0.3 -> 4.0.4

* Sun Feb 22 2026 Anton Farygin <rider@altlinux.org> 4.0.3-alt1
- 3.7.3 -> 4.0.3

* Fri Jan 17 2025 Anton Farygin <rider@altlinux.ru> 3.7.3-alt1
- 3.6.8 -> 3.7.3

* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 3.6.8-alt1
- 3.6.2 -> 3.6.8

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 3.6.2-alt1
- first build for ALT
