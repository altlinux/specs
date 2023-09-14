%define _unpackaged_files_terminate_build 1
%define pypi_name PySide6
%define mod_name pyside6

%def_with check

Name: python3-module-%mod_name
Version: 6.4.2
Release: alt2

Summary: Python bindings for the Qt cross-platform application and UI framework
Group: Development/Python3
License: BSD-3-Clause and GPL-2.0 and GPL-3.0 and LGPL-3.0 GFDL-1.3-no-invariants-only
URL: https://wiki.qt.io/Qt_for_Python

# Download from https://www.nic.funet.fi/pub/mirrors/download.qt-project.org/official_releases/QtForPython/pyside6/PySide6-6.4.2-src/pyside-setup-opensource-src-6.4.2.tar.xz
Source: pyside-setup-opensource-%version.tar
Patch: always-link-to-python-libraries.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): cmake
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-packaging
BuildRequires: python3-devel
BuildRequires: clang-devel
BuildRequires: libmlir15.0-devel
BuildRequires: llvm15.0-devel
BuildRequires: libpolly15.0-devel
BuildRequires: clang15.0-tools
BuildRequires: clangd15.0
BuildRequires: libnumpy-py3-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: zlib-devel

# Common dependencies
BuildRequires: qt6-base-devel
BuildRequires: libqt6-core
BuildRequires: libqt6-test
BuildRequires: libqt6-xml

# Essential modules
BuildRequires: libqt6-concurrent
BuildRequires: libqt6-gui
BuildRequires: libqt6-network
BuildRequires: libqt6-printsupport
BuildRequires: libqt6-sql
BuildRequires: libqt6-widgets

# Optional modules
BuildRequires: libqt6-bluetooth
BuildRequires: qt6-connectivity-devel
BuildRequires: libqt6-dbus
BuildRequires: qt6-designer
BuildRequires: libqt6-designer
BuildRequires: libqt6-help
BuildRequires: libqt6-multimediawidgets
BuildRequires: libqt6-networkauth
BuildRequires: qt6-networkauth-devel
BuildRequires: libqt6-opengl
BuildRequires: libqt6-openglwidgets
BuildRequires: libqt6-positioning
BuildRequires: qt6-positioning-devel
BuildRequires: libqt6-quick
BuildRequires: libqt6-quickcontrols2
BuildRequires: libqt6-quickwidgets
BuildRequires: qt6-sensors
BuildRequires: qt6-sensors-devel
BuildRequires: libqt6-sensorsquick
BuildRequires: libqt6-serialport
BuildRequires: qt6-serialport-devel
BuildRequires: libqt6-spatialaudio
BuildRequires: libqt6-statemachine
BuildRequires: qt6-svg
BuildRequires: qt6-svg-devel
BuildRequires: libqt6-svgwidgets
BuildRequires: libqt6-uitools
BuildRequires: libqt6-webchannel
BuildRequires: qt6-webchannel-devel

BuildRequires: libqt6-qml
BuildRequires: libqt6-qmlcompiler
BuildRequires: libqt6-qmlcore
BuildRequires: libqt6-qmllocalstorage
BuildRequires: libqt6-qmlmodels
BuildRequires: libqt6-qmlworkerscript
BuildRequires: libqt6-qmlxmllistmodel

BuildRequires: qt6-scxml
BuildRequires: qt6-scxml-devel
BuildRequires: libqt6-websockets
BuildRequires: qt6-websockets-devel
BuildRequires: qt6-3d
BuildRequires: qt6-3d-devel
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-mysql
BuildRequires: qt6-sql-odbc
BuildRequires: qt6-sql-postgresql
BuildRequires: qt6-multimedia
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-charts
BuildRequires: qt6-charts-devel
BuildRequires: qt6-declarative
BuildRequires: qt6-tools-devel

%if_with check
BuildRequires: xvfb-run
BuildRequires: mesa-dri-drivers
BuildRequires: ctest
%endif

%description
PySide6 is the official Python module from the Qt for Python project,
which provides access to the complete Qt 6.0+ framework.

%package devel
Summary: Development files related to %name
Group: Development/Python3
Provides: python3-module-pyside6-devel = %EVR

%description devel
%summary.

%package -n shiboken6
Summary: Python/C++ bindings helper module
Group: Development/Python3

%description -n shiboken6
The purpose of the shiboken6 Python module is to access information related
to the binding generation that could be used to integrate C++ programs
to Python, or even to get useful information to debug an application.

%package -n python3-module-shiboken6
Summary: Python/C++ bindings helper module
Group: Development/Python3
Provides: python3-module-shiboken6 = %EVR

%description -n python3-module-shiboken6
The purpose of the shiboken6 Python module is to access information related
to the binding generation that could be used to integrate C++ programs
to Python, or even to get useful information to debug an application.

%package -n python3-module-shiboken6-devel
Summary: Python/C++ bindings helper module
Group: Development/Python3
Requires: shiboken6
Requires: python3-module-shiboken6
Provides: python3-module-shiboken6-devel = %EVR

