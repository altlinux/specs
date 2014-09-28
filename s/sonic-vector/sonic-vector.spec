Name: sonic-vector
Version: 0.1
Release: alt1.hg20140909
Summary: Application for showing comparative alignments of audio recordings
License: Free
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/vect
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/vect
Source: %name-%version.tar

BuildPreReq: gcc-c++ dataquay-minefeld-devel libsvapp-devel
BuildPreReq: libsvcore-devel libsvgui-devel bzlib-devel libfftw3-devel
BuildPreReq: libsndfile-devel libsamplerate-devel libvamp-devel
BuildPreReq: librubberband-devel libsord-devel libserd-devel
BuildPreReq: liblo-devel libportaudio2-devel libjack-devel
BuildPreReq: liblrdf-devel liboggz-devel libfishsound-devel
BuildPreReq: libmad-devel libid3tag-devel libX11-devel
BuildPreReq: qt5-base-devel libalsa-devel

%description
An experimental application for showing comparative alignments of audio
recordings. Uses the Sonic Visualiser Libraries code. Not yet ready for
general use.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%configure \
	--enable-debug
%make_build

%install
install -d %buildroot%_bindir
install -m755 vect %buildroot%_bindir/

install -d %buildroot%_qt5_translationdir
install -p -m644 i18n/*.qm %buildroot%_qt5_translationdir/

rm -f icons/README icons/sv-macicon.icns
install -d %buildroot%_pixmapsdir
install -p -m644 icons/* %buildroot%_pixmapsdir/

%files
%_bindir/*
%_qt5_translationdir/*
%_pixmapsdir/*

%changelog
* Sun Sep 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20140909
- Initial build for Sisyphus

