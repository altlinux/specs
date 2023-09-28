Name: xdp-tools
Version: 1.3.1
Release: alt2
Summary: Utilities and example programs for use with XDP
License: GPL-2.0 and LGPL-2.1 and BSD-2-Clause
Group: Development/Tools
URL: https://github.com/xdp-project/xdp-tools

Source0: xdp-tools-%{version}.tar

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define llvm_version 16.0

%add_debuginfo_skiplist  %_libdir/bpf/*.o
%add_verify_elf_skiplist %_libdir/bpf/*.o
%brp_strip_none          %_libdir/bpf/*
%set_verify_elf_method strict

BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-devel
BuildRequires: llvm%llvm_version-devel

BuildRequires: bpftool
BuildRequires: m4
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: pkgconfig(libbpf)
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(zlib)

# Always keep xdp-tools and libxdp packages in sync
Requires: libxdp = %{version}-%{release}

%description
Utilities and example programs for use with XDP.

%package -n libxdp
Summary: XDP helper library
Group: System/Libraries

%description -n libxdp
The libxdp package contains the libxdp library for managing XDP programs,
used by the %{name} package


%package -n libxdp-devel
Summary: Development files for libxdp
Group: Development/C
Requires: libxdp = %{version}-%{release}

%description -n libxdp-devel
The libxdp-devel package contains headers used for building XDP programs using
libxdp.


%prep
%setup -q
%autopatch -p1


%build
export LIBDIR='%_libdir'
export CLANG=clang
export LLC=llc
export BPFTOOL='%_sbindir/bpftool'
export PRODUCTION=1
export DYNAMIC_LIBXDP=1
export FORCE_SYSTEM_LIBBPF=1
export ALTWRAP_LLVM_VERSION="%llvm_version"

./configure
make V=1


%install
export DESTDIR='%buildroot'
export SBINDIR='%_sbindir'
export LIBDIR='%_libdir'
export MANDIR='%_mandir'
export DATADIR='%_datadir'
export HDRDIR='%_includedir/xdp'

for target in lib/libxdp xdp-filter xdp-loader xdp-dump xdp-bench xdp-monitor xdp-trafficgen;
do
	make -C "$target" install V=1
done

# test scripts
rm -rf -- %buildroot%_datadir/xdp-tools

# static libs
rm -f -- %buildroot%_libdir/*.a


%files
%_sbindir/xdp-filter
%_sbindir/xdp-loader
%_sbindir/xdpdump
%_sbindir/xdp-bench
%_sbindir/xdp-monitor
%_sbindir/xdp-trafficgen
%_libdir/bpf/xdpfilt_*.o
%_libdir/bpf/xdpdump_*.o
%_man8dir/*

%files -n libxdp
%_libdir/*.so.*
%dir %_libdir/bpf
%_libdir/bpf/xdp-dispatcher.o
%_libdir/bpf/xsk_def_xdp_prog*.o
%_man3dir/*

%files -n libxdp-devel
%_includedir/xdp
%_libdir/*.so
%_libdir/pkgconfig/libxdp.pc

%changelog
* Thu Sep 28 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3.1-alt2
- Build with clang/llvm 16 (earlier versions can't target LoongArch).

* Tue May 30 2023 Alexey Gladkov <legion@altlinux.ru> 1.3.1-alt1
- First build.


