%define mname unicore.hub
%define oname %mname.client

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20150319
Summary: Client library to interact with Universal Core's unicore.hub
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unicore.hub.client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore.hub.client.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-requests
BuildPreReq: python-module-responses python-module-six
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-modules-wsgiref
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-requests
BuildPreReq: python3-module-responses python3-module-six
BuildPreReq: python3-module-pytest-cov
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname requests responses six wsgiref

%description
Client library to interact with Universal Core's unicore.hub.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Client library to interact with Universal Core's unicore.hub.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Client library to interact with Universal Core's unicore.hub
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname requests responses six wsgiref

%description -n python3-module-%oname
Client library to interact with Universal Core's unicore.hub.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Client library to interact with Universal Core's unicore.hub.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
py.test --verbose --cov ./unicore/hub unicore/hub
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version --verbose --cov ./unicore/hub unicore/hub
popd
%endif

%files
%doc *.rst
%python_sitelibdir/unicore/hub/client
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/unicore/hub/client/tests

%files tests
%python_sitelibdir/unicore/hub/client/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/unicore/hub/client
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/unicore/hub/client/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/unicore/hub/client/tests
%endif

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150319
- Initial build for Sisyphus

