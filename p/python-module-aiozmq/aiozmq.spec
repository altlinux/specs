%define oname aiozmq

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1.git20150102
Summary: ZeroMQ integration with asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiozmq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiozmq.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio-tests python-module-msgpack
BuildPreReq: python-tools-pep8 pyflakes python-module-zmq
BuildPreReq: python-module-wheel python-module-coverage
BuildPreReq: python-module-elpy python-module-jedi ipython
BuildPreReq: python-module-rope_py3k python-module-ipdb
%endif
BuildPreReq: python-module-sphinx-devel /dev/pts
BuildPreReq: python-module-sphinxcontrib-spelling
BuildPreReq: python-module-readthedocs-sphinx-ext
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio-tests python3-module-msgpack
BuildPreReq: python3-tools-pep8 python3-pyflakes python3-module-zmq
BuildPreReq: python3-module-wheel python3-module-coverage
BuildPreReq: python3-module-elpy python3-module-jedi
BuildPreReq: python3-module-rope_py3k python3-module-ipdb
%endif

%py_provides %oname
%py_requires asyncio msgpack zmq

%description
asyncio (PEP 3156) support for ZeroMQ.

%package -n python3-module-%oname
Summary: ZeroMQ integration with asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio msgpack zmq

%description -n python3-module-%oname
asyncio (PEP 3156) support for ZeroMQ.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
asyncio (PEP 3156) support for ZeroMQ.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
asyncio (PEP 3156) support for ZeroMQ.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
%if_with python2
python setup.py test
python runtests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py -v
popd
%endif

%if_with python2
%files
%doc ACKS.txt CHANGES.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc ACKS.txt CHANGES.txt *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20150102
- Initial build for Sisyphus

