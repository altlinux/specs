%define git_commit 6eb62e1515072827db992c2befd80b71b2d04329

Name: vulkan-memory-allocator
Version: 3.0.1
Release: alt1.git6eb62e1

Summary: Vulkan Memory Allocator
License: MIT
Group: Development/C++

Url: https://gpuopen.com/%name/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/%git_commit/VulkanMemoryAllocator-%git_commit.tar.gz
Source: VulkanMemoryAllocator-%git_commit.tar

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libvulkan-devel

%description
Easy to integrate Vulkan memory allocation library.

%package -n lib%name-devel
Summary: Vulkan Memory Allocator
Group: Development/C++

%description -n lib%name-devel
Easy to integrate Vulkan memory allocation library.

%prep
%setup -n VulkanMemoryAllocator-%git_commit

%build
%cmake -DVMA_BUILD_DOCUMENTATION:BOOL=ON
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%doc CHANGELOG.md LICENSE.txt README.md
%_includedir/vk_mem_alloc.h
%dir %_datadir/cmake/VulkanMemoryAllocator
%_datadir/cmake/VulkanMemoryAllocator/VulkanMemoryAllocatorConfig.cmake
%_defaultdocdir/VulkanMemoryAllocator

%changelog
* Sat Aug 12 2023 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1.git6eb62e1
- Initial build for ALT Linux
