Name: libsolv
Version: 0.7.22
Release: alt1

Summary: Library for solving packages and reading repositories
License: BSD
Group:   System/Libraries
Url:     https://github.com/openSUSE/libsolv

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: librpm-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: bzlib-devel
BuildRequires: liblzma-devel
BuildRequires: libzstd-devel

%description
This is libsolv, a free package dependency solver using a satisfiability
algorithm.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
%{summary}.

%package tools
Summary: Package dependency solver tools
Group: System/Configuration/Packaging

%description tools
%{summary}.

%prep
%setup

%build
%cmake -GNinja \
       -DENABLE_RPMDB=ON \
       -DENABLE_RPMDB_BYRPMHEADER=ON \
       -DENABLE_RPMDB_LIBRPM=ON \
       -DENABLE_RPMPKG_LIBRPM=ON \
       -DENABLE_RPMMD=ON \
       -DENABLE_COMPLEX_DEPS=ON \
       -DWITH_LIBXML2=ON \
       -DENABLE_LZMA_COMPRESSION=ON \
       -DENABLE_BZIP2_COMPRESSION=ON \
       -DENABLE_ZSTD_COMPRESSION=ON
       
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc CREDITS NEWS README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/solv
%_libdir/pkgconfig/*.pc
%_datadir/cmake/Modules/FindLibSolv.cmake
%_man3dir/*.3*

%files tools
%_bindir/*
%_man1dir/*.1*

%changelog
* Sun Oct 30 2022 Andrey Cherepanov <cas@altlinux.org> 0.7.22-alt1
- Initial build for Sisyphus
