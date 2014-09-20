Name: vamp-live-host
Version: 0.1
Release: alt2.hg20131203
Summary: Vamp Live Host - activate events based on features of live audio
License: Free
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vamp-live-host
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/vamp-live-host
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel qt5-base-devel libjack-devel
BuildPreReq: libalsa-devel libid3tag-devel libmad-devel libsvcore-devel
BuildPreReq: libfishsound-devel liboggz-devel liblrdf-devel liblo-devel
BuildPreReq: libserd-devel libsord-devel libsamplerate-devel
BuildPreReq: libsndfile-devel libfftw3-devel bzlib-devel
BuildPreReq: libportaudio2-devel

%description
A program that listens to live audio, runs one or more Vamp audio
feature extraction plugins on that incoming audio, and causes a
configurable set of events to occur in close to real-time based on the
features extracted from it.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%add_optflags -I%_includedir/svcore -I%_includedir/svcore/base
%autoreconf
%configure \
	--enable-debug
%make_build V=1

%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir/

%files
%doc README
%_bindir/*

%changelog
* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.hg20131203
- Built with portaudio

* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20131203
- Initial build for Sisyphus

