Name: libyuv
Summary: YUV conversion and scaling functionality library
Version: 0.0.1433
Release: alt1
License: BSD
Group: Development/C
Url: http://code.google.com/p/libyuv/
# https://freeswitch.org/stash/scm/sd/libyuv.git
# http://files.freeswitch.org/repo/deb/debian/pool/main/liby/libyuv/
Source0: %name-%version.tar
Patch0: libyuv-alt-buildfix.patch
BuildRequires: libgtest-devel gcc-c++
BuildRequires: libjpeg-devel cmake

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
Requires: %name = %version-%release

%description devel
Additional header files for development with %name.

%prep
%setup
%patch0 -p2

%build
%ifarch %ix86
    %add_optflags -msse2
%endif
%cmake
%make -C BUILD

%install
%make -C BUILD install DESTDIR=%buildroot

%files
%doc AUTHORS LICENSE PATENTS
%_libdir/%name.so.*

%files devel
%_includedir/%name
%_includedir/%name.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
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

