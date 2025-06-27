%define _unpackaged_files_terminate_build 1
%define _udevrulesdir /lib/udev/rules.d

%define sover 0
%define libname %{name}%{sover}

Name: libosmosdr
Version: 0.1.r10.gba4fd96
Release: alt2

Summary: Software defined radio support for OsmoSDR hardware
License: GPL-3.0
Group: Engineering
Url: https://gitea.osmocom.org/sdr/osmo-sdr.git

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0)

%description
OsmoSDR is a 100%% Free Software based small form-factor inexpensive
SDR (Software Defined Radio) project.

The hardware part of OsmoSDR brings information from an antenna connector
to a USB plug.

This package is the software that provides control of the USB hardware
and an API to pass data to software defined radio applications on the host.

This package contains a command line utility.

%package -n %libname
Summary: Software defined radio support for OsmoSDR hardware (library)
Group: System/Libraries

%description -n %libname
OsmoSDR is a 100%% Free Software based small form-factor inexpensive
SDR (Software Defined Radio) project.

The hardware part of OsmoSDR brings information from an antenna connector
to a USB plug.

This package is the software that provides control of the USB hardware
and an API to pass data to software defined radio applications on the host.

This package contains the shared library.

%package devel
Summary: Software defined radio support for OsmoSDR hardware (development files)
Group: Engineering
Requires: %libname = %version

%description devel
OsmoSDR is a 100%% Free Software based small form-factor inexpensive
SDR (Software Defined Radio) project.

The hardware part of OsmoSDR brings information from an antenna connector
to a USB plug.

This package is the software that provides control of the USB hardware
and an API to pass data to software defined radio applications on the host.

This package contains development files.

%prep
%setup -q -n %{name}-%{version}/software/libosmosdr/
%patch -P 0 -p3

%build
%cmake \
      -DLIB_INSTALL_DIR=%_libdir \
      -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# remove static library
rm -rfv %buildroot%_libdir/libosmosdr.a

# put udev-rule file in the correct location
install -m 0644 -D osmosdr.rules %buildroot%_udevrulesdir/10-osmosdr.rules

%files
%doc AUTHORS COPYING README
%_bindir/osmo_sdr
%_udevrulesdir/10-osmosdr.rules

%files -n %libname
%_libdir/libosmosdr.so.%{sover}*

%files devel
%_libdir/libosmosdr.so
%_includedir/*.h
%_libdir/pkgconfig/libosmosdr.pc

%changelog
* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.r10.gba4fd96-alt2
- Applied repocop fix for sisyphus_check

* Mon Jun 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.r10.gba4fd96-alt1
- Initial build for Sisyphus
