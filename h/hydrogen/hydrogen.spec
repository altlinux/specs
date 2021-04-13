
%define _unpackaged_files_terminate_build 1

Name: hydrogen
Version: 1.0.2
Release: alt1

Summary: Hydrogen Drum Machine
License: GPL
Group: Sound
URL: http://www.hydrogen-music.org

# https://github.com/hydrogen-music/hydrogen.git
Source0: %name-%version.tar

BuildRequires: ccmake ctest doxygen gcc-c++ graphviz ladspa_sdk libalsa-devel libarchive-devel libjack-devel liblo-devel liblrdf-devel
BuildRequires: libportaudio2-devel libportmidi librubberband-devel libsndfile-devel libtar-devel libpulseaudio-devel cppunit-devel
BuildRequires: qt5-base-devel qt5-tools-devel qt5-xmlpatterns-devel zlib-devel

BuildRequires: desktop-file-utils

%description
Hydrogen is a sample based drum machine with:
 Graphical user interface based on QT 
 Sample based real-time audio engine
 Oss Audio driver
 Jack Audio driver
 Export to disk audio driver
 Alsa Midi input
 Ability to import/export xml-based song file
 64 ticks per pattern
 16 voices with volume, mute, solo, pan capabilities
 Import of samples in wav, au, aiff format

%prep
%setup

%build
%cmake -DWANT_RUBBERBAND=ON
%cmake_build DESTDIR=%buildroot

%install
%cmakeinstall_std prefix=%_prefix

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Midi \
	%buildroot%_desktopdir/org.hydrogenmusic.Hydrogen.desktop

%files
%doc -P AUTHORS ChangeLog README.txt
%_bindir/*
%_datadir/%name/
%_libdir/*.so
%_desktopdir/*.desktop
%_datadir/appdata/*.xml
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/%name.1*

# TODO: put headers into separate subpackage
%exclude /usr/include/%name

%changelog
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
