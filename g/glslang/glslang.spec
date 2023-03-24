%define soname 12
%define build_type RelWithDebInfo
%define _cmake %cmake -DCMAKE_BUILD_TYPE=%build_type
%define optflags_lto %nil

Name: glslang
Version: 12.1.0
Release: alt1
Epoch: 1

Summary: OpenGL and OpenGL ES shader front end and validator
Group: Development/C++
License: BSD

Url: https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: https://github.com/KhronosGroup/%name/archive/%version/%name-%version.tar
Patch0: %{name}-alt-shared-opt.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel libspirv-tools-devel >= 2023.2

%description
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

%package -n lib%{name}%{soname}
Summary: %{name} shared libraries
Group: Development/C++

%description -n lib%{name}%{soname}
Contains shared libraries used by %{name}.

%package devel
Summary: %name development headers and libraries
Group: Development/C++
Requires: %name = %EVR

%description devel
%name development headers and libraries.

%prep
%setup
%autopatch -p2

%build
%_cmake \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_DATADIR=%_libdir/cmake \
  -DBUILD_SHARED_LIBS:BOOL=TRUE
%cmake_build
%cmake_install
pushd %buildroot%_includedir
rm -rf SPIRV
ln -s glslang/SPIRV SPIRV
popd

%files
%doc README-spirv-remap.txt
%_bindir/*

%files -n lib%{name}%{soname}
%_libdir/*.so.*

%files devel
%doc README.md
%_libdir/lib*.so
%_libdir/cmake/*
%_includedir/%name
%_includedir/SPIRV

%changelog
* Thu Mar 23 2023 L.A. Kostis <lakostis@altlinux.ru> 1:12.1.0-alt1
- 12.1.0.
- Return cmake hacks.

* Fri Mar 03 2023 L.A. Kostis <lakostis@altlinux.ru> 1:12.0.0-alt1
- 12.0.0.
- Bump soname.

* Tue Dec 13 2022 L.A. Kostis <lakostis@altlinux.ru> 1:11.13.0-alt1
- Updated to 11.13.0 (branch sdk-1.3.236).

* Wed Nov 23 2022 L.A. Kostis <lakostis@altlinux.ru> 1:11.12.0-alt2
- Disable LTO (cause problems on ix86).

* Sat Oct 15 2022 L.A. Kostis <lakostis@altlinux.ru> 1:11.12.0-alt1
- 11.12.0 (branch sdk-1.3.231).

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 1:11.11.0-alt1
- 11.11.0 (tag sdk-1.3.224).
- Remove cmake hacks.

* Sun Apr 10 2022 L.A. Kostis <lakostis@altlinux.ru> 1:11.9.0-alt1
- 11.9.0 (tag sdk-1.3.211).

* Sat Nov 13 2021 L.A. Kostis <lakostis@altlinux.ru> 1:11.7.0-alt1
- 11.7.0.

* Wed Nov 03 2021 L.A. Kostis <lakostis@altlinux.ru> 1:11.6.0-alt1
- 11.6.0.

* Sun Jun 27 2021 L.A. Kostis <lakostis@altlinux.ru> 1:11.5.0-alt1
- 11.5.0.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 1:11.4.0-alt1
- 11.4.0.

* Mon Feb 15 2021 L.A. Kostis <lakostis@altlinux.ru> 1:11.1.0-alt1
- Version 11.1.0.
- Update -alt patches.
- Breaking change: soname have changed.

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 1:8.13.3743-alt1.2
- Rollback to 8.13.3743-alt1.1 (ALT #39673)

* Fri Feb 05 2021 Nazarov Denis <nenderus@altlinux.org> 11.1.0-alt1
- Version 11.1.0

* Sat Sep 12 2020 L.A. Kostis <lakostis@altlinux.ru> 8.13.3743-alt1.1
- Fix dependencies.

* Thu Jun 04 2020 L.A. Kostis <lakostis@altlinux.ru> 8.13.3743-alt1
- stable release April 27, 2020 (8.13.3743).
- update -alt patches.
- added cmake files.

* Thu Aug 29 2019 L.A. Kostis <lakostis@altlinux.ru> 7.12.3352-alt1
- stable release August 20, 2019 (7.12.3352).
- added strict dependency to spirv-tools.

* Fri May 03 2019 L.A. Kostis <lakostis@altlinux.ru> 7.11.3188-alt2
- Try to fix build w/ shared libspirv-tools.

* Thu May 02 2019 L.A. Kostis <lakostis@altlinux.ru> 7.11.3188-alt1
- bump to stable release April 5, 2019 (7.11.3188).
- .spec: cleanups
- build shared libs.

* Sun Mar 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.2.2596-alt2%%ubt
- fix install paths

* Sat Mar 10 2018 Nazarov Denis <nenderus@altlinux.org> 6.2.2596-alt1%%ubt
- Version 6.2.2596

* Tue Apr 18 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1.M80P.1
- Build for branch p8

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt2
- Update to latest from git

* Sun Apr 16 2017 Nazarov Denis <nenderus@altlinux.org> 3.0-alt1
- Initial build for ALT Linux
