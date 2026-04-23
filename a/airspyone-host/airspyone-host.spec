%define _unpackaged_files_terminate_build 1
%define _udevrulesdir /lib/udev/rules.d

%define shortname airspy
%define major 0
%define libname lib%{shortname}%{major}
%define devel_name lib%{shortname}-devel

Name: airspyone-host
Version: 1.0.10
Release: alt3

Summary: AirSpy - tiny and efficient software defined radio receiver
License: GPL-2.0 and MIT and BSD
Group: Engineering
URL: http://airspy.com/
VCS: https://github.com/airspy/airspyone_host

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0)

%description
Airspy is an open source Software Defined Radio that can receive
between 24 MHz and 1750 MHz. Airspy has a 10 MHz bandwidth.
12bit ADC @ 20 MSPS (80dB SFDR, 64dB SNR, 10.4 ENOB).
It is a High Speed USB device powered by the USB bus.

This package contains a set of command line utilities:
* airspy_cpldjtag: program CLPD
* airspy_info: probe device and show configuration
* airspy_max2837: chip register read/write tool
* airspy_rffc5071: chip register read/write tool
* airspy_si5351c: chip register read/write tool
* airspy_spiflash: read and write flash data from file.
* airspy_transfer: file based transmit and receive sdr

%package -n %libname
Group: Engineering
Summary: AirSpy - tiny and efficient software defined radio receiver (library)
Requires: %name = %{version}-%{release}

%description -n %libname
Airspy is an open source Software Defined Radio that can receive
between 24 MHz and 1750 MHz. Airspy has a 10 MHz bandwidth.
12bit ADC @ 20 MSPS (80dB SFDR, 64dB SNR, 10.4 ENOB).
It is a High Speed USB device powered by the USB bus.

This package contains the shared library.

%package -n %devel_name
Group: Engineering
Summary: AirSpy - tiny and efficient software defined radio receiver (development)
Requires: %libname = %{version}-%{release}
Provides: %{shortname}-devel = %{version}-%{release}

%description -n %devel_name
Airspy is an open source Software Defined Radio that can receive
between 24 MHz and 1750 MHz. Airspy has a 10 MHz bandwidth.
12bit ADC @ 20 MSPS (80dB SFDR, 64dB SNR, 10.4 ENOB).
It is a High Speed USB device powered by the USB bus.

This package contains development files.

%prep
%setup
%patch -p1

%build
%add_optflags -std=gnu17
%cmake \
       -DINSTALL_UDEV_RULES=ON \
       -Wno-dev
%cmake_build

%install
%cmake_install

# move udev-rule file to the correct location
mkdir -p %buildroot%_udevrulesdir
mv -v %buildroot%_sysconfdir/udev/rules.d/52-%{shortname}.rules %buildroot%_udevrulesdir/52-%{shortname}.rules

# remove static library
find %buildroot -name "*.a" -delete -print

%files
%_udevrulesdir/52-%{shortname}.rules
%_bindir/%{shortname}_*

%files -n %libname
%_libdir/lib%{shortname}.so.*

%files -n %devel_name
%_libdir/pkgconfig/lib%{shortname}.pc
%_libdir/lib%{shortname}.so
%dir %_includedir/lib%{shortname}
%_includedir/lib%{shortname}/*.h

%changelog
* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.10-alt3
- Fixed FTBFS caused by gcc15.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.10-alt2
- Applied repocop fix for sisyphus_check

* Mon Jun 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus
