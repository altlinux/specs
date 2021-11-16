%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_LIBDIR=%_datadir
%define sover 1
%define glslang_ver 11.7.0
%define spirv_tools_ver 2021.4
%def_disable static
%def_with doc

Name: shaderc
Version: 2021.3
Release: alt0.1

Summary: A collection of tools, libraries and tests for shader compilation 
Group: Development/C++
License: Apache-2.0

URL: https://github.com/google/shaderc
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-alt-skip-dirs.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ spirv-headers >= 1.5.5 libspirv-tools-devel >= %spirv_tools_ver glslang-devel >= %glslang_ver
BuildRequires: python3-devel
%if_with doc
BuildRequires: asciidoctor
%endif

%description
A collection of tools, libraries and tests for shader compilation.
At the moment it includes:

- glslc, a command line compiler for GLSL/HLSL to SPIR-V, and
- libshaderc, a library API for accessing `glslc` functionality.

%package -n lib%{name}-devel
Summary: %name devel libraries and headers
Group: Development/C++
Requires: lib%{name}%{sover} = %EVR

%description -n lib%{name}-devel
%name development libraries and headers

%package -n lib%{name}%{sover}
Summary: %name support libraries
Group: System/Libraries
Provides: lib%{name} = %EVR

%description -n lib%{name}%{sover}
%name support libraries

%package -n glslc
Summary: command line compiler for GLSL/HLSL to SPIR-V
Group: System/Libraries
Requires: lib%{name} = %EVR

%description -n glslc
Command line compiler for GLSL/HLSL to SPIR-V

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1

%build
%_cmake \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DSHADERC_SKIP_TESTS:BOOL=ON \
  -DSHADERC_SKIP_EXAMPLES:BOOL=ON \
  -DSHADERC_SPIRV_TOOLS_DIR=%_prefix \
  -DSHADERC_SPIRV_HEADERS_DIR=%_includedir \
  -DSHADERC_GLSLANG_DIR=%_prefix
echo '"%name v%version v%version\\n"' >> %_target_platform/build-version.inc
echo '"spirv-tools v%spirv_tools_ver v%spirv_tools_ver\\n"' >> %_target_platform/build-version.inc
echo '"glslang v%glslang_ver v%glslang_ver\\n"' >> %_target_platform/build-version.inc
%cmake_build
%cmakeinstall_std

%files -n lib%{name}%{sover}
%_libdir/lib%{name}_shared.so.*

%files -n lib%{name}-devel
%doc README.md CHANGES AUTHORS LICENSE
%_includedir/%{name}
%_pkgconfigdir/%name.pc
%_libdir/lib%{name}_shared.so

%files -n glslc
%_bindir/*

%changelog
* Sat Nov 13 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.3-alt0.1
- Initial build for ALTLinux.


