%define sover 0

Name: btrack
Version: 1.0.0
Release: alt1.hg20140708
Summary: Causal beat tracking algorithm intended for real-time use
License: GPLv3+
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/btrack
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.soundsoftware.ac.uk/hg/btrack
# branch: develop
Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel python-devel libfftw3-devel
BuildPreReq: libsamplerate-devel libnumpy-devel

%description
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

%package docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description docs
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

This package contains documentation for %name.

%package -n lib%name
Summary: Causal beat tracking algorithm intended for real-time use
Group: System/Libraries

%description -n lib%name
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

This package contains development files of %name.

%package -n vamp-%name-plugin
Summary: Vamp plugin of %name
Group: Sound
Requires: lib%name = %EVR

%description -n vamp-%name-plugin
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

This package contains Vamp plugin of %name.

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python
Requires: lib%name = %EVR

%description -n python-module-%name
BTrack is a causal beat tracking algorithm intended for real-time use.
It is implemented in C++ with wrappers for Python and the Vamp plug-in
framework.

This package contains Python module of %name.

%prep
%setup

%build
%add_optflags %optflags_shared

pushd src
g++ -c %optflags -I. *.cpp
g++ -shared *.o -Wl,-soname=lib%name.so.%sover -lsamplerate -lfftw3 \
	-o ../lib%name.so.%sover
ln -s lib%name.so.%sover ../lib%name.so
popd

pushd modules-and-plug-ins/python-module 
%python_build_debug
popd

pushd modules-and-plug-ins/vamp-plugin
%make_build
popd

%install
install -d %buildroot%_includedir/%name
install -p -m644 src/*.h %buildroot%_includedir/%name/

install -d %buildroot%_libdir
install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

pushd modules-and-plug-ins/python-module 
%python_install
popd

pushd modules-and-plug-ins/vamp-plugin
install -d %buildroot%_libdir/vamp
install -m644 %name.so %buildroot%_libdir/vamp/
popd

%files -n lib%name
%doc *.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n vamp-%name-plugin
%_libdir/vamp

%files -n python-module-%name
%python_sitelibdir/*

%files docs
%doc doc/html/*

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20140708
- Initial build for Sisyphus

