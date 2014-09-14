%define sover 0

Name: svgui
Version: 2.1
Release: alt1.hg20140912
Summary: SV GUI Library
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/svgui
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/svgui
Source: %name-%version.tar

BuildPreReq: gcc-c++ doxygen graphviz qt5-base-devel libvamp-devel
BuildPreReq: librubberband-devel libsndfile-devel libsamplerate-devel
BuildPreReq: libfftw3-devel bzlib-devel liblrdf-devel libmad-devel
BuildPreReq: libalsa-devel libjack-devel liboggz-devel liblo-devel
BuildPreReq: libfishsound-devel libid3tag-devel libsvcore-devel
BuildPreReq: dataquay-devel

%description
Implementations of the layer and view abstractions from Sonic
Visualiser, as well as any additional Qt widgets used by SV.

%package -n lib%name
Summary: SV GUI Library
Group: System/Libraries

%description -n lib%name
Implementations of the layer and view abstractions from Sonic
Visualiser, as well as any additional Qt widgets used by SV.

%package -n lib%name-devel
Summary: Development files of SV GUI Library
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Implementations of the layer and view abstractions from Sonic
Visualiser, as well as any additional Qt widgets used by SV.

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for SV GUI Library
Group: Development/Documentation
#BuildArch: noarch

%description -n lib%name-devel-docs
Implementations of the layer and view abstractions from Sonic
Visualiser, as well as any additional Qt widgets used by SV.

This package contains development documentation for lib%name.

%prep
%setup

find -type f -name '.*' -exec rm -fR '{}' +

%build
export PATH=$PATH:%_qt5_bindir
%autoreconf
%configure \
	--enable-debug
%make_build V=1

g++ -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-llo -lpthread -lbz2 -lfftw3f -lasound -lQt5Core -ldl -lsamplerate \
	-lvamp-hostsdk -lfishsound -lid3tag -lsndfile -lQt5Xml -ldataquay \
	-lmad -loggz -llrdf -lQt5Network -lsvcore -lQt5Gui -lQt5Widgets \
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
* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.hg20140912
- Initial build for Sisyphus

