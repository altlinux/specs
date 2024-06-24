# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%ifarch loongarch64
# XXX: only lld supports thin LTO. However
# - as of LLVM 16 lld does not support LoongArch targets at all
# - as of LLVM 17 lld does not support LoongArch relocations properly
#   and is unable to link with libraries produced by GNU ld (i.e. glibc)
%def_without lld
%define optflags_lto %nil
%else
%def_with lld
%define optflags_lto -flto=thin
%endif

# Based on https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

Name: bpftrace
Version: 0.21.0
Release: alt1
Summary: High-level tracing language for Linux eBPF
Group: Development/Debuggers
License: Apache-2.0
URL: https://github.com/iovisor/bpftrace
# Docs: https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md
# Docs: https://github.com/iovisor/bpftrace/blob/master/docs/tutorial_one_liners.md
# Docs: http://www.brendangregg.com/BPF/bpftrace-cheat-sheet.html
# Docs: http://www.brendangregg.com/ebpf.html#bpftrace
# PR: https://lwn.net/Articles/793749/
# PR: http://www.brendangregg.com/blog/2018-10-08/dtrace-for-linux-2018.html

Source: %name-%version.tar
ExclusiveArch:	x86_64 aarch64 loongarch64

%define llvm_ver 17
%define llvm_pkgver %llvm_ver.0
BuildRequires(pre): rpm-macros-cmake
BuildRequires: asciidoctor
BuildRequires: binutils-devel
BuildRequires: cereal-devel
BuildRequires: clang%llvm_pkgver-devel
BuildRequires: cmake
BuildRequires: flex
BuildRequires: libbcc-devel
BuildRequires: libbpf-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libpcap-devel
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
%if_with lld
BuildRequires: lld%llvm_pkgver
%endif
BuildRequires: llvm%llvm_pkgver-devel
BuildRequires: /proc
BuildRequires: python3-module-setuptools
BuildRequires: systemtap-sdt-devel
BuildRequires: xxd

# Assuming 'kernel' dependency will bring un-def kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires: dwarves
BuildRequires: kernel-headers-modules-un-def
BuildRequires: libgtest-devel
BuildRequires: rpm-build-vm
}}

%description
bpftrace is a high-level tracing language for Linux enhanced Berkeley
Packet Filter (eBPF) available in recent Linux kernels (4.x). bpftrace
uses LLVM as a backend to compile scripts to BPF-bytecode and makes use of
BCC for interacting with the Linux BPF system, as well as existing Linux
tracing capabilities: kernel dynamic tracing (kprobes), user-level dynamic
tracing (uprobes), and tracepoints. The bpftrace language is inspired by
awk and C, and predecessor tracers such as DTrace and SystemTap. bpftrace
was created by Alastair Robertson.

%prep
%setup
sed -i 's/@.*@/True/' tests/runtime/engine/cmake_vars.py

%build
%remove_optflags -frecord-gcc-switches
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
%if_with lld
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export Clang_DIR=/usr/share/cmake/Modules/clang
# -DBUILD_TESTING:BOOL=ON will require googletest and try to clone it from github
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_disabled check
	-DBUILD_TESTING:BOOL=OFF \
%endif
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_DIR=$(llvm-config-%llvm_ver --cmakedir) \
	-DLLVM_REQUESTED_VERSION=%llvm_ver \
	-DOFFLINE_BUILDS:BOOL=ON \
	-DALLOW_UNSAFE_PROBE:BOOL=ON \
	-DUSE_SYSTEM_BPF_BCC:BOOL=ON \
	%nil
%cmake_build

%install
%cmake_install
find %buildroot%_datadir/%name/tools -name '*.bt' | xargs chmod a+x

# Fix man pages.
pushd %buildroot%_man8dir
 rename '' bpftrace- *.gz
 rename bpftrace-bpftrace bpftrace bpftrace-bpftrace*.gz
popd

# Need to keep BEGIN_trigger and END_trigger
# https://github.com/iovisor/bpftrace/issues/954
%brp_strip_debug %_bindir/bpftrace

