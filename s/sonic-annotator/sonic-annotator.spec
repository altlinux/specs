Name: sonic-annotator
Version: 1.0
Release: alt1.hg20140426
Summary: A batch tool for audio feature extraction
License: GPLv2
Group: Sound
Url: http://vamp-plugins.org/sonic-annotator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/sonic-annotator
Source: %name-%version.tar

BuildPreReq: gcc-c++ dataquay-minefeld-devel libsvcore-devel
BuildPreReq: qt5-base-devel bzlib-devel libfftw3-devel libsndfile-devel
BuildPreReq: libsamplerate-devel libsord-devel libserd-devel liblo-devel
BuildPreReq: liblrdf-devel liboggz-devel libfishsound-devel libmad-devel
BuildPreReq: libid3tag-devel libalsa-devel xmllint raptor2 libvamp-devel
BuildPreReq: libjack-devel libportaudio2-devel

%description
Sonic Annotator is a batch tool for feature extraction and annotation of
audio files using Vamp plugins.

Sonic Annotator can use any installed Vamp plugin to process a wide
range of audio file types, loading audio data either from the local
filesystem or from http or ftp URLs on the Internet. It can then write
the results in RDF or comma-separated text formats.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%add_optflags -I%_includedir/svcore
%configure \
	--enable-debug
%make_build V=1

%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir/

%files
%doc CHANGELOG CITATION README
%_bindir/*

%changelog
* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140426
- Initial build for Sisyphus

