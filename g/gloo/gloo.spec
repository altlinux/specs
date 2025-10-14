%define _unpackaged_files_terminate_build 1

%define abiversion 0

%def_with doc
%def_with devel
%def_with mpich
%def_with mpi

%global mpi_list openmpi mpich

Name:    gloo
Version: 0.1.0
Release: alt1.gite348db90

Summary: Collective communications library with various primitives for multi-machine training
License: BSD-3-Clause
Group:   System/Libraries
Url:     https://github.com/pytorch/gloo

Source: %name-%version.tar

Patch0: 0001-gloo-CMake-fixes.patch

# Gloo can only be built on 64-bit systems.
ExcludeArch: %ix86

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-environment-modules
BuildRequires: gcc-c++
BuildRequires: environment-modules
BuildRequires: libhiredis-devel
BuildRequires: libuv-devel
BuildRequires: openmpi-devel
BuildRequires: rdma-core-devel
BuildRequires: redis-devel

Requires: lib%name-doc

%description
Gloo is a collective communications library. It comes with a number of
collective algorithms useful for machine learning applications. These
include a barrier, broadcast, and allreduce.

Transport of data between participating machines is abstracted so that
IP can be used at all times, or InifiniBand (or RoCE) when available.
In the latter case, if the InfiniBand transport is used, GPUDirect can
be used to accelerate cross machine GPU-to-GPU memory transfers.

Where applicable, algorithms have an implementation that works with
system memory buffers, and one that works with NVIDIA GPU memory buffers.
In the latter case, it is not necessary to copy memory between host and
device; this is taken care of by the algorithm implementations.

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
Gloo is a collective communications library. It comes with a number of
collective algorithms useful for machine learning applications. These
include a barrier, broadcast, and allreduce.

Transport of data between participating machines is abstracted so that
IP can be used at all times, or InifiniBand (or RoCE) when available.
In the latter case, if the InfiniBand transport is used, GPUDirect can
be used to accelerate cross machine GPU-to-GPU memory transfers.

Where applicable, algorithms have an implementation that works with
system memory buffers, and one that works with NVIDIA GPU memory buffers.
In the latter case, it is not necessary to copy memory between host and
device; this is taken care of by the algorithm implementations.

%if_with doc
%package -n lib%name-doc
Summary: Documentation and license for %name
Group: Documentation 
Buildarch: noarch

%description -n lib%name-doc
Documentation only package used by other packages for %name.
%endif

%if_with devel
%package -n lib%name-devel
Summary: Headers and libraries for %name
Requires: lib%name%abiversion = %EVR
Group: Development/C++

%description -n lib%name-devel
Libraries and headers for developing applications that use %name.
%endif

%if_with mpi 
%package -n lib%name-openmpi
Summary: Gloo - openmpi version
BuildRequires: openmpi-devel
Group: System/Libraries
Requires: lib%name-doc

%description -n lib%name-openmpi
Gloo is a collective communications library. It comes with a number of
collective algorithms useful for machine learning applications. These
include a barrier, broadcast, and allreduce.

Transport of data between participating machines is abstracted so that
IP can be used at all times, or InifiniBand (or RoCE) when available.
In the latter case, if the InfiniBand transport is used, GPUDirect can
be used to accelerate cross machine GPU-to-GPU memory transfers.

Where applicable, algorithms have an implementation that works with
system memory buffers, and one that works with NVIDIA GPU memory buffers.
In the latter case, it is not necessary to copy memory between host and
device; this is taken care of by the algorithm implementations.

This package can use openmpi as a backend.

%package -n lib%name-openmpi-devel
Summary: Development libraries and headers for %name-openmpi
Requires: lib%name-openmpi = %EVR
Group: Development/C++

%description -n lib%name-openmpi-devel 
Libraries and header files for developing applications
that use %name-openmpi.
%endif

%if_with mpich
%package -n lib%name-mpich
Summary: Gloo - mpich version
Group: System/Libraries
BuildRequires: mpich-devel
Requires: lib%name-doc

