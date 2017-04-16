%define commit d1141843c0b2401900fd311550c77512f37a67e1

Name: glslang
Version: 3.0
Release: alt2

Summary: OpenGL and OpenGL ES shader front end and validator
Group: Development/C++
License: BSD

Url: https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/KhronosGroup/%name/archive/%commit/%name-%commit.tar.gz

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
%setup -n %name-%commit

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
%makeinstall_std -C %_target_platform
%ifarch x86_64
%__mv %buildroot%_prefix/lib %buildroot%_libdir
%endif

%files
%doc README-spirv-remap.txt
%_bindir/*

%files devel
%doc README.md
%_libdir/lib*.a
%_includedir/%name
%_includedir/SPIRV

%changelog
* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt2
- Update to latest from git

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1
- Initial build for ALT Linux
