Name: libcec
Version: 6.0.2
Release: alt1

Summary: CEC support shared library
License: GPLv2
Group: System/Libraries
Url: http://libcec.pulse-eight.com/

Source0: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ libcec-platform-devel liblockdev-devel libudev-devel
BuildRequires: python3-dev rpm-build-python3 swig

%package devel
Summary: CEC support development library
Group: Development/C
Requires: %name = %version-%release

%package utils
Summary: CEC utilities
Group: System/Kernel and hardware
Requires: %name = %version-%release

%package -n python3-module-cec
Summary: libcec python module
Group: Development/Python
Requires: %name = %version-%release

%description
libcec provides support for Pulse-Eight's USB-CEC adapter
and other CEC capable hardware.

%description devel
libcec provides support for Pulse-Eight's USB-CEC adapter
and other CEC capable hardware.
This package contains development files of libcec.

%description utils
libcec provides support for Pulse-Eight's USB-CEC adapter
and other CEC capable hardware.
This package contains commandline utilities of libcec.

%description -n python3-module-cec
libcec provides support for Pulse-Eight's USB-CEC adapter
and other CEC capable hardware.
This package contains Python bindings for libcec.

%prep
%setup
sed -ri '/DESTINATION/ s,lib/python,%_lib/python,' src/libcec/cmake/CheckPlatformSupport.cmake
sed -ri '/set_target_properties.+\sPROPERTIES\sVERSION/d' src/cec*-client/CMakeLists.txt

%build
%cmake -DHAVE_LINUX_API=1
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/libcec
%_pkgconfigdir/libcec.pc

%files utils
%_bindir/cec-client
%_bindir/cecc-client

%files -n python3-module-cec
%_bindir/pyCecClient
%python3_sitelibdir/_cec.so
%python3_sitelibdir/cec.py

%changelog
* Tue Aug 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.2-alt1
- 6.0.2 released

* Tue Nov 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.3-alt1
- 4.0.3 released

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Wed Jul 22 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Fri Jan 09 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Mar 12 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Sun Nov 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.4-alt1
- 2.0.4 released

* Fri Nov 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.3-alt1
- 2.0.3 released

* Fri Oct 26 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- initial
