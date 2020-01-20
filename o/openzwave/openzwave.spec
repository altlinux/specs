Name: openzwave
Version: 1.6
Release: alt1

Summary: API to use a Z-Wave controller
License: LGPLv3
Group: System/Kernel and hardware
Url: http://www.openzwave.com/

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ tinyxml-devel

%package -n libopenzwave
Summary: API to use a Z-Wave controller
Group: System/Libraries

%package -n libopenzwave-devel
Summary: API to use a Z-Wave controller
Group: Development/C++

%define desc OpenZWave is an open-source, cross-platform library designed\
to enable anyone to add support for Z-Wave home-automation devices\
to their applications, without requiring any in depth knowledge of\
the Z-Wave protocol.

%description
%desc

%description -n libopenzwave
%desc
This package contains openzwave shared library.

%description -n libopenzwave-devel
%desc
This package contains development part of openzwave.

%define docdir %_defaultdocdir/openzwave

%prep
%setup

%build
CPPFLAGS='%optflags' USE_BI_TXML=0 USE_HID=0 PREFIX=%prefix \
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=%prefix \
	docdir=%docdir sysconfdir=%_datadir/openzwave \
	instlibdir=%_libdir install

%files
%docdir
%_bindir/MinOZW

%files -n libopenzwave
%_datadir/openzwave
%_libdir/libopenzwave.so.*

%files -n libopenzwave-devel
%_bindir/ozw_config
%_includedir/openzwave
%_libdir/libopenzwave.so
%_pkgconfigdir/libopenzwave.pc

%changelog
* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6-alt1
- initial
