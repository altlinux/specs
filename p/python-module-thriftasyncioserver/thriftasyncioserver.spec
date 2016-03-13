%define oname thriftasyncioserver

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.7
Release: alt1.git20141214.1
Summary: Thrift Server using the Python 3 asyncio module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/thriftasyncioserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Marketcircle/thriftasyncioserver.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-thrift
BuildPreReq: python-module-wheel python-module-six
BuildPreReq: python-module-flake8
%endif
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-thrift
BuildPreReq: python3-module-wheel python3-module-six
BuildPreReq: python3-module-flake8
%endif

%py_provides %oname
%py_requires asyncio thrift

%description
Server for Apache Thrift using the Python 3 asyncio module.

%package -n python3-module-%oname
Summary: Thrift Server using the Python 3 asyncio module
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio thrift

%description -n python3-module-%oname
Server for Apache Thrift using the Python 3 asyncio module.

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

%make docs

%check
%if_with python2
python setup.py test
flake8 thriftasyncioserver tests
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3-flake8 thriftasyncioserver tests
popd
%endif

%if_with python2
%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.7-alt1.git20141214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.git20141214
- Initial build for Sisyphus

