%define soversion() %(echo "%1" | awk -F. '{print $1"."$2}')

Name: libdatachannel
Version: 0.19.3
Release: alt1
Summary: WebRTC network library featuring Data Channels, Media Transport, and WebSockets

License: MPL-2.0
Group: Networking/Other
Url: https://libdatachannel.org/
# Source-url: https://github.com/paullouisageneau/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: nlohmann-json-devel
BuildRequires: plog-devel
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(nice)
BuildRequires: libsrtp2-devel
BuildRequires: libusrsctp-devel
BuildRequires: libgnutls-devel
BuildRequires: libnettle-devel

%description
libdatachannel is a standalone implementation of WebRTC Data Channels,
WebRTC Media Transport, and WebSockets in C++17 with C bindings for POSIX
platforms (including GNU/Linux, Android, FreeBSD, Apple macOS and iOS)
and Microsoft Windows.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake -DPREFER_SYSTEM_LIB=ON -DUSE_GNUTLS=ON -DUSE_NICE=ON
%cmake_build

%install
%cmake_install

%files
%doc LICENSE
%_libdir/%name.so.%{soversion %version}*

%files devel
%doc README.md DOC.md
%_includedir/rtc/
%_libdir/cmake/LibDataChannel/
%_libdir/%name.so

%changelog
* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 0.19.3-alt1
- initial build
