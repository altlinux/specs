%define sover 0

Name: svcore
Version: 2.1
Release: alt1.hg20140910
Summary: Core application library from the Sonic Visualiser project
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/svcore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/svcore
Source: %name-%version.tar

Requires: lib%name = %version-%release

BuildPreReq: doxygen graphviz gcc-c++ qt5-base-devel libvamp-devel
BuildPreReq: bzlib-devel libfftw3-devel libsndfile-devel
BuildPreReq: libsamplerate-devel librubberband-devel liblo-devel
BuildPreReq: libjack-devel liblrdf-devel liboggz-devel
BuildPreReq: libfishsound-devel libmad-devel libid3tag-devel
BuildPreReq: libalsa-devel dataquay-devel

%description
Core application library from the Sonic Visualiser project, also used by
GUI-less applications such as Sonic Annotator. Includes audio file
wrappers and other file format support, data models, basic utility
functions, and the support required by SV for MIDI, OSC, RDF, and audio
plugins.

%package -n lib%name
Summary: Core application library from the Sonic Visualiser project
Group: System/Libraries

%description -n lib%name
Core application library from the Sonic Visualiser project, also used by
GUI-less applications such as Sonic Annotator. Includes audio file
wrappers and other file format support, data models, basic utility
functions, and the support required by SV for MIDI, OSC, RDF, and audio
plugins.

%package -n lib%name-devel
Summary: Development files of core application library from the Sonic Visualiser project
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Core application library from the Sonic Visualiser project, also used by
GUI-less applications such as Sonic Annotator. Includes audio file
wrappers and other file format support, data models, basic utility
functions, and the support required by SV for MIDI, OSC, RDF, and audio
plugins.

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for core application library from the Sonic Visualiser project
Group: Development/Documentation
#BuildArch: noarch

%description -n lib%name-devel-docs
Core application library from the Sonic Visualiser project, also used by
GUI-less applications such as Sonic Annotator. Includes audio file
wrappers and other file format support, data models, basic utility
functions, and the support required by SV for MIDI, OSC, RDF, and audio
plugins.

This package contains development documentation for lib%name.

%prep
%setup

find -type f -name '.*' -exec rm -fR '{}' +

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%configure
%make_build V=1

g++ -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-llo -lpthread -lbz2 -lfftw3f -lasound -lQt5Core -ldl -lsamplerate \
	-lvamp-hostsdk -lfishsound -lid3tag -lsndfile -lQt5Xml -ldataquay \
	-lmad -loggz -llrdf -lQt5Network \
	-Wl,-soname=lib%name.so.%sover -o lib%name.so.%sover

%install
for i in $(find ./ -name '*.h*'); do
	j=$(echo $i |sed 's|\(.*\)/[^/]*|\1|')
	install -d %buildroot%_includedir/%name/$j
	install -p -m644 $i %buildroot%_includedir/%name/$j/
done

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

doxygen

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc doc/html/*

%changelog
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.hg20140910
- Initial build for Sisyphus

