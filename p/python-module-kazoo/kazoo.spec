%define oname kazoo

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20141002
Summary: Higher Level Zookeeper Client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/kazoo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-zk/kazoo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-nose python-module-gevent
BuildPreReq: python-module-greenlet python-module-jinja2
BuildPreReq: python-module-Pygments python-module-docutils
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-mock
BuildPreReq: python3-module-nose python3-module-gevent
BuildPreReq: python3-module-greenlet python3-module-jinja2
BuildPreReq: python3-module-Pygments python3-module-docutils
%endif

%py_provides %oname

%description
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Higher Level Zookeeper Client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This packag contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
kazoo implements a higher level API to Apache Zookeeper for Python
clients.

This packag contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20141002
- Initial build for Sisyphus

