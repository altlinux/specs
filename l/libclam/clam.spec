Name:    libclam
Version: 1.4.0
Release: alt1

Summary: CLAM - C++ Library for Audio and Music
License: GPLv2+
Url:     http://clam-project.org/
Group:   System/Libraries
Packager: Andrey Cherepanov <cas@altlinux.org>
Source0: %name-%version.tar.bz2
Patch0:	 %name-1.3.0-alt-gcc4.6.patch
Patch1:  link-to-vorbis-ogg.patch
Patch2:  gcc48.patch
Patch3:  time_utc.patch
Patch4:  xerces-c-3.patch

BuildRequires: doxygen gcc-c++ graphviz id3lib-devel ladspa_sdk libfftw3-devel
BuildRequires: libmad-devel libsndfile-devel libvorbis-devel
BuildRequires: libxerces-c-devel scons texlive-latex-recommended libalsa-devel
BuildRequires: libogg-devel

BuildPreReq: libjack-devel /proc

%description
CLAM stands for C++ Library for Audio and Music and in Catalan means something
like a "continuous sound produced by a large number of people as to show
approval or disapproval of a given event" It is the best name we could find
after long discussions and it is certainly much better than its original name
(MTG-Classes).

CLAM is a framework to develop audio and music applications in C++.

It provides tools to perform advanced analysis, transformations and synthesis,
visualization for audio and music related objects, and other tools that are
useful to abstract target platform for most tasks in an audio applications
such as audio devices, file formats, threading...

##########################################
##########################################
%package devel
Summary: CLAM - C++ Library for Audio and Music - development files
Group: Development/C++
Requires: %name = %version

%description devel
CLAM is a framework to develop audio and music applications in C++.
It provides tools to perform advanced analysis, transformations and synthesis,
visualization for audio and music related objects, and other tools that are
useful to abstract target platform for most tasks in an audio applications
such as audio devices, file formats, threading...

This package contains the files needed to develop with the following libraries:
clam-core, clam-processing, clam-audioio, clam-vmfl and clam-vmqt.

##########################################
##########################################
%package doc
Summary: Contains the clam-framework documentation and some example programs
Group: Documentation
BuildArch: noarch

%description doc
This package contains the framework documentation and some example programs.

##########################################
##########################################
%prep
%setup 
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Set correct libdir in x86_64
subst "s,/lib,/%_lib,g" scons/libs/clam_build_helpers.py

%build
install -dm 755 %buildroot%_prefix

[ -n "$NPROCS" ] || NPROCS=1

scons 	-j$NPROCS configure \
	prefix=%buildroot%_prefix \
	release=1 \
	double=0 \
	xmlbackend=xercesc \
	with_ladspa_support=1 \
	with_osc_support=1 \
	with_jack=yes \
	with_jack_support=1 \
	with_fftw=1 \
	with_fftw3=1 \
	with_nr_fft=1 \
	with_sndfile=1 \
	with_oggvorbis=1 \
	with_mad=1 \
	with_id3=1 \
	with_alsa=1 \
	with_portaudio=0 \
	with_portmidi=0 

# Link libclam_core with -ldl
subst "s/^\(LIBS.*\)\]/\1, \'dl\'\]/" ./scons/libs/core/flags.conf

scons -j 1

# and now doxygenate CLAM stuff
doxygen ./doxygen.cfg

%install
install -dm 755 %buildroot%_libdir
scons install

# Fix directory name with sconstools
mv %buildroot%_datadir/{clam,%name}

%files
%_libdir/libclam_*.so.*

%files devel
%doc CHANGES INSTALL
%dir %_includedir/CLAM
%_includedir/CLAM/*
%_libdir/libclam_*.so
%_libdir/pkgconfig/*
%_datadir/%name/sconstools/*.py*

%files doc
%doc CHANGES INSTALL
%doc doxygen/*

%changelog
* Wed Oct 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version
- Fix project URL and license
- Reformat spec
- Apply patches from Debian
- Build with libxerces-c 3.x

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.0-alt1.4.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libclam-doc

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.4.qa1
- NMU: rebuilt for updated dependencies.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.4
- Fixed build with glibc 2.16

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.3
- Enabled jack support

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.0-alt1.2.1
- Rebuild with Python-2.7

* Tue Feb 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.2
- Disabled jack support

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.1
- Rebuilt with python 2.6

* Tue Jul 21 2009 Timur Batyrshin <erthad@altlinux.org> 1.3.0-alt1
- initial build for sisyphus

* Wed Feb 14 2007 Toni Graffy <toni@links2linux.de> - 0.98.0-0.pm.1
- update to 0.98
* Wed Jan 31 2007 Toni Graffy <toni@links2linux.de> - 0.97.0-0.pm.1
- initial build 0.97.0

