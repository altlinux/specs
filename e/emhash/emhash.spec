%define _unpackaged_files_terminate_build 1
%define git 09fb043

Name:    emhash
Version: 20250817
Release: alt1.g%{git}
Summary: Fast and memory efficient c++ flat hash map/set
Group:   Development/C++
License: MIT
URL:     https://github.com/ktprime/emhash
Vcs:     https://github.com/ktprime/emhash

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
%ifarch aarch64
BuildRequires: sse2neon-devel
%endif

# x86 is not supported due type collision/overflow errors in
# benchmark code/third-party libs
ExclusiveArch: x86_64 aarch64

%description
Fast and memory efficient open addressing C++ flat hash table/map

%package devel
Summary: Fast and memory efficient c++ flat hash map/set
Group:   Development/C++
BuildArch: noarch

%description devel
Fast and memory efficient open addressing C++ flat hash table/map

%package benchmark
Summary: emhash benchmarks
Group:   Development/C++

%description benchmark
Fast and memory efficient open addressing C++ flat hash table/map
benchmarks.

%prep
%setup

# unbundle sse2neon
%ifarch aarch64
pushd thirdparty/emilib
ln -svf %_includedir/sse2neon.h ./
popd
%endif

%build
%cmake \
    -DCMAKE_INSTALL_INCLUDEDIR=%_includedir/%name \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir
%cmake_build

%install
%cmakeinstall_std
for n in e f h m s; do
    install -m755 -pD %_cmake__builddir/"$n"bench %buildroot%_bindir/"$n"bench
done
install -m755 -pD %_cmake__builddir/bs %buildroot%_bindir/bs
install -m755 -pD %_cmake__builddir/bi %buildroot%_bindir/bi

%files devel
%doc LICENSE README.md
%_includedir/%name
%_datadir/cmake/*

%files benchmark
%_bindir/*

%changelog
* Mon Aug 25 2025 L.A. Kostis <lakostis@altlinux.ru> 20250817-alt1.g09fb043
- aarch64: use system sse2neon.
- Initial build for ALTLinux.
