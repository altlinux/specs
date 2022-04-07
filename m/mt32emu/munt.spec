Name: mt32emu
Version: 2.6.2
Release: alt1
Summary: MT-32, CM-32L and LAPC-I synthesiser modules emulator
Group: Sound
Url: https://github.com/munt/munt
License: GPLv2
Source: %name-%version.tar.gz

Provides: munt %version-%release
Obsoletes: munt < %version-%release

Requires: %name-smf2wav = %version-%release, %name-alsadrv = %version-%release

# Automatically added by buildreq on Mon Aug 23 2021
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libalsa-devel libglvnd-devel libgpg-error libpulseaudio-devel libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base qt5-base-devel sh4
BuildRequires: cmake libjack-devel libportaudio2-devel qt5-base-devel glib2-devel

%description
GUI and a console applications that make use of mt32emu library

%package -n libmt32emu
Group: Sound
Summary: a C/C++ library to emulate Roland MT-32, CM-32L and LAPC-I
%description -n libmt32emu
mt32emu is a C/C++ library which allows to emulate (approximately) the Roland
MT-32, CM-32L and LAPC-I synthesiser modules.

%package -n libmt32emu-devel
Group: Development/C++
Summary: Devel file for %summary
%description -n libmt32emu-devel
%summary

%package qt
Group: Sound
Summary: Synthesiser application emulating Roland MT-32, CM-32L and LAPC-I
%description qt
The main synthesiser application. It facilitates both realtime synthesis and
conversion of pre-recorded SMF files to WAVE making use of the mt32emu library
and [the Qt framework](https://www.qt.io/). Key features:

1. Support for multiple simultaneous synths with separate state & configuration.
2. GUI to configure synths, manage ROMs, connections to external MIDI ports and
   MIDI programs and interfaces to the host audio systems.
3. Emulates the funny MT-32 LCD. Also displays the internal synth state in
   realtime.
4. Being a cross-platform application, provides support for different operating
   systems and multimedia systems such as Windows multimedia, PulseAudio, JACK
   Audio Connection Kit, ALSA, OSS and CoreMIDI.
5. Contains built-in MIDI player of Standard MIDI files optimised for mt32emu.
6. Makes it easy to record either the MIDI input or the produced audio output.
7. Simplifies batch conversion of collections of SMF files to .wav / .raw audio
   files.

%package alsadrv
Group: Sound
Summary: Uses the mt32emu library to provide an ALSA MIDI driver
%description alsadrv
mt32emu_alsadrv is a module of the Munt project. It uses the mt32emu library and
provides an ALSA MIDI driver which emulates (approximately) the Roland MT-32,
CM-32L and LAPC-I synthesiser modules.

%package smf2wav
Group: Sound
Summary: Use the mt32emu library to produce a WAVE Standard MIDI file
%description smf2wav
mt32emu-smf2wav is a part of the Munt project. It makes use of the
mt32emu library to produce a WAVE file from a Standard MIDI file (SMF).
Files in this format commonly have the extension ".smf" or ".mid".

%prep
%setup

%build
%cmake  -Dlibmt32emu_SHARED=True \
        -Dlibmt32emu_C_INTERFACE=True \
        -Dlibmt32emu_PKGCONFIG_INSTALL_PREFIX:PATH=%_libdir

%cmake_build
make -C mt32emu_alsadrv/ mt32d \
	INCLUDES=-I../%_cmake__builddir/mt32emu/include \
	CXXFLAGS="-O2 -Wno-write-strings -Wno-unused-result -Wno-deprecated-declarations \
		-L../%_cmake__builddir/mt32emu"

%install
%cmake_install
install -m755 mt32emu_alsadrv/mt32d %buildroot%_bindir/

%files
%doc *.md
%dir %_defaultdocdir/munt

%files smf2wav
%_bindir/mt32emu-smf2wav
%doc %_defaultdocdir/munt/smf2wav

%files alsadrv
%_bindir/mt32d
%doc mt32emu_alsadrv/*.txt

%files -n libmt32emu
%_libdir/*.so.*

%files -n libmt32emu-devel
%doc %_defaultdocdir/munt/libmt32emu
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_libdir/cmake/MT32Emu

%files qt
%doc %_defaultdocdir/munt/mt32emu-qt
%_bindir/mt32emu-qt
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/munt.*

%changelog
* Thu Apr 07 2022 Fr. Br. George <george@altlinux.org> 2.6.2-alt1
- Autobuild version bump to 2.6.2

* Tue Aug 24 2021 Fr. Br. George <george@altlinux.ru> 2.5.2-alt1
- Update submajor version
- Separate packages
- Build Qt player and library

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.2.0-alt1.git.5.gb414aeb.1
- NMU: spec: adapted to new cmake macros.

* Mon Aug 21 2017 Ildar Mulyukov <ildar@altlinux.ru> 2.2.0-alt1.git.5.gb414aeb
- initial build for ALT Linux Sisyphus
- only smf2wav and alsadrv are built, no QT, no GUI

