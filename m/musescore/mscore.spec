
# TODO(iv@):
# - check if we can enable more importexport modules
# - unbundle fonts (they are now shipped as Qt resources)
# - see what other libraries we can unbundle (liblouis? pugixml? utfcpp?)
# - check what other ways of calling home (in addition to updates) should be disabled

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# disable lto to workaround "No data signature found" rcc
# issue -- https://bugreports.qt.io/browse/QTBUG-73834
%define optflags_lto %nil

%define rname mscore
%define mversion 4.6

Name: musescore
Version: %mversion.0
Release: alt1

Summary: Music notation and composition software

License: GPLv2
Group: Sound
Url: https://musescore.org
Vcs: https://github.com/musescore/MuseScore.git

# verify-elf: ERROR: ./usr/bin/mscore: uses non-LFS functions: fopen fstat stat
# and I don't want to fix that -- iv@
ExcludeArch: %ix86

Source: %name-%version.tar
Patch:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-xdg

BuildRequires: cmake gcc-c++

# Qt6:
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6NetworkAuth)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6QuickControls2)
BuildRequires: pkgconfig(Qt6QuickTemplates2)
BuildRequires: pkgconfig(Qt6QuickWidgets)
BuildRequires: pkgconfig(Qt6ShaderTools)
BuildRequires: pkgconfig(Qt6StateMachine)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Test)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6WebSockets)
BuildRequires: pkgconfig(Qt6Xml)

# Others:
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(flac++)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libopusenc)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(portaudiocpp)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)

BuildRequires: liblame-devel

# Docs:
# BuildRequires: doxygen ghostscript-utils graphviz latex2html

# QML dependencies:
Requires: libqt6-quickcontrols2
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quickcontrols2fusion
Requires: libqt6-quickeffects
Requires: libqt6-quicklayouts
Requires: libqt6-qml

%description
Music notation and composition software

* WYSIWYG design, notes are entered on a "virtual notepaper"
* TrueType font(s) for printing & display allows for high quality scaling to all sizes
* easy & fast note entry
* many editing functions
* MusicXML import/export
* Midi (SMF) import/export
* MuseData import
* Midi input for note entry
* integrated sequencer and software synthesizer to play the score
* print or create pdf files

%prep
%setup
%autopatch -p1

%build
export LANG="C.UTF-8"
export PATH="%_qt6_bindir:$PATH"

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DMUSESCORE_BUILD_CONFIGURATION=app \
    -DMUSE_APP_BUILD_MODE=release \
    -DMUSE_MODULE_DIAGNOSTICS_CRASHPAD_CLIENT:BOOL=OFF \
    -DMUE_BUILD_UPDATE_MODULE:BOOL=OFF \
    -DMUSE_ENABLE_UNIT_TESTS:BOOL=OFF \
    -DMUE_BUILD_BRAILLE_TESTS:BOOL=OFF \
    -DMUE_BUILD_ENGRAVING_TESTS:BOOL=OFF \
    -DMUE_BUILD_IMPORTEXPORT_TESTS:BOOL=OFF \
    -DMUE_BUILD_NOTATION_TESTS:BOOL=OFF \
    -DMUE_BUILD_PLAYBACK_TESTS:BOOL=OFF \
    -DMUE_BUILD_PROJECT_TESTS:BOOL=OFF \
    -DMUE_BUILD_CONVERTER_TESTS:BOOL=OFF \
    -DMUSE_COMPILE_USE_PCH:BOOL=OFF \
    -DMUE_COMPILE_USE_SYSTEM_FLAC:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_FREETYPE:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_HARFBUZZ:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_OPUS:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_OPUSENC:BOOL=ON \
    -DMUE_COMPILE_USE_SYSTEM_TINYXML:BOOL=ON \
    -DMUE_DOWNLOAD_SOUNDFONT:BOOL=OFF \
    -DMUSE_MODULE_GLOBAL_LOGGER_DEBUGLEVEL:BOOL=OFF \
    -DMUSE_COMPILE_STRING_DEBUG_HACK:BOOL=OFF \
    -DMUSE_MODULE_NETWORK_WEBSOCKET:BOOL=ON \
    -DMUSE_MODULE_UPDATE:BOOL=OFF \
    -DMUSE_MODULE_AUDIO_JACK:BOOL=OFF \
    -DMUSE_PIPEWIRE_AUDIO_DRIVER:BOOL=ON \
    -Wno-dev

