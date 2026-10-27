%define _unpackaged_files_terminate_build 1
%define libname libvsgImGui
%define sover 0

Name:    vsgImGui
Version: 0.8.0
Release: alt1

Summary: Integration of VulkanSceneGraph with ImGui
License: MIT
Group:   Other
Url:     https://github.com/vsg-dev/vsgImGui
VCS:     https://github.com/vsg-dev/vsgImGui

Source: %name-%version.tar
Source1: imgui.tar
Source2: implot.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libvsg-devel
BuildRequires: libxcb-devel
BuildRequires: vulkan-devel

%description
%summary.

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

pushd src
tar -xf %SOURCE1
tar -xf %SOURCE2
popd

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files -n %libname%sover
%_libdir/%libname.so.%version
%_libdir/%libname.so.%sover

%files -n %libname-devel
%_includedir/*
%_libdir/%libname.so
%_cmakedir/*

%changelog
* Thu Oct 08 2026 Artem Semenov <savoptik@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
