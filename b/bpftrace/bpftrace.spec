# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

# Based on https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

Name: bpftrace
Version: 0.25.1
Release: alt1
Summary: High-level tracing language for Linux
Group: Development/Debuggers
License: Apache-2.0
Url: https://bpftrace.org/
Vcs: https://github.com/bpftrace/bpftrace

Source: %name-%version.tar
Source1: libbpf-0.tar
ExclusiveArch: x86_64 aarch64 loongarch64 riscv64

%define llvm_ver 19
%define llvm_pkgver %llvm_ver.1
BuildRequires(pre): rpm-macros-cmake
BuildRequires: asciidoctor
BuildRequires: binutils-devel
BuildRequires: cereal-devel
BuildRequires: clang%llvm_pkgver-devel
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libbcc-devel
BuildRequires: libbpf-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libpcap-devel
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
BuildRequires: llvm%llvm_pkgver-devel
BuildRequires: /proc
BuildRequires: python3-module-setuptools
BuildRequires: xxd

# Assuming 'kernel' dependency will bring un-def kernel
%{?!_without_check:%{?!_disable_check:
BuildRequires(pre): rpm-build-kernel
BuildRequires: bc
BuildRequires: bpftool
BuildRequires: dwarves
BuildRequires: iproute2
BuildRequires: iputils
BuildRequires: kernel-headers-modules-%kernel_latest
BuildRequires: libgtest-devel
BuildRequires: python3(looseversion)
BuildRequires: rpm-build-vm
}}

%description
bpftrace is a general purpose tracing tool and language for Linux.
It leverages eBPF to provide powerful, efficient tracing capabilities
with minimal overhead. bpftrace uses LLVM as a compiler backend,
and libbpf for interacting with the Linux BPF subsystem, including
kernel dynamic tracing (kprobes, hardware and software perf events),
user-level dynamic tracing (USDT, uprobes), tracepoints (regular, raw),
and more. The bpftrace language is inspired by awk, C, and predecessor
tracers such as DTrace and SystemTap.

%prep
%setup
tar xf %SOURCE1 -C .

%build
# -DBUILD_TESTING:BOOL=ON will require googletest and try to clone it from github
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_disabled check
	-DBUILD_TESTING:BOOL=OFF \
%endif
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_DIR=$(llvm-config-%llvm_ver --cmakedir) \
	-DClang_DIR=$(llvm-config-%llvm_ver --cmakedir)/../clang \
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

# Clean up for %%doc docs
rm docs/coding_guidelines.md \
	docs/design_principles.md \
	docs/developers.md \
	docs/fuzzing.md \
	docs/nix.md \
	docs/release_process.md

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
	delete-blocks hardware	tests/runtime/probe
	delete-blocks testprogs	tests/runtime/*
%ifarch aarch64
	sed -i 's/xattr.h/user.h/' tests/runtime/basic
%endif
	vm-run --kvm=cond --sbin tests/runtime-tests.sh
fi

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md CHANGELOG.md docs
%_bindir/*
%_datadir/%name
%_man8dir/*
%_datadir/bash-completion/completions/bpftrace

%changelog
* Thu Mar 26 2026 Vitaly Chikunov <vt@altlinux.org> 0.25.1-alt1
- Update to v0.25.1 (2026-03-25).

* Sun Mar 22 2026 Vitaly Chikunov <vt@altlinux.org> 0.25.0-alt1
- Update to v0.25.0 (2026-03-13).

* Mon Dec 15 2025 Vitaly Chikunov <vt@altlinux.org> 0.24.2-alt1
- Update to v0.24.2 (2025-12-12).

* Fri Oct 10 2025 Vitaly Chikunov <vt@altlinux.org> 0.24.1-alt1
- Update to v0.24.1 (2025-10-03).
- spec: Build with gcc instead of clang.

* Sat Sep 20 2025 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt1
- Update to v0.24.0 (2025-09-17).

* Mon Jul 07 2025 Ivan A. Melnikov <iv@altlinux.org> 0.23.3-alt2
- NMU: build on riscv64

* Fri May 30 2025 Vitaly Chikunov <vt@altlinux.org> 0.23.3-alt1
- Update to v0.23.3 (2025-05-22).
- spec: Switch build to Clang/LLVM 19.

* Sat Apr 12 2025 Vitaly Chikunov <vt@altlinux.org> 0.23.1-alt1
- Update to v0.23.1 (2025-04-11).

* Wed Mar 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.23.0-alt1
- Update to v0.23.0 (2025-03-25).

* Fri Jan 17 2025 Vitaly Chikunov <vt@altlinux.org> 0.22.1-alt1
- Update to v0.22.1 (2025-01-16).

* Tue Dec 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.21.3-alt1
- Update to v0.21.3 (2024-12-16).
- spec: Fix FTBFS due to removal of un-def kernel flavour.
- spec: Switch build to Clang/LLVM 18.
- spec: Update Url.

* Sat Jul 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.21.2-alt1
- Update to v0.21.2 (2024-07-19).

* Wed Jun 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.21.1-alt1
- Update to v0.21.1 (2024-06-24).
- spec: Do not use lld, do not change LTO mode.

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
