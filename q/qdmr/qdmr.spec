
Name: qdmr
Version: 0.10.4
Release: alt1

Summary: GUI application and command-line-tool to program DMR radios
License: GPLv3+
Group: Engineering

Url: https://dm3mat.darc.de/qdmr
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libusb-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-tools-devel
BuildRequires: rpm-macros-cmake

%description
QDMR is a friendly code-plug programming software for DMR radios.
QDMR supports radios by several vendors, and stores code-plug in
a human readable format.

%package -n libdmrconf
Summary: DMR radios programming library
Group: System/Libraries

%description -n libdmrconf
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats.

%package -n libdmrconf-devel
Summary: DMR radios programming library - development files
Group: Development/KDE and QT
Requires: qt5-base-devel
Requires: libyaml-cpp-devel

%description -n libdmrconf-devel
QDMR is a friendly code-plug programming software for DMR radios.
libdmrconf handles the actual programming of radios via UART and
conversion of code-plug between human readable and vendor-specific
binary formats. This package is useful for developing software
with libdmrconf. It is not required for QDMR users.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/qdmr
%_bindir/dmrconf
%_sysconfdir/udev/rules.d/*
%_datadir/icons/hicolor/*/*.png
%_datadir/applications/qdmr.desktop

%files -n libdmrconf
%prefix/%_lib/libdmrconf.so.*

%files -n libdmrconf-devel
%prefix/%_lib/libdmrconf.so
%prefix/include/libdmrconf/*.hh
%prefix/include/libdmrconf/*.h

%changelog
* Wed Nov 30 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.4-alt1
- v0.10.3
- Amongst other things fixes detection of DM-1701

* Sun May 22 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.10.2.2-alt1
- Initial build
