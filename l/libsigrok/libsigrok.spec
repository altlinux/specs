Name: libsigrok
Version: 0.6.0
Release: alt0.20230127

Summary: sigrok -- signal analysis software suite
License: GPLv3
Group: System/Libraries
Url: https://sigrok.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ doxygen
BuildRequires: glib2-devel libzip-devel libserialport-devel
BuildRequires: libftdi1-devel libusb-devel libieee1284-devel
BuildRequires: libhidapi-devel libbluez-devel
BuildRequires: libcheck-devel libglibmm-devel python3-dev swig
BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: libnumpy-py3-devel pkgconfig(pygobject-3.0)

%package devel
Summary: sigrok -- signal analysis software suite
Group: Development/C

%package -n libsigrokcxx
Summary: sigrok -- signal analysis software suite
Group: System/Libraries

%package -n libsigrokcxx-devel
Summary: sigrok -- signal analysis software suite
Group: Development/C++

%package -n python3-module-sigrok
Summary: sigrok -- signal analysis software suite
Group: Development/Python

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

%description -n python3-module-sigrok
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

this package provides Python bindings for libsigrok

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
install -pm0644 -D contrib/60-libsigrok.rules %buildroot%_udevrulesdir/60-libsigrok.rules
install -pm0644 contrib/61-libsigrok-plugdev.rules %buildroot%_udevrulesdir/
install -pm0644 contrib/61-libsigrok-uaccess.rules %buildroot%_udevrulesdir/

%pre
%_sbindir/groupadd -r -f plugdev &> /dev/null

%files
%_udevrulesdir/*-libsigrok*.rules
%_libdir/libsigrok.so.*
%_datadir/mime/packages/*.xml
%_iconsdir/hicolor/*/*/*

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

%files -n python3-module-sigrok
%python3_sitelibdir/sigrok
%python3_sitelibdir/libsigrok-%version-*-info

%changelog
* Wed Feb 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.20230127
- git snapshot libsigrok-unreleased-1543-ge7c7aa11

* Mon Jun 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.20220423
- git snapshot libsigrok-unreleased-1460-ge3847923

* Tue Aug 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.20210723
- git snapshot libsigrok-unreleased-1316-gb96051a5

* Wed Jul 15 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt1
- 0.5.2 released

* Tue Oct 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.1-alt1
- 0.5.1 released

* Fri Oct 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt3
- buildreqs revised

* Wed Jun 21 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt2
- added udev rules file, uaccess and group based

* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
