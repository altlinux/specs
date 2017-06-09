Name: vulkan-examples
Version: 1.0.5
Release: alt1

Summary: Examples and demos for the new Vulkan API

License: MIT
Url: https://github.com/SaschaWillems/Vulkan
Group: Development/Other

# Source-git: https://github.com/SaschaWillems/Vulkan
Source: %name-%version.tar

# Automatically added by buildreq on Fri Jun 09 2017
# optimized out: cmake cmake-modules libstdc++-devel pkg-config python-base python-modules python3 python3-base
BuildRequires: ccmake gcc-c++ libassimp-devel libxcb-devel vulkan-devel libXau-devel libXdmcp-devel

# use system libs
#BuildRequires: libglm-devel

%description
Vulkan C++ examples and demos

A comprehensive collection of open source C++ examples for Vulkan(tm),
the new graphics and compute API from Khronos.

Please, download Media Pack from
http://vulkan.gpuinfo.org/examples.php
and unpack it to %_libdir/%name/data directory

%prep
%setup
# never use binary libs
rm -rf libs

# TODO
#%__subst "s|.*external/glm.*||g" CMakeLists.txt
#rm -rf external/glm

%__subst "s|GLM_ARCH_X86|0|g" external/glm/glm/detail/func_common.inl

%build
%cmake_insource -DCMAKE_CXX_FLAGS=-D_FILE_OFFSET_BITS=64
%make_build

%install
#makeinstall_std
mkdir -p %buildroot/%_libdir/%name/
rm -f bin/*.dll
cp -a bin %buildroot/%_libdir/%name/

%files
%_libdir/%name/

%changelog
* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial release for ALT Sisyphus
