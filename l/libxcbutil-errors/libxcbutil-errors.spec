# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define abi_ver 0
%define srcname xcb-util-errors

Name: libxcbutil-errors
Version: 1.0.1
Release: alt1
Summary: XCB utility library that gives readable names to error, event, & request codes
Group: System/Libraries
License: X11
Url: http://xcb.freedesktop.org
# Source-url: %url/dist/%srcname-%version.tar.xz
Source: %srcname-%version.tar

BuildRequires: python3-devel
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-proto)
BuildRequires: pkgconfig(xorg-macros) >= 1.16.0

%description
xcb-util-errors is a utility library that gives human readable names to error
codes and event codes and also to major and minor numbers. The necessary
information is drawn from xcb-proto's protocol descriptions.
This library is especially useful when working with extensions and is mostly
useful for debugging.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %srcname-%version

%build
%autoreconf
%configure --disable-static PYTHON=%_bindir/python3
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_libdir/libxcb-errors.so.%{abi_ver}*

%files devel
%_includedir/xcb/xcb_errors.h
%_libdir/libxcb-errors.so
%_pkgconfigdir/xcb-errors.pc

%changelog
* Mon Dec 25 2023 Anton Midyukov <antohami@altlinux.org> 1.0.1-alt1
- initial build for ALT Sisyphus
