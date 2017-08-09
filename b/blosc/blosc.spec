Name: blosc
Version: 1.12.1
Release: alt1
Summary: Blosc: A blocking, shuffling and lossless compression library
License: MIT
Group: System/Libraries
Url: http://www.blosc.org/

# https://github.com/Blosc/c-blosc.git
Source: %name-%version.tar
Patch1: %name-%version-alt-pkgconfigdir.patch

BuildPreReq: cmake gcc-c++ libsnappy-devel zlib-devel
BuildPreReq: liblz4-devel

%description
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

%package -n lib%name
Summary: Blosc: A blocking, shuffling and lossless compression library
Group: System/Libraries

%description -n lib%name
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

%package -n lib%name-devel
Summary: Development files of Blosc library
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

This package contains development files of Blosc library.

%prep
%setup
%patch1 -p1

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DBUILD_BENCHMARKS:BOOL=OFF \
	-DBUILD_STATIC:BOOL=ON \
	-DBUILD_TESTS:BOOL=OFF \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

# remove unpackaged files
rm %buildroot%_libdir/libblosc.a

%files -n lib%name
%doc *.rst
%_libdir/libblosc.so.*

%files -n lib%name-devel
%_includedir/blosc.h
%_includedir/blosc-export.h
%_libdir/libblosc.so
%_pkgconfigdir/blosc.pc

%changelog
* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.1-alt1
- Updated to upstream release version 1.12.1.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev.git20150428
- Version 1.6.1.dev

* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140611
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140501
- Initial build for Sisyphus

