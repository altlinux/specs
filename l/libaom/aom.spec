%define _unpackaged_files_terminate_build 1

%define oname aom

# tests require approximately 500Mb of video data and run really long (up to a few hours)
%def_disable check

Name: lib%oname
Version: 0.1
Release: alt1.git6cd8e17
Summary: AV1 Codec Library

Group: System/Libraries
License: BSD
Url: http://aomedia.org/

# https://aomedia.googlesource.com/aom/
Source: %name-%version.tar

BuildRequires: cmake gcc-c++ doxygen /usr/bin/dot

%description
AOMedia Video 1, almost universally referred to as AV1,
is an open, royalty-free video coding format designed
for video transmissions over the Internet.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools for %name
Group: Other
Requires: %name = %EVR

%description tools
The %name-tools package contains tools for %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %name = %EVR

%description docs
The %name-docs package contains documentation files for %name.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DAOM_TARGET_CPU:STRING=generic \
	-DENABLE_DOCS:BOOL=ON \
	-DENABLE_EXAMPLES:BOOL=ON \
	-DENABLE_TOOLS:BOOL=ON

%cmake_build

%install
%cmakeinstall_std

%check
# just add test data and correspondingly modify test data path
# NOTE: running tests may take very long time
export LIBAOM_TEST_DATA_PATH=$(pwd)/.gear/testdata
export LD_LIBRARY_PATH=%buildroot%_libdir:$(pwd)/BUILD/third_party/googletest/src/googletest
%make -C BUILD runtests

%files
%doc LICENSE PATENTS README.md
%_libdir/*.so.*

%files devel
%_includedir/%oname
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*

%files docs
%doc BUILD/docs/html

%changelog
* Fri Jan 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.git6cd8e17
- Initial build for ALT.
