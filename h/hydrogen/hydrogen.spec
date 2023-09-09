
%define _unpackaged_files_terminate_build 1

Name: hydrogen
Version: 1.2.2
Release: alt1

Summary: Hydrogen Drum Machine
License: GPL
Group: Sound
URL: http://www.hydrogen-music.org

# https://github.com/hydrogen-music/hydrogen.git
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ccmake ctest doxygen gcc-c++ graphviz ladspa_sdk libalsa-devel libarchive-devel libjack-devel liblo-devel liblrdf-devel
BuildRequires: libportaudio2-devel libportmidi-devel librubberband-devel libsndfile-devel libtar-devel libpulseaudio-devel cppunit-devel
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel qt5-xmlpatterns-devel zlib-devel

BuildRequires: desktop-file-utils

%description
Hydrogen is an advanced sample-based drum machine. Its main
goal is to bring professional yet simple and intuitive
pattern-based drum programming. Its features include:
* Very user-friendly, modular, fast and intuitive graphical
  interface based on Qt5.
* Sample-based stereo audio engine, with import of sound
  samples in wav, au and aiff formats.
* Support of samples in compressed FLAC file.
* Separate command-line interface (h2cli)
* Pattern-based sequencer, with unlimited number of patterns
  and ability to chain patterns into a song.
* Playlist with scripting support.
* Multi layer support for instruments (up to 16 samples
  for each instrument).
* Sample Editor, with basic cut and loop functions.
* JACK, ALSA, PulseAudio, PortAudio, CoreAudio and OSS audio
  drivers.
* Export song to wav, aiff, flac or midi file.

%prep
%setup
%patch0 -p1

%build
%cmake '-DVERSION_SUFFIX:STRING=%release' \
    -DWANT_RUBBERBAND=ON \
    -DWANT_PORTAUDIO=ON -DWANT_PORTMIDI=ON
%cmake_build

%install
%cmake_install

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Midi \
	%buildroot%_desktopdir/org.hydrogenmusic.Hydrogen.desktop

%files
%doc -P AUTHORS ChangeLog README.md
%_bindir/*
%_datadir/%name/
%_libdir/*.so
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/%name.1*

# TODO: put headers into separate subpackage
%exclude /usr/include/%name

%changelog
* Sat Sep 09 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sat Jun 10 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue May 09 2023 Ivan A. Melnikov <iv@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Mar 24 2022 Ivan A. Melnikov <iv@altlinux.org> 1.1.1-alt1
- 1.1.1
- set VERSION_SUFFIX to %%release

* Thu Sep 23 2021 Ivan A. Melnikov <iv@altlinux.org> 1.1.0-alt1
- 1.1.0
- Enable PortAudio and PortMidi support.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.0.2-alt1.1
- NMU: spec: adapt to new cmake macros.

* Mon Apr 12 2021 Ivan A. Melnikov <iv@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7-alt1
- Updated to upstream version 0.9.7.

* Mon Feb 25 2013 Alex Karpov <karpov@altlinux.ru> 0.9.6-alt0.beta3
- new beta

* Tue Jul 03 2012 Alex Karpov <karpov@altlinux.ru> 0.9.6-alt0.beta2
- new beta

* Wed Jan 11 2012 Alex Karpov <karpov@altlinux.ru> 0.9.6-alt0.beta1
- new beta

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.5-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for hydrogen

* Thu Mar 17 2011 Alex Karpov <karpov@altlinux.ru> 0.9.5-alt1
- new version

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt3
- Fixed build

* Fri Sep 18 2009 Taras Ablamsky <atl@altlinux.ru> 0.9.4-alt2
- 0.9.4

* Thu Mar 26 2009 Taras Ablamsky <atl@altlinux.ru> 0.9.4-alt1.M41.1.beta3
- built for M41

* Sun Mar 22 2009 Taras Ablamsky <atl@altlinux.ru> 0.9.4-alt1.beta3
- 0.9.4-beta3

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 0.9.3-alt1
- 0.9.0 -> 0.9.3
- fixed gcc-4.1 issues
- fixed wasp plugin linkage

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.0-alt0.7.1.1
- Rebuilt with libflac-1.1.2-alt1

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.0-alt0.7.1
- Rebuilt with libstdc++.so.6.

* Thu Sep 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt0.7
- new version.
- manpages by avp@.

* Wed Dec 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt0.7
- 0.8.1 release.

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt0.6beta4
- 0.8.1beta4.

* Sun May 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Mar 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Mon Feb 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.5-alt1
- First build for Sisyphus.
