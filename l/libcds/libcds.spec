%ifarch x86_64
%define archbit 64
%else
%define archbit 32
%endif

Name: libcds
Version: 1.6.0
Release: alt1

Summary: C++ template library of lock-free and fine-grained algorithms

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://libcds.sourceforge.net/
Group: System/Libraries
License: BSD like

# Source-url: http://prdownloads.sourceforge.net/libcds/cds-%version/cds-%version.tar.gz
Source: %name-%version.tar

# manually removed:  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Tue Dec 09 2014
# optimized out: libcloog-isl4 libstdc++-devel python3-base
BuildRequires: boost-devel-headers boost-intrusive-devel gcc-c++ libdb4-devel

%package devel
Group: Development/Other
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
The %name-devel package provides header files for %name.


%description
CDS is a C++ template library of lock-free and fine-grained algorithms.
It contains a collection of concurrent data structure implementations:

Atomic operations with memory ordering support for x86, amd64, Itanium, Sparc processor architectures
Safe memory reclamation (SMR) algorithms:
    Michael's Hazard Pointer
    Pass-the-Buck SMR
    Gidenstam's Hazard Pointer with reference counting
    User-space RCU
Data structures - a lot of intrusive and non-intrusive container algorithms for different SMR schemas
    intrusive and non-intrusive stacks
    intrusive and non-intrusive queues: Michael & Scott lock-free and read/write lock-based,
      Moir et al algo, Ladan-Mozes & Shavit optimistic queue, basket queue, bounded (ring-buffered) algos
    intrusive and non-intrusive deque: Michael's algo
    intrusive and non-intrusive ordered lists: Michael's algo, Lazy list algo
    intrusive and non-intrusive sets and maps: Michael hash-map,
      Split-ordere list by Ori Shalev & Nir Shavit, Skip-list, Cuckoo hash map/set 
Synchronization primitives - spin-lock with different back-off technique
Michael's memory allocator. See cds::memory::michael::Heap in documentation


%prep
%setup

%build
cd build
# tried to build test files in anyway, so ok for all
export CDS_PLATFORM_DEBUG_LDFLAGS=-lpthread
./build.sh -t release -o linux -z "%optflags" -b %archbit || :

%install
mkdir -p %buildroot%_libdir/
cp bin/gcc*/%{name}.so %buildroot%_libdir/
cp bin/gcc*/%{name}.so.* %buildroot%_libdir/
mkdir -p %buildroot%_includedir/
cp -a cds/ %buildroot%_includedir/

%files
%_libdir/%{name}.so.*

%files devel
%_libdir/%{name}.so
%_includedir/cds/

%changelog
* Tue Dec 09 2014 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- initial build for ALT Linux Sisyphus

