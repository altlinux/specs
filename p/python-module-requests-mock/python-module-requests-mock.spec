%define oname requests-mock

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.1
Summary: Mock out responses from the requests package
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-mock/

Source: %oname-%version.tar.gz
Patch: requests-mock-alt-fix-urllib3.patch
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pbr python-module-requests
BuildPreReq: python-module-six python-module-coverage
BuildPreReq: python-module-wheel python-module-discover
BuildPreReq: python-module-fixtures python-module-mock
BuildPreReq: python-module-testrepository python-module-testtools
BuildPreReq: python-module-urllib3 python-module-mimeparse
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
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

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version
%patch -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files docs
%doc doc/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- drop pickle package

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141216
- Initial build for Sisyphus

