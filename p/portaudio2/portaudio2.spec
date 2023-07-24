%def_disable snapshot
%define _name portaudio
%def_enable docs

Name: %{_name}2
Version: 19
Release: alt8

Summary: PortAudio is a free, cross platform, open-source, audio I/O library
License: MIT
Group: System/Libraries
Url: http://www.portaudio.com/

%if_disabled snapshot
Source: http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz
%else
Vcs: https://github.com/PortAudio/portaudio.git
Source: %_name-%version.tar
%endif

# Automatically added by buildreq on Mon Sep 19 2011
BuildRequires: gcc-c++ libalsa-devel libjack-devel
%{?_enable_docs:BuildRequires: doxygen graphviz}

%description
PortAudio is a free, cross platform, open-source, audio I/O
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support.

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc.

%package -n lib%name
Summary: PortAudio is a free, cross platform, open-source, audio I/O library
Group: System/Libraries

%description -n lib%name
PortAudio is a free, cross platform, open-source, audio I/O
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support.

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc.

%package -n lib%name-devel
Summary: Static library and header files for the PortAudio library
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: libportaudio-devel

%description -n lib%name-devel
PortAudio is a free, cross platform, open-source, audio I/O
library. It lets you write simple audio programs in 'C' that will
compile and run on many platforms including Windows, Macintosh
(8,9,X), Unix (OSS), SGI, and BeOS. PortAudio is intended to
promote the exchange of audio synthesis software between
developers on different platforms, and was recently selected as
the audio component of a larger PortMusic project that includes
MIDI and sound file support.

PortAudio provides a very simple API for recording and/or playing
sound using a simple callback function. Example programs are
included that synthesize sine waves and pink noise, perform fuzz
distortion on a guitar, list available audio devices, etc.

This package contains the static PortAudio library and its header
files.

%prep
%setup -n portaudio%{?_enable_snapshot:-%version}
sed -i '/^Libs:/s/ @/\nLibs.private: @/
        s/^\(Requires:\)/\1 alsa/' portaudio-2.0.pc.in

%build
%autoreconf
# and do it one more time for ac-2.71
%autoreconf
%configure --disable-static --enable-cxx
%make_build lib/libportaudio.la
%make_build
%{?_enable_docs:doxygen}

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%doc README.md
%{?_enable_docs:%doc doc/html}

%changelog
* Mon Jul 24 2023 Yuri N. Sedunov <aris@altlinux.org> 19-alt8
- updated to pa_stable_v190700_20210406
- fixed build with autoconf-2.71

* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 19-alt7
- updated to pa_stable_v190600_20161030-10-g8dc6d59
- add documentation to devel subpackage
- fixed SMP-build in spec

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 19-alt6
- updated to pa_stable_v190600_20161030

* Tue Feb 26 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 19-alt5
- limit make jobs to 3

* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 19-alt4
- updated to pa_stable_v19_20110326

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 19-alt3.svn1134.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 19-alt3.svn1134
- fixed build

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 19-alt2.svn1134
- added a patch to build against new JACK
  (http://osdir.com/ml/audio.portaudio.devel/2007-04/msg00141.html)
- removed obsolete %%post{,un}_ldconfig

* Fri Dec 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 19-alt1.svn1134
- fixed build with new auto*

* Sat Sep 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 19-alt0.svn1134
- initial build

