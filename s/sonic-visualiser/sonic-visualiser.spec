Name: sonic-visualiser
Version: 2.4
Release: alt1.hg20140912
Summary: Application for viewing and analysing the contents of music audio files
License: GPLv2+
Group: Sound
Url: http://sonicvisualiser.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/sonic-visualiser
Source: %name-%version.tar

BuildPreReq: gcc-c++ qt5-base-devel libsvcore-devel libsvgui-devel
BuildPreReq: libsvapp-devel libvamp-devel librubberband-devel
BuildPreReq: libsndfile-devel libsamplerate-devel libfftw3-devel
BuildPreReq: bzlib-devel liblrdf-devel libmad-devel libfishsound-devel
BuildPreReq: liboggz-devel liblo-devel libalsa-devel libjack-devel
BuildPreReq: libX11-devel libid3tag-devel libsord-devel libserd-devel
BuildPreReq: dataquay-devel
BuildPreReq: doxygen graphviz

%description
Sonic Visualiser is an application for viewing and analysing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to it.

We hope Sonic Visualiser will be of particular interest to
musicologists, archivists, signal-processing researchers and anyone else
looking for a friendly way to take a look at what lies inside the audio
file.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%configure \
	--enable-debug
qmake sv.pro
%make_build V=1

%install
install -d %buildroot%_bindir
install -d %buildroot%_desktopdir
install -d %buildroot%_pixmapsdir
install -d %buildroot%_qt5_translationdir

install -m755 %name %buildroot%_bindir/
install -p -m755 *.desktop %buildroot%_desktopdir/
install -p -m644 icons/* %buildroot%_pixmapsdir/
install -p -m644 i18n/* %buildroot%_qt5_translationdir/

%find_lang --with-qt %name

#doxygen

%files -f %name.lang
%doc CHANGELOG CITATION README*
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.hg20140912
- Initial build for Sisyphus

