%define sover 0

Name: qm-dsp
Version: 1.7
Release: alt4

Summary: A C++ library for audio analysis
License: GPLv2+
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/qm-dsp

# hg clone https://code.soundsoftware.ac.uk/hg/qm-dsp
Source: %name-%version.tar

BuildPreReq: doxygen graphviz gcc-c++ qt5-base-devel libvamp-devel
BuildPreReq: bzlib-devel libfftw3-devel libsndfile-devel
BuildPreReq: libsamplerate-devel librubberband-devel liblo-devel
BuildPreReq: libjack-devel liblrdf-devel liboggz-devel
BuildPreReq: libfishsound-devel libmad-devel libid3tag-devel
BuildPreReq: libalsa-devel dataquay-minefeld-devel libclapack-devel
BuildPreReq: libopenblas-devel

%description
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

%package -n lib%name
Summary: A C++ library for audio analysis
Group: System/Libraries

%description -n lib%name
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

%package -n lib%name-devel
Summary: Development files of a C++ library for audio analysis
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for a C++ library for audio analysis
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
A C++ library for audio analysis, developed in the Centre for Digital
Music, originally by Christian Landone.

Primarily used by the QM Vamp Plugins.

This package contains development documentation for lib%name.

%prep
%setup
%ifnarch %ix86 x86_64
sed -ri -e 's, -msse2*,,g' -e 's, -mfpmath=sse,,' build/linux/Makefile*
%endif

find -type f -name '.*' -exec rm -fR '{}' +
rm -fR ext/kissfft/.hg build/linux/amd64

%build
%if "%_lib" == "lib64"
%make_build -f build/linux/Makefile.linux64
%else
%make_build -f build/linux/Makefile.linux32
%endif

g++ -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-llo -lpthread -lbz2 -lfftw3f -lasound -lQt5Core -ldl -lsamplerate \
	-lvamp-hostsdk -lfishsound -lid3tag -lsndfile -lQt5Xml -ldataquay \
	-lmad -loggz -llrdf -lQt5Network -lopenblas -lclapack \
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
%doc *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc doc/html/*

%changelog
* Mon Dec 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7-alt4
- rebuilt for non-x86 arches

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7-alt3.hg20140805
- Rebuilt for new c++ ABI.

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2.hg20140805
- Built with dataquay-minefeld instead of dataquay

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20140805
- Initial build for Sisyphus
