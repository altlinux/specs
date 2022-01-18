%define sover 0

Name: onsetsds
Version: 2011.02.10
Release: alt1.1
Summary: Musical onset detection library
License: GPLv2
Group: Sound
Url: http://sourceforge.net/projects/onsetsds/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libsndfile-devel libfftw3-devel gcc-c++

%description
Onset detector for musical signals, with an emphasis on real-time onset
detection for interactive music systems. Hence this aims to be a small,
efficient, lightweight onset detection system that provides good-quality
detection.

%package -n lib%name
Summary: Musical onset detection library
Group: System/Libraries

%description -n lib%name
Onset detector for musical signals, with an emphasis on real-time onset
detection for interactive music systems. Hence this aims to be a small,
efficient, lightweight onset detection system that provides good-quality
detection.

%package -n lib%name-devel
Summary: Development files of musical onset detection library
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Onset detector for musical signals, with an emphasis on real-time onset
detection for interactive music systems. Hence this aims to be a small,
efficient, lightweight onset detection system that provides good-quality
detection.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for musical onset detection library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Onset detector for musical signals, with an emphasis on real-time onset
detection for interactive music systems. Hence this aims to be a small,
efficient, lightweight onset detection system that provides good-quality
detection.

This package contains development documentation for %name.

%prep
%setup

%build
%add_optflags -fpermissive

pushd src
for i in *.c; do
	gcc %optflags %optflags_shared -c $i
done
gcc -shared *.o -Wl,-soname=lib%name.so.%sover \
	-lfftw3f -lsndfile -o lib%name.so.%sover
popd

%install
install -d %buildroot%_includedir
install -d %buildroot%_libdir

install -p -m644 src/*.h %buildroot%_includedir/
install -m644 src/*.so.* %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%files -n lib%name
%doc AUTHORS ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-docs
%doc doc/html/*

%changelog
* Tue Jan 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2011.02.10-alt1.1
- C sources must be compiled with a C compiler

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.02.10-alt1
- Initial build for Sisyphus