%check
%_cmake__builddir/src/bpftrace --version	 # not requires root
vm-run %_cmake__builddir/src/bpftrace --info # should be fast enough even w/o kvm
vm-run --kvm=cond %_cmake__builddir/src/bpftrace -l 'kprobe:*_sleep_*'
if kvm-ok; then
	PATH=$PWD/.gear:$PATH
	cd %_cmake__builddir
	delete-blocks casted	tests/runtime/intcast
	delete-blocks kfunc	tests/runtime/call
	delete-blocks kprobe_offset_fail_size	tests/runtime/probe
	delete-blocks testprogs	tests/runtime/*
	delete-blocks tracetest_testprobe_semaphore	tests/runtime/usdt
	delete-blocks uaddr	tests/runtime/call
	delete-blocks watchpoint	tests/runtime/watchpoint
%ifarch aarch64
	delete-blocks kfunc	tests/runtime/regression
	delete-blocks task	tests/runtime/basic
	sed -i 's/xattr.h/user.h/' tests/runtime/basic
%endif
	vm-run --kvm=cond --sbin tests/runtime-tests.sh
fi

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%_bindir/*
%_datadir/%name
%_man8dir/*

%changelog
* Mon Jun 24 2024 Vitaly Chikunov <vt@altlinux.org> 0.21.0-alt1
- Update to v0.21.0 (2024-06-21).

* Sun May 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.20.4-alt1
- Update to v0.20.4 (2024-05-21).

* Mon Apr 22 2024 Vitaly Chikunov <vt@altlinux.org> 0.20.3-alt2
- Fix FTBFS Do not build with Clang/LLVM 18.

* Thu Apr 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.20.3-alt1
- Update to v0.20.3 (2024-03-25).

* Sun Mar 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.20.2-alt1
- Update to v0.20.2 (2024-03-07).
- Fix potential security issue with kheader unpacking.

* Sat Mar 09 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.20.1-alt2
- NMU: fixed FTBFS on LoongArch

* Sun Mar 03 2024 Vitaly Chikunov <vt@altlinux.org> 0.20.1-alt1
- Update to v0.20.1 (2024-01-29).

* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 0.19.1-alt2
- Fixed FTBFS.

* Sun Nov 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.19.1-alt1
- Update to v0.19.1 (2023-10-04).

* Wed Aug 30 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt3
- Fix FTBFS errors and crash for LLVM 15.

* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt2
- Fix SIGSEGV when vmlinux is not available and loading BTF data failed.

* Sun Oct 09 2022 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt1
- Update to v0.16.0 (2022-08-30).

* Sat May 28 2022 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- Updated to v0.15.0 (2022-05-24).

* Fri Jan 21 2022 Vitaly Chikunov <vt@altlinux.org> 0.13.1-alt1
- Updated to v0.13.1 (2021-12-21).
- Do not strip BEGIN/END triggers from bpftrace (closes: #41750).

* Thu Sep 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.12.1-alt3
- Rebuilt with LTO.

* Wed May 12 2021 Arseny Maslennikov <arseny@altlinux.org> 0.12.1-alt2
- NMU: spec: adapt to new cmake macros.

* Fri Apr 30 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.1-alt1
- Update to v0.12.1 (2021-04-16).
- spec: Build with default Clang/LLVM (>= 11).

* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.4-alt1
- Update to v0.11.4 (2020-11-13).

* Tue Aug 25 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt3
- Rename man pages with bpftrace- prefix.
- Rebuild with debuginfo.

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt2
- Rebuild with clang10.

* Fri Jul 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt1
- Update to v0.11.0.

* Sat Jul 04 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt2
- Fix build with libbcc-devel-0.15.0.

* Wed Apr 15 2020 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to v0.10.0 released at 2020-04-12. New features: kfuncs,
  C++ Symbol demangling, if-else control flow.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt2
- spec: Rework BuildRequires.

* Sat Mar 14 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Update to v0.9.4.
- Update license tag from ASL 2.0 to Apache-2.0.
- Add %%check with some tests.

* Fri May 17 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.169.ga4bf870-alt1
- First import v0.9-169-ga4bf870.
