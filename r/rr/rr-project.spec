# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
# Cannot be enabled due to librrpage.so:
#  %%define _stripped_files_terminate_build 1
#  %%set_verify_elf_method strict

Name:		rr
Version:	5.6.0
Release:	alt2
Summary:	Record and Replay Framework
Group:		Development/Debuggers
License:	MIT and BSD and Apache-2.0
URL:		https://rr-project.org/
Vcs:		https://github.com/rr-debugger/rr
# Upstream issue tracker: https://github.com/mozilla/rr/issues/

Source:		%name-%version.tar
ExclusiveArch:	x86_64 aarch64

Obsoletes:	rr-project < %EVR
Provides:	rr-project = %EVR
Requires:	gdb

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: capnproto-devel
BuildRequires: cmake
BuildRequires: gcc-c++
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

%prep
%setup

%build
# %%define optflags_lto %nil
# %%add_optflags -Wno-error=maybe-uninitialized
%cmake -Ddisable32bit=ON -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_datadir/rr/src

# By default, with `--strip-all` it strips `.replay.text` causing `rr replay` crash.
# https://github.com/rr-debugger/rr/issues/3364
%brp_strip_none %_libdir/rr/lib*.so

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md scripts/zen_workaround.py
%_bindir/rr
%_bindir/rr_exec_stub
%_bindir/signal-rr-recording.sh
%_bindir/rr-collect-symbols.py
%_datadir/rr
%_datadir/bash-completion/completions/rr
%_libdir/rr

%changelog
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

