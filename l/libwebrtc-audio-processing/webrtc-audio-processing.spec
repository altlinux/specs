%define rname webrtc-audio-processing

Name: lib%rname
Version: 1.3
Release: alt1
Summary: WebRTC Audio Processing library
License: BSD
Group: System/Libraries
Url: https://freedesktop.org/software/pulseaudio/%rname/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %url/%rname-%version.tar.gz
Patch: webrtc-fix-typedefs-on-other-arches.patch

BuildRequires: gcc-c++ meson libabseil-cpp-devel

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package devel
Summary: WebRTC Audio Processing library and header files
Group: Development/C

%description devel
libwebrtc-devel contains the libraries and header files needed to
develop programs which make use of %rname

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%add_optflags -Wno-return-type
%ifarch %ix86
%add_optflags -march=native
%endif
%meson
%meson_build

%install
%meson_install

%files
%doc NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/webrtc-audio-processing-1
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Sep 14 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3 (closes: #47582)

* Wed May 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt2
- Restored patch for generic arch support.

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3 from freedesktop.org

* Fri Sep 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt2
- Fixed build on non-x86 architectures.

* Sun May 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release
