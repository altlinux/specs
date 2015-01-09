Name: libcec
Version: 2.2.0
Release: alt1

Summary: CEC Adaptor communication shared library
License: GPL
Group: System/Libraries
Url: http://libcec.pulse-eight.com/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ liblockdev-devel libudev-devel

%package devel
Summary: CEC Adaptor communication development library
Group: Development/C
Requires: %name = %version-%release

%package utils
Summary: CEC Adaptor commulication utilities
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description
libcec provides support for the Pulse-Eight USB-CEC adapter.

%description devel
libcec provides support for the Pulse-Eight USB-CEC adapter.
This package contains development files of libcec.

%description utils
libcec provides support for the Pulse-Eight USB-CEC adapter.
This package contains commandline utilities of libcec.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/libcec
%_pkgconfigdir/libcec.pc

%files utils
%_bindir/cec-client

%changelog
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
