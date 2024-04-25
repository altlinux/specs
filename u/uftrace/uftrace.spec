# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict unresolved=relaxed

Name: uftrace
Version: 0.16
Release: alt1
Summary: Function graph tracer for C/C++/Rust/Python
License: GPL-2.0-only
Group: Development/Debuggers
Url: https://uftrace.github.io/
Vcs: https://github.com/namhyung/uftrace
# armh:    mcount_estimate_return_depth  : FAIL
# ppc64le: Unsupported (ls arch).
ExclusiveArch: aarch64 %ix86 x86_64 riscv64
# Internal tracing helper
%add_python3_req_skip uftrace_python

Source: %name-%version.tar
BuildRequires: libcapstone-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libluajit-devel
BuildRequires: libncursesw-devel
BuildRequires: libpython3-devel
BuildRequires: libstdc++-devel
BuildRequires: libtraceevent-devel
BuildRequires: libunwind-devel
BuildRequires: pandoc
BuildRequires: rpm-build-python3
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
BuildRequires: python3
}}

%description
uftrace is a function call graph tracer for C, C++, Rust and Python
programs.

It hooks into the entry and exit of each function, recording timestamps as
well as the function's arguments and return values. uftrace is capable of
tracing both user and kernel functions, as well as library functions and
system events providing an integrated execution flow in a single timeline.

%prep
%setup
sed -i '1i\#! %__python3' python/uftrace.py

%build
%define optflags_lto %nil
# (Default) -Werror=unused-variable will cause libelf detection to fail.
%add_optflags -Wno-error=unused-variable %(getconf LFS_CFLAGS)
# Custom configure script.
%configure
%make_build V=1

%install
# Custom bash completions script, but lets put it in bash-completion dir anyway.
%makeinstall_std completiondir=%_datadir/bash-completion/completions V=1

%check
# Basic smoke testing.
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
gcc -pg -o hello tests/s-hello.c
uftrace ./hello
uftrace record ./hello
uftrace report
uftrace graph
uftrace info
# Upstream tests.
unset MAKEFLAGS
timeout 120 %make_build unittest V=1
# The following tests do not return test-case failure status.
%if 0
# x86: hasher-privd: parent: handle_io: idle time limit (3600 seconds) exceeded
# When too much parallelism:
#   mcount: /usr/src/RPM/BUILD/uftrace-0.14/libmcount/record.c:81:prepare_shmem_buffer
#    ERROR: mmap shmem buffer: No space left on device
[ ${NPROCS:=$(nproc)} -gt 8 ] && NPROCS=8
timeout 600 %make_build runtest V=1
%endif
timeout 120 %make_build pytest V=1

%files
%define _customdocdir %_docdir/%name
%doc COPYING CONTRIBUTING.md NEWS README.md TODO
%_bindir/uftrace
%_libdir/libmcount*.so
%_libdir/uftrace.py
%_libdir/uftrace_python.so
%_man1dir/uftrace*.1*
%_datadir/bash-completion/completions/uftrace

%changelog
* Thu Apr 25 2024 Vitaly Chikunov <vt@altlinux.org> 0.16-alt1
- Update to v0.16 (2024-04-24).

* Sat Jan 13 2024 Vitaly Chikunov <vt@altlinux.org> 0.15.1-alt1
- Update to v0.15.1 (2024-01-11).

* Mon Jan 08 2024 Vitaly Chikunov <vt@altlinux.org> 0.15-alt1
- Update to v0.15 (2024-01-07).

* Sat Dec 23 2023 Vitaly Chikunov <vt@altlinux.org> 0.14-alt1
- Update to v0.14-88-gad862218 (2023-12-19).
- Return package after removal by cleaner (14+ weeks x86_64 ftbfs).

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- new version 0.12 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- new version 0.11 (with rpmrb script)

* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version 0.10 (with rpmrb script)
- enable tests

* Tue Oct 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script)

* Tue Oct 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Sisyphus
