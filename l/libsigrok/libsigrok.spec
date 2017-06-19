Name: libsigrok
Version: 0.5.0
Release: alt1

Summary: sigrok -- signal analysis software suite
License: GPLv3
Group: System/Libraries
Url: https://sigrok.org/

Source: %name-%version-%release.tar

BuildRequires: glib2-devel libzip-devel libserialport-devel
BuildRequires: libftdi1-devel libusb-devel libieee1284-devel
# c++ bindings
BuildRequires: gcc-c++ doxygen libcheck-devel libglibmm-devel
# python bindings
#BuildRequires: swig pkgconfig(pygobject-3.0)

%package devel
Summary: sigrok -- signal analysis software suite
Group: Development/C

%package -n libsigrokcxx
Summary: sigrok -- signal analysis software suite
Group: System/Libraries

%package -n libsigrokcxx-devel
Summary: sigrok -- signal analysis software suite
Group: Development/C++

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

libsigrok is a shared library written in C which provides the basic API
for talking to hardware and reading/writing the acquired data into various
input/output file formats.

%description devel
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

libsigrok is a shared library written in C which provides the basic API
for talking to hardware and reading/writing the acquired data into various
input/output file formats.

this package provides development part of libsigrok.

%description -n libsigrokcxx
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

libsigrokcxx is a C++ bindings for libsigrok

%description -n libsigrokcxx-devel
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

this package provides development part of libsigrokcxx.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libsigrok.so.*

%files devel
%_libdir/libsigrok.so
%_includedir/libsigrok
%_pkgconfigdir/libsigrok.pc

%files -n libsigrokcxx
%_libdir/libsigrokcxx.so.*

%files -n libsigrokcxx-devel
%_libdir/libsigrokcxx.so
%_includedir/libsigrokcxx
%_pkgconfigdir/libsigrokcxx.pc

%changelog
* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
