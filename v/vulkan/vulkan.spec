Name: vulkan
Version: 1.0.37
Release: alt0.2
Summary: Vulkan loader and validation layers

Group: System/Libraries
License: MIT
Url: http://www.khronos.org/

# https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/tree/sdk-1.0.37
Source0: vulkan.tar.xz
# https://github.com/KhronosGroup/glslang
Source1: glslang.tar.xz
# git clone https://github.com/KhronosGroup/SPIRV-Tools.git
Source2: SPIRV-Tools.tar.xz

BuildRequires: bison
BuildRequires(pre): cmake gcc-c++
BuildRequires: libImageMagick-devel libpciaccess-devel libsystemd-devel
BuildRequires: python-modules python-modules-json python3-dev libxcb-devel libXau-devel libXdmcp-devel libX11-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel

Requires: vulkan-filesystem

%description
Vulkan is a new generation graphics and compute API that provides
high-efficiency, cross-platform access to modern GPUs used in a wide
variety of devices from PCs and consoles to mobile phones and embedded
platforms.

This package contains the reference ICD loader and validation layers for
Vulkan.

%package devel
Summary: vulkan development package
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development headers for vulkan applications.

%package filesystem
Summary: vulkan filesystem package
Group: System/Base
BuildArch: noarch

%description filesystem
Filesystem for vulkan.

%prep
%setup -n %name -b1 -b2

# sigh inttypes
sed -i 's/inttypes.h/cinttypes/' layers/*.{cpp,h}

%build
# first, glslang and SPIRV-Tools
for dir in glslang SPIRV-Tools; do
pushd %_builddir/$dir
%cmake ..
pushd BUILD
%make_build
make install DESTDIR=$(pwd)/install
cd install
ln -s usr/* .
popd
popd
done

# and finally, loader, layers, and demo clients
%cmake .. \
           -DEXTERNAL_SOURCE_ROOT=%_builddir \
	   -DBUILD_TESTS=OFF \
	   -DCUSTOM_GLSLANG_BIN_ROOT=ON \
	   -DCUSTOM_SPIRV_TOOLS_BIN_ROOT=ON \
	   -DGLSLANG_BINARY_ROOT=%_builddir/glslang/BUILD \
	   -DSPIRV_TOOLS_BINARY_ROOT=%_builddir/SPIRV-Tools/BUILD \
	   -DBUILDTGT_DIR=BUILD \
	   -DBUILD_WSI_MIR_SUPPORT=OFF
pushd BUILD
%make_build
popd

%install
pushd BUILD
# XXX upstream
mkdir -p %buildroot{%_includedir,%_bindir,%_libdir}
mkdir -p %buildroot%_datadir/vulkan/{explicit_layer,implicit_layer}.d
install demos/vulkaninfo %buildroot%_bindir/vulkaninfo
cp -a layers/*.so %buildroot%_libdir/
cp -a loader/libvulkan* %buildroot%_libdir/
popd
cd include ; cp -rp vulkan %buildroot%_includedir ; cd ..
for i in layers/linux/*.json ; do
    sed 's@./@@' $i > %buildroot%_datadir/vulkan/explicit_layer.d/$(basename $i)
done
# bleh
rm -f %buildroot/%_datadir/vulkan/explicit_layer.d/*implicit*

mkdir -p %buildroot%_datadir/vulkan/icd.d

%files
%doc README.md LICENSE.txt
%_bindir/*
%_datadir/vulkan/explicit_layer.d/*.json
%_libdir/libVkLayer*.so
%_libdir/libvulkan.so.1*

%files devel
%_includedir/vulkan
%_libdir/libvulkan.so

%files filesystem
%dir %_datadir/vulkan
%dir %_datadir/vulkan/icd.d
%dir %_datadir/vulkan/explicit_layer.d
%dir %_datadir/vulkan/implicit_layer.d

%changelog
* Mon Dec 26 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.2
- Updated builreq: added wayland.

* Mon Dec 26 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.1
- Updated to vulkan sdk-1.0.37:
  + glslang 6a60c2.
  + spirv-tools 945e9f.
  + spirv-headers c470b6.

* Sat Oct 01 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.26-alt0.1
- First build for ALTLinux.

* Tue Feb 16 2016 Adam Jackson <ajax@redhat.com> - 1.0.3-2
- Update loader to not build cube or tri. Drop bundled LunarGLASS and llvm
  since they're only needed for those demos.

* Tue Feb 16 2016 Adam Jackson <ajax@redhat.com> - 1.0.3-1
- Initial packaging
