%define oname dap
Name: python-module-%oname
Version: 2.2.6.7
Release: alt1.svn20081222.3.1
Summary: Python implementation of the Data Access Protocol (DAP)
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/dap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pydap.googlecode.com/svn/trunk/dap
Source: %oname-%version.tar.gz
Source1: dap-nspkg.pth
BuildArch: noarch

%py_requires paste.deploy

BuildPreReq: python-devel python-module-httplib2 python-module-setuptools
BuildPreReq: python-module-paste python-module-cheetah
%setup_python_module %oname

%description
This is a Python implementation of the Data Access Protocol, a
scientific protocol for data access developed by the OPeNDAP team
(http://opendap.org). This implementation is developed from scratch,
following the latest specification of the protocol (DAP 2.0 Draft
Community Standard 2005/04/27) and based on my experience with OPeNDAP
servers on the wild.

Using this module one can access hundreds of scientific datasets from
Python programs, accessing data in an efficient, transparent and
pythonic way. Arrays are manipulated like normal multi-dimensional
arrays (like numpy.array, e.g.), with the fundamental difference that
data is downloaded on-the-fly when a variable is sliced. Sequential
data can be filtered on the server side before being downloaded, saving
bandwith and time.

The module also implements a DAP server, allowing datasets from a
multitude of formats (netCDF, Matlab, CSV, GrADS/GRIB files, SQL RDBMS)
to be served on the internet. The server specifies a plugin API for
supporting new data formats in an easy way. The DAP server is
implemented as a WSGI application (see PEP 333), running on a variery
of servers, and can be combined with WSGI middleware to support
authentication, gzip compression and much more.

%prep
%setup
install -p -m644 %SOURCE1 .
mv dap-nspkg.pth dap-%version-py%_python_version-nspkg.pth

%build
%python_build

%install
%python_install
install -p -m644 *.pth %buildroot%python_sitelibdir

cp -f %oname/__init__.py \
	%buildroot%python_sitelibdir/%oname/__init__.py
cp -f %oname/responses/__init__.py \
	%buildroot%python_sitelibdir/%oname/responses/__init__.py
cp -f %oname/plugins/__init__.py \
	%buildroot%python_sitelibdir/%oname/plugins/__init__.py

install -d %buildroot%python_sitelibdir/%oname/tests
install -p -m644 tests/* %buildroot%python_sitelibdir/%oname/tests

%files
%doc LICENSE README TODO docs/*
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.6.7-alt1.svn20081222.3.1
- Rebuild with Python-2.7

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.3
- Added .pth file

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.2
- Rebuilt with python 2.6

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.1
- Fixed loading of responses and plugins submodules

* Fri Oct 2 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222
- Initial build for Sisyphus

