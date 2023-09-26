%define _unpackaged_files_terminate_build 1

Name: CTK
Version: 0.1.0
Release: alt4.git.a203172b
Summary: A set of common support code for medical imaging, surgical navigation, and related purposes
License: Apache-2.0
Group: Development/Tools
Url: https://commontk.org/

# Exclusion source: pythonqt
ExcludeArch: %arm

# https://github.com/commontk/CTK.git
Source: %name-%version.tar

Patch1: %name-alt-build.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel qt5-script-devel qt5-tools-devel-static qt5-xmlpatterns-devel qt5-multimedia-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif
BuildRequires: python3-devel
BuildRequires: libdcmtk-devel dcmtk
BuildRequires: libvtk-devel
BuildRequires: libitk-devel
BuildRequires: libqrestapi-devel
BuildRequires: qtsoap5-devel
BuildRequires: pythonqt-devel

Requires: lib%name = %EVR

%add_python3_path %_libdir/cmake

%description
The Common Toolkit is a community effort to provide support code
for medical image analysis, surgical navigation, and related projects.

%package -n lib%name
Summary: A set of common support code for medical imaging, surgical navigation, and related purposes
Group: System/Libraries

%description -n lib%name
The Common Toolkit is a community effort to provide support code
for medical image analysis, surgical navigation, and related projects.

This package contains CTK shared libraries.

%package devel
Summary: A set of common support code for medical imaging, surgical navigation, and related purposes
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR
Requires: %name-qt5-designer-plugin = %EVR
Requires: python3-module-%name = %EVR
Requires: pythonqt-devel

%description devel
The Common Toolkit is a community effort to provide support code
for medical image analysis, surgical navigation, and related projects.

This package contains development files for CTK.

%package qt5-designer-plugin
Summary: A set of common support code for medical imaging, surgical navigation, and related purposes
Group: Development/C++

%description qt5-designer-plugin
The Common Toolkit is a community effort to provide support code
for medical image analysis, surgical navigation, and related projects.

This package contains CTK plugins for qt5 designer.

%package -n python3-module-%name
Summary: A set of common support code for medical imaging, surgical navigation, and related purposes
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-%name
The Common Toolkit is a community effort to provide support code
for medical image analysis, surgical navigation, and related projects.

This package provides Python bindings to CTK.

%prep
%setup
%patch1 -p1

%ifarch %not_qt5_qtwebengine_arches
for f in \
    CMake/ctkMacroSetupQt.cmake \
    Libs/CommandLineModules/Frontend/QtWebKit/CMakeLists.txt \
    #
do
    sed -i 's|WebEngineWidgets|WebKitWidgets|' $f
done
sed -i 's|QT_VERSION_CHECK(5,|QT_VERSION_CHECK(6,|' Libs/CommandLineModules/Frontend/QtWebKit/ctkCmdLineModuleFrontend*
%endif


%build
%cmake \
	-DCTK_SUPERBUILD:BOOL=OFF \
	-DCTK_QT_VERSION=5 \
	-DCTK_BUILD_ALL_PLUGINS:BOOL=ON \
	-DCTK_BUILD_ALL_LIBRARIES:BOOL=ON \
	-DCTK_BUILD_ALL_APPS:BOOL=ON \
	-DCTK_INSTALL_LIB_DIR:STRING=%_lib \
	-DCTK_INSTALL_PLUGIN_DIR:STRING=%_lib \
	-DCTK_INSTALL_CMAKE_DIR:STRING=%_lib/cmake/CTK \
	-DCTK_INSTALL_QTPLUGIN_DIR:STRING=%_qt5_plugindir \
	-DCTK_INSTALL_PYTHON_DIR:STRING=%_lib/python3/site-packages \
	-DCTK_LIB_Visualization/VTK/Widgets_USE_TRANSFER_FUNCTION_CHARTS:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core_PYTHONQT_USE_VTK:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core_PYTHONQT_WRAP_QTCORE:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core_PYTHONQT_WRAP_QTGUI:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core_PYTHONQT_WRAP_QTUITOOLS:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Core_PYTHONQT_WRAP_QTNETWORK:BOOL=ON \
	-DCTK_LIB_Scripting/Python/Widgets:BOOL=ON \
	-DCTK_ENABLE_Python_Wrapping:BOOL=ON \
	-DCTK_PLUGIN_LIBRARY_OUTPUT_DIRECTORY:STRING=%_lib/ctk/plugins \
	-DCTK_INSTALL_PLUGIN_DIR:STRING=%_lib/ctk/plugins \
	-DPYTHON_EXECUTABLE=%__python3 \
	%nil

%cmake_build

%install
%cmakeinstall_std

# install symlinks for library discovery: they are loaded dynamically, but they have dependencies on each other as well
# separate library is used for dynamic loading, symlink in generic directory is used for loading as dependency
install -d %buildroot%_libdir
find %buildroot%_libdir/ctk/plugins -name '*.so*' | while read i ; do
	ln -sr $i %buildroot%_libdir/
done

%files
%_bindir/*

%files -n lib%name
%doc LICENSE
%doc README.rst
%_libdir/lib*.so.*
%_libdir/ctk
%_libdir/liborg_commontk_*.so

%files devel
%_includedir/*
%_libdir/lib*.so
%exclude %_libdir/liborg_commontk_*.so
%_libdir/cmake/%name

%files qt5-designer-plugin
%_qt5_plugindir/designer/*.so

%files -n python3-module-%name
%python3_sitelibdir/ctkSimplePythonShell.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/ctk
%python3_sitelibdir/qt
%python3_sitelibdir/*.so

%changelog
* Wed Jun 07 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0.1.0-alt4.git.a203172b
- Built from a203172b634253cc3717346de30305ffe721d91c for imports fixes (#46364).
- Updated dependencies.

* Thu Jan 27 2022 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt3.git.dc2e1289
- build with webkit on e2k and ppc64le

* Fri Jul 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt2.git.dc2e1289
- Fixed compatibility with p9.

* Fri May 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1.git.dc2e1289
- Initial build for ALT.
