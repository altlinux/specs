%define _unpackaged_files_terminate_build 1
%define oname pytest-flask

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1.1
Summary: A set of py.test fixtures to test Flask applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-flask/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vitalk/pytest-flask.git
Source0: https://pypi.python.org/packages/b4/b5/6d86a2362be78d1d817c7a1d5105100b7b51089dd56ca907d4fed9461570/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-flask python-module-werkzeug
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-flask python3-module-werkzeug
%endif

%py_provides pytest_flask

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-jinja2 python3-module-pytest python3-module-setuptools
BuildRequires: python-module-flask python-module-setuptools python3-module-flask python3-module-setuptools rpm-build-python3
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest

%description
A set of py.test fixtures to test Flask extensions and applications.

Plugin provides some fixtures to simplify app testing:

* client - an instance of app.test_client,
* client_class - client fixture for class-based tests,
* config - you application config,
* accept_json, accept_jsonp, accept_any - accept headers suitable to use
  as parameters in client.

%package -n python3-module-%oname
Summary: A set of py.test fixtures to test Flask applications
Group: Development/Python3
%py3_provides pytest_flask

%description -n python3-module-%oname
A set of py.test fixtures to test Flask extensions and applications.

Plugin provides some fixtures to simplify app testing:

* client - an instance of app.test_client,
* client_class - client fixture for class-based tests,
* config - you application config,
* accept_json, accept_jsonp, accept_any - accept headers suitable to use
  as parameters in client.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO README.rst docs
%python_sitelibdir/*

%if_with python3
%endif
%files -n python3-module-%oname
%doc PKG-INFO README.rst docs
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141124.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141124
- Version 0.6.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141103
- Version 0.5.0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141028
- Initial build for Sisyphus

