%define oname asynqp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20141203
Summary: An AMQP library for asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/asynqp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/benjamin-hodgson/asynqp.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio-tests python-module-contexts
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio-tests python3-module-contexts
%endif

%py_provides %oname
%py_requires asyncio

%description
asynqp is an AMQP (aka RabbitMQ) client library for Python 3.x's new
asyncio module.

%package -n python3-module-%oname
Summary: An AMQP library for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
asynqp is an AMQP (aka RabbitMQ) client library for Python 3.x's new
asyncio module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
%if_with python2
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
py.test test/*.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version test/*.py
popd
%endif

%if_with python2
%files
%doc *.md RELEASING TODO doc/*.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md RELEASING TODO doc/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141203
- Initial build for Sisyphus

