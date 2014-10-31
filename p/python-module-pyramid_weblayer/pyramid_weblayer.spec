%define oname pyramid_weblayer

%def_with python3

Name: python-module-%oname
Version: 0.13
Release: alt1.git20141028
Summary: Common / reusable utilities for a Pyramid web application
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_weblayer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thruflo/pyramid_weblayer.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-html2text python-module-markdown2
BuildPreReq: python-module-pyga python-module-pyramid-tests
BuildPreReq: python-module-pyramid_basemodel python-module-pyramid_hsts
BuildPreReq: python-module-pyramid_layout python-module-transaction
BuildPreReq: python-module-zope.interface python-module-coverage
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-webtest python-module-inflect
BuildPreReq: python-module-pyramid_tm
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-html2text python3-module-markdown2
BuildPreReq: python3-module-pyga python3-module-pyramid-tests
BuildPreReq: python3-module-pyramid_basemodel python3-module-pyramid_hsts
BuildPreReq: python3-module-pyramid_layout python3-module-transaction
BuildPreReq: python3-module-zope.interface python3-module-coverage
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-webtest python3-module-inflect
BuildPreReq: python3-module-pyramid_tm python-tools-2to3
%endif

%py_provides %oname
%py_requires zope.interface

%description
Common / shared utilities for a Pyramid web application. (Some
originally re-factored from the depreciated weblayer micro-framework).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Common / shared utilities for a Pyramid web application. (Some
originally re-factored from the depreciated weblayer micro-framework).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Common / reusable utilities for a Pyramid web application
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface

%description -n python3-module-%oname
Common / shared utilities for a Pyramid web application. (Some
originally re-factored from the depreciated weblayer micro-framework).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Common / shared utilities for a Pyramid web application. (Some
originally re-factored from the depreciated weblayer micro-framework).

This package contains tests for %oname.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md UNLICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md UNLICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20141028
- Initial build for Sisyphus

