Name: ffs
Version: 1.1.201
Release: alt1.rev20549.svn20150305
Summary: Fast Flexible Serialization
License: BSD
Group: Development/Other
Url: http://www.cc.gatech.edu/systems/projects/EVPath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.research.cc.gatech.edu/kaos/ffs/trunk/
# login: anon
# password: anon
Source: %name-%version.tar

BuildPreReq: cmake ctest flex libcercs_env-devel libatl-devel doxygen
BuildPreReq: libdill-devel gcc-c++ graphviz

Requires: lib%name = %EVR

%description
FFS (Fast Flexible Serialization) is a system for efficiently marshaling
data for communication or storage in a heterogeneous computing
environment.

FFS is more complex than the type systems built into many middleware
environments because it was designed to operate efficiently in
situations where a priori knowledge shared between the sender (writer)
and receiver (reader) is limited.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
FFS (Fast Flexible Serialization) is a system for efficiently marshaling
data for communication or storage in a heterogeneous computing
environment.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
FFS (Fast Flexible Serialization) is a system for efficiently marshaling
data for communication or storage in a heterogeneous computing
environment.

This package contains development files of %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
FFS (Fast Flexible Serialization) is a system for efficiently marshaling
data for communication or storage in a heterogeneous computing
environment.

This package contains documentation for %name.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DBUILD_SHARED_STATIC:STRING=SHARED \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

pushd cod/doc
doxygen
popd
mv cod/doc/html cod/cod

%install
%makeinstall_std

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files docs
%doc doc/examples doc/*.pdf cod/cod

%changelog
* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.201-alt1.rev20549.svn20150305
- Initial build for Sisyphus

