Name: blosc
Version: 1.3.6
Release: alt1.git20140611
Summary: Blosc: A blocking, shuffling and lossless compression library
License: MIT
Group: System/Libraries
Url: http://blosc.pytables.org/trac
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake gcc-c++ libhdf5-devel libsnappy-devel zlib-devel
BuildPreReq: hdf5-8-tools liblz4-devel

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

%package -n lib%name-hdf5filter
Summary: Blosc compression filter for the HDF5 library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-hdf5filter
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

This package contains Blosc compression filter for the HDF5 library.

%package -n lib%name-hdf5filter-devel
Summary: Development files of Blosc compression filter for the HDF5 library
Group: Development/C++
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-hdf5filter = %EVR

%description -n lib%name-hdf5filter-devel
Blosc is a high performance compressor optimized for binary data. It has
been designed to transmit data to the processor cache faster than the
traditional, non-compressed, direct memory fetch approach via a memcpy()
OS call. Blosc is the first compressor (that I'm aware of) that is meant
not only to reduce the size of large datasets on-disk or in-memory, but
also to accelerate memory-bound computations.

This package contains development files of Blosc compression filter for
the HDF5 library.

%prep
%setup

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
	-DBUILD_HDF5_FILTER:BOOL=ON \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%files -n lib%name
%doc *.rst
%_libdir/libblosc.so.*

%files -n lib%name-devel
%_includedir/blosc.h
%_libdir/libblosc.so

%files -n lib%name-hdf5filter
%_libdir/libblosc_filter.so

%files -n lib%name-hdf5filter-devel
%doc hdf5/README.rst
%_includedir/blosc_filter.h

%changelog
* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140611
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.git20140501
- Initial build for Sisyphus

