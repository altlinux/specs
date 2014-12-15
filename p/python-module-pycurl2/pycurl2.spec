%define oname pycurl2

%def_disable check

Name: python-module-%oname
Version: 7.20.0
Release: alt1.a1.git20130808
Summary: PycURL2 - cURL library module for python
License: LGPLv2.1/MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycurl2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Lispython/pycurl.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests libcurl-devel
BuildPreReq: python-module-nose python-module-unittest2
BuildPreReq: python-module-simplejson
BuildPreReq: python-module-sphinx-devel

%py_provides %oname

%description
PycURL2 is a fork from original PycURL library that no maintained from
7.19.0 (Sep 9 2008).

PycURL2 is a Python interface to libcurl. PycURL2 can be used to fetch
objects identified by a URL from a Python program, similar to the urllib
Python module. PycURL2 is mature, very fast, and supports a lot of
features.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PycURL2 is a fork from original PycURL library that no maintained from
7.19.0 (Sep 9 2008).

PycURL2 is a Python interface to libcurl. PycURL2 can be used to fetch
objects identified by a URL from a Python program, similar to the urllib
Python module. PycURL2 is mature, very fast, and supports a lot of
features.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PycURL2 is a fork from original PycURL library that no maintained from
7.19.0 (Sep 9 2008).

PycURL2 is a Python interface to libcurl. PycURL2 can be used to fetch
objects identified by a URL from a Python program, similar to the urllib
Python module. PycURL2 is mature, very fast, and supports a lot of
features.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%install
%python_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
exit 1

%files
%doc ChangeLog *.rst
%dir %python_sitelibdir/%oname
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html examples

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.20.0-alt1.a1.git20130808
- Initial build for Sisyphus

