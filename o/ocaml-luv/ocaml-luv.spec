# LUV_USE_SYSTEM_LIBUV=yes no more works for tests
%def_without check
%ifarch %ocaml_native_arch
%define relax %nil
%else
%define relax ||:
%endif
%define  modulename luv
Name:    ocaml-%modulename
Version: 0.5.14
Release: alt1
Summary: Binding to libuv for ocaml: cross-platform asynchronous I/O
License: MIT
Group:   Development/ML
URL:     https://github.com/aantron/luv
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune
BuildRequires: libuv-devel >= 1.48.0-alt2
%if_with check
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-alcotest-devel
%endif
BuildRequires: ocaml-ctypes-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6


%description
%name is a binding to libuv, the cross-platform C library that does asynchronous
I/O in Node.js and runs its main loop.

Besides asynchronous I/O, libuv also supports multiprocessing and
multithreading. Multiple event loops can be run in different threads. libuv also
exposes a lot of other functionality, amounting to a full OS API, and an
alternative to the standard module Unix.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
export LUV_USE_SYSTEM_LIBUV=yes
%dune_build -p %modulename,luv_unix

%install
%dune_install %modulename luv_unix

%check
export LUV_USE_SYSTEM_LIBUV=yes
export TRAVIS=true
# remove version test, broken in upstream
rm -f test/version.ml
sed -i '/Version\.tests\;/d' test/tester.ml
%dune_check -p %modulename,luv_unix %relax

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Sep 16 2024 Anton Farygin <rider@altlinux.ru> 0.5.14-alt1
- 0.5.14

* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 0.5.13-alt1
- 0.5.13

* Fri Nov 17 2023 Anton Farygin <rider@altlinux.ru> 0.5.12-alt2
- relaxed tests when ocaml in bytecode-only

* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 0.5.12-alt1
- 0.5.12

* Sun Feb 20 2022 Anton Farygin <rider@altlinux.ru> 0.5.11-alt1
- 0.5.11

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 0.5.10-alt1
- 0.5.10

* Thu Jul 29 2021 Anton Farygin <rider@altlinux.ru> 0.5.8-alt2
- increased version libluv in tests to fix the build with libluv 1.41.1

* Mon May 17 2021 Anton Farygin <rider@altlinux.ru> 0.5.8-alt1
- 0.5.8

* Fri Mar 12 2021 Anton Farygin <rider@altlinux.org> 0.5.7-alt2
- libuv-1.41.0-alt2 was built without assertions and this change made it
  possible to enable tests
- added patches from upstream with fixes for testing on non-x86 architectures

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 0.5.7-alt1
- first build for ALT
