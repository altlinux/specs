%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: python3-module-PySide2
Version: 5.15.2
Release: alt2.1

Summary: Python bindings for the Qt 5 cross-platform application and UI framework
Group: Development/Python3
License: BSD-3-Clause and GPL-2.0 and GPL-3.0 and LGPL-3.0
URL: https://wiki.qt.io/Qt_for_Python

# Download from https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-$version-src/
Source: pyside-setup-opensource-src-%version.tar
Patch1: pyside2-link-with-python.patch
Patch2: python-pyside2-options_py.patch

# patches from debian
Patch10: py3.10-prep-Finally-support-Python-3.10.patch
Patch11: py3.10-prep-Fix-a-very-old-refcounting-error-in-time_test.patch
Patch12: py3.10-prep-Fix-parser.py-for-changed-typing-module.patch
Patch13: py3.10-prep-reset-the-type-cache-after-feature-switching.patch


BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): cmake
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-wheel
BuildRequires: libnumpy-py3-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-charts-devel
BuildRequires: qt5-datavis3d-devel
BuildRequires: qt5-remoteobjects-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-scxml-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-speech-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-3d-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-scxml
BuildRequires: qt5-declarative-devel

Provides: python3-pyside2 = %EVR

%filter_from_requires /^python3(shibokensupport.signature.typing)/d
%filter_from_requires /^python3(signature_bootstrap)/d
%global optflags_lto %nil

%description
PySide2 is the official Python module from the Qt for Python project,
which provides access to the complete Qt 5.13+ framework.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility,
since the previous versions (without the 2) refer to Qt 4.

%package devel
Summary: Development files related to %name
Group: Development/Python3
Provides: python-pyside2-devel = %EVR

%description devel
%{summary}.

%package -n pyside2-tools
Summary: PySide2 tools for the Qt 5 framework
Group: Development/Python3
 
%description -n pyside2-tools
PySide2 provides Python bindings for the Qt5 cross-platform application
and UI framework.

This package ships the following accompanying tools:
* pyside2-rcc - PySide2 resource compiler
* pyside2-uic - Python User Interface Compiler for PySide2
* pyside2-lupdate - update Qt Linguist translation files for PySide2

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n shiboken2
Summary: Python/C++ bindings generator for PySide2
Group: Development/Python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/shiboken2/files.dir/shibokensupport

%description -n shiboken2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python3-module-shiboken2
Summary: Python/C++ bindings libraries for PySide2
Group: Development/Python3
Provides: python3-shiboken2 = %EVR

%description -n python3-module-shiboken2
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%package -n python3-module-shiboken2-devel
Summary: Python/C++ bindings helper module for PySide2
Group: Development/Python3
Requires: shiboken2
Requires: python3-module-shiboken2
Provides: python3-shiboken2-devel = %EVR
 
%description -n python3-module-shiboken2-devel
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

The name Shiboken2 and PySide2 make reference to the Qt 5 compatibility, since
the previous versions (without the 2) refer to Qt 4.

%prep
%setup -n pyside-setup-opensource-src-%version
%patch1 -p2
%patch2 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%ifarch %e2k
# Clang ported to Elbrus generates unstable code on -O2
%global _optlevel 1
%endif
export CXX=/usr/bin/clang++
# CMAKE_CXX_FLAGS is already included -O%_optlevel, so CMAKE_CXX_FLAGS_RELEASE need -O2 removed
%cmake -DUSE_PYTHON_VERSION=3 -DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG"
%cmake_build

%install
%cmakeinstall_std

# Generate egg-info manually and install since we're performing a cmake build.
%__python3 setup.py egg_info
for name in PySide2 shiboken2 shiboken2_generator; do
  mkdir -p %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info
  cp -p $name.egg-info/{PKG-INFO,not-zip-safe,top_level.txt} \
        %buildroot%python3_sitelibdir/$name-%version-py%_python3_version.egg-info/
done


%files
%doc README.md
%_libdir/libpyside2*.so.*
%python3_sitelibdir/PySide2
%python3_sitelibdir/PySide2*.egg-info

%files devel
%doc examples
%_datadir/PySide2/
%_includedir/PySide2/
%_libdir/libpyside2*.so
%_libdir/cmake/PySide2*
%_libdir/pkgconfig/pyside2.pc

%files -n pyside2-tools
%doc README.pyside2.md
%_bindir/pyside2-*
%_man1dir/pyside2-*

%files -n shiboken2
%doc README.shiboken2-generator.md
%_bindir/shiboken2
 
%files -n python3-module-shiboken2
%doc README.shiboken2.md
%_libdir/libshiboken2*.so.*
%python3_sitelibdir/shiboken2/
%python3_sitelibdir/shiboken2-*.egg-info/
 
%files -n python3-module-shiboken2-devel
%doc README.shiboken2.md
%_includedir/shiboken2/
%_libdir/cmake/Shiboken2-%version/
%_libdir/libshiboken2*.so
%_libdir/pkgconfig/shiboken2.pc
%python3_sitelibdir/shiboken2_generator/
%python3_sitelibdir/shiboken2_generator-*.egg-info/

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 5.15.2-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt2
- build wth qtwebkit instead of qtwebengine on e2k and ppc64le

* Wed Dec 15 2021 Grigory Ustinov <grenka@altlinux.org> 5.15.2-alt1
- Build new version for python3.10.

* Sat Oct 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.15.0-alt6
- fixed build for Elbrus

* Mon Sep 20 2021 Andrey Cherepanov <cas@altlinux.org> 5.15.0-alt5
- FTBFS: fix build with LTO.

* Tue Feb 16 2021 Grigory Ustinov <grenka@altlinux.org> 5.15.0-alt4
- Fixed build with python3.9.

* Fri Feb 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt3
- merge with p9

* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 5.12.6-alt0.2.p9
- FTBFS: build with llvm7.0.

* Tue Aug 25 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt2
- use g++ on p9

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Sun May 17 2020 Andrey Cherepanov <cas@altlinux.org> 5.12.6-alt0.1.p9
- Backport to p9 (build with g++).

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 5.12.6-alt1
- Initial build in Sisyphus.
