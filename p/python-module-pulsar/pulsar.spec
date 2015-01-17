%define oname pulsar

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.git20141118
Summary: Event driven concurrent framework for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pulsar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/quantmind/pulsar.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-trollius
BuildPreReq: python-module-coverage python-module-django
BuildPreReq: python-module-setproctitle python-tools-pep8
BuildPreReq: python-module-psutil python-module-greenlet
BuildPreReq: python-module-SQLAlchemy python-module-unidecode
BuildPreReq: python-module-psycopg2
BuildPreReq: python-module-mock
BuildPreReq: python-modules-multiprocessing /proc
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-trollius
BuildPreReq: python3-module-coverage python3-module-django
BuildPreReq: python3-module-setproctitle python3-tools-pep8
BuildPreReq: python3-module-psutil python3-module-greenlet
BuildPreReq: python3-module-SQLAlchemy python3-module-unidecode
BuildPreReq: python3-module-psycopg2 python3-module-asyncio
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires trollius django setproctitle psutil sqlalchemy unidecode
%py_requires psycopg2 multiprocessing
%add_python_req_skip pythoncom win32api win32event win32service
%add_python_req_skip win32serviceutil

%description
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Event driven concurrent framework for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires trollius django setproctitle psutil sqlalchemy unidecode
%py3_requires psycopg2 multiprocessing asyncio
%add_python3_req_skip pythoncom win32api win32event win32service
%add_python3_req_skip win32serviceutil

%description -n python3-module-%oname
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Event driven concurrent framework for python. With pulsar you can write
asynchronous servers performing one or several activities in different
threads and/or processes.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%add_optflags -fno-strict-aliasing
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

%make -C docs pickle
%make -C docs html

cp -fR ../docs/pulsar/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc ../docs/pulsar/html examples

%files tests
%python_sitelibdir/*/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20141118
- Initial build for Sisyphus