%description -n python3-module-shiboken6-devel
The purpose of the shiboken6 Python module is to access information related
to the binding generation that could be used to integrate C++ programs
to Python, or even to get useful information to debug an application.

%prep
%setup -n pyside-setup-opensource-%version
%patch -p0

%build
# Fix installation dir
sed -i 's/purelib/platlib/' sources/shiboken6/cmake/ShibokenHelpers.cmake

%global optflags_lto %nil

export CXX=/usr/bin/clang++

export PYTHONPATH=$PWD/%_cmake__builddir/sources

%cmake -G Ninja \
  -DNUMPY_INCLUDE_DIR:STRING=%python3_sitelibdir/numpy/core/include \
  -DPYTHON_EXECUTABLE:STRING=python3 \
  -DBUILD_TESTS=ON \
  -DQFP_NO_STRIP:BOOL=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo

%ninja_build -C "%_cmake__builddir"

%install
export PYTHONPATH=$PWD/%_cmake__builddir/sources
DESTDIR="/usr/src/tmp/%{name}-buildroot" cmake --install %_cmake__builddir/sources/shiboken6
DESTDIR="/usr/src/tmp/%{name}-buildroot" cmake --install %_cmake__builddir/sources/pyside6

sed -i 's#env python$#python3#' %buildroot%_bindir/shiboken_tool.py

mkdir -p %buildroot%_qt6_plugindir/designer
mv %buildroot/usr/plugins/designer/libPySidePlugin.so %buildroot%_qt6_plugindir/designer

#Generate egg-info manually and install since we're performing a cmake build.
export PATH="%_qt6_bindir:$PATH"
export SETUPTOOLS_USE_DISTUTILS=stdlib
%__python3 setup.py egg_info
for name in PySide6 shiboken6 shiboken6_generator; do
  mkdir -p %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info
  cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
        %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info/
done

%check
export PATH=%_qt6_bindir:$PATH

# Needed by the shiboken tests
export LD_LIBRARY_PATH=%buildroot%_qt6_libdir::$LD_LIBRARY_PATH

%define xvfb_command xvfb-run -s "-screen 0 1600x1200x16 -ac +extension GLX +render -noreset" \\

# Since we need CMAKE_SKIP_RPATH to avoid having bogus RUNPATH in the shiboken libraries,
# It needs to know the path to a couple tests folders
for dir in libminimal libother libsample libsmart; do
  export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/sources/shiboken6/tests/$dir:$LD_LIBRARY_PATH
done

pushd $PWD/%_cmake__builddir/sources
%xvfb_command
ctest \
  --output-on-failure \
  --force-new-ctest-process \
  --test-dir shiboken6 \
  --parallel %_smp_build_ncpus
popd

export PYTHONPATH=%buildroot%python3_sitelibdir:$PYTHONPATH
export PYTHONPATH=$PWD/%_cmake__builddir/sources/pyside6/tests/pysidetest/:$PYTHONPATH
pushd $PWD/%_cmake__builddir/sources
%xvfb_command
ctest \
  --output-on-failure \
  --force-new-ctest-process \
  --test-dir pyside6 \
  --parallel %_smp_build_ncpus \
  --exclude-regex 'pysidetest_new_inherited_functions_test|pysidetest_qvariant_test|registry_existence_test|signals_disconnect_test|support_voidptr_test|QtCore_loggingcategorymacros_test|QtGui_qpen_test|QtGui_timed_app_and_patching_test|QtWidgets_application_test|Qt3DExtras_qt3dextras_test'
popd


%files
%doc README.md
%_libdir/libpyside6.abi3.so.*
%_libdir/libpyside6qml.abi3.so.*
%dir %_qt6_plugindir/designer
%_qt6_plugindir/designer/libPySidePlugin.so
%python3_sitelibdir/PySide6
%python3_sitelibdir/PySide6-%version-*.egg-info

%files devel
%_datadir/PySide6/
%_includedir/PySide6/
%_libdir/libpyside6*.so
%_libdir/libpyside6qml.abi3.so
%_libdir/cmake/PySide6*
%_libdir/pkgconfig/pyside6.pc

%files -n shiboken6
%doc README.shiboken6.md
%_bindir/shiboken6
%_bindir/shiboken_tool.py

%files -n python3-module-shiboken6
%doc README.shiboken6.md
%_libdir/libshiboken6*.so.*
%python3_sitelibdir/shiboken6/
%python3_sitelibdir/shiboken6-%version-*.egg-info

%files -n python3-module-shiboken6-devel
%_includedir/shiboken6/
%dir %_libdir/cmake
%_libdir/cmake/Shiboken6*
%_libdir/libshiboken6*.so
%_libdir/pkgconfig/shiboken6.pc
%python3_sitelibdir/shiboken6_generator/
%python3_sitelibdir/shiboken6_generator-%version-*.egg-info

%changelog
* Thu Sep 14 2023 Anton Vyatkin <toni@altlinux.org> 6.4.2-alt2
- Fix FTBFS.

* Sun Sep 03 2023 Anton Vyatkin <toni@altlinux.org> 6.4.2-alt1
- Initial build for Sisyphus.
