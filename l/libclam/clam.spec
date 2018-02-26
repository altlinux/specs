Summary: CLAM - C++ Library for Audio and Music
Name: libclam
Version: 1.3.0
Release: alt1.2.1
License: GPL
Url: http://clam.iua.upf.edu
Group: System/Libraries
Packager: Timur Batyrshin <erthad@altlinux.org>
Source0: %name-%version.tar.bz2


BuildRequires: doxygen gcc-c++ graphviz id3lib-devel ladspa_sdk libfftw3-devel libmad-devel libsndfile-devel libvorbis-devel libxerces-c28-devel scons texlive-latex-recommended libalsa-devel

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

%description doc
This package contains the framework documentation and some example programs.

##########################################
##########################################
%prep
%setup 

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
	with_jack=no \
	with_jack_support=0 \
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

scons 	-j$NPROCS

# and now doxygenate CLAM stuff
doxygen ./doxygen.cfg

%install
install -dm 755 %buildroot%_libdir
scons install
mv %buildroot%_prefix/libX/* %buildroot%_libdir

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

