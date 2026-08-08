%define _unpackaged_files_terminate_build 1
%define soname 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define oname meshoptimizer

Name:    lib%oname
Version: 1.2
Release: alt2
Summary: Mesh optimization library that makes meshes smaller and faster to render
Group:   Development/C++
License: MIT
URL:     https://github.com/zeux/meshoptimizer
Vcs:     https://github.com/zeux/meshoptimizer

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
When a GPU renders triangle meshes, various stages of the GPU pipeline have to
process vertex and index data. The efficiency of these stages depends on the
data you feed to them; this library provides algorithms to help optimize meshes
for these stages, as well as algorithms to reduce the mesh complexity and
storage overhead.

%package -n %name%soname
Summary: Mesh optimization library that makes meshes smaller and faster to render
Group:   System/Libraries
Provides: %name = %EVR

%description -n %name%soname
When a GPU renders triangle meshes, various stages of the GPU pipeline have to
process vertex and index data. The efficiency of these stages depends on the
data you feed to them; this library provides algorithms to help optimize meshes
for these stages, as well as algorithms to reduce the mesh complexity and
storage overhead.

%package devel
Summary: %name development headers and libraries
Group:   Development/C++

%description devel
%name development headers and libraries

%prep
%setup

%build
%cmake \
    -DMESHOPT_BUILD_SHARED_LIBS=ON \
    -DMESHOPT_SOVERSION=%soname \
    %nil
%cmake_build

%install
%cmakeinstall_std

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%soname.*

%files devel
%doc *.md
%_libdir/%name.so
%_includedir/%oname.h
%_libdir/cmake/%oname

%changelog
* Sat Aug 08 2026 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt2
- Enable shared libraries.

* Fri Aug 07 2026 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt1
- Initial build for ALTLinux.
