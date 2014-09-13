Name: jsonxx
Version: 20140722
Release: alt1
Summary: Self contained Flex/Bison JSON parser for C++11
License: MIT
Group: System/Libraries
Url: https://bitbucket.org/tunnuz/json
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tunnuz/json.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake flex

%description
JSON++ is a self contained Flex/Bison JSON parser for C++11. It parses
strings and files in JSON format, and builds an in-memory tree
representing the JSON structure. JSON objects are mapped to std::maps,
arrays to std::vectors, JSON native types are mapped onto C++ native
types. The library also includes printing on streams. Classes exploit
move semantics to avoid copying parsed structures around. It doesn't
require any additional library (not even libfl).

%package -n lib%name
Summary: Self contained Flex/Bison JSON parser for C++11
Group: System/Libraries

%description -n lib%name
JSON++ is a self contained Flex/Bison JSON parser for C++11. It parses
strings and files in JSON format, and builds an in-memory tree
representing the JSON structure. JSON objects are mapped to std::maps,
arrays to std::vectors, JSON native types are mapped onto C++ native
types. The library also includes printing on streams. Classes exploit
move semantics to avoid copying parsed structures around. It doesn't
require any additional library (not even libfl).

%package -n lib%name-devel
Summary: Development files of JSON++
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
JSON++ is a self contained Flex/Bison JSON parser for C++11. It parses
strings and files in JSON format, and builds an in-memory tree
representing the JSON structure. JSON objects are mapped to std::maps,
arrays to std::vectors, JSON native types are mapped onto C++ native
types. The library also includes printing on streams. Classes exploit
move semantics to avoid copying parsed structures around. It doesn't
require any additional library (not even libfl).

This package contains development files of JSON++.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
install -d %buildroot%_includedir/json++
install -d %buildroot%_libdir

install -p -m644 *.hh %buildroot%_includedir/json++/
cp -P *.so* %buildroot%_libdir/

%files -n lib%name
%doc *.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140722-alt1
- Initial build for Sisyphus

