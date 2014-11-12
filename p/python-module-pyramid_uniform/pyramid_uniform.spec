%define oname pyramid_uniform

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20141108
Summary: Form handling for Pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_uniform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cartlogic/pyramid_uniform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-FormEncode
BuildPreReq: python-module-webhelpers2 python-module-six
BuildPreReq: python-module-coverage python-module-nose
BuildPreReq: python-module-nose-cover3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-FormEncode
BuildPreReq: python3-module-webhelpers2 python3-module-six
BuildPreReq: python3-module-coverage python3-module-nose
BuildPreReq: python3-module-nose-cover3
%endif

%py_provides %oname

%description
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Form handling for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Form rendering and validation for Pyramid. Doesn't render HTML itself,
so you have full control over form markup.

Heavily inspired by the pyramid_simpleform package, with some fixes and
updates to work with WebHelpers2 and Python 3.

This package contains documentation for %oname.

%prep
%setup

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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES *.rst
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
%doc CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141108
- Initial build for Sisyphus

