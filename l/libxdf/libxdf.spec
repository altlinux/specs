%define _unpackaged_files_terminate_build 1

%define soname 0

Name: libxdf
Version: 0.99.6
Release: alt2
Summary: C++ library for loading XDF files 
Group: Sciences/Medicine
License: BSD-2-Clause
Url: https://xdf-modules.github.io/libxdf/

# https://github.com/xdf-modules/libxdf.git
Source: %name-%version.tar

Patch1: %name-upstream-install.patch
Patch2: %name-alt-build-shared-library.patch
Patch3: 0001-Fix-build-on-GCC13.patch

BuildRequires: gcc-c++ cmake
BuildRequires: libpugixml-devel

%description
Libxdf is a cross-platform C++ library for loading multimodal, multi-rate signals
stored in XDF files. Libxdf is used in the biosignal viewing application SigViewer
and the LSL application XDFStreamer.

It can also be integrated into other C++ applications.

%package devel
Summary: C++ library for loading XDF files 
Group: Development/C++
Requires: %name = %EVR

%description devel
Libxdf is a cross-platform C++ library for loading multimodal, multi-rate signals
stored in XDF files. Libxdf is used in the biosignal viewing application SigViewer
and the LSL application XDFStreamer.

It can also be integrated into other C++ applications.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# remove bundled copy of pugixml
rm -rf pugixml

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.txt
%doc README.md CHANGELOG.txt
%_libdir/*.so.%{soname}
%_libdir/*.so.%{soname}.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/%name

%changelog
* Tue Jul 18 2023 Artyom Bystrov <arbars@altlinux.org> 0.99.6-alt2
- Fix build on GCC13

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.99.6-alt1
- Initial build for ALT.
