%define _unpackaged_files_terminate_build 1
%define rname volk
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: vulkan-volk
Version: 1.3.290
Release: alt1
Summary: Meta loader for Vulkan API

Group: Development/C++
License: MIT
Url: https://github.com/zeux/volk

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ vulkan-headers >= %version

%description
volk is a meta-loader for Vulkan. It allows you to dynamically load entrypoints
required to use Vulkan without linking to vulkan-1.dll or statically linking
Vulkan loader. Additionally, volk simplifies the use of Vulkan extensions by
automatically loading all associated entrypoints. Finally, volk enables loading
Vulkan entrypoints directly from the driver which can increase performance by
skipping loader dispatch overhead.

%package devel
Summary: %name headers and libraries
Group: Development/C++
# there's another project with nearly the same name
# https://libvolk.org
Conflicts: libvolk-devel

%description devel
%rname development headers and libraries.

%prep
%setup

%build
%cmake -DVOLK_HEADERS_ONLY=true -DVOLK_INSTALL=true
%cmake_build

%install
%cmakeinstall_std

%files devel
%_libdir/*.a
%_includedir/%{rname}.h
%_includedir/%{rname}.c
%dir %_libdir/cmake/%rname
%_libdir/cmake/%rname/*.cmake

%changelog
* Wed Aug 28 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.290-alt1
- 1.3.290.

* Thu May 30 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.283-alt1
- 1.3.283.

* Thu Mar 07 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.275-alt1
- Use vulkan-volk name to avoid conflict with existing
  libvolk package.
- initial build for ALTLinux.
