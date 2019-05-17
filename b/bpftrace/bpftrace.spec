# Based on https://github.com/iovisor/bpftrace/blob/master/INSTALL.md

Name:		bpftrace
Version:	0.9.0.0.169.ga4bf870
Release:	alt1
Summary:	High-level tracing language for Linux eBPF
Group:		Development/Debuggers
License:	ASL 2.0
URL:		https://github.com/iovisor/bpftrace
Source:		%name-%version.tar
ExclusiveArch:	x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires:	bison
BuildRequires:	cmake >= 3.0.0
BuildRequires:	flex
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	clang-devel >= 5.0.0
BuildRequires:	llvm-devel >= 5.0.0
BuildRequires:	lld
BuildRequires:	llvm-devel-static
BuildRequires:	clang-devel-static
BuildRequires:	/proc
BuildRequires:	libbcc-devel
BuildRequires:	libelf-devel
BuildRequires:	git-core

%description
BPFtrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). BPFtrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for interacting
with the Linux BPF system, as well as existing Linux tracing capabilities:
kernel dynamic tracing (kprobes), user-level dynamic tracing (uprobes), and
tracepoints. The BPFtrace language is inspired by awk and C, and predecessor
tracers such as DTrace and SystemTap.

See http://www.brendangregg.com/blog/2018-10-08/dtrace-for-linux-2018.html

%prep
%setup -q

%build
%remove_optflags -frecord-gcc-switches
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
export Clang_DIR=/usr/share/cmake/Modules/clang
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_TESTING:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DOFFLINE_BUILDS:BOOL=ON

%cmake_build bpftrace

%install
%set_verify_elf_method relaxed
%cmake_install install/strip DESTDIR=%buildroot
mkdir -p %buildroot%_man8dir
mv %buildroot/usr/man/man8/* %buildroot%_man8dir

%files
%doc LICENSE README.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%_bindir/*
%_datadir/%name
%_man8dir/*

%changelog
* Fri May 17 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.0.0.169.ga4bf870-alt1
- First import v0.9-169-ga4bf870.
