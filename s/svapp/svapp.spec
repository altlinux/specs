%define sover 0

Name: svapp
Version: 2.1
Release: alt2.hg20140912
Summary: SV App Framework
License: GPLv2
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/svapp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/svapp
Source: %name-%version.tar

BuildPreReq: gcc-c++ qt5-base-devel libvamp-devel librubberband-devel
BuildPreReq: libsndfile-devel libsamplerate-devel libfftw3-devel
BuildPreReq: bzlib-devel liblrdf-devel libmad-devel liboggz-devel
BuildPreReq: liblo-devel libalsa-devel libjack-devel libsvcore-devel
BuildPreReq: libid3tag-devel libfishsound-devel libsvgui-devel
BuildPreReq: dataquay-minefeld-devel libportaudio2-devel
BuildPreReq: doxygen graphviz

%description
Document class and base class for main window instance for applications
that "resemble Sonic Visualiser", with the same pane and layer structure
but not necessarily the same user functions.

%package -n lib%name
Summary: SV App Framework
Group: System/Libraries

%description -n lib%name
Document class and base class for main window instance for applications
that "resemble Sonic Visualiser", with the same pane and layer structure
but not necessarily the same user functions.

%package -n lib%name-devel
Summary: Development files of SV App Framework
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Document class and base class for main window instance for applications
that "resemble Sonic Visualiser", with the same pane and layer structure
but not necessarily the same user functions.

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for SV App Framework
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Document class and base class for main window instance for applications
that "resemble Sonic Visualiser", with the same pane and layer structure
but not necessarily the same user functions.

This package contains development documentation for lib%name.

%prep
%setup

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
	-lsvgui -ljack -lportaudio -lrubberband \
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
* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2.hg20140912
- Built with dataquay-minefeld instead of dataquay

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.hg20140912
- Initial build for Sisyphus

