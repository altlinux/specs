%define _libexecdir %_usr/libexec

Name: peci
Version: 1.0
Release: alt0.1.g230b8570

Summary: A command-line utility with functions that map to the libpeci APIs.
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/openbmc/
Vcs: https://github.com/openbmc/libpeci.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: boost-devel
BuildRequires: systemd-devel

%description
A command-line utility with functions that map to the libpeci APIs. It can be used
to test PECI functionality across the library, driver, and hardware.

A raw-peci daemon that exposes a raw PECI interface that is accessible over D-Bus.
It can be used when an application needs to send a raw PECI command without loading the full PECI library.

%package -n lib%name
Summary: Library files for %name
Group: System/Libraries

%description -n lib%name
libpeci is a library that provides various APIs to interface with the IOCTLs provided by the PECI driver in the OpenBMC kernel.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for developing
applications that use lib%name.

%prep
%setup

%build
export CXXFLAGS="%{optflags} -std=c++23"
%meson -Draw-peci=enabled
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*
%_unitdir/com.intel.peci.service

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc

%changelog
* Wed Aug 20 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt0.1.g230b8570
- Initial build for ALT.

