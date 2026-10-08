%define _unpackaged_files_terminate_build 1
%define libname libvsgPoints
%define sover 0

Name:    vsgPoints
Version: 0.7.0
Release: alt1

Summary: VulkanSceneGraph library and example suite for rendering point clouds
License: MIT
Group:   Other
Url:     https://github.com/vsg-dev/vsgPoints
VCS:     https://github.com/vsg-dev/vsgPoints.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: glslang-devel
BuildRequires: libvsg-devel
BuildRequires: libvsgXchange-devel
BuildRequires: vulkan-devel

%description
Cross platform, open source (MIT license) C++17 library and example set
for rendering large point cloud data using VulkanSceneGraph. vsgPoints
provides support for generating hierarchical LOD and paged LOD scene
graph hierarchies to provide excellent performance and scalability. The
support for database paging enables handling of very large point
databases, over a billion point datasets run at a solid 60fps even on
integrated GPUs.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Def files and headers fore %name
Group: Development/C++

%description -n %libname-devel
%summary.


%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%_bindir/*

%files -n %libname%sover
%_libdir/%libname.so.%sover.*
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%changelog
* Wed Oct 07 2026 Artem Semenov <savoptik@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
