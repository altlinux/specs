%define _unpackaged_files_terminate_build 1
%define sover 0
%define libname libosg2vsg
%define pluginsVersion 3.6.5

Name: osg2vsg
Version: 0.4.0
Release: alt1

Summary: Adapter library for converting OpenSceneGraph Images and 3D models to VulkanSceneGraph
License: MIT
Group:   Other
Url:     https://github.com/vsg-dev/osg2vsg

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libGL-devel
BuildRequires: libvsg-devel
BuildRequires: vulkan-devel

%description
osg2vsg is a small utility library with tools that convert OpenSceneGraph
images and 3D models into VSG and Vulkan equivalents, and provide
integration between OpenSceneGraph with OpenGL and VulkanSceneGraph with
Vulkan.

%package -n %libname%sover
Summary: Lib files fore %name
Group: System/Libraries

%description -n %libname%sover
%summary.

%package -n %libname-devel
Summary: Dev files and headers fore %name
Group: Development/C++

%description -n %libname-devel
%summary.

%package plugins
Summary: Plugins fore %name
Version: %pluginsVersion
Group: Other

%description plugins
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

%files -n %libname%sover
%_libdir/%libname.so.%sover.*
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%files plugins
%_libdir/osgPlugins-%pluginsVersion/*.so

%changelog
* Wed Oct 07 2026 Artem Semenov <savoptik@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
