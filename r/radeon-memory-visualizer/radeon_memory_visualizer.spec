Name: radeon-memory-visualizer
Version: 1.5
Release: alt0.2
License: MIT
Summary: Software tool to analyze video memory usage on AMD Radeon GPUs
Url: https://github.com/GPUOpen-Tools/radeon_memory_visualizer
Group: System/Configuration/Hardware

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ qt5-svg-devel python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx_rtd_theme

Requires: %name-data = %EVR

# doesn't compile on 32-bit
ExclusiveArch: aarch64 x86_64 ppc64le

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

%install
pushd %_cmake__builddir
mkdir -p %buildroot{%_bindir,%_datadir/rmv}
install -m755 frontend/RadeonMemoryVisualizer %buildroot%_bindir/
cp -ar docs %buildroot%_datadir/rmv/
cp -ar samples %buildroot%_datadir/rmv/

%files
%doc License.txt NOTICES.txt README.md Release_Notes.txt
%_bindir/RadeonMemoryVisualizer

%files data
%dir %_datadir/rmv
%_datadir/rmv/*

%changelog
* Thu Jan 12 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt0.2
- Set arch to 64-bit only.

* Wed Jan 11 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt0.1
- Initial build for ALTLinux.
