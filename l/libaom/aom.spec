%define _unpackaged_files_terminate_build 1

%define oname aom

# tests require approximately 500Mb of video data and run really long (up to a few hours)
%def_disable check

Name: lib%oname
Version: 1.0.0
Release: alt2
Summary: AV1 Codec Library

Group: System/Libraries
License: BSD
Url: http://aomedia.org/

# https://aomedia.googlesource.com/aom/
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

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
%patch1 -p1

# Override old version from changelog
echo -n %version > version

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DAOM_TARGET_CPU:STRING=generic \
	-DENABLE_DOCS:BOOL=ON \
	-DENABLE_EXAMPLES:BOOL=ON \
	-DENABLE_TOOLS:BOOL=ON \
	%nil

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
* Mon Aug 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed version detection (Closes: #37096).

* Thu Feb 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Fri Jan 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.git6cd8e17
- Initial build for ALT.
