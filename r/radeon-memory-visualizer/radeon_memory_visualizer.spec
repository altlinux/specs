%define optflags_lto %nil

Name: radeon-memory-visualizer
Version: 1.10
Release: alt0.1
License: MIT
Summary: Software tool to analyze video memory usage on AMD Radeon GPUs
Url: https://github.com/GPUOpen-Tools/radeon_memory_visualizer
Group: System/Configuration/Hardware

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ qt6-svg-devel python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx_rtd_theme linuxdeployqt chrpath

Requires: %name-data = %EVR

# doesn't compile on 32-bit
ExclusiveArch: aarch64 x86_64 ppc64le loongarch64

%description
The Radeon Memory Visualizer (RMV) is a software tool that will allow users to
analyze video memory usage on AMD Radeon GPUs. RMV will reveal detailed
information regarding an application's video memory consumption and access
patterns. This will allow users to understand how memory is being leveraged and
open the door to new optimization opportunities.

%package data
Summary: help and samples for RMV
Group: System/Configuration/Hardware
BuildArch: noarch

%description data
Samples and help files for Radeon Memory Visualizer (RMV).

%prep
%setup
%patch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DDISABLE_EXTRA_QT_LIB_DEPLOY=ON
%cmake_build
pushd external/radeon_developer_panel/docs
/usr/bin/sphinx-build ./source %_builddir/%name-%version/%_cmake__builddir/docs/help/rdp/html/. -t public
popd

%install
pushd %_cmake__builddir
mkdir -p %buildroot{%_bindir,%_datadir/rmv}
install -m755 frontend/RadeonMemoryVisualizer %buildroot%_bindir/
cp -ar docs %buildroot%_datadir/rmv/
cp -ar samples %buildroot%_datadir/rmv/
popd
install -m644 LICENSE.txt %buildroot%_datadir/rmv/

%files
%doc LICENSE.txt NOTICES.txt README.md RELEASE_NOTES.txt
%_bindir/RadeonMemoryVisualizer

%files data
%dir %_datadir/rmv
%_datadir/rmv/*

%changelog
* Wed Jul 03 2024 L.A. Kostis <lakostis@altlinux.ru> 1.10-alt0.1
- 1.10.
- qt5->qt6.

* Thu Feb 01 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.8-alt0.2
- NMU: build for LoongArch.

* Wed Jan 31 2024 L.A. Kostis <lakostis@altlinux.ru> 1.8-alt0.1
- 1.8.

* Mon Nov 06 2023 L.A. Kostis <lakostis@altlinux.ru> 1.7-alt0.1
- 1.7.
- BR: added linuxdeployqt.

* Mon Jul 10 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6.1-alt0.1
- 1.6.1.
- Added fixes to external libs to compile with gcc-13.

* Sat Apr 29 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt0.1
- 1.6.

* Fri Jan 13 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt0.3
- Added Radeon Developer Panel documentation.
- Fixed samples, license and documentation links.

* Thu Jan 12 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt0.2
- Set arch to 64-bit only.

* Wed Jan 11 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt0.1
- Initial build for ALTLinux.
