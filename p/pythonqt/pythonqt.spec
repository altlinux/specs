%define _unpackaged_files_terminate_build 1

Name: pythonqt
Version: 3.6.1
Release: alt1
Summary: CMake-ified version of PythonQt
License: LGPL-2.1
Group: Development/C++
Url: https://github.com/commontk/PythonQt
VCS: https://github.com/commontk/PythonQt.git
Source: %name-%version.tar

Patch1: pythonqt-alt-install.patch

BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel qt5-declarative-devel-static qt5-multimedia-devel qt5-svg-devel qt5-tools-devel-static qt5-xmlpatterns-devel
BuildRequires: python3-devel

%description
PythonQt is a dynamic Python binding for Qt.
It offers an easy way to embed the Python scripting language into your Qt applications.

%package -n lib%name
Summary: CMake-ified version of PythonQt
Group: System/Libraries

%description -n lib%name
PythonQt is a dynamic Python binding for Qt.
It offers an easy way to embed the Python scripting language into your Qt applications.

This package contains PythonQt shared libraries.

%package devel
Summary: CMake-ified version of PythonQt
Group: Development/C++
Requires: lib%name = %EVR

%description devel
PythonQt is a dynamic Python binding for Qt.
It offers an easy way to embed the Python scripting language into your Qt applications.

This package contains development files for PythonQt.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DPythonQt_Wrap_QtAll:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc COPYING
%doc README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Jul 30 2025 Anton Farygin <rider@altlinux.com> 3.6.1-alt1
- updated to 3.6.1 from the CTK git repository

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 0-alt3.git.dafdb72
- Fixed build with python3.11.

* Wed Jan 12 2022 Grigory Ustinov <grenka@altlinux.org> 0-alt2.git.dafdb72
- Fixed build with python3.10.

* Mon May 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0-alt1.git.dafdb72
- Initial build for ALT.
