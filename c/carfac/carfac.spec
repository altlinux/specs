%define sover 0

Name: carfac
Version: 0.0
Release: alt1.git20140829
Summary: Cascade of Asymmetric Resonators with Fast-Acting Compression cochlear model
License: ASL v2.0
Group: Sound
Url: https://github.com/google/carfac
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/google/carfac.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ scons eigen3 libgtest-devel

%description
The CAR-FAC (cascade of asymmetric resonators with fast-acting
compression) is a cochlear model implemented as an efficient sound
processor, for mono, stereo, or multi-channel sound inputs.

%package -n lib%name
Summary: Cascade of Asymmetric Resonators with Fast-Acting Compression cochlear model
Group: System/Libraries

%description -n lib%name
The CAR-FAC (cascade of asymmetric resonators with fast-acting
compression) is a cochlear model implemented as an efficient sound
processor, for mono, stereo, or multi-channel sound inputs.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The CAR-FAC (cascade of asymmetric resonators with fast-acting
compression) is a cochlear model implemented as an efficient sound
processor, for mono, stereo, or multi-channel sound inputs.

This package contains development files of lib%name.

%prep
%setup

%build
pushd cpp
EIGEN_PATH=%_includedir/eigen3 scons -j %__nprocs
rm -f lib%name.a
g++ -shared *.o -Wl,-soname=lib%name.so.%sover \
	-o lib%name.so.%sover
popd

%install
install -d %buildroot%_includedir/%name
install -p -m644 cpp/*.h %buildroot%_includedir/%name/

install -d %buildroot%_libdir
install -m644 cpp/lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%check
pushd cpp
EIGEN_PATH=%_includedir/eigen3 scons test
popd

%files -n lib%name
%doc AUTHORS CONTRIBUTORS *.txt *.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.git20140829
- Initial build for Sisyphus

