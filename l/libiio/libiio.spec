# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libiio
Version: 0.25
Release: alt1
Summary: Library for Industrial IO
License: LGPL-2.0
URL: https://analogdevicesinc.github.io/libiio/
Group: System/Libraries
# Source-url:  https://github.com/analogdevicesinc/%name/archive/v%version.tar.gz
Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libavahi-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: libaio-devel
BuildRequires: libusb-devel
BuildRequires: libxml2-devel
#BuildRequires: man2html
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-sphinx_rtd_theme

%description
Library for interfacing with Linux IIO devices.

libiio is used to interface to Linux Industrial Input/Output (IIO) Subsystem.
The Linux IIO subsystem is intended to provide support for devices that in some 
sense are analog to digital or digital to analog converters (ADCs, DACs). This 
includes, but is not limited to ADCs, Accelerometers, Gyros, IMUs, Capacitance 
to Digital Converters (CDCs), Pressure Sensors, Color, Light and Proximity 
Sensors, Temperature Sensors, Magnetometers, DACs, DDS (Direct Digital 
Synthesis), PLLs (Phase Locked Loops), Variable/Programmable Gain Amplifiers 
(VGA, PGA), and RF transceivers.

%package utils
Summary: Utilities for Industrial IO
Group: Engineering
Requires: %name = %EVR

%description utils
Utilities for accessing IIO using libiio.

%package devel
Summary: Development package for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Files for development with %name.

%package doc
Summary: Development documentation for %name
Group: Development/Documentation
Requires: %name = %EVR

%description doc
Documentation for development with %name.

%package -n python3-iio
Summary: Python 3 bindings for Industrial IO (libiio)
Group: Development/Python3
Requires: %name = %EVR
BuildArch: noarch

%description -n python3-iio
Python 3 bindings for Industrial IO.

%prep
%setup
#sed -i 's/${LIBIIO_VERSION_MAJOR}-doc//' CMakeLists.txt

sed '/set(UDEV_RULES_INSTALL_DIR/d' CMakeLists.txt

%build
%cmake  -DPYTHON_BINDINGS=on \
	-DWITH_DOC=off \
	-DWITH_MAN=on \
	-DUDEV_RULES_INSTALL_DIR=%_udevrulesdir
%cmake_build

%install
%cmake_install

# Remove libtool archives.
find %buildroot -name '*.la' -delete

%files
%doc COPYING.txt
%_libdir/%name.so.*
%_udevrulesdir/90-libiio.rules
%_man1dir/*
%_man3dir/*

%files utils
%_bindir/iio_*
%_sbindir/iiod

%files devel
%_includedir/iio.h
%_libdir/pkgconfig/%name.pc
%_libdir/%name.so

#files doc
#doc %_docdir/%name

%files -n python3-iio
%python3_sitelibdir_noarch/__pycache__/iio*
%python3_sitelibdir_noarch/iio.py
%python3_sitelibdir_noarch/pylibiio*

%changelog
* Mon Aug 12 2024 Anton Midyukov <antohami@altlinux.org> 0.25-alt1
- Initial build
