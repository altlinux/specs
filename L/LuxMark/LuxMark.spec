%define optflags_lto %nil

Name: LuxMark
Version: 4.0
Release: alt3.alpha1
License: GPLv3
Group: Graphics
Summary: LuxMark is OpenCL benchmark based on LuxCoreRender
Url: https://www.luxcorerenderer.org
# Vcs: https://github.com/LuxCoreRender/LuxMark/archive/refs/tags/luxmark_v%{version}alpha1.tar.gz
Source0: %name-%version.tar

Patch0: LuxCore-embree4.patch
Patch1: %name-oidn2.patch
Patch2: %name-openexr3.patch
Patch3: luxcorerender-oiio-2.3.patch
Patch4: LuxCore-extra-deps.patch
Patch5: LuxMark-alt-scenes-dir.patch
Patch6: LuxMark-use-cxx-standard-17.patch
Patch7: LuxMark-alt-unbundle-libcpuid.patch

BuildRequires(pre): cmake ninja-build /proc
BuildRequires: gcc-c++ libopenimageio-devel libjpeg-devel openexr-devel libblosc-devel
BuildRequires: zlib-devel libpng-devel qt5-base-devel libgomp-devel libfmt-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: boost-python3-devel bcd-devel libspdlog-devel LuxCore-devel LuxCore-static
BuildRequires: openvdb-devel opensubdiv-devel embree-devel openimagedenoise-devel
%ifarch x86_64
BuildRequires: libcpuid-devel
%endif

ExclusiveArch: x86_64 aarch64

Requires: %name-scenes = %EVR

%description
LuxMark is OpenCL benchmark based on LuxCoreRender
(https://www.luxcorerender.org) and written using LuxCore API. You can find
more information about LuxMark at https://wiki.luxcorerender.org/LuxMark.

%package scenes
Summary: %name benchmark scenes
Group: Graphics
BuildArch: noarch

%description scenes
%name benchmark scenes

%prep
%setup
%autopatch -p1
%ifarch aarch64
%patch7 -p1 -R
%endif

%build
sed -i -e 's/bcd/bcdcore/' cmake/Dependencies.cmake
sed -i -e 's/opensubdiv/osdCPU/' cmake/Dependencies.cmake
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release \
	-Wno-dev \
	-DCMAKE_CXX_FLAGS="%optflags -DSPDLOG_FMT_EXTERNAL" \
	-DOPENEXR_ROOT=%prefix \
	-DOIDN_SEARCH_PATH=%prefix
%cmake_build

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name/scenes}
install -pm755 %_cmake__builddir/bin/luxmark %buildroot%_bindir/
cp -pr scenes-dist/* %buildroot%_datadir/%name/scenes/

%files
%_bindir/luxmark

%files scenes
%_datadir/%name

%changelog
* Mon Jul 21 2025 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt3.alpha1
- x86_64: employ SSE4.2.

* Wed Apr 23 2025 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt2.alpha1
- Use system libcpuid.

* Sat Apr 12 2025 L.A. Kostis <lakostis@altlinux.ru> 4.0-alt1.alpha1
- Initial build for ALTLinux.
