%define _unpackaged_files_terminate_build 1
%define libname libvsgQt
%define sover 0

Name:    vsgQt
Version: 0.5.0
Release: alt1

Summary: Qt integration with VulkanSceneGraph
License: MIT
Group:   Other
Url:     https://github.com/vsg-dev/vsgQt
VCS:     https://github.com/vsg-dev/vsgQt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libvsg-devel
BuildRequires: qt5-base-devel
BuildRequires: vulkan-devel
%{?_with_chek:BuildRequires: ctest}

%description
vsgQt provides full Vulkan support through the VulkanSceneGraph's built
in Window and VkSurface support rather than the limited Vulkan support
that Qt 5.10 or later provide. Using the VulkanSceneGraph for providing
Vulkan support avoids the restriction that Qt's VulkanWindow has with
not being able to share VkDevice between windows, and provides
compatibility with Qt versions prior to it adding Vulkan support.
Sharing vsg::Device and VkDevice between Windows is crucial for
providing multiple windows without blowing up GPU memory usage.

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
sed -i 's/set(VSGQT_SOVERSION 3)/set(VSGQT_SOVERSION 0)/' CMakeLists.txt

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
* Wed Oct 07 2026 Artem Semenov <savoptik@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
