Name: musepack
Version: r475
Release: alt1
Summary: Portable Musepack decoder library
License: BSD
Group: Sound
Url: https://www.musepack.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake libcuefile-devel libreplaygain-devel

Requires: libmpcdec0 = %EVR

%description
Musepack is a free, high performance, high quality lossy audio
compression codec. For more information on musepack visit
http://www.musepack.net.

%package -n libmpcdec0
Summary: Library that decodes musepack compressed audio data
Group: System/Libraries

%description -n libmpcdec0
libmpcdec is a library that decodes musepack compressed audio data.

%package -n libmpcdec0-devel
Summary: Development files of libmpcdec
Group: Development/C
Requires: libmpcdec0 = %EVR
Conflicts: libmpcdec-devel

%description -n libmpcdec0-devel
libmpcdec is a library that decodes musepack compressed audio data.

This package contains development files of libmpcdec.

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
%makeinstall_std

%files
%_bindir/*

%files -n libmpcdec0
%_libdir/*.so.*

%files -n libmpcdec0-devel
%doc docs/mainpage.txt
%_includedir/*
%_libdir/*.so

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r475-alt1
- Initial build for Sisyphus

