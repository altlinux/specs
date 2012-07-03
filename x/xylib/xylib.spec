Name: xylib
Version: 0.8
Release: alt1
Summary: Library for reading x-y data
License: LGPL v2.1
Group: File tools
Url: http://xylib.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ boost-devel zlib-devel bzlib-devel

Requires: lib%name = %version-%release

%description
xylib is a portable library for reading x-y data from powder
diffraction, spectroscopy and other experimental methods. Supported
formats: VAMAS, pdCIF, Bruker, Philips, Rigaku DAT, Sietronics CPI,
DBWS/DMPLOT, Koalariet XDD and others.

%package -n lib%name
Summary: Shared libraries of xylib
Group: System/Libraries

%description -n lib%name
xylib is a portable library for reading x-y data from powder
diffraction, spectroscopy and other experimental methods. Supported
formats: VAMAS, pdCIF, Bruker, Philips, Rigaku DAT, Sietronics CPI,
DBWS/DMPLOT, Koalariet XDD and others.

This package contains shared libraries of xylib.

%package -n lib%name-devel
Summary: Development files of xylib
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
xylib is a portable library for reading x-y data from powder
diffraction, spectroscopy and other experimental methods. Supported
formats: VAMAS, pdCIF, Bruker, Philips, Rigaku DAT, Sietronics CPI,
DBWS/DMPLOT, Koalariet XDD and others.

This package contains development files of xylib.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no
%make_build

%install
%makeinstall_std

%files
%doc COPYING README* TODO
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Rebuilt for debuginfo

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

