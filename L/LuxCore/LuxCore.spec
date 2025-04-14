%define git a342e1e68
# disable for now
%define optflags_lto %nil

Name: LuxCore
Version: 2.10.0
Release: alt1.g%{git}
License: Apache-2.0
Group: Graphics
Summary: LuxCoreRender is a physically correct, unbiased rendering engine
Url: https://www.luxcorerenderer.org
# Vcs: https://github.com/LuxCoreRender/LuxCore/archive/refs/tags/v%{version}-dev1.tar.gz
Source0: %name-%version.tar

Patch0: LuxCore-embree4.patch
Patch1: LuxCore-atomic-header.patch
Patch2: LuxCore-system-bcd.patch
Patch3: LuxCore-unbundle.patch
Patch4: LuxCore-use-cxx-standard-17.patch
Patch5: luxcorerender-oiio-2.3.patch
Patch6: luxcorerender-pr611-boost_181.patch
Patch7: luxcorerender-system.patch
Patch8: luxcorerender-system2.patch
Patch9: luxcorerender-openexr3.patch
Patch10: luxcorerender-fmt10.patch

BuildRequires(pre): cmake rpm-build-python3 ninja-build
BuildRequires: gcc-c++ libopenimageio-devel openexr-devel libjpeg-devel
BuildRequires: zlib-devel libpng-devel boost-devel
BuildRequires: boost-filesystem-devel boost-python3-devel boost-program_options-devel
BuildRequires: boost-interprocess-devel libGL-devel libgtk+3-devel flex embree-devel
BuildRequires: openimagedenoise-devel libblosc-devel libXrandr-devel python3-module-pyside6
BuildRequires: libXinerama-devel libglfw3-devel libopencolorio-devel bcd-devel nlohmann-json-devel
BuildRequires: openvdb-devel opensubdiv-devel libspdlog-devel chrpath

# due embree
ExclusiveArch: x86_64 aarch64

%description
LuxCoreRender is a physically correct, unbiased rendering engine. It is built
on physically based equations that model the transportation of light. This
allows it to accurately capture a wide range of phenomena which most other
rendering programs are simply unable to reproduce.

%package        core
Summary:        Core binaries for %{name}
Group:		Graphics

%description    core
The %{name}-core package contains core binaries for using %{name}.

%package        devel
Summary:        Development files for %{name}
Group:		Development/C++
Provides:       LuxRender-devel = %EVR

%description        devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example of application using %{name}
Group:		Graphics
Requires:       %{name} = %EVR

%description    examples
The %{name}-examples package contains sample binaries using %{name}.

%package static
Summary:	luxcorerender static libraries
Group:		System/Libraries
Requires:	%{name}-devel = %EVR

%description static
Static libraries for the %name render.

%prep
%setup
%autopatch -p1

# Fix bundled deps
rm -rf pywheel pyunittests
rm -rf samples/luxcoreui/deps/glfw-*
rm -rf deps/{bcd-*,expat-*,eigen-*,json-*,opencolorio-*,opensubdiv-*,spdlog-*,openvdb-*,yaml-cpp-*}

# Switch to WIP system bcd
sed -i -e 's/bcd/bcdio bcdcore/' CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt src/luxcore/CMakeLists.txt

# Link to system version
sed -i -e 's/opencolorio/OpenColorIO/' CMakeLists.txt src/luxcore/CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt
sed -i -e 's/OpenColorIO/OpenColorIO spdlog fmt/' CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt
sed -i -e 's/opensubdiv/osdCPU/' CMakeLists.txt src/luxcore/CMakeLists.txt tests/luxcoreimplserializationdemo/CMakeLists.txt

# Explicitly avoid using static boost library: seems needed on boost 1.78
sed -i -e '\@set.*Boost_USE_STATIC_LIBS@s|ON|OFF|' cmake/Dependencies.cmake

# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release \
	-Wno-dev \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_CXX_FLAGS="%optflags -DSPDLOG_FMT_EXTERNAL" \
	-DOPENXR_ROOT=%_prefix \
	-DEMBREE_ROOT=%_prefix
%cmake_build

%install
pushd %{_cmake__builddir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
        
install -Dpm 0755 bin/* %{buildroot}%{_bindir}/
install -Dpm 0755 lib/*.{a,so*} %{buildroot}%{_libdir}/
        
# Remove rpaths
chrpath --delete %{buildroot}%{_bindir}/*
chrpath --delete %{buildroot}%{_libdir}/*.so*
popd
        
# Install include files
cp -pr include/{luxcore,luxrays,slg} %{buildroot}%{_includedir}/
cp -pr %_cmake__builddir/generated/include/{luxcore,luxrays} %buildroot%_includedir/

# Relocate pyluxcore
mkdir -p %{buildroot}%{python3_sitelibdir}
mv %{buildroot}%{_libdir}/pyluxcore.so %{buildroot}%{python3_sitelibdir}

# change the search path in exporter so it finds pylux in its new location
# borrowed from Arch Linux
for file in `grep -rl import\ pyluxcore ${pkgdir}` ; 
        do sed -i 's/from .* import pyluxcore/import pyluxcore/g' $file;
done

%files
%doc AUTHORS.txt COPYING.txt

%files core
%{_bindir}/*

%files devel
%_includedir/luxcore
%_includedir/luxrays
%_includedir/slg

%files static
%_libdir/libluxcore.a
%_libdir/libluxrays.a
%_libdir/libslg-core.a
%_libdir/libslg-film.a
%_libdir/libslg-kernels.a

%changelog
* Sat Apr 12 2025 L.A. Kostis <lakostis@altlinux.ru> 2.10.0-alt1.ga342e1e68
- Initial build for ALTLinux.
- Use patches from luxcorerender-2.7-0.30.beta1.fc43.

