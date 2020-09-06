# https://bugzilla.altlinux.org/show_bug.cgi?id=38832
%def_without packaged_openh264
%def_with packaged_vpx

Name: libowt-tg
Version: 4.3.0.1
Release: alt1

Summary: Open WebRTC Toolkit with Telegram desktop patches

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/desktop-app/tg_owt

# Source-url: https://github.com/desktop-app/tg_owt/archive/master.zip
Source: %name-%version.tar

# Source1-url: https://github.com/desktop-app/patches/archive/master.zip
#Source1: patches-%version.tar

Patch2: 0001-system-arch.h-improve-arch-detection-via-gcc-defines.patch
Patch3: fix-absl-build.patch
Patch4: 0001-add-support-for-packaged-libvpx-enabled-via-TG_OWT_V.patch

ExcludeArch: armh

# Automatically added by buildreq on Sun Aug 23 2020
BuildRequires: libalsa-devel libavformat-devel libdb4-devel libjpeg-devel libopus-devel libpulseaudio-devel libssl-devel yasm

BuildRequires: gcc-c++ cmake ninja-build

%if_with packaged_vpx
BuildRequires: libvpx-devel
%endif

%if_with packaged_openh264
BuildRequires: libopenh264-devel
%endif

# TODO: obsoleted in the distro
#BuildRequires: libyuv-devel

#add_optflags -D_FILE_OFFSET_BITS=64

%description
Open WebRTC Toolkit with Telegram desktop patches.

WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.
WebRTC implements the W3C's proposal for video conferencing on the web.

%package devel
Summary: Open WebRTC Toolkit library and header files
Group: Development/C
#Requires: %name = %EVR
AutoReq:no
AutoProv:no

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup
%patch2 -p1
%patch3 -p2
%patch4 -p1

%if_with packaged_vpx
rm -rfv src/third_party/libvpx/
%endif

%if_with packaged_openh264
rm -rfv src/third_party/openh264/
mkdir -p src/third_party/openh264/src/codec/api/
ln -s %_includedir/wels src/third_party/openh264/src/codec/api/svc
%__subst "s|.*openh264.*||" CMakeLists.txt
%endif

#rm -rfv src/third_party/libyuv/
#mkdir -p src/third_party/libyuv/
#ln -s %_includedir src/third_party/libyuv/include

# TODO: implement via cmake
cat <<EOF >cmake/arch.cmake
# generated in spec
set(is_x86 0)
set(is_x64 0)
set(is_arm7 0)
set(is_arm8 0)
set(is_arm 0)

EOF
%ifarch armh
cat <<EOF >>cmake/arch.cmake
set(is_arm7 1)
set(is_arm 1)
EOF
%endif
%ifarch aarch64
cat <<EOF >>cmake/arch.cmake
set(is_arm8 1)
set(is_arm 1)
EOF
%endif
%ifarch %ix86
cat <<EOF >>cmake/arch.cmake
set(is_x86 1)
EOF
%endif
%ifarch x86_64 ppc64le
cat <<EOF >>cmake/arch.cmake
set(is_x64 1)
EOF
%endif


%ifarch armh
# WEBRTC_HAS_NEON
%__subst "s|-msse2|-mfpu=neon|" cmake/init_target.cmake
%endif
%ifarch aarch64 armh ppc64le
%__subst "s|-msse2|-Wall|" cmake/init_target.cmake
%__subst "s|modules/audio_processing/utility/ooura_fft_sse2.cc||" CMakeLists.txt
%__subst "s|modules/audio_processing/utility/ooura_fft_tables_neon_sse2.h||" CMakeLists.txt
%__subst "s|modules/video_processing/util/denoiser_filter_sse2.cc||" CMakeLists.txt
%__subst "s|common_audio/resampler/sinc_resampler_sse.cc||" CMakeLists.txt
%__subst "s|modules/desktop_capture/differ_vector_sse2.cc||" CMakeLists.txt
%__subst "s|common_audio/fir_filter_sse.cc||" CMakeLists.txt
%endif

%build
mkdir -p out/Debug
cd out/Debug
cmake -G Ninja \
          -DCMAKE_BUILD_TYPE=Release \
          -DTG_OWT_SPECIAL_TARGET=linux \
%if_with packaged_vpx
          -DTG_OWT_VPX_PACKAGED_BUILD=TRUE \
%endif
          -DTG_OWT_LIBJPEG_INCLUDE_PATH=%_includedir \
          -DTG_OWT_OPENSSL_INCLUDE_PATH=%_includedir \
          -DTG_OWT_OPUS_INCLUDE_PATH=%_includedir/opus \
          -DTG_OWT_FFMPEG_INCLUDE_PATH=%_includedir \
          ../..
ninja

%install
mkdir -p %buildroot/usr/src/
cp -a src/ %buildroot/usr/src/%name
find %buildroot/usr/src/%name/third_party/ -name "*.pl" -print -delete
find %buildroot/usr/src/%name/third_party/ -name "*.py" -print -delete

mkdir -p %buildroot/%_libdir/
cp out/Debug/libtg_owt.a %buildroot/%_libdir/

%files devel
%_libdir/libtg_owt.a
/usr/src/%name/

%changelog
* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.1-alt1
- build from git a4d3a58afda96b4e92426fb464f644205e07acae
- temp. exclude armh arch

* Sat Aug 22 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- build OWT patched for Telegram Desktop
