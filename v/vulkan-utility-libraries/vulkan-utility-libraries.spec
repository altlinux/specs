%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: vulkan-utility-libraries
Version: 1.4.350.0
Release: alt1
Summary: Utility libraries for Vulkan developers

Group: System/Libraries
License: Apache-2.0
Url: http://www.khronos.org/

# https://github.com/KhronosGroup/Vulkan-Utility-Libraries.git
Source0: %name.tar

BuildRequires(pre): cmake gcc-c++
BuildRequires: vulkan-headers = %version

Requires: vulkan-devel

%description
The Vulkan::LayerSettings library was created to standardize layer
configuration code for various SDK layer deliverables.

The Vulkan::UtilityHeaders library contains header only files that provide
useful functionality to developers.

%package -n libVulkanUtilityLibraries-devel
Summary: Vulkan utility libraries development files
Group: Development/C++
Provides: %name-devel = %EVR

%description -n libVulkanUtilityLibraries-devel
Development headers for Vulkan applications.

%prep
%setup -n %name

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n libVulkanUtilityLibraries-devel
%_libdir/*.a
%_includedir/vulkan/*
%dir %_libdir/cmake/VulkanUtilityLibraries
%_libdir/cmake/VulkanUtilityLibraries/*.cmake

%changelog
* Thu May 21 2026 L.A. Kostis <lakostis@altlinux.ru> 1.4.350.0-alt1
- 1.4.350.0.

* Thu Feb 19 2026 L.A. Kostis <lakostis@altlinux.ru> 1.4.341.0-alt1
- 1.4.341.0.

* Fri Jan 23 2026 L.A. Kostis <lakostis@altlinux.ru> 1.4.335.0-alt1
- 1.4.335.0.

* Thu Oct 23 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.328.1-alt1
- 1.4.328.1.

* Tue Aug 12 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.321-alt1
- 1.4.321.

* Sun May 11 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.313-alt1
- 1.4.313.

* Fri Feb 07 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.304-alt1
- 1.4.304.

* Wed Dec 11 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.296-alt1
- 1.3.296.

* Wed Aug 28 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.290-alt1
- 1.3.290.

* Thu May 30 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.283-alt1
- 1.3.283.

* Tue Mar 05 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.277-alt1
- 1.3.277.
- BR: require headers only.

* Mon Nov 13 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3.268-alt1
- Initial build for ALTLinux.

