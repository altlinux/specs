%define _unpackaged_files_terminate_build 1

Name: CTKAppLauncherLib
Version: 0.1.29
Release: alt1
Summary: Simple and small program allowing to set the environment of any executable
License: Apache-2.0
Group: Development/Tools
Url: https://commontk.org/

ExcludeArch: %arm

# https://github.com/commontk/AppLauncher.git
Source: %name-%version.tar

# copied from CTK
Source1: ctkExport.h.in

Patch1: ctkapplauncherlib-alt-build.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel

Requires: lib%name = %EVR

%description
CTK Application launcher is a lightweight open-source utility
allowing to set environment before starting a real application.

%package -n lib%name
Summary: Simple and small program allowing to set the environment of any executable
Group: System/Libraries

%description -n lib%name
CTK Application launcher is a lightweight open-source utility
allowing to set environment before starting a real application.

This package contains CTKAppLauncherLib shared libraries.

%package devel
Summary: Simple and small program allowing to set the environment of any executable
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR

%description devel
CTK Application launcher is a lightweight open-source utility
allowing to set environment before starting a real application.

This package contains development files for CTKAppLauncherLib.

%prep
%setup
%patch1 -p1

install -d Libs
install %SOURCE1 ./Libs/CTKExport.h.in

%build
%cmake \
	-DCTKAppLauncher_QT_VERSION=5 \
	-DCTKAppLauncher_INSTALL_LauncherLibrary:BOOL=ON \
	-DCTKAppLauncher_INSTALL_DEVELOPMENT:BOOL=ON \
	-DCTKAppLauncher_VISIBILITY_HIDDEN:BOOL=OFF \
	-DCTK_INSTALL_LIB_DIR:STRING=%_lib \
	-DCTK_INSTALL_CMAKE_DIR:STRING=%_lib/cmake/%name \
	-DCTK_INSTALL_CONFIG_DIR:STRING=%_lib/cmake/%name \
	-DBUILD_TESTING:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%files -n lib%name
%doc LICENSE_Apache_20
%doc README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%changelog
* Mon May 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.29-alt1
- Initial build for ALT.
