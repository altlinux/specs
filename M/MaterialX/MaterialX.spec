%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%ifnarch %ix86
%set_verify_elf_method strict
%else
%set_verify_elf_method lfs=relaxed
%endif

%define soname 1
%def_with oiio
%def_with python
%def_with viewer

Name: MaterialX
Version: 1.39.4
Release: alt0.2
Summary: MaterialX is an open standard for representing rich material and look-development content in computer graphics
Group: Development/Other
License: Apache-2.0
Url: http://www.materialx.org
VCS: https://github.com/AcademySoftwareFoundation/MaterialX
Source0: %name-%version.tar
Source1: NanoGUI.tar
Source2: glfw.tar
Source3: nanovg.tar

Patch0: %name-alt-unbundle-stb.patch
Patch1: %name-alt-install.patch
Patch2: %name-alt-searchpath.patch
Patch3: %name-alt-python.patch

BuildRequires(pre): cmake ninja-build
BuildRequires: gcc-c++ libX11-devel libXt-devel libGL-devel libstb-devel
%if_with oiio
BuildRequires: libopenimageio-devel
%endif
%if_with python
BuildRequires: rpm-build-python3 python3-devel
%endif
%if_with viewer
BuildRequires: libXrandr-devel libXinerama-devel libXcursor-devel libXi-devel
%endif

%description
MaterialX is an open standard for representing rich material and
look-development content in computer graphics, enabling its
platform-independent description and exchange across applications and
renderers.

%package -n lib%name%{soname}
Summary: %name libraries
Group: System/Libraries
Requires: %name-libraries = %EVR
Provides: lib%name = %EVR

%description -n lib%name%{soname}
MaterialX is an open standard for representing rich material and
look-development content in computer graphics, enabling its
platform-independent description and exchange across applications and
renderers.

This package provides MaterialX libraries.

%package devel
Summary: %name development headers and libraries
Group: Development/C++
Requires: lib%name = %EVR, libXt-devel

%description devel
%name development headers and libraries

%package libraries
Summary: %name Data Libraries
Group: Graphics
BuildArch: noarch

%description libraries
standard data libraries for MaterialX, providing declarations and graph
definitions for the MaterialX nodes, and source code for all supported shader
generators.

%package resources
Summary: %name Resources
Group: Graphics
BuildArch: noarch

%description resources
%name resources:
- Sample geometry files. Includes files used by test suite.
- Sample image files. Includes files used by test suite.
- Set of MaterialX documents.

%package viewer
Summary: %name viewer
Group: Graphics
Requires: %name-resources = %EVR

%description viewer
Default material viewer.

%package -n python3-modules-%name
Summary: %name python3 bindings
Group: Development/Python3
Requires: %name-libraries = %EVR

%description -n python3-modules-%name
%name python3 bindings

%prep
%setup -a1 -a2 -a3
%autopatch -p1
# unbundle stb
rm -rf source/MaterialXRender/External/StbImage

pushd python
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)
popd

%build
subst 's|2\.8\.12|3.5|' source/MaterialXView/NanoGUI/resources/bin2c.cmake
%ifnarch %ix86 x86_64
subst 's,march=nehalem,march=native,' source/MaterialXView/NanoGUI/CMakeLists.txt
%endif
%cmake -GNinja \
	-DCMAKE_STRIP:STRING="" \
	%if_with oiio
	-DMATERIALX_BUILD_OIIO=ON \
	%endif
	-DMATERIALX_INSTALL_LIB_PATH=%_lib \
	-DMATERIALX_INSTALL_STDLIB_PATH=%_datadir/%name/libraries \
	%if_with python
	-DMATERIALX_BUILD_PYTHON=ON \
	%endif
	%if_with viewer
	-DMATERIALX_BUILD_VIEWER=ON \
	%endif
	-DMATERIALX_BUILD_SHARED_LIBS=ON \
	%ifarch %e2k
	-DCMAKE_SKIP_INSTALL_RPATH=OFF \
	%endif
	%nil
%cmake_build

%install
%cmake_install
%if_with python
ln -s %_datadir/%name/libraries %buildroot%python3_sitelibdir/%name/libraries
%endif

%files -n lib%{name}%{soname}
%doc LICENSE CHANGELOG.md README.md THIRD-PARTY.md
%_libdir/lib%{name}*.so.%{soname}*
%dir %_datadir/%name

%files devel
%_includedir/%{name}*
%_libdir/lib%{name}*.so
%_libdir/cmake

%if_with viewer
%files viewer
%_bindir/MaterialXView
%endif

%files libraries
%_datadir/%name/libraries

%files resources
%_datadir/%name/resources

%if_with python
%files -n python3-modules-%name
%python3_sitelibdir/%name
%endif

%changelog
* Mon Jun 22 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.39.4-alt0.2
- e2k build fix (need rpath)

* Fri Nov 14 2025 L.A. Kostis <lakostis@altlinux.ru> 1.39.4-alt0.1
- 1.39.4.

* Thu Mar 20 2025 L.A. Kostis <lakostis@altlinux.ru> 1.39.3-alt0.1
- Initial build for ALTLinux.

