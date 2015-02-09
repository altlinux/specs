%define oname pybars3

%def_with python3

Name: python-module-%oname
Version: 0.7.2
Release: alt1.git20150123
Summary: Handlebars.js templating for Python 3 and 2
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pybars3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wbond/pybars3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pymeta3 python-module-fixtures
BuildPreReq: python-module-testtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pymeta3 python3-module-fixtures
BuildPreReq: python3-module-testtools
%endif

%py_provides %oname pybars
%py_requires pymeta3

%description
Handlebars.js template support for Python 3 and 2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Handlebars.js template support for Python 3 and 2.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Handlebars.js templating for Python 3 and 2
Group: Development/Python3
%py3_provides %oname pybars
%py3_requires pymeta3

%description -n python3-module-%oname
Handlebars.js template support for Python 3 and 2.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Handlebars.js template support for Python 3 and 2.

This package contains tests for %oname.

%prep
%setup

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
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc NEWS *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc NEWS *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150123
- Initial build for Sisyphus

