Name: libreplaygain
Version: r483
Release: alt1.svn20131021
Summary: Analyzes input samples and give the recommended dB change
License: LGPLv2.1+
Group: System/Libraries
Url: https://www.musepack.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.musepack.net/libreplaygain/
Source: %name-%version.tar

BuildPreReq: cmake

%description
ReplayGainAnalysis - analyzes input samples and give the recommended dB
change
Copyright (C) 2001 David Robinson and Glen Sawyer
Improvements and optimizations added by Frank Klemm, and by Marcel Mller

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
ReplayGainAnalysis - analyzes input samples and give the recommended dB
change
Copyright (C) 2001 David Robinson and Glen Sawyer
Improvements and optimizations added by Frank Klemm, and by Marcel Mller

This package contains development files of %name.

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
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r483-alt1.svn20131021
- Initial build for Sisyphus

