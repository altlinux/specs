# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
# Cannot be enabled due to librrpage.so:
#  %%define _stripped_files_terminate_build 1
#  %%set_verify_elf_method strict

Name:		rr
Version: 5.8.0
Release: alt1
Summary:	Record and Replay Framework
Group:		Development/Debuggers
License:	MIT and BSD and Apache-2.0
URL:		https://rr-project.org/
Vcs:		https://github.com/rr-debugger/rr
# Upstream issue tracker: https://github.com/mozilla/rr/issues/
Obsoletes:	rr-project < %EVR
Provides:	rr-project = %EVR
Requires:	gdb
ExclusiveArch:	x86_64 aarch64
AutoReqProv: nopython

Source:		%name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: capnproto-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: patchelf
BuildRequires: python3-module-pexpect
BuildRequires: rpm-build-python
BuildRequires: rpm-build-python3
BuildRequires: zlib-devel

%description
rr is a lightweight tool for recording, replaying and debugging execution
of applications (trees of processes and threads). Debugging extends gdb
with very efficient reverse-execution, which in combination with standard
gdb/x86 features like hardware data watchpoints, makes debugging much
more fun.

rr currently requires either:

- An Intel CPU with Nehalem (2010) or later microarchitecture.
- Certain AMD Zen or later processors.
- Certain AArch64 microarchitectures (e.g. ARM Neoverse N1 or the Apple
  Silicon M-series).

# Version 5.8.0 is manually tested on i9-10900.
# 98% tests passed, 24 tests failed out of 1515
%package testsuite
Summary: Test suite for rr (debugger)
Group: Development/Other
Requires: rr = %EVR
AutoReqProv: nopython
Requires: ctest

%description testsuite
%summary.
Prerequisites:
- Supported hardware (Intel 64)
- echo 1 > /proc/sys/kernel/perf_event_paranoid
- echo 0 > /proc/sys/kernel/userns_restrict
# cd /usr/lib64/rr/testsuite/obj
# ctest

%package checkinstall
Summary: CI test for %name
Group: Development/Other
Requires(post): rr-testsuite = %EVR

%description checkinstall
%summary.

%prep
%setup

%build
# %%define optflags_lto %nil
# Workarounds for 5.6.0:
%add_optflags -Wno-error=redundant-move -Wno-error=maybe-uninitialized -Wno-error=dangling-reference
%cmake -Ddisable32bit=ON -DINSTALL_TESTSUITE=ON -Wno-dev
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_datadir/rr/src
# By default, with `--strip-all` it strips `.replay.text` causing `rr replay` crash.
# https://github.com/rr-debugger/rr/issues/3364
%brp_strip_none %_libdir/rr/librr*.so
# verify-elf: ERROR: ./usr/lib64/rr/testsuite/obj/bin/constructor: RPATH contains illegal entry "/usr/src/RPM/BUILD": /usr/src/RPM/BUILD/rr-5.6.0/x86_64-alt-linux/lib/rr
patchelf --set-rpath '%_libdir/rr' %buildroot%_libdir/rr/testsuite/obj/bin/constructor
patchelf --set-rpath '%_libdir/rr' %buildroot%_libdir/rr/testsuite/obj/bin/step_into_lib

# https://github.com/rr-debugger/rr/issues/3625#issuecomment-1763326259
# debuginfo should not be stripped out of testsuite.
# We cannot also make it R package because of cyclic dependence.
%add_debuginfo_skiplist %_libdir/rr/testsuite %_libdir/rr/libtest_lib*.so

%post checkinstall
set -ex
# librrpage should have special pages.
readelf -S %_libdir/rr/librrpage.so | grep -Fw '.record.text'
readelf -S %_libdir/rr/librrpage.so | grep -Fw '.replay.text'
# Tests in testsuite should be non-stripped.
file %_libdir/rr/libtest_lib.so | grep 'with debug_info, not stripped'
file %_libdir/rr/testsuite/obj/bin/alternate_thread_diversion | grep 'with debug_info, not stripped'

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md scripts/zen_workaround.* wiki
%_bindir/rr
%_bindir/rr_exec_stub
%_bindir/signal-rr-recording.sh
%_bindir/rr-collect-symbols.py
%_datadir/rr
%_datadir/bash-completion/completions/rr
%_libdir/rr
%exclude %_libdir/rr/libtest_lib*.so
%exclude %_libdir/rr/testsuite

%files testsuite
%_libdir/rr/libtest_lib*.so
%_libdir/rr/testsuite

%files checkinstall

%changelog
* Tue May 21 2024 Vitaly Chikunov <vt@altlinux.org> 5.8.0-alt1
- Update to 5.8.0 (2024-05-20).

* Mon Oct 16 2023 Vitaly Chikunov <vt@altlinux.org> 5.7.0-alt1
- Update to 5.7.0 (2023-10-03).
- Testsuite should not have debuginfo stripped or separated.
- Install wiki (markdown) pages into %%doc.
- spec: Add checkinstall package.

* Sun Oct 01 2023 Vitaly Chikunov <vt@altlinux.org> 5.6.0-alt4
- Package testsuite.

* Sun Jul 16 2023 Vitaly Chikunov <vt@altlinux.org> 5.6.0-alt3
- Workaround ALT beekeeper rebuild failures (gcc13).

* Sat Nov 05 2022 Vitaly Chikunov <vt@altlinux.org> 5.6.0-alt2
- Fix rebuild after kernel headers update in v6.0.

* Tue Aug 16 2022 Vitaly Chikunov <vt@altlinux.org> 5.6.0-alt1
- Update to 5.6.0-10-g336edc30 (2022-08-16).

* Wed Oct 13 2021 Vitaly Chikunov <vt@altlinux.org> 5.5.0-alt2
- Do not install librraudit.so (fixes build for glibc-2.34).

* Sat Oct 09 2021 Vitaly Chikunov <vt@altlinux.org> 5.5.0-alt1
- Update to 5.5.0 (2021-09-20).

* Sat Jun 12 2021 Arseny Maslennikov <arseny@altlinux.org> 5.4.0-alt3
- NMU: spec: adapt to new cmake macros.

* Sun Dec 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt2
- spec: Temporary disable '-Werror=class-memaccess'.
- spec: Update licenses.

* Thu Oct 29 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt1
- Update to 5.4.0 (2020-10-29).
- spec: Rename from rr-project to rr.

* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.3.0-alt1
- Update to 5.3.0.

* Sat Nov 30 2019 Vitaly Chikunov <vt@altlinux.org> 5.2.0.0.253.g4c734005-alt1
- Update to 5.2.0-253-g4c734005.

* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 5.2.0-alt1
- First build of rr for ALT.

