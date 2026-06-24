%define _unpackaged_files_terminate_build 1

Name: ananicy-cpp
Version: 1.2.0
Release: alt2

Summary: Rewrite of ananicy in c++ for lower cpu and memory usage

License: GPL-3.0-only
Group: System/Kernel and hardware
Url: https://gitlab.com/ananicy-cpp/ananicy-cpp

# Source-url: https://gitlab.com/ananicy-cpp/ananicy-cpp/-/archive/v%version/v%version.tar.gz
Source: %name-%version.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-cmake
BuildRequires: bpftool
BuildRequires: gcc-c++ clang
BuildRequires: cmake
BuildRequires: libfmt-devel
BuildRequires: nlohmann-json-devel
BuildRequires: libbpf-devel
BuildRequires: ninja-build
BuildRequires: libspdlog-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-devel
BuildRequires: libelf-devel
Requires: ananicy-rules

%description
%summary.

%prep
%setup

# partialy based on https://gitlab.com/ananicy-cpp/ananicy-cpp/-/merge_requests/42
%__subst '1a #include <unistd.h>' src/platform/linux/debug.cpp
%__subst '1a #include <unistd.h>' src/platform/linux/process.cpp
%__subst '1a #include <unistd.h>' src/platform/systemd/service.cpp
%__subst '1a #include <unistd.h>' src/tests/unit-core.cpp
%__subst '1a #include <unistd.h>' src/tests/unit-cpuset.cpp
%__subst '1a #include <cstdint>' src/platform/linux/backtrace.cpp
%__subst '1a #include <cstring>' src/utility/argument_parsing/argument.cpp
%__subst '1a #include <cstring>' src/platform/linux/singleton_process.cpp

%build
%cmake \
    -GNinja \
    -DENABLE_SYSTEMD=ON \
    -DUSE_BPF_PROC_IMPL=ON \
    -DBPF_BUILD_LIBBPF=OFF \
    -DUSE_EXTERNAL_FMTLIB=ON \
    -DUSE_EXTERNAL_JSON=ON \
    -DUSE_EXTERNAL_SPDLOG=ON \
    -DVERSION=%version
%cmake_build --target %name

%install
%cmake_install --component Runtime

%files
%doc LICENSE
%doc README.md
%_bindir/ananicy-cpp
%_unitdir/ananicy-cpp.service

%changelog
* Tue Jun 23 2026 Boris Yumankulov <boria138@altlinux.org> 1.2.0-alt2
- fix FTBFS

* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Thu Feb 12 2026 Ilya Sorochan <k0tran@altlinux.org> 1.1.1-alt2
- add pregenerated vmlinux.h for loongarch and riscv (fixes FTBFS)

* Wed Sep 10 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.1-alt1
- initial build for ALT Sisyphus


