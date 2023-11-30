# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: ocaml-parmap
Version: 1.2.5
Release: alt1
Summary: Small OCaml library allowing to exploit multicore architectures
Group: Development/ML
# Parmap is distributed under the LGPL licence version 2, with the usual special linking exception to section 6 for OCaml programs.
License: LGPL-2.0 with OCaml-LGPL-linking-exception
Url: http://rdicosmo.github.io/parmap/
Vcs: https://github.com/rdicosmo/parmap

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-ocaml
BuildRequires: dune
BuildRequires: ocaml
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-result-devel

%description
Parmap is a minimalistic library allowing to exploit multicore
architectures for OCaml programs with minimal modifications.

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
%dune_build -p parmap

%install
%dune_install

%check
# `dune runtests' actually are very CPU intensive benchmarks ('scale' tests),
# and we don't need to run benchmarks for integration testing. Run single and
# fastest test just to be sure parmap is working at all.
dune exec -p parmap tests/simplescalefold.exe

%files -f ocaml-files.runtime
%_docdir/parmap
%_libdir/ocaml/stublibs/dllparmap_stubs.so*

%files devel -f ocaml-files.devel

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed Sep 08 2021 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Mar 30 2021 Anton Farygin <rider@altlinux.org> 1.2-alt2
- spec: added build flags from the dune project when starting the test

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 1.2-alt1
- 1.1.1 -> 1.2
- specfile BR: ocaml-dune-devel renamed to ocaml-dune-configurator-devel
- specfile build and install: use macros from rpm-build-ocaml 1.4

* Sat Oct 17 2020 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt3
- spec: Fix Beekeeper rebuild and minor spec changes.
- Update to latest upstream patches (fix build warnings only).

* Thu May 14 2020 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt2
- spec: Fix beekeeper rebuild kill by removing benchmark tests in %%check.

* Fri Feb 07 2020 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 1.0-alt3.rc10
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.rc10
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt1.rc10
- up to 1.0-rc10
- rebuilt with ocaml 4.07

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1.rc9
- First build of ocaml-parmap for ALT.

