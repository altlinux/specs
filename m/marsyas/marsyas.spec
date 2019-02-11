%define _unpackaged_files_terminate_build 1

Name: marsyas
Version: 0.6.0
Release: alt2.alpha.git20150301
Summary: Music Analysis, Retrieval and Synthesis for Audio Signals
License: GPLv2
Group: Sound
Url: http://marsyas.info/

# https://github.com/marsyas/marsyas.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

ExclusiveArch: %ix86 x86_64

BuildRequires: gcc-c++ cmake doxygen graphviz libjack-devel clang-devel
BuildRequires: qt5-base-devel libalsa-devel qt5-declarative-devel
BuildRequires: libann-devel libmad-devel liblame-devel libvorbis-devel
BuildRequires: swig libvamp-devel libGLUT-devel python-devel
BuildRequires: libfreetype-devel libXi-devel libXmu-devel zlib-devel
BuildRequires: libann-devel liblinear-devel
BuildRequires: libsvm-devel librtmidi-devel libpng12-devel
BuildRequires: libXres-devel libXtst-devel libXcomposite-devel
BuildRequires: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXft-devel libXinerama-devel libxkbfile-devel
BuildRequires: libXpm-devel libXrandr-devel libXScrnSaver-devel
BuildRequires: libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: %_bindir/latex %_bindir/gs
BuildRequires: texi2dvi texi2html makeinfo
BuildRequires: tex(dvips.def)

%description
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

%package -n vamp-%name
Summary: %name plugin for vamp
Group: Sound

%description -n vamp-%name
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

This package contains %name plugin for vamp.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

This package contains %name plugin for vamp.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

This package contains development files of %name.

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python

%description -n python-module-%name
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

This package contains Python module of %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
Marsyas (Music Analysis, Retrieval and Synthesis for Audio Signals) is
an open source software framework for audio processing with specific
emphasis on Music Information Retrieval applications. It has been
designed and written by George Tzanetakis (gtzan@cs.uvic.ca) with help
from students and researchers from around the world. Marsyas has been
used for a variety of projects in both academia and industry.

This package contains documentation for %name.

%prep
%setup
%patch1 -p1

for i in ANN liblinear libsvm RtMidi zlib* libpng*
do
	rm -fR src/otherlibs/$i
done

%build
%add_optflags -I%_includedir/ANN -I$PWD/src/marsyas
%add_optflags -I$PWD/src/marsyas/marsystems %optflags_shared
%add_optflags $(rtmidi-config --cppflags)

%cmake_insource \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DMARSYAS_AUDIOIO:BOOL=ON \
	-DWITH_CPP11:BOOL=ON \
	-DFREETYPE_INCLUDE_DIRS:PATH=%_includedir/freetype2 \
	-DFREETYPE_INCLUDE_DIR_ft2build:PATH=%_includedir/freetype2 \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	%nil

%make_build VERBOSE=1

pushd doc
doxygen
popd

%install
%makeinstall_std

install -d %buildroot%_libdir/vamp
install -m644 lib/mvamp.so src/mvamp/mvamp.* %buildroot%_libdir/vamp/

rm -f doc/CMakeLists.txt

%files
%doc AUTHORS PRE-0.3-TODO.txt README TODO
%_bindir/*

%files -n vamp-%name
%_libdir/vamp

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir/*

%files docs
%doc MIREX doc/*.txt doc/examples doc/out-www

%changelog
* Mon Feb 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt2.alpha.git20150301
- Fixed build with gcc-8.

* Fri Jun 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1.alpha.git20150301.3
- Rebuilt with new librtmidi 3.0.0.

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1.alpha.git20150301.2
- Fixed build with new librtmidi.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1.alpha.git20150301.1
- Updated build dependencies.
- Rebuilt for new gcc abi.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.alpha.git20150301
- New snapshot

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.alpha.git20140911
- Initial build for Sisyphus

