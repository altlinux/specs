%define sover 1
%define glslang_ver 14.2.0
%define spirv_tools_ver 2024.2
%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type
%def_disable static
%def_with doc

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: shaderc
Version: 2024.1
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
BuildRequires: python3-devel ninja-build
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

%if_enabled static
%package -n lib%{name}-devel-static
Summary: %name devel static libraries
Group: Development/C++
Requires: lib%{name}-devel = %EVR

%description -n lib%{name}-devel-static
%name development static libraries
%endif

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
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
%_cmake \
  -GNinja \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DSHADERC_SKIP_TESTS:BOOL=ON \
  -DSHADERC_SKIP_EXAMPLES:BOOL=ON \
  -DSHADERC_SPIRV_TOOLS_DIR=%_prefix \
  -DSHADERC_SPIRV_HEADERS_DIR=%_includedir \
  -DSHADERC_GLSLANG_DIR=%_prefix
echo '"%name v%version v%version\\n"' >> %_target_platform/build-version.inc
echo '"spirv-tools v%spirv_tools_ver v%spirv_tools_ver\\n"' >> %_target_platform/build-version.inc
echo '"glslang v%glslang_ver v%glslang_ver\\n"' >> %_target_platform/build-version.inc
ninja \
  -vvv \
  -j %__nprocs \
  -C %_cmake__builddir

%install
%cmake_install
%if_disabled static
rm -f %buildroot%_libdir/*.a
%endif

%files -n lib%{name}%{sover}
%_libdir/lib%{name}_shared.so.*

%files -n lib%{name}-devel
%doc README.md CHANGES AUTHORS LICENSE
%_includedir/%{name}
%_pkgconfigdir/%name.pc
%_libdir/lib%{name}_shared.so

%if_enabled static
%_libdir/lib%{name}.a
%_libdir/lib%{name}_combined.a
%_pkgconfigdir/%{name}_static.pc
%_pkgconfigdir/%{name}_combined.pc
%endif

%files -n glslc
%_bindir/*

%changelog
* Thu Jun 13 2024 L.A. Kostis <lakostis@altlinux.ru> 2024.1-alt0.1
- 2024.1 (closes #50637).
- BR: bump deps.

* Fri Mar 08 2024 L.A. Kostis <lakostis@altlinux.ru> 2023.8-alt0.1
- v2023.8.
- Bump glslang and SPIRV-Tools deps.

* Tue Nov 14 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.7-alt0.1
- v2023.7.
- Bump glslang and SPIRV-Tools deps.
- Complete packaging in case of static libraries.
- Fix debuginfo files generation.

* Sun Sep 17 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.6-alt0.1
- v2023.6.

* Thu May 25 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.4-alt0.1
- v2023.4.
- Bump glslang and SPIRV-Tools deps.

* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.3-alt0.1
- v2023.3.
- Set cmake release target.

* Fri Mar 03 2023 L.A. Kostis <lakostis@altlinux.ru> 2023.2-alt0.1
- v2023.2.
- Bump glslang and SPIRV-Tools deps.

* Wed Dec 14 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.4-alt0.1
- v2022.4.
- Bump glslang and SPIRV-Tools deps.

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.3-alt0.1
- v2022.3.

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 2022.2-alt0.1
- v2022.2.

* Sat Nov 13 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.3-alt0.1
- Initial build for ALTLinux.
