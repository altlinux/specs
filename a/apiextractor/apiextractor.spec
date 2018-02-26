Name: apiextractor
Version: 0.10.11
Release: alt1.git20120104
Summary: Development of bindings of Qt-based libraries for high level languages
License: GPLv2
Group: Development/KDE and QT
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake ctest libqt4-devel phonon-devel
BuildPreReq: gcc-c++ libxslt-devel libxml2-devel xml-utils
BuildPreReq: python-module-sphinx-devel xsltproc qt4-designer
BuildPreReq: libqt4-assistant-devel xml-utils

%description
The API Extractor library is used by the binding generator to parse
headers of a given library and merge this data with information provided
by typesystem (XML) files, resulting in a representation of how the API
should be exported to the chosen target language. The generation of
source code for the bindings is performed by specific generators using
the API Extractor library.

The API Extractor is based on QtScriptGenerator codebase.

%package -n lib%name
Summary: Development of bindings of Qt-based libraries for high level languages
Group: System/Libraries

%description -n lib%name
The API Extractor library is used by the binding generator to parse
headers of a given library and merge this data with information provided
by typesystem (XML) files, resulting in a representation of how the API
should be exported to the chosen target language. The generation of
source code for the bindings is performed by specific generators using
the API Extractor library.

The API Extractor is based on QtScriptGenerator codebase.

This package contains shared libraries of the API Extractor.

%package -n lib%name-devel
Summary: Development files of the API Extractor
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The API Extractor library is used by the binding generator to parse
headers of a given library and merge this data with information provided
by typesystem (XML) files, resulting in a representation of how the API
should be exported to the chosen target language. The generation of
source code for the bindings is performed by specific generators using
the API Extractor library.

The API Extractor is based on QtScriptGenerator codebase.

This package contains development files of the API Extractor.

%package -n lib%name-devel-doc
Summary: Documentation for the API Extractor
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The API Extractor library is used by the binding generator to parse
headers of a given library and merge this data with information provided
by typesystem (XML) files, resulting in a representation of how the API
should be exported to the chosen target language. The generation of
source code for the bindings is performed by specific generators using
the API Extractor library.

The API Extractor is based on QtScriptGenerator codebase.

This package contains development documentation for the API Extractor.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc

%build
export PATH=$PATH:%_qt4dir/bin
FLAGS="$(pkg-config phonon --cflags)"
%add_optflags $FLAGS
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DENABLE_GCC_OPTIMIZATION:BOOL=ON \
	-DENABLE_VERSION_SUFFIX:BOOL=OFF \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DQT_PHONON_INCLUDE_DIR:PATH="%_includedir/kde4" \
	.

%make_build VERBOSE=1

pushd doc
%make doc
popd

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS COPYING
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake

%files -n lib%name-devel-doc
%doc doc/html/*

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.11-alt1.git20120104
- Version 0.10.11

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.10-alt1
- Version 0.10.10

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.9-alt2
- Disabled  version suffix

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.9-alt1
- Initial build for Sisyphus

