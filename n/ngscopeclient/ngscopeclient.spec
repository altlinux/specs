Name: ngscopeclient
Version: 0.1.1
Release: alt1

Summary: Advanced T&M remote control and analysis suite
License: BSD-3-Clause
Group: Engineering
URL: https://www.ngscopeclient.org/
VCS: https://github.com/ngscopeclient/scopehal-apps

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: deps-%version.tar

BuildRequires: cmake gcc-c++ glslc glslang-devel libgomp-devel
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: pkgconfig(sigc++-3.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(shaderc)
BuildRequires: pkgconfig(SPIRV-Tools)
BuildRequires: pkgconfig(hidapi-hidraw)
BuildRequires: pkgconfig(liblxi)
BuildRequires: pkgconfig(libtirpc)

%description
Streamline hardware test
* Drag and drop to create complex, GPU-accelerated analysis pipelines
  in the filter graph editor
* Open source toolchain supporting Windows, Linux, and MacOS
* Easily extensible to support any T&M instrument with a SCPI interface
  or native API
* Combine multiple instruments into a unified test platform
* Automate production test with the C++ API
* Analyze complex protocols such as Ethernet and PCIe

%prep
%setup -a1

%build
%cmake	-DNGSCOPECLIENT_PACKAGE_VERSION=v%version \
	-DNGSCOPECLIENT_PACKAGE_VERSION_LONG=v0.1.1-559-ge280fe4c
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/ngscopeclient
%_libdir/libscopehal.so
%_libdir/libscopeprotocols.so
%_datadir/ngscopeclient
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.*
%_datadir/mime/packages/*.xml

%changelog
* Wed Jun 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.1-alt1
- v0.1.1-559-ge280fe4c snapshot
