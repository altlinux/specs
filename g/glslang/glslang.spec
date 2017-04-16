Name: glslang
Version: 3.0
Release: alt1

Summary: OpenGL and OpenGL ES shader front end and validator
Group: Development/C++
License: BSD

Url: https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/KhronosGroup/%name/archive/%version/%name-%version.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-dev

%description
glslang is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%package devel
Summary: OpenGL and OpenGL ES shader front end and validator
Group: Development/C++

%description devel
glslang is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

spirv-remap is a utility to improve compression of SPIR-V binary
files via entropy reduction, plus optional stripping of debug
information and load/store optimization. It transforms SPIR-V to
SPIR-V, remapping IDs. The resulting modules have an increased ID
range (IDs are not as tightly packed around zero), but will compress
better when multiple modules are compressed together, since
compressor's dictionary can find better cross module commonality.

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING="Release"

popd

%make_build -C %_target_platform

%install

%__make install -C %_target_platform

%__mkdir_p %buildroot{%_bindir,%_libdir,%_includedir/%name/{SPIRV,StandAlone,%name/{Include,MachineIndependent/preprocessor,OSDependent,Public}}}

%__cp -a %_target_platform/install/bin/* %buildroot%_bindir
%__cp -a %_target_platform/install/lib/* %buildroot%_libdir

%__cp -a SPIRV/{*.h,*.hpp} %buildroot%_includedir/%name/SPIRV
%__cp -a StandAlone/*.h %buildroot%_includedir/%name/StandAlone
%__cp -a %name/Include/*.h %buildroot%_includedir/%name/%name/Include
%__cp -a %name/MachineIndependent/*.h %buildroot%_includedir/%name/%name/MachineIndependent
%__cp -a %name/MachineIndependent/preprocessor/*.h %buildroot%_includedir/%name/%name/MachineIndependent/preprocessor
%__cp -a %name/OSDependent/Linux/*.h %buildroot%_includedir/%name/%name/OSDependent
%__cp -a %name/Public/*.h %buildroot%_includedir/%name/%name/Public

%files
%doc README-spirv-remap.txt
%_bindir/*

%files devel
%doc README.md
%_libdir/lib*.a
%_includedir/%name

%changelog
* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1
- Initial build for ALT Linux
