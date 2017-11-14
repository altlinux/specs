Name: hydrogen
Version: 0.9.7
Release: alt1

Summary: Hydrogen Drum Machine
License: GPL
Group: Sound
URL: http://www.hydrogen-music.org

# https://github.com/hydrogen-music/hydrogen.git
Source0: %name-%version.tar
Source1: %name-32x32.xpm
Source2: %name-16x16.xpm
Source3: %name-48x48.xpm
Patch1: %name-%version-upstream-detect-pulse.patch
Patch2: %name-%version-upstream-detect-rubberband.patch
Patch3: %name-%version-alt-desktop.patch
Patch4: %name-%version-alt-man-dir.patch

BuildRequires: ccmake ctest doxygen gcc-c++ graphviz ladspa_sdk libalsa-devel libarchive-devel libjack-devel liblo liblrdf-devel
BuildRequires: libportaudio2-devel libportmidi librubberband-devel libsndfile-devel libtar-devel libpulseaudio-devel cppunit-devel
BuildRequires: libqt4-sql-mysql phonon-devel

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export QTDIR=%_libdir/qt4
%cmake -DWANT_RUBBERBAND=ON
%cmake_build DESTDIR=%buildroot

%install
export QTDIR=%_libdir/qt4
%cmakeinstall_std prefix=%_prefix

install -pD -m644 %SOURCE1 %buildroot%_niconsdir/%name.xpm
install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.xpm

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Midi \
	%buildroot%_desktopdir/hydrogen.desktop

%files
%doc -P AUTHORS ChangeLog README.txt
%_bindir/*
%_datadir/%name/
%_libdir/*.so
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_miconsdir/%name.xpm
%_desktopdir/%name.desktop
%_man1dir/%name.1*

%changelog
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
