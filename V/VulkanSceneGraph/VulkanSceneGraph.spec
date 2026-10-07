%define _unpackaged_files_terminate_build 1
%define sover 1
%define libname libvsg

Name: VulkanSceneGraph
Version: 1.1.16
Release: alt1

Summary: Vulkan & C++17 based Scene Graph Project
License: MIT
Group: System/Libraries
Url: https://www.vulkanscenegraph.org
VCS: https://github.com/vsg-dev/VulkanSceneGraph

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libvulkan-devel
BuildRequires: glslang-devel
BuildRequires: libxcb-devel

%description
VulkanSceneGraph (VSG), is a modern, cross platform, high performance scene
graph library built upon Vulkan graphics/compute API. The software is written in
C++17, and follows the CppCoreGuidelines and FOSS Best Practices.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Dev files an headers fore %name
Group: Development/C
Provides: %name-devel = %EVR

%description -n %libname-devel
%summary.

%prep
%setup

%__subst 's/set(VSG_SOVERSION 17)/set(VSG_SOVERSION 1)/' CMakeLists.txt

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%files -n %libname%sover
%_libdir/%libname.so.%sover.*
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%changelog
* Tue Oct 06 2026 Artem Semenov <savoptik@altlinux.org> 1.1.16-alt1
- Initial build for Sisyphus.
