%global srcname qvr

Name:    libqvr
Version: 4.1.0
Release: alt1

Summary: QT library for VR applications
License: MIT
Group:   System/Libraries
Url:     https://github.com/marlam/qvr

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: texlive-collection-latexrecommended
BuildRequires: qt6-base-devel
BuildRequires: doxygen libopenvr-devel

%description
QVR is a library that makes writing Virtual Reality (VR) applications very
easy. It is based on Qt and requires no other libraries.

%package devel
Summary: Development headers and libraries for %name
Group:   Development/C++
Requires: %name = %EVR

%description devel
This package provides development headers and libraries for %name

%package doc
Summary: Additional documentation for %name
Group: Development/Documentation

%description doc
This package provides additional documentation for %name.

%prep
%setup

%build
# Build docs
pushd doc/intro-slides
%make_build
popd

pushd libqvr
%cmake -DQVR_BUILD_DOCUMENTATION=ON
%cmake_build
popd

%install
pushd libqvr
%cmake_install

%files
%doc LICENSE README.md
%_libdir/%name.so.*

%files devel
%_includedir/%srcname
%_libdir/%name.so
%_libdir/cmake/QVR-%version/

%files doc
%doc doc/intro-slides/%srcname.pdf
%doc %_docdir/%name/

%changelog
* Fri Jan 17 2025 Sergey Palcheh <minergenon@altlinux.org> 4.1.0-alt1
- initial build for ALT Sisyphus

