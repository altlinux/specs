%define git 7e48885
%define spirv_tools_rev 9e19fc0f31ceaf1f6bc907dbf17dcfded85f2ce8

Name: vulkan
Version: 1.1.70
Release: alt1
Summary: Vulkan loader and validation layers

Group: System/Libraries
License: ASL 2.0
Url: http://www.khronos.org/

# https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers
Source0: vulkan.tar.xz
# https://github.com/KhronosGroup/glslang
Source1: glslang.tar.xz
# https://github.com/KhronosGroup/SPIRV-Tools.git
Source2: SPIRV-Tools.tar.xz
Patch1: spirv-tools-alt-use-python3.patch
Patch2: 0003-layers-Don-t-set-an-rpath.patch
Patch3: vulkan-alt-use-file-rev-spirv-tools.patch

BuildRequires: bison chrpath
BuildRequires(pre): cmake gcc-c++ rpm-build-python3
BuildRequires: libImageMagick-devel libpciaccess-devel libsystemd-devel
BuildRequires: python3-devel libxcb-devel libXau-devel libXdmcp-devel libX11-devel libXrandr-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel

# textrel due asm optimisation in loader code
%ifarch i586
%set_verify_elf_method textrel=relaxed
%endif

%description
Vulkan is a new generation graphics and compute API that provides
high-efficiency, cross-platform access to modern GPUs used in a wide
variety of devices from PCs and consoles to mobile phones and embedded
platforms.

This package contains the reference ICD loader and validation layers for Vulkan.

%package -n lib%{name}1
Summary: Vulkan loader libraries
Group: System/Libraries
Requires: vulkan-filesystem = %version-%release
Provides: %name = %version-%release
Obsoletes: %name

%description -n lib%{name}1
Vulkan is a new generation graphics and compute API that provides
high-efficiency, cross-platform access to modern GPUs used in a wide
variety of devices from PCs and consoles to mobile phones and embedded
platforms.

This package contains the reference ICD loader for Vulkan.

%package validation-layers
Summary: Vulkan API validation layers
Group: Development/C++
Requires: lib%{name}1 = %version-%release

%description validation-layers
Vulkan API validation layer for developers.

%package -n lib%name-devel
Summary: Vulkan development package
Group: Development/C++
Requires: lib%{name}1 = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%description -n lib%name-devel
Development headers for Vulkan applications.

%package filesystem
Summary: Vulkan filesystem package
Group: System/Base
BuildArch: noarch

%description filesystem
Filesystem for Vulkan API.

%package demos
Summary: Vulkan demos
Group: System/X11
Requires: lib%{name}1 = %version-%release

%description demos
Vulkan API demos.

%prep
%setup -n %name -b1 -b2
pushd ../SPIRV-Tools
%patch1 -p2
popd
%patch2 -p1
%patch3 -p2

