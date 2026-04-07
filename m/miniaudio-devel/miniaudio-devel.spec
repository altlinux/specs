Name: miniaudio-devel
Version: 0.11.25
Release: alt1

Summary: Header-only audio playback and capture library

License: Unlicense OR MIT-0
Group: Development/C
URL: https://github.com/mackron/miniaudio
# Source-url: https://github.com/mackron/miniaudio/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%description
miniaudio is a single-file library for audio playback and capture.
To use it, just #define MINIAUDIO_IMPLEMENTATION in one C or C++ file
before including miniaudio.h.

Key features:
- Audio playback, capture, full-duplex, and loopback
- Data conversion (sample format, channel, sample rate)
- Decoding (WAV, FLAC, MP3)
- Device abstraction (WASAPI, DirectSound, WinMM, CoreAudio, sndio,
  audio4, OSS, PulseAudio, ALSA, JACK, AAudio, OpenSL, Web Audio)
- Node graph for advanced mixing and effect processing

%prep
%setup

%install
install -d %buildroot%_includedir/miniaudio/extras
install -m 644 miniaudio.h %buildroot%_includedir/miniaudio/
install -m 644 extras/miniaudio_libopus.h %buildroot%_includedir/miniaudio/extras/
install -m 644 extras/miniaudio_libvorbis.h %buildroot%_includedir/miniaudio/extras/
install -d %buildroot%_datadir/pkgconfig
cat > %buildroot%_datadir/pkgconfig/miniaudio.pc <<EOF
prefix=%_prefix
exec_prefix=\${prefix}
includedir=%_includedir

Name: miniaudio
Description: An audio playback and capture library.
URL: https://miniaud.io/
License: Unlicense OR MIT-0
Version: %version

Cflags: -I\${includedir}/miniaudio
EOF

%files
%_includedir/miniaudio/
%_datadir/pkgconfig/miniaudio.pc

%changelog
* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 0.11.25-alt1
- initial build for ALT Sisyphus