%cmake_build

%install
export LANG="C.UTF-8"
export PATH="%_qt6_bindir:$PATH"
%cmake_install

rm -rvf %buildroot%_includedir %buildroot%_libdir

%files
%doc README.md
%_bindir/*
%_datadir/metainfo/org.musescore.MuseScore.appdata.xml
%_desktopdir/*.desktop
%_datadir/mscore-%mversion
%_man1dir/*
%_xdgmimedir/packages/musescore.xml
%_iconsdir/hicolor/*/apps/mscore.*
%_iconsdir/hicolor/*/mimetypes/application-x-musescore.*
%_iconsdir/hicolor/*/mimetypes/application-x-musescore+xml.*

%changelog
* Fri Oct 03 2025 Ivan A. Melnikov <iv@altlinux.org> 4.6.0-alt1
- 4.6.0
- switch to Qt6
- disable updates module

* Fri Apr 11 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.6.2-alt5
- NMU: fix FTBFS with cmake 4.0

* Wed Feb 05 2025 Ivan A. Melnikov <iv@altlinux.org> 3.6.2-alt4
- drop unused BR on Qt5 WebEngine
- add missing Qt5 Quick dependencies

* Wed Feb 05 2025 Ivan A. Melnikov <iv@altlinux.org> 3.6.2-alt3
- fix FTBFS
- package more icons

* Mon Jun 12 2023 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt2
- exclude build on ppc64le (due missed qt5-webengine-devel)

* Tue Apr 06 2021 Grigory Ustinov <grenka@altlinux.org> 3.6.2-alt1
- Build new version.

* Tue Oct 27 2020 Grigory Ustinov <grenka@altlinux.org> 3.5.2-alt1
- Automatically updated to 3.5.2.

* Wed Aug 26 2020 Grigory Ustinov <grenka@altlinux.org> 3.5-alt1
- Automatically updated to 3.5.

* Mon Feb 10 2020 Grigory Ustinov <grenka@altlinux.org> 3.4.2-alt1
- new version 3.4.2

* Wed Feb 05 2020 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt1
- Build new version 3.4.1.
- Fix license.

* Thu Dec 26 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.4-alt1
- Build new version 3.3.4.

* Fri Nov 15 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.2-alt1
- Build new version.

* Wed Nov 06 2019 Grigory Ustinov <grenka@altlinux.org> 3.3-alt1
- Build new version.

* Mon Jul 08 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.3-alt1
- Build new version.

* Thu May 30 2019 Grigory Ustinov <grenka@altlinux.org> 3.1-alt1
- Build new version.

* Tue Apr 16 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.5-alt1
- Build new version (Closes: #36475).
- Build with system libfreetype (Closes: #36386).

* Wed Sep 12 2018 Grigory Ustinov <grenka@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt3
- Fix FTBFS (Add missing rpm-build-xdg).

* Thu Nov 23 2017 Fr. Br. George <george@altlinux.ru> 2.1.0-alt2
- Fix sf3 coredump

* Thu Nov 16 2017 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Feb 16 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.2-alt1
- 2.0.2
- build from upstream git repo

* Mon Apr 15 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up
- Fix broken fonts usage in 1.2

* Sat Jun  2 2012 Terechkov Evgenii <evg@altlinux.org> 1.2-alt1
- 1.2

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.3-alt1.1
- Removed bad RPATH

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.6.3-alt1
- new version (ALT bug 23626), update buildreqs
- fix dependencies (ALT bug #21884)

* Tue Apr 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script), fix bug #19710
- update buildreqs

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus
