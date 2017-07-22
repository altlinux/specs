%define oname libwebrtc-audio-processing
Name: libwebrtc-audio-processing
Version: 0.3
Release: alt1

Summary: Library for echo cancellation

License: BSD
Group: Development/C++
Url: http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%oname-%version.tar.xz
Source: %name-%version.tar

Patch0: webrtc-fix-typedefs-on-other-arches.patch
# WIP to only explicitly add -mfpu=neon where needed for neon runtime detection
# currently doesn't work due to %%configure injecting incompatible CFLAGS atm, see below
Patch1: webrtc-audio-processing-0.3-neon.patch
# bz#1336466, https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch4: webrtc-audio-processing-0.2-big-endian.patch

BuildRequires: gcc-c++

%description
webrtc-audio-processing is a library derived from Google WebRTC project that
provides echo cancellation functionality. This library is used by for example
PulseAudio to provide echo cancellation.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/C++

%description devel
The %name-devel package contains libraries and header
files for developing applications that use %name.

%prep
%setup
%patch0 -p1 -b .typedef
%patch1 -p1 -b .neon
%patch4 -p1 -b .bigendian

%build
# for patch1
%autoreconf
%ifarch %arm
# disable neon support
# can't unconditionally enable neon, and --enable-neon=runtime is broken (WebRtc_GetCPUFeaturesARM is unimplemented)
%global neon --enable-neon=no
## hack to ensure -mfpu=neon flag appears last when using --enable-neon=yes|runtime
#export CFLAGS="%optflags -mfpu=neon"
#export CXXFLAGS="%optflags -mfpu=neon"
## except that enables it for *all* objects, not just the ones we want (see patch1),
## seems CFLAGS always trumps project flags, see also:
## http://www.gnu.org/software/automake/manual/html_node/Flag-Variables-Ordering.html
%endif

%configure \
  %{?neon} \
  --disable-silent-rules \
  --disable-static
%make_build

%install
%makeinstall_std

%files
%doc NEWS AUTHORS README.md
%doc COPYING
%_libdir/libwebrtc_audio_processing.so.1*

%files devel
%_libdir/libwebrtc_audio_processing.so
%_pkgconfigdir/webrtc-audio-processing.pc
%_includedir/webrtc_audio_processing/

%changelog
* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.3-1
- 0.3

* Fri May 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-7
- better/upstreamable x86_msse2.patch

* Fri May 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-6
- simpler/upstreamable no_undefined.patch (fdo#96244)

* Wed May 25 2016 Than Ngo <than@redhat.com> - 0.2-5
- add url to upstream bug report

* Tue May 24 2016 Than Ngo <than@redhat.com> - 0.2-4
- add support big endian

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-3
- ExclusiveArch primary archs, FTBFS on big endian arches (#1336466)

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-2
- link w/ --no-undefined
- fix x86 sse2 runtime detection

* Thu May 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.2-1
- webrtc-audio-processing-0.2 (#1335536)
- %%files: track ABI/API closer

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Kyle McMartin <kyle@fedoraproject.org> - 0.1-6
- webrtc-fix-typedefs-on-other-arches.patch: fix ftbfs on non-x86/arm due to
  a build #error in typedefs.h, however, the defines are not used anywhere in
  the code. Fixes build on ppc{,64}, s390x, and aarch64.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Debarshi Ray <rishi@fedoraproject.org> 0.1-4
- Rebuilt to fix broken binary possibly caused by broken toolchain

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 9 2012 Dan Horák <dan[at]danny.cz> 0.1-2
- set ExclusiveArch x86 and ARM for now

* Fri Oct 5 2012 Christian Schaller <christian.schaller@gmail.com> 0.1-1
- Initial Fedora spec.
