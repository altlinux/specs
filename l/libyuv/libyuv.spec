%ifarch %e2k
%def_disable clang
%else
%def_enable clang
%endif

# check version in include/libyuv/version.h
Name: libyuv
Version: 0.0.1805
Release: alt1.1

Summary: YUV conversion and scaling functionality library

License: BSD
Group: Development/C
Url: http://code.google.com/p/libyuv/

# Source-url: https://chromium.googlesource.com/libyuv/libyuv/+archive/ad890067f661dc747a975bc55ba3767fe30d4452.tar.gz
Source: %name-%version.tar
Patch0: libyuv-alt-buildfix.patch

%if_enabled clang
BuildRequires: clang
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake libstdc++-devel
BuildRequires: libjpeg-devel
BuildRequires: libgtest-devel

%description
This is an open source project that includes YUV conversion and scaling
functionality. Converts all webcam formats to YUV (I420). Convert YUV to
formats for rendering/effects. Rotate by 90 degrees to adjust for mobile
devices in portrait mode. Scale YUV to prepare content for compression,
with point, bilinear or box filter.

%package devel
Summary: The development files for %name
Group: Development/C
Requires: pkgconfig
Requires: %name = %EVR

%description devel
Additional header files for development with %name.

%package tools
Summary: Tools for %name
Group: File tools
Requires: pkgconfig
Requires: %name = %EVR

%description tools
yuvconvert tool.

%prep
%setup
%patch0 -p2

%build
%define optflags_lto %nil
%ifarch %ix86
    %add_optflags -msse2
%endif
%if_enabled clang
export CC=clang
export CXX=clang++
%endif
%cmake \
    -DENABLE_TEST=1 \
    -DCMAKE_SKIP_BUILD_RPATH=1
%cmake_build

%install
%cmake_install
rm -rfv %buildroot/usr/lib/libyuv.a

%check
$(echo */libyuv_unittest)

%files
%doc AUTHORS LICENSE PATENTS
%_libdir/%name.so.*

%files tools
%_bindir/yuvconvert

%files devel
%_includedir/%name/
%_includedir/%name.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Sun Jan 02 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.0.1805-alt1.1
- fixed build for Elbrus

* Fri Nov 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1805-alt1
- up to 1805 git.63ce1d05

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 0.0.1767-alt1
- new version from git ad890067f661dc747a975bc55ba3767fe30d4452
- new version (0.0.1767) with rpmgs script

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.0.1433-alt2.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1433-alt2
- fixed build on aarch64

* Sat Feb 20 2016 Anton Farygin <rider@altlinux.ru> 0.0.1433-alt1
- build new version from Freeswitch fork

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.25.20121221svn522
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.24.20121221svn522
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.22.20121221svn522
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.21.20121221svn522
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.20.20121221svn522
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.19.20121221svn522
- initial fc import

