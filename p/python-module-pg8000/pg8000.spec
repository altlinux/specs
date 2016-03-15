%define oname pg8000

%def_with python3

Name: python-module-%oname
Version: 1.10.2
Release: alt1.git20150629.1.1
Summary: PostgreSQL interface library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pg8000/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mfenniak/pg8000.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-pytz
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-pytz
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-setuptools-tests python3-module-nose python3-module-pytz python3-module-setuptools-tests rpm-build-python3 time

%description
pg8000 is a Pure-Python interface to the PostgreSQL database engine. It
is one of many PostgreSQL interfaces for the Python programming
language. pg8000 is somewhat distinctive in that it is written entirely
in Python and does not rely on any external libraries (such as a
compiled python module, or PostgreSQL's libpq library). pg8000 supports
the standard Python DB-API version 2.0.

pg8000's name comes from the belief that it is probably about the 8000th
PostgreSQL interface for Python.

%if_with python3
%package -n python3-module-%oname
Summary: PostgreSQL interface library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pg8000 is a Pure-Python interface to the PostgreSQL database engine. It
is one of many PostgreSQL interfaces for the Python programming
language. pg8000 is somewhat distinctive in that it is written entirely
in Python and does not rely on any external libraries (such as a
compiled python module, or PostgreSQL's libpq library). pg8000 supports
the standard Python DB-API version 2.0.

pg8000's name comes from the belief that it is probably about the 8000th
PostgreSQL interface for Python.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pg8000 is a Pure-Python interface to the PostgreSQL database engine. It
is one of many PostgreSQL interfaces for the Python programming
language. pg8000 is somewhat distinctive in that it is written entirely
in Python and does not rely on any external libraries (such as a
compiled python module, or PostgreSQL's libpq library). pg8000 supports
the standard Python DB-API version 2.0.

pg8000's name comes from the belief that it is probably about the 8000th
PostgreSQL interface for Python.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc README* doc/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc README* doc/build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.2-alt1.git20150629.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1.git20150629.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.git20150629
- Initial build for Sisyphus

