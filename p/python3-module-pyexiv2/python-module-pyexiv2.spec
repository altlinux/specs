%define oname pyexiv2

Name: python3-module-%oname
Version: 0.3.2
Release: alt1.bzr20120921.1

Summary: A python binding to exiv2, the C++ library for manipulation of EXIF and IPTC image metadata
License: GPLv2+
Group: Development/Python3

Url: http://tilloy.net/dev/pyexiv2/
# bzr branch lp:~osomon/pyexiv2/py3k
Source0: pyexiv2-%version.tar.bz2
Patch1: %oname-0.1.3-overridecxx.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel boost-python3-devel flex gcc-c++ scons
BuildPreReq: libexiv2-devel

%description
Pyexiv2 is a python binding to exiv2, the C++ library for manipulation of EXIF
and IPTC image metadata. It is a python module that allows your python scripts
to read and write metadata (EXIF, IPTC, thumbnail) embedded in image files
(JPEG, TIFF, ...).

It is designed as a high level interface to the functionalities offered by exiv2
(and is built on top of it). Using python's built-in data types and standard
modules, it provides easy manipulation of image metadata.

%prep
%setup -n %oname-%version
%patch1 -p1
sed -i 's|boost_python|boost_python3|' src/SConscript

%build
scons -j %__nprocs CXXFLAGS="%optflags"

%install
# Why CXXFLAGS here?? scons will try to recompile sources when CXXFLAGS value
# differ from used for compilation...
scons install DESTDIR=%buildroot CXXFLAGS="%optflags"

%files
%python3_sitelibdir/*
%doc doc/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.3.2-alt1.bzr20120921.1
- rebuild with boost 1.57.0

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.bzr20120921
- Initial build for Sisyphus

