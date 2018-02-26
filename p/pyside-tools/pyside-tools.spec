Name: pyside-tools
Version: 0.2.14
Release: alt1.git20120427
Summary: Tools for python bindings for the Qt cross-platform application
License: GPLv2 & BSD
Group: Development/Tools
Url: http://www.pyside.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://gitorious.org/pyside/pyside-tools.git
Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ cmake libqt4-devel
BuildPreReq: libshiboken-devel shiboken libpyside-qt4-devel
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

%package -n python-module-pysideuic
Summary: Python module of PySide tools
Group: Development/Python

%description -n python-module-pysideuic
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework, as well as a complete
toolchain for rapidly generating bindings for any Qt-based C++ class
hierarchies. PySide Qt bindings allow both free open source and
proprietary software development and ultimately aim to support all of
the platforms as Qt itself.

This package contains python module of PySide tools.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DBUILD_TESTS:BOOL=OFF \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE*
%_bindir/*
%_man1dir/*

%files -n python-module-pysideuic
%python_sitelibdir/*
%exclude %python_sitelibdir/pysideuic/port_v3

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.14-alt1.git20120427
- Version 0.2.14

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.13-alt1
- Initial build for Sisyphus

