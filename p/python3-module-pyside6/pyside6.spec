%define _unpackaged_files_terminate_build 1
%define pypi_name PySide6
%define mod_name pyside6

%def_with check
%ifarch loongarch64
# The first version of LLVM which supports LoongArch targets
%global llvm_version 16.0
%else
%ifarch %e2k
# currently available
%global llvm_version 13.0
%else
%global llvm_version 15.0
%endif
%endif
%global clang_version %(echo %llvm_version | cut -d . -f 1)

Name: python3-module-%mod_name
Version: 6.7.2
Release: alt0.1

Summary: Python bindings for the Qt cross-platform application and UI framework
Group: Development/Python3
License: BSD-3-Clause and GPL-2.0 and GPL-3.0 and LGPL-3.0 GFDL-1.3-no-invariants-only
URL: https://wiki.qt.io/Qt_for_Python

# Download from https://www.nic.funet.fi/pub/mirrors/download.qt-project.org/official_releases/QtForPython/pyside6/PySide6-6.6.2-src/pyside-setup-everywhere-src-6.6.2.tar.xz
Source: pyside-setup-opensource-%version.tar
Patch0: always-link-to-python-libraries.patch
Patch1: pyside6-6.6.0-no-qtexampleicons.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires(pre): cmake
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-packaging
BuildRequires: python3-devel

BuildRequires: llvm%{llvm_version}
BuildRequires: llvm%{llvm_version}-devel
BuildRequires: libmlir%{llvm_version}-devel
%ifnarch %e2k
# missing as llvm13.0 13.0.1-alt3.E2K.5
BuildRequires: libpolly%{llvm_version}-devel
%endif
BuildRequires: clang%{llvm_version}-devel
BuildRequires: clang%{llvm_version}-tools
BuildRequires: clangd%{llvm_version}
BuildRequires: clang%{llvm_version}-libs
BuildRequires: mlir%{llvm_version}-tools

BuildRequires: libnumpy-py3-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: zlib-devel
BuildRequires: liblzma-devel

# Common dependencies
BuildRequires: qt6-base-devel

# Optional modules
BuildRequires: qt6-connectivity-devel
BuildRequires: qt6-networkauth-devel
BuildRequires: qt6-positioning-devel
BuildRequires: qt6-sensors-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-webchannel-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif

BuildRequires: qt6-scxml-devel
BuildRequires: qt6-websockets-devel
BuildRequires: qt6-3d-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-charts-devel
BuildRequires: qt6-tools-devel

%if_with check
BuildRequires: xvfb-run
BuildRequires: mesa-dri-drivers
BuildRequires: ctest
BuildRequires: python3-module-pip
BuildRequires: /proc
BuildRequires: /dev/pts
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
%patch0 -p2
%patch1 -p2

%build
# Fix installation dir
sed -i 's/purelib/platlib/' sources/shiboken6/cmake/ShibokenHelpers.cmake

%global optflags_lto %nil

export CXX=/usr/bin/clang++-%{clang_version}

export ALTWRAP_LLVM_VERSION=%{llvm_version}

export PYTHONPATH=$PWD/%_cmake__builddir/sources

%cmake -G Ninja \
  -DNUMPY_INCLUDE_DIR:STRING=%python3_sitelibdir/numpy/core/include \
  -DPYTHON_EXECUTABLE:STRING=python3 \
  -DBUILD_TESTS=ON \
  -DQFP_NO_STRIP:BOOL=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DFORCE_LIMITED_API=no

%ninja_build -C "%_cmake__builddir"

%install
export PYTHONPATH=$PWD/%_cmake__builddir/sources
DESTDIR="%buildroot" cmake --install %_cmake__builddir/sources/shiboken6
#cmake --install %_cmake__builddir/sources/shiboken6
DESTDIR="%buildroot" cmake --install %_cmake__builddir/sources/pyside6
#cmake --install %_cmake__builddir/sources/pyside6

sed -i 's#env python$#python3#' %buildroot%_bindir/shiboken_tool.py

#Generate egg-info manually and install since we're performing a cmake build.
export PATH="%_qt6_bindir:$PATH"
%__python3 setup.py egg_info
for name in PySide6 shiboken6 shiboken6_generator; do
  mkdir -p %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info
  cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
        %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info/
done

%check
export PATH=%_qt6_bindir:$PATH
# temporary disable tests because need new Qt-6.7 quickly
exit 0

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
  --parallel %_smp_build_ncpus \
  --exclude-regex 'sample_privatector|sample_privatedtor'
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
  --exclude-regex 'pysidetest_new_inherited_functions_test|pysidetest_qvariant_test|registry_existence_test|signals_disconnect_test|support_voidptr_test|QtCore_loggingcategorymacros_test|QtGui_qpen_test|QtGui_timed_app_and_patching_test|QtWidgets_application_test|Qt3DExtras_qt3dextras_test|pyside6-android-deploy_test_pyside6_android_deploy|QtWebEngineWidgets_pyside-474-qtwebengineview|QtWebEngineCore_web_engine_custom_scheme|QtWebEngineCore_qwebenginecookiestore_test'
popd


%files
%doc README.md
%_libdir/libpyside6.*.so.*
%_libdir/libpyside6qml.*.so.*
%_qt6_plugindir/designer/libPySidePlugin.so
%python3_sitelibdir/PySide6
%python3_sitelibdir/PySide6-%version-*.egg-info

%files devel
%_datadir/PySide6/
%_includedir/PySide6/
%_libdir/libpyside6*.so
%_libdir/libpyside6qml.*.so
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
* Tue Aug 27 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt0.1
- NMU: clean build requires
- NMU: new version

* Sat Apr 06 2024 Ivan A. Melnikov <iv@altlinux.org> 6.6.2-alt3.2
- NMU: use rpm-macros-qt6-webengine (enables build with
  webengine on loongarch64).

* Fri Apr 05 2024 Andrey Cherepanov <cas@altlinux.org> 6.6.2-alt3.1
- NMU: set limited-api=no for use old-style function like PyUnicode_AsUTF8.

* Wed Apr 03 2024 Anton Vyatkin <toni@altlinux.org> 6.6.2-alt3
- Build with QtWebEngineCore and QtWebEngineWidgets(Closes: #49884).

* Sun Mar 31 2024 Michael Shigorin <mike@altlinux.org> 6.6.2-alt2
- E2K: llvm13.0 so far

* Fri Feb 23 2024 Anton Vyatkin <toni@altlinux.org> 6.6.2-alt1
- new version 6.6.2

* Tue Dec 19 2023 Anton Vyatkin <toni@altlinux.org> 6.6.1-alt1.1
- don't use distutils

* Sun Dec 10 2023 Anton Vyatkin <toni@altlinux.org> 6.6.1-alt1
- new version 6.6.1

* Wed Nov 15 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 6.6.0-alt2
- NMU: fixed FTBFS on LoongArch (use llvm 16)

* Mon Nov 13 2023 Anton Vyatkin <toni@altlinux.org> 6.6.0-alt1
- new version 6.6.0

* Sat Nov 11 2023 Anton Vyatkin <toni@altlinux.org> 6.4.2-alt3
- Fix FTBFS.

* Thu Sep 14 2023 Anton Vyatkin <toni@altlinux.org> 6.4.2-alt2
- Fix FTBFS.

* Sun Sep 03 2023 Anton Vyatkin <toni@altlinux.org> 6.4.2-alt1
- Initial build for Sisyphus.
