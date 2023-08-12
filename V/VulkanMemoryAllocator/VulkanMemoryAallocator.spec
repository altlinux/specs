%define git_commit 6eb62e1515072827db992c2befd80b71b2d04329

Name: VulkanMemoryAllocator
Version: 3.0.1
Release: alt1.git6eb62e1

Summary: Vulkan Memory Allocator
License: MIT
Group: Development/C++

Url: https://gpuopen.com/vulkan-memory-allocator/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

# https://github.com/GPUOpen-LibrariesAndSDKs/%name/archive/%git_commit/%name-%git_commit.tar.gz
Source: %name-%git_commit.tar

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libvulkan-devel

%description
Easy to integrate Vulkan memory allocation library.

%package -n libvulkan-memory-allocator-devel
Summary: Vulkan Memory Allocator
Group: Development/C++

%description -n libvulkan-memory-allocator-devel
Easy to integrate Vulkan memory allocation library.

%prep
%setup -n %name-%git_commit

%build
%cmake -DVMA_BUILD_DOCUMENTATION:BOOL=ON
%cmake_build

%install
%cmake_install

%files -n libvulkan-memory-allocator-devel
%doc CHANGELOG.md LICENSE.txt README.md
%_includedir/vk_mem_alloc.h
%dir %_datadir/cmake/%name
%_datadir/cmake/%name/%{name}Config.cmake
%_defaultdocdir/%name

%changelog
* Sat Aug 12 2023 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1.git6eb62e1
- Initial build for ALT Linux
