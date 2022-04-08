%define _unpackaged_files_terminate_build 1

Name: libqt-mvvm
Version: 0.2.0
Release: alt1

Summary: This model-view-viewmodel framework is intended for development of large Qt based applications written in C++.
License: GPLv3+
Group: Other
Url: https://github.com/august-alt/qt-mvvm

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-common
BuildRequires: doxygen
BuildRequires: qcustomplot-qt5-devel

Source0: %name-%version.tar

%description
Group policy editor

%package -n libqt-mvvm-devel
Summary: Headers for libqt-mvvm framework.
Group: Development/C
Requires: libqt-mvvm = %version-%release
Provides: libqt-mvvm-devel = %version-%release

%description -n libqt-mvvm-devel
The libsmbclient-devel package contains the header files needed to
develop programs that use set libqt-mvvm libraries.

%prep
%setup -q

%build
%cmake -DMVVM_DISCOVER_TESTS=OFF -DMVVM_ENABLE_FILESYSTEM=OFF -DMVVM_BUILD_EXAMPLES=OFF -DMVVM_USE_SYSTEM_QCUSTOMPLOT=ON
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_libdir/libmvvm_*

%files -n libqt-mvvm-devel 
%_libdir/cmake/mvvm/*
%_includedir/*

%changelog
* Wed Apr 06 2021 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt1
- Initial build

