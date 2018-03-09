%define sover 0

Name: spirv-tools
Version: 2018.2
Release: alt1%ubt

Summary: API and commands for processing SPIR-V modules
Group: Development/C++
License: Apache 2.0

Url: https://www.khronos.org/registry/spir-v/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/KhronosGroup/SPIRV-Tools/archive/v%version/SPIRV-Tools-%version.tar.gz
Patch0: %name-soname-alt.patch

BuildRequires(pre): rpm-build-ubt

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python-devel
BuildRequires: python-modules-json
BuildRequires: spirv-headers

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V.

%package -n lib%name%sover
Summary: SPIR-V tool component library
Group: System/Libraries

%description -n lib%name%sover
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%package -n lib%name-devel
Summary: Development headers for the SPIR-V tool library
Group: Development/C++

%description -n lib%name-devel
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%prep
%setup -n SPIRV-Tools-%version
%patch0 -p1

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DSPIRV-Headers_SOURCE_DIR=%prefix \
	-DSPIRV_SKIP_TESTS:BOOL=TRUE

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc CHANGES LICENSE README.md
%_bindir/spirv-*

%files -n lib%name%sover
%_libdir/libSPIRV-Tools.so.*
%_libdir/libSPIRV-Tools-link.so.*
%_libdir/libSPIRV-Tools-opt.so.*
%_libdir/libSPIRV-Tools-shared.so.*

%files -n lib%name-devel
%_libdir/libSPIRV-Tools.so
%_libdir/libSPIRV-Tools-link.so
%_libdir/libSPIRV-Tools-opt.so
%_libdir/libSPIRV-Tools-shared.so
%_pkgconfigdir/SPIRV-Tools.pc
%_pkgconfigdir/SPIRV-Tools-shared.pc
%_includedir/%name

%changelog
* Fri Mar 09 2018 Nazarov Denis <nenderus@altlinux.org> 2018.2-alt1%ubt
- Version 2018.2

* Tue Apr 18 2017 Nazarov Denis <nenderus@altlinux.org> 2016.6-alt0.M80P.1
- Build for branch p8

* Sat Apr 15 2017 Nazarov Denis <nenderus@altlinux.org> 2016.6-alt1
- Initial build for ALT Linux
