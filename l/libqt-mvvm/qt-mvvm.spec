%define _unpackaged_files_terminate_build 1

Name: libqt-mvvm
Version: 0.2.0
Release: alt2

Summary: This model-view-viewmodel framework is intended for development of large Qt based applications written in C++.
License: GPLv3+
Group: System/Libraries
Url: https://github.com/gpospelov/qt-mvvm

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
This model-view-viewmodel framework is intended for development of
large Qt based applications written in C++.
Main features of the framework are:
    Application model to store arbitrary data of GUI session.
    Serialization of application models to json.
    Undo/redo based on command pattern.
    View model to show parts of application model in Qt widgets. Depends on Qt.
    Scientific plotting based on qcustomplot.
    Automatic generation of widgets from model content.
    Property editors.
    Flexible layout of Qt's trees and tables.

%package -n libqt-mvvm-devel
Summary: Headers for libqt-mvvm framework.
Group: Development/KDE and QT
Requires: libqt-mvvm = %version-%release
Provides: libqt-mvvm-devel = %version-%release

%description -n libqt-mvvm-devel
The libqt-mvvm-devel package contains the header files needed to
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
%_libdir/libmvvm_*.so.*

%files -n libqt-mvvm-devel 
%_libdir/cmake/mvvm/*
%_libdir/libmvvm_*.so
%_includedir/*

%changelog
* Wed Apr 06 2021 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt2
- Fixes:
  - Improve package description.
  - Provide better separation between development and library packages.

* Wed Apr 06 2021 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt1
- Initial build

