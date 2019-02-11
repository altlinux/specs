%define _unpackaged_files_terminate_build 1

Name: yaafe
Version: 0.64
Release: alt3.git20130420
Summary: Yaafe - Yet Another Audio Feature Extractor
License: LGPLv3
Group: Sound
Url: http://yaafe.sourceforge.net/

# git://git.code.sf.net/p/yaafe/code
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: cmake gcc-c++ libargtable2-devel libsndfile-devel
BuildRequires: libmpg123-devel libhdf5-devel liblapack-devel
BuildRequires: libfftw3-devel dvipng
BuildRequires: python-module-sphinx-devel texlive-latex-recommended

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
%patch1 -p1

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%cmake \
	-DCMAKE_INSTALL_PYTHON_PACKAGES=%python_sitelibdir_noarch \
	-DCMAKE_INSTALL_YAAFE_EXTENSIONS=%_libdir/yaafe_extensions \
	-DWITH_HDF5:BOOL=ON \
	-DWITH_MPG123:BOOL=ON \
	-DWITH_LAPACK:BOOL=ON \
	-DWITH_FFTW3:BOOL=ON \
	-DWITH_TIMERS:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

export LD_LIBRARY_PATH=%buildroot%_libdir
%make -C doc html

install -d %buildroot%_sysconfdir/profile.d
cat <<EOF > %buildroot%_sysconfdir/profile.d/%name.sh
export YAAFE_PATH=%_libdir/yaafe_extensions
EOF

chmod +x %buildroot%_sysconfdir/profile.d/%name.sh

# don't put CMakeLists.txt into documentation
rm -f matlab/CMakeLists.txt

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
%doc doc/build/html
%doc matlab

%changelog
* Mon Feb 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.64-alt3.git20130420
- Fixed build with gcc-8.

* Fri Oct 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.64-alt2.git20130420
- Fixed build with new toolchain.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.64-alt1.git20130420
- Initial build for Sisyphus

