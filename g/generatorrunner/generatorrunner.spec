Name: generatorrunner
Version: 0.6.17
Release: alt1.git20111230
Summary: Development of binding generators for C++ and Qt-based libraries
License: GPLv2
Group: Development/KDE and QT
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://gitorious.org/pyside/generatorrunner.git
Source: %name-%version.tar

BuildPreReq: libqt4-devel cmake libapiextractor-devel
BuildPreReq: gcc-c++ phonon-devel libqt4-assistant-devel xml-utils
BuildPreReq: python-module-sphinx-devel qt4-designer xsltproc
BuildPreReq: libxml2-devel libxslt-devel

Requires: lib%name = %version-%release

%description
GeneratorRunner is a tool that eases the development of binding
generators for C++ and Qt-based libraries by providing a framework to
help automating most of the process. It uses the ApiExtractor library to
parse the header files and manipulate the classes information while
generating the binding code using front-end modules provided by the
user.

GeneratorRunner is based on the QtScriptGenerator project.

%package -n lib%name
Summary: Shared libraries of GeneratorRunner
Group: System/Libraries

%description -n lib%name
GeneratorRunner is a tool that eases the development of binding
generators for C++ and Qt-based libraries by providing a framework to
help automating most of the process. It uses the ApiExtractor library to
parse the header files and manipulate the classes information while
generating the binding code using front-end modules provided by the
user.

GeneratorRunner is based on the QtScriptGenerator project.

This package contains shared libraries of GeneratorRunner.

%package -n lib%name-devel
Summary: Development files of GeneratorRunner
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
GeneratorRunner is a tool that eases the development of binding
generators for C++ and Qt-based libraries by providing a framework to
help automating most of the process. It uses the ApiExtractor library to
parse the header files and manipulate the classes information while
generating the binding code using front-end modules provided by the
user.

GeneratorRunner is based on the QtScriptGenerator project.

This package contains development files of GeneratorRunner.

%prep
%setup

sed -i "s|@generatorrunner_VERSION@|0.6|" data/generatorrunner.pc.in

%prepare_sphinx doc
ln -s ../objects.inv doc/source

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
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DQT_PHONON_INCLUDE_DIR:PATH="%_includedir/kde4" \
	.

%make_build VERBOSE=1

pushd doc
%make doc
popd

%install
%makeinstall_std

%files
%doc AUTHORS COPYING
%doc doc/html
%_bindir/*
%_libdir/generatorrunner*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake
%_pkgconfigdir/*

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.17-alt1.git20111230
- Version 0.6.17

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.16-alt1
- Version 0.6.16

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.15-alt2
- Disabled version suffix

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.15-alt1
- Initial build for Sisyphus

