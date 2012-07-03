Name: pyside-tools-py3
Version: 0.2.14
Release: alt2.git20120427
Summary: Tools for python bindings for the Qt cross-platform application (Python 3)
License: GPLv2 & BSD
Group: Development/Tools
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://gitorious.org/pyside/pyside-tools.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel gcc-c++ cmake libqt4-devel
BuildPreReq: libshiboken-py3-devel shiboken-py3 libpyside-qt4-py3-devel
BuildPreReq: phonon-devel qt4-designer xml-utils xsltproc
BuildPreReq: libxml2-devel libxslt-devel libqt4-assistant-devel

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains PySide tools.

%package -n python3-module-pysideuic
Summary: Python 3 module of PySide tools
Group: Development/Python3

%description -n python3-module-pysideuic
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains python module of PySide tools.

%prep
%setup

sed -i 's|%_bindir/env python|%_bindir/env python3|' \
	pyside-uic pysideuic/icon_cache.py

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DBUILD_TESTS:BOOL=OFF \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DPYTHON_EXECUTABLE:FILEPATH="%_bindir/python3" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
pushd %buildroot%_man1dir
for i in $(ls); do
	mv $i py3_$i
done
popd

%files
%doc AUTHORS LICENSE*
%_bindir/*
%_man1dir/*

%files -n python3-module-pysideuic
%python3_sitelibdir/*
%exclude %python3_sitelibdir/pysideuic/port_v2

%changelog
* Sun May 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt2.git20120427
- Renamed pyside-tools-qt3 -> pyside-tools-py3

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt1.git20120427
- Version 0.2.14 for Python 3

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.13-alt1
- Initial build for Sisyphus

