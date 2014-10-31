%define oname pyramid_layout

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20140829
Summary: Pyramid add-on for facilitating UI layout
License: Repoze Public License
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_layout/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_layout.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-pyramid_zcml
BuildPreReq: python-module-coverage python-module-nose
BuildPreReq: python-module-mock python-module-webtest
BuildPreReq: python-module-PasteDeploy python-module-zope.deprecation
BuildPreReq: python-module-zope.component python-module-repoze.lru
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-pyramid_zcml
BuildPreReq: python3-module-coverage python3-module-nose
BuildPreReq: python3-module-mock python3-module-webtest
BuildPreReq: python3-module-PasteDeploy python3-module-zope.deprecation
BuildPreReq: python3-module-zope.component python3-module-repoze.lru
%endif

%py_provides %oname

%description
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid add-on for facilitating UI layout
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

This package contains pickles for %oname.

%package docs
Summary: Documentaton for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pyramid Layout is an add-on for the Pyramid Web Framework which allows
developers to utilize the concept of a UI layout to your Pyramid
application. Different layouts may be registered for use in different
contexts of your application. The concept of panels is also introduced
to facilitate rendering of subsections of a page in a consistent way
across different views in a reusable way.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
mkdir -p docs/_themes
cp -fR %_datadir/pylons_sphinx_theme/* docs/_themes/

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

export PYTHONPATH=$PWD
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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html demo

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20140829
- Initial build for Sisyphus

