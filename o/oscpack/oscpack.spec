%define sover 0

Name: oscpack
Version: 1.1.0
Release: alt1.svn20140913
Summary: A simple C++ Open Sound Control (OSC) packet manipulation library
License: MIT
Group: Sound
Url: https://code.google.com/p/oscpack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://oscpack.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake

%description
Oscpack is simply a set of C++ classes for packing and unpacking OSC
packets. Oscpack includes a minimal set of UDP networking classes for
Windows and POSIX. The networking classes are sufficient for writing
many OSC applications and servers, but you are encouraged to use another
networking framework if it better suits your needs. Oscpack is not an
OSC application framework. It doesn't include infrastructure for
constructing or routing OSC namespaces, just classes for easily
constructing, sending, receiving and parsing OSC packets. The library
should also be easy to use for other transport methods (e.g. serial).

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Oscpack is simply a set of C++ classes for packing and unpacking OSC
packets. Oscpack includes a minimal set of UDP networking classes for
Windows and POSIX. The networking classes are sufficient for writing
many OSC applications and servers, but you are encouraged to use another
networking framework if it better suits your needs. Oscpack is not an
OSC application framework. It doesn't include infrastructure for
constructing or routing OSC namespaces, just classes for easily
constructing, sending, receiving and parsing OSC packets. The library
should also be easy to use for other transport methods (e.g. serial).

This package contains shared library of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Oscpack is simply a set of C++ classes for packing and unpacking OSC
packets. Oscpack includes a minimal set of UDP networking classes for
Windows and POSIX. The networking classes are sufficient for writing
many OSC applications and servers, but you are encouraged to use another
networking framework if it better suits your needs. Oscpack is not an
OSC application framework. It doesn't include infrastructure for
constructing or routing OSC namespaces, just classes for easily
constructing, sending, receiving and parsing OSC packets. The library
should also be easy to use for other transport methods (e.g. serial).

This package contains development files of %name.

%prep
%setup

cp -fR examples tests ../

%build
%add_optflags %optflags_shared
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

g++ -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-Wl,-soname=lib%name.so.%sover -o lib%name.so.%sover

%install
install -d %buildroot%_includedir
install -p -m644 osc/*.h ip/*.h %buildroot%_includedir/

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

install -d %buildroot%_bindir
install -m755 OscDump OscReceiveTest OscSendTests OscUnitTests \
	SimpleReceive SimpleSend \
	%buildroot%_bindir/

%files
%doc ../examples ../tests
%doc CHANGES README TODO
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20140913
- Initial build for Sisyphus