# sigh inttypes
sed -i 's/inttypes.h/cinttypes/' layers/*.{cpp,h}

%build
# first, glslang and SPIRV-Tools
for dir in glslang SPIRV-Tools; do
pushd %_builddir/$dir
if [ "$dir" == "SPIRV-Tools" ]; then
%cmake \
       -DSPIRV_BUILD_COMPRESSION:BOOL=ON \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
else
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
fi
%cmake_build
%cmakeinstall_std DESTDIR=$(pwd)/install
pushd install
ln -s usr/* .
popd
popd
done

# create rev file to make vulkan happy
ln -s %_builddir/SPIRV-Tools %_builddir/glslang/External/spirv-tools
echo %spriv_tools_rev > %_builddir/SPIRV-Tools/rev_file

# and finally, loader, layers, and demo clients
%cmake \
 	   -DCMAKE_BUILD_TYPE=Release \
           -DEXTERNAL_SOURCE_ROOT=%_builddir \
	   -DBUILD_TESTS=OFF \
	   -DBUILD_VKJSON=OFF \
	   -DCUSTOM_GLSLANG_BIN_ROOT=ON \
	   -DCUSTOM_SPIRV_TOOLS_BIN_ROOT=ON \
	   -DGLSLANG_BINARY_ROOT=%_builddir/glslang/BUILD \
	   -DSPIRV_TOOLS_BINARY_ROOT=%_builddir/SPIRV-Tools/BUILD \
	   -DSPIRV_TOOLS_OPT_LIB:FILEPATH=%_builddir/SPIRV-Tools/install/%_lib \
	   -DSPIRV_TOOLS_INCLUDE_DIR:FILEPATH=%_builddir/SPIRV-Tools/include \
	   -DBUILDTGT_DIR=BUILD \
	   -DCMAKE_INSTALL_SYSCONFDIR:PATH=%_sysconfdir \
	   -DBUILD_WSI_MIR_SUPPORT=OFF
%cmake_build

%install
%cmakeinstall_std
install -T BUILD/demos/smoketest %buildroot%_bindir/vulkan-smoketest
mkdir -p %buildroot%_datadir/vulkan/{explicit,implicit}_layer.d/
mv %buildroot%_sysconfdir/vulkan/explicit_layer.d/*.json %buildroot%_datadir/vulkan/explicit_layer.d/
mkdir -p %buildroot%_datadir/vulkan/icd.d

# remove RPATH
chrpath -d %buildroot%_bindir/vulkaninfo

%files demos
%_bindir/*

%files -n lib%{name}1
%doc README.md LICENSE.txt
%_libdir/libvulkan.so.1*

%files -n lib%name-devel
%dir %_includedir/vulkan
%_includedir/vulkan
%_libdir/libvulkan.so
%_pkgconfigdir/vulkan.pc

%files validation-layers
%dir %_sysconfdir/vulkan/explicit_layer.d
%dir %_datadir/vulkan/explicit_layer.d
%dir %_datadir/vulkan/implicit_layer.d
%_datadir/vulkan/explicit_layer.d/*.json
%_libdir/libVkLayer*.so

%files filesystem
%dir %_sysconfdir/vulkan
%dir %_datadir/vulkan
%dir %_datadir/vulkan/icd.d

%changelog
* Fri Mar 16 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.70-alt1
- Updated to vulkan sdk-1.1.70.

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 1.0.68-alt0.1
- Updated to vulkan sdk-1.0.68:
  + glslang 2651cca.
  + spirv-tools 9e19fc0.
  + spirv-headers ce30920.

* Sun Oct 08 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.61-alt0.2
- i586: Don't check for textrel due asm optimization in loader code.

* Sat Oct 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.61-alt0.1
- Updated to vulkan sdk-1.0.61:
  + glslang 3a21c88.
  + spirv-tools 7e2d26c.
  + spirv-headers 2bb92e6.

* Wed Jun 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.51-alt0.2.115665a
- Fix Obsoletes.
- libvulkan->libvulkan1 in accordance with ALT Shared Libs Policy.

* Wed Jun 07 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.51-alt0.1.115665a
- Bumped to vulkan sdk GIT 115665a:
  + glslang 136b1e2.
  + spirv-tools e7aff80.
  + spirv-headers 63e1062.

* Tue Jun 06 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.42-alt0.2
- .spec re-write:
  + sync with Fedora packaging.
  + remove rpath from vk (patch taken from debian.org).
  + split libvulkan and validation layers.
  + move demos to separate package (as for Mesa).

* Sun Mar 19 2017 L.A. Kostis <lakostis@altlinux.ru> 1.0.42-alt0.1
- Updated to vulkan sdk-1.0.42:
  + glslang dfbdd9.
  + spirv-tools c3caa5.
  + spirv-headers f61848.
- SPIRV-Tools: use python3 by default.

* Wed Dec 28 2016 L.A. Kostis <lakostis@altlinux.ru> 1.0.37-alt0.3
- .spec: use cmake macros instead of ugly hacks.

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
