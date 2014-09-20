Name: tony
Version: 0.6
Release: alt2.hg20140909
Summary: High quality scientific pitch and note annotation 
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/tony
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/tony
Source: %name-%version.tar

BuildPreReq: gcc-c++ qt5-base-devel libsvcore-devel libsvgui-devel
BuildPreReq: libsvapp-devel libvamp-devel librubberband-devel
BuildPreReq: libsndfile-devel libsamplerate-devel libfftw3-devel
BuildPreReq: bzlib-devel liblrdf-devel libmad-devel libfishsound-devel
BuildPreReq: liboggz-devel liblo-devel libalsa-devel libjack-devel
BuildPreReq: libX11-devel libid3tag-devel libsord-devel libserd-devel
BuildPreReq: dataquay-minefeld-devel libportaudio2-devel
BuildPreReq: doxygen graphviz

%description
Tony is a software program for high quality scientific pitch and note
annotation in three steps: automatic visualisation/sonification, easy
correction, and export.

%prep
%setup

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%configure \
	--enable-debug
qmake tonyapp.pro
%make_build V=1

%install
install -d %buildroot%_bindir
install -d %buildroot%_pixmapsdir

install -m755 %name %buildroot%_bindir/
for i in 'draw' 'select' 'speaker'
do
	rm -f icons/$i.png
done
install -p -m644 icons/* %buildroot%_pixmapsdir/

%files
%doc CHANGELOG README
%_bindir/*
%_pixmapsdir/*

%changelog
* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.hg20140909
- Built with portaudio
- Built with dataquay-minefeld instead of dataquay

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.hg20140909
- Initial build for Sisyphus

