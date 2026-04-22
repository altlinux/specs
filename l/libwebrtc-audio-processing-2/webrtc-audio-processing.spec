%def_enable snapshot

%define _name webrtc-audio-processing
%define ver_major 2
%define api_ver 2

Name: lib%_name-%api_ver
Version: %ver_major.1
Release: alt2

Summary: WebRTC Audio Processing library
License: BSD-3-Clause
Group: System/Libraries
Url: https://freedesktop.org/software/pulseaudio/%_name/

Vcs: https://anongit.freedesktop.org/git/pulseaudio/webrtc-audio-processing

%if_disabled snapshot
Source: %url/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Patch2000: webrtc-e2k.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ libabseil-cpp-devel

%description
WebRTC is an open source project that enables web browsers with
Real-Time Communications (RTC) capabilities via simple Javascript APIs.
The WebRTC components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package devel
Summary: WebRTC Audio Processing library and header files
Group: Development/C

%description devel
libwebrtc-devel contains the libraries and header files needed to
develop programs which make use of %_name

%prep
%setup -n %_name-%version
%ifarch %e2k
%patch2000 -p1
%endif

%build
%add_optflags -Wno-return-type

%ifarch %ix86
%add_optflags -march=native
%endif

%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/lib%_name-%api_ver.so.*
%doc NEWS README.md

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%changelog
* Wed Apr 22 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt2
- updated to v2.1-7-gd0569cf (fixed build with abseil-cpp-202508/gcc-15)

* Sun Jul 06 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1.1
- fixed build for E2K (ilyakurdyukov@)

* Tue Feb 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- first build for Sisyphus
