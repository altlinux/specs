Name: webrtc-audio-processing
Version: 0.1
Release: alt2
Summary: WebRTC Audio Processing library
License: BSD
Group: System/Libraries
Url: http://code.google.com/p/webrtc/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz
Patch: %name-%version-alt-link.patch
Patch1: webrtc-fix-typedefs-on-other-arches.patch

BuildRequires: gcc-c++

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc
Summary: WebRTC Audio Processing library
Group: System/Libraries

%description -n libwebrtc
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-devel
Summary: WebRTC Audio Processing library and header files
Group: Development/C
Requires: libwebrtc = %version-%release

%description -n libwebrtc-devel
libwebrtc-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files -n libwebrtc
%_libdir/*.so.*

%files -n libwebrtc-devel
%_includedir/webrtc_audio_processing
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Sep 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt2
- Fixed build on non-x86 architectures.

* Sun May 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release

