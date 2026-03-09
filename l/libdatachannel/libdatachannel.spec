%define sover 0.24

Name: libdatachannel
Version: 0.24.1
Release: alt1
Summary: WebRTC network library

License: MPL-2.0
Group: Networking/Other
URL: https://libdatachannel.org/
VCS: https://github.com/paullouisageneau/libdatachannel
Source: %name-%version.tar
Patch: %name-%version-%release.patch

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

%package -n %name%sover
Summary: WebRTC network library
Group: Networking/Other
Obsoletes: %name < %version

%description -n %name%sover
libdatachannel is a standalone implementation of WebRTC Data Channels,
WebRTC Media Transport, and WebSockets in C++17 with C bindings for POSIX
platforms (including GNU/Linux, Android, FreeBSD, Apple macOS and iOS)
and Microsoft Windows.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name%sover = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%autopatch -p1
%ifarch %e2k
sed -i -E 's/(std::.*<.*> .*)\{\};/\1={};/' examples/streamer/ArgParser.hpp
%endif

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPREFER_SYSTEM_LIB=ON \
	-DUSE_GNUTLS=ON \
	-DUSE_NICE=ON
%cmake_build

%install
%cmake_install

%files -n %name%sover
%doc LICENSE
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files devel
%doc README.md DOC.md
%_includedir/rtc/
%_libdir/cmake/LibDataChannel/
%_libdir/%name.so

%changelog
* Mon Mar 09 2026 Anton Midyukov <antohami@altlinux.org> 0.24.1-alt1
- Buil old version 0.24.1.
- Build with -DCMAKE_BUILD_TYPE=RelWithDebInfo.

* Mon Dec 29 2025 Anton Midyukov <antohami@altlinux.org> 0.24.0-alt1
- New version 0.24.0.

* Wed Apr 16 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.22.3-alt2
- e2k build fix

* Sun Dec 08 2024 Anton Midyukov <antohami@altlinux.org> 0.22.3-alt1
- new version (0.22.3) with rpmgs script

* Wed Mar 13 2024 Anton Midyukov <antohami@altlinux.org> 0.20.2-alt1
- new version (0.20.2) with rpmgs script

* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 0.19.3-alt1
- initial build
