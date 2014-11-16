Name: yaafe
Version: 0.64
Release: alt1.git20130420
Summary: Yaafe - Yet Another Audio Feature Extractor
License: LGPLv3
Group: Sound
Url: http://yaafe.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.code.sf.net/p/yaafe/code
Source: %name-%version.tar

BuildPreReq: cmake gcc-c++ libargtable2-devel libsndfile-devel
BuildPreReq: libmpg123-devel libhdf5-devel liblapack-devel
BuildPreReq: libfftw3-devel dvipng
BuildPreReq: python-module-sphinx-devel texlive-latex-recommended

Requires: lib%name = %EVR

%description
Yet Another Audio Feature Extractor is a toolbox for audio analysis.
Easy to use and efficient at extracting a large number of audio features
simultaneously. WAV and MP3 files supported, or embedding in C++, Python
or Matlab applications.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
Yet Another Audio Feature Extractor is a toolbox for audio analysis.
Easy to use and efficient at extracting a large number of audio features
simultaneously. WAV and MP3 files supported, or embedding in C++, Python
or Matlab applications.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR

%description -n lib%name-devel
Yet Another Audio Feature Extractor is a toolbox for audio analysis.
Easy to use and efficient at extracting a large number of audio features
simultaneously. WAV and MP3 files supported, or embedding in C++, Python
or Matlab applications.

This package contains development files of %name.

%package -n python-module-yaafelib
Summary: Python bindings for %name
Group: Development/Python
BuildArch: noarch
Requires: lib%name = %EVR

%description -n python-module-yaafelib
Yet Another Audio Feature Extractor is a toolbox for audio analysis.
Easy to use and efficient at extracting a large number of audio features
simultaneously. WAV and MP3 files supported, or embedding in C++, Python
or Matlab applications.

This package contains python bindings for %name.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
Yet Another Audio Feature Extractor is a toolbox for audio analysis.
Easy to use and efficient at extracting a large number of audio features
simultaneously. WAV and MP3 files supported, or embedding in C++, Python
or Matlab applications.

This package contains documentation for %name.

%prep
%setup

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
mkdir BUILD
pushd BUILD
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_PREFIX_PATH=%_libdir \
	-DCMAKE_INSTALL_PYTHON_PACKAGES=%python_sitelibdir_noarch \
	-DCMAKE_INSTALL_YAAFE_EXTENSIONS=%_libdir/yaafe_extensions \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DWITH_HDF5:BOOL=ON \
	-DWITH_MPG123:BOOL=ON \
	-DWITH_LAPACK:BOOL=ON \
	-DWITH_FFTW3:BOOL=ON \
	-DWITH_TIMERS:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	..
%make_build VERBOSE=1
popd

%install
%makeinstall_std -C BUILD

export LD_LIBRARY_PATH=%buildroot%_libdir
%make -C doc html

install -d %buildroot%_sysconfdir/profile.d
cat <<EOF > %buildroot%_sysconfdir/profile.d/%name.sh
export YAAFE_PATH=%_libdir/yaafe_extensions
EOF

%files
%doc DISCLAIMER README
%_bindir/*

%files -n lib%name
%_sysconfdir/profile.d/%name.sh
%_libdir/yaafe_extensions
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/%name

%files -n python-module-yaafelib
%python_sitelibdir_noarch/*

%files docs
%doc doc/build/html/*

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.64-alt1.git20130420
- Initial build for Sisyphus

