%define oname jsonrpcclient

%def_with python3
%def_without python2

Name: python-module-%oname
Version: 2.5.2
Release: alt1.1
Summary: JSON-RPC 2.0 client library for Python 3
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonrpcclient/

Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-requests python-module-jsonschema
BuildRequires: python-module-nose python-module-rednose
BuildRequires: python-module-nose-cov python-module-responses
BuildRequires: python-module-cov-core python-module-coverage
BuildRequires: python2.7(future) python2.7(testfixtures) python2.7(zmq) python2.7(tornado)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-requests python3-module-jsonschema
BuildRequires: python3-module-nose python3-module-rednose
BuildRequires: python3-module-nose-cov python3-module-responses
BuildRequires: python3-module-cov-core python3-module-coverage
BuildRequires: python3(future) python3(testfixtures) python3(zmq) python3(tornado)
%endif

%py_provides %oname

%description
JSON-RPC 2.0 client library for Python 3.

%if_with python3
%package -n python3-module-%oname
Summary: JSON-RPC 2.0 client library for Python 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JSON-RPC 2.0 client library for Python 3.
%endif

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
python setup.py build_ext -i
rm -fR build
PYTHONPATH=%buildroot%python_sitelibdir py.test
%endif
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
rm -fR build
PYTHONPATH=%buildroot%python3_sitelibdir py.test3
popd
%endif

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.2-alt1
- Updated to upstream version 2.5.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 1.1.2-alt2
- Rebuild into Sisyphus

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1
- Version 1.0.12

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Version 1.0.10

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Version 1.0.7

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus

