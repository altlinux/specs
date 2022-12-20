%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname aom
%define soname 3
%define libname lib%{oname}%{soname}

# tests require downloading ~750Mb of video data
# and run really long (up to a few hours)
%def_disable longcheck

# TODO: remove later this fix for documentation
%define _cmake__builddir BUILD

Name: lib%oname
Version: 3.5.0
Release: alt1
Summary: AV1 Codec Library
Group: System/Libraries
License: BSD-2-Clause
Url: https://aomedia.org/

# https://aomedia.googlesource.com/aom/
Source: %name-%version.tar
# ffmpeg -i testdata/rush_hour_444.y4m -vframes 10 -pix_fmt yuv420p rush_hour_420.yuv
Source1: rush_hour_420.yuv

Patch1: %name-alt-version.patch
Patch2: %name-alt-dont-install-static-libs.patch
Patch2000: %name-e2k-simd.patch

BuildRequires: cmake gcc-c++ doxygen /usr/bin/dot
%ifarch %ix86 x86_64
BuildRequires: yasm
%endif
%if_enabled longcheck
BuildRequires: python3
%endif

%description
AOMedia Video 1, almost universally referred to as AV1,
is an open, royalty-free video coding format designed
for video transmissions over the Internet.

%package -n %libname
Summary: AV1 Codec Library
Group: System/Libraries

%description -n %libname
AOMedia Video 1, almost universally referred to as AV1,
is an open, royalty-free video coding format designed
for video transmissions over the Internet.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %libname = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools for %name
Group: Other
Requires: %libname = %EVR

%description tools
The %name-tools package contains tools for %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
Requires: %libname = %EVR

%description docs
The %name-docs package contains documentation files for %name.

%prep
%setup
%patch1 -p1
%patch2 -p1
cp -p %SOURCE1 .
%ifarch %e2k
%patch2000 -p1
%endif

# Override old version from changelog
echo -n %version > version

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
%ifarch armh ppc64le
	-DAOM_TARGET_CPU:STRING=generic \
%endif
	-DENABLE_DOCS:BOOL=ON \
	-DENABLE_EXAMPLES:BOOL=ON \
	-DENABLE_TOOLS:BOOL=ON \
%if_disabled longcheck
	-DENABLE_TESTS:BOOL=OFF \
%endif
	%nil

%cmake_build

%install
%cmakeinstall_std

%check
# simple check using examples
export LD_LIBRARY_PATH=%buildroot%_libdir
%_cmake__builddir/examples/lossless_encoder 352 288 rush_hour_420.yuv rush_hour_420.av1
%_cmake__builddir/examples/simple_decoder rush_hour_420.av1 output.yuv
cmp rush_hour_420.yuv output.yuv

%if_enabled longcheck
# just add test data and correspondingly modify test data path
# NOTE: running tests may take very long time
export LIBAOM_TEST_DATA_PATH=$(pwd)/testdata
export LD_LIBRARY_PATH=%buildroot%_libdir:$(pwd)/%_cmake__builddir/third_party/googletest/src/googletest
%make -C %_cmake__builddir runtests
%endif

%files -n %libname
%doc LICENSE PATENTS README.md
%_libdir/*.so.%{soname}
%_libdir/*.so.%{soname}.*

%files devel
%_includedir/%oname
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*

%files docs
%doc %_cmake__builddir/docs/html

%changelog
* Tue Dec 20 2022 Valery Inozemtsev <shrek@altlinux.ru> 3.5.0-alt1
- Updated to upstream version 3.5.0.

* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Tue Dec 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Mon Aug 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.2-alt2
- Disabled installation of static libraries.

* Tue Jul 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.2-alt1
- Updated to upstream version 3.1.2.

* Mon Jun 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1
- Updated to upstream version 3.1.0.

* Wed Jun 02 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.0.0-alt5
- ppc64le optimizations excluded (failed tests)

* Tue Jun 01 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.0.0-alt4
- added simple check

* Mon May 31 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.0.0-alt3
- enabled target specific optimizations (except armh)
- added SIMD patch for Elbrus

* Mon May 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt2
- Fixed build with new cmake macros (Closes: #40126).

* Fri Apr 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Wed Mar 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1
- Updated to upstream version 2.0.2.

* Mon Jan 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1
- Updated to upstream version 2.0.1.

* Thu Jul 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Mon Aug 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed version detection (Closes: #37096).

* Thu Feb 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Fri Jan 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.git6cd8e17
- Initial build for ALT.
