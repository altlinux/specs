Name: cqvamp
Version: 1.0
Release: alt1
Summary: Vamp plugin implementing the Constant-Q transform of a time-domain signal
License: MIT
Group: Sound
Url: https://code.soundsoftware.ac.uk/projects/constant-q-cpp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ libvamp-devel doxygen graphviz
BuildPreReq: boost-devel libsndfile-devel

%description
A C++ library and Vamp plugin implementing the Constant-Q transform of
a time-domain signal.

The Constant-Q transform is a time-to-frequency-domain transform related
to the short-time Fourier transform, but with output bins spaced
logarithmically in frequency, rather than linearly. The output bins are
therefore linearly spaced in terms of musical pitch.

%package -n libcq
Summary: A C++ library implementing the Constant-Q transform of a time-domain signal
Group: System/Libraries

%description -n libcq
A C++ library implementing the Constant-Q transform of a time-domain
signal.

The Constant-Q transform is a time-to-frequency-domain transform related
to the short-time Fourier transform, but with output bins spaced
logarithmically in frequency, rather than linearly. The output bins are
therefore linearly spaced in terms of musical pitch.

%package -n libcq-devel
Summary: Development files of C++ library implementing the Constant-Q transform
Group: Development/C++
Requires: libcq = %EVR

%description -n libcq-devel
A C++ library implementing the Constant-Q transform of a time-domain
signal.

The Constant-Q transform is a time-to-frequency-domain transform related
to the short-time Fourier transform, but with output bins spaced
logarithmically in frequency, rather than linearly. The output bins are
therefore linearly spaced in terms of musical pitch.

This package contains development files of libcq.

%package -n libcq-devel-docs
Summary: Documentation for C++ library implementing the Constant-Q transform
Group: Development/Documentation
BuildArch: noarch

%description -n libcq-devel-docs
A C++ library implementing the Constant-Q transform of a time-domain
signal.

The Constant-Q transform is a time-to-frequency-domain transform related
to the short-time Fourier transform, but with output bins spaced
logarithmically in frequency, rather than linearly. The output bins are
therefore linearly spaced in terms of musical pitch.

This package contains development documentation for libcq.

%prep
%setup

%build
export LD_LIBRARY_PATH=$PWD
%make_build -f Makefile.linux test/processfile
%make_build -f Makefile.linux

doxygen

%install
%makeinstall_std -f Makefile.linux LIBDIR=%_libdir

%files
%doc CITATION README
%_libdir/vamp

%files -n libcq
%_libdir/*.so.*

%files -n libcq-devel
%_includedir/*
%_libdir/*.so

%files -n libcq-devel-docs
%doc doc/html/*

%changelog
* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

