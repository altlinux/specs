%define commit ae43cdcbd25c56e3481bbc8a0ce2bfcebba9f7c2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    monado-vulkan-layers
Version: 0.9.0
Release: alt1.git%shortcommit

Summary: Optional Vulkan Layers for Monado.
License: BSL-1.0
Group:   System/Libraries
Url:     https://gitlab.freedesktop.org/monado/utilities/vulkan-layers

# Source-url: https://gitlab.freedesktop.org/monado/utilities/vulkan-layers/-/archive/%commit/vulkan-layers-%commit.tar.gz
Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libvulkan-devel glslc glslang-devel
Requires: vulkan-filesystem

%description
Optional Vulkan Layers for Monado

%prep
%setup

%build
%cmake \
	-Wno-dev

%cmake_build

%install
%cmake_install

%files
%doc LICENSE
%_libdir/libVkLayer_MND_enable_timeline_semaphore.so
%_datadir/vulkan/implicit_layer.d/VkLayer_MND_enable_timeline_semaphore.json

%changelog
* Wed Feb 12 2025 Sergey Palcheh <minergenon@altlinux.org> 0.9.0-alt1.gitae43cdc
- initial build for ALT Sisyphus

