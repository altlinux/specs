%define oname requests-mock

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.git20141216.1
Summary: Mock out responses from the requests package
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-mock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stackforge/requests-mock.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pbr python-module-requests
BuildPreReq: python-module-six python-module-coverage
BuildPreReq: python-module-wheel python-module-discover
BuildPreReq: python-module-fixtures python-module-mock
BuildPreReq: python-module-testrepository python-module-testtools
BuildPreReq: python-module-urllib3 python-module-mimeparse
BuildPreReq: python-module-sphinx-devel git
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pbr python3-module-requests
BuildPreReq: python3-module-six python3-module-coverage
BuildPreReq: python3-module-wheel python3-module-discover
BuildPreReq: python3-module-fixtures python3-module-mock
BuildPreReq: python3-module-testrepository python3-module-testtools
BuildPreReq: python3-module-urllib3 python3-module-mimeparse
BuildPreReq: python3-module-sphinx
%endif

%py_provides requests_mock
%py_requires requests six fixtures

%description
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

As the requests library has very limited options for how to load and use
adapters requests-mock also provides a number of ways to make sure the
mock adapter is used. These are only loading mechanisms, they do not
contain any logic and can be used as a reference to load the adapter in
whatever ways works best for your project.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock testtools

%description tests
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Mock out responses from the requests package
Group: Development/Python3
%py3_provides requests_mock
%py3_requires requests six fixtures

%description -n python3-module-%oname
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

As the requests library has very limited options for how to load and use
adapters requests-mock also provides a number of ways to make sure the
mock adapter is used. These are only loading mechanisms, they do not
contain any logic and can be used as a reference to load the adapter in
whatever ways works best for your project.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires mock testtools

%description -n python3-module-%oname-tests
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

This package contains documentation for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

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

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

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
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141216
- Initial build for Sisyphus