%description -n lib%name-mpich
Gloo is a collective communications library. It comes with a number of
collective algorithms useful for machine learning applications. These
include a barrier, broadcast, and allreduce.

Transport of data between participating machines is abstracted so that
IP can be used at all times, or InifiniBand (or RoCE) when available.
In the latter case, if the InfiniBand transport is used, GPUDirect can
be used to accelerate cross machine GPU-to-GPU memory transfers.

Where applicable, algorithms have an implementation that works with
system memory buffers, and one that works with NVIDIA GPU memory buffers.
In the latter case, it is not necessary to copy memory between host and
device; this is taken care of by the algorithm implementations.

This package can use mpich as a backend.

%package -n lib%name-mpich-devel
Summary: Development libraries and headers
Group: Development/C++
Requires: lib%name-mpich = %EVR

%description -n lib%name-mpich-devel
Libraries and header files for developing applications
that use %name-mpich.
%endif

%prep
%setup -n %name-%version
%autopatch -p1


%build
# Without MPI
%define _cmake__builddir build-nompi
%cmake -DBUILD_SHARED_LIBS=ON \
       -DUSE_IBVERBS=ON \
       -DUSE_MPI=OFF \
       -DUSE_LIBUV=OFF \
       -DUSE_REDIS=ON \
       -DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

# With mpich
%if_with mpich
%define _cmake__builddir build-mpich
%cmake  -DBUILD_SHARED_LIBS=ON \
       -DUSE_IBVERBS=ON \
       -DUSE_MPI=ON \
       -DUSE_LIBUV=OFF \
       -DUSE_REDIS=ON \
       -DCMAKE_INSTALL_PREFIX=%_libdir/mpich \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCMAKE_C_COMPILER=%_libdir/mpich/bin/mpicc \
       -DCMAKE_CXX_COMPILER=%_libdir/mpich/bin/mpicxx 
%cmake_build
%endif

# With openmpi
%if_with mpi
%define _cmake__builddir build-openmpi
%cmake -DBUILD_SHARED_LIBS=ON \
       -DUSE_IBVERBS=ON \
       -DUSE_MPI=ON \
       -DUSE_LIBUV=OFF \
       -DUSE_REDIS=ON \
       -DCMAKE_INSTALL_PREFIX=%_libdir/openmpi \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCMAKE_C_COMPILER=%_libdir/openmpi/bin/mpicc \
       -DCMAKE_CXX_COMPILER=%_libdir/openmpi/bin/mpicxx
%cmake_build
%endif

%install
%define _cmake__builddir build-nompi
%cmake_install

install -d %{buildroot}%{_datadir}/Gloo/docs
cp -a docs/* %{buildroot}%{_datadir}/Gloo/docs

%if_with mpich
%define _cmake__builddir build-mpich
%cmake_install
%endif

%if_with mpi
%define _cmake__builddir build-openmpi
%cmake_install
%endif

%if_with doc
%files -n lib%name-doc
%doc *.md LICENSE 
%dir %_datadir/Gloo
%doc %_datadir/Gloo/docs
%endif

%files -n lib%name%abiversion
%_libdir/lib%name.so.*

%if_with devel
%files -n lib%name-devel
%_includedir/%name
%_cmakedir/Gloo
%_libdir/lib%name.so
%endif

%if_with mpich

%files -n lib%name-mpich
%_libdir/mpich/lib/lib%name.so.*

%files -n lib%name-mpich-devel
%_libdir/mpich/lib/lib%name.so
%_libdir/mpich/lib/cmake/
%_libdir/mpich/include/

%endif

%if_with mpi

%files -n lib%name-openmpi
%_libdir/openmpi/lib/lib%name.so.*

%files -n lib%name-openmpi-devel
%_libdir/openmpi/lib/lib%name.so
%_libdir/openmpi/lib/cmake/
%_libdir/openmpi/include/

%endif

%changelog
* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 0.1.0-alt1.gite348db90
- Initial build for Sisyphus.
