Name: gpsynth
Version: 0.0
Release: alt1.hg20110825.1
Summary: Emulates a target sound file
License: GPLv3
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/gpsynth
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/gpsynth
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake jsoncpp-devel libfftw3-devel
BuildPreReq: boost-devel libsndfile-devel boost-filesystem-devel
#BuildPreReq: boost-program_options-devel boost-process-devel
BuildPreReq: boost-program_options-devel boost-asio-devel
#BuildPreReq: libjson-devel

%description
A program that uses genetic programming techniques to artificially
evolve SuperCollider synthesizers towards the ability to emulate a
target sound file.

%prep
%setup

rm -fR third_party/json

%build
%add_optflags -I%_includedir/jsoncpp
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc README
%_bindir/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.0-alt1.hg20110825.1
- rebuild with boost 1.57.0
- fix build with recent gcc

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.hg20110825
- Initial build for Sisyphus

