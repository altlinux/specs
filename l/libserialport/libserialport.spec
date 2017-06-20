Name: libserialport
Version: 0.1.1
Release: alt2

Summary: Serial port handling library
License: LGPLv3
Group: System/Libraries
Url: https://sigrok.org/

Source: %name-%version-%release.tar

%package devel
Summary: Serial port handling library
Group: Development/C

%description
libserialport is a minimal library written in C that is intended
to take care of the OS-specific details when writing software
that uses serial ports.
this package contains libserialport shared library.

%description devel
libserialport is a minimal library written in C that is intended
to take care of the OS-specific details when writing software
that uses serial ports.
this package contains libserialport development part.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libserialport.so.*

%files devel
%_libdir/libserialport.so
%_includedir/libserialport.h
%_pkgconfigdir/libserialport.pc

%changelog
* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.1-alt2
- initial
