%define _unpackaged_files_terminate_build 1

%define soname 1

Name: partio
Version: 1.14.6
Release: alt1
Summary: A library for particle IO and manipulation
Group: Development/Other
License: BSD-3-Clause
URL: https://github.com/wdas/partio

# https://github.com/wdas/partio.git
Source: %name-%version.tar

Patch1: partio-fedora-version-libraries.patch
Patch2: partio-alt-install-tests.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: cmake gcc-c++
BuildRequires: python3-devel
BuildRequires: freeglut-devel
BuildRequires: libglvnd-devel
BuildRequires: zlib-devel
BuildRequires: swig
BuildRequires: doxygen /usr/bin/dot
BuildRequires: libgtest-devel
BuildRequires: ctest

%add_python3_req_skip Qt Qt.QtCore Qt.QtGui Qt.QtWidgets

%description
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

%package -n lib%name%soname
Summary: A library for particle IO and manipulation
Group: System/Libraries

%description -n lib%name%soname
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

%package devel
Summary: A library for particle IO and manipulation
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR
Requires: python3-module-%name = %EVR
Requires: %name-tests = %EVR

%description devel
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

This package contains development files for Partio.

%package doc
Summary: A library for particle IO and manipulation
Group: Documentation

%description doc
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

This package contains documentation for Partio.

%package -n python3-module-%name
Summary: A library for particle IO and manipulation
Group: Development/Python3

%description -n python3-module-%name
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

This package contains python bindings for Partio.

%package tests
Summary: A library for particle IO and manipulation
Group: Development/Other

%description tests
C++ (with python bindings) library for easily reading/writing/manipulating
common animation particle formats such as PDB, BGEO, PTC.

This package contains tests for Partio.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i \
	-e "s:@PROJECT_VERSION_FULL@:%version:g" \
	-e "s:@PROJECT_VERSION@:$(echo %version | cut -d . -f 1):g" \
	src/lib/CMakeLists.txt

# change python shebangs to python3
find . -name '*.py' | xargs sed -i \
	-e '1s|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
	-e '1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
	%nil

%build
%cmake \
	-DCXXFLAGS_STD=c++17 \
	-DPARTIO_GTEST_ENABLED:BOOL=ON \
	%nil

%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_datadir/swig/%{name}.i

%files -n lib%name%soname
%doc LICENSE
%doc README.md
%_libdir/lib*.so.%{soname}
%_libdir/lib*.so.%{soname}.*

%files devel
%_includedir/*
%_libdir/lib*.so

%files doc
%doc %_defaultdocdir/%name/html

%files -n python3-module-%name
%python3_sitelibdir/*.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.so

%files tests
%dir %_libdir/partio
%_libdir/partio/test

%changelog
* Wed Jan 25 2023 Nazarov Denis <nenderus@altlinux.org> 1.14.6-alt1
- Version 1.14.6

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.0-alt1
- Initial build for ALT.
