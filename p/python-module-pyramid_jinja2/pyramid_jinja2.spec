%define oname pyramid_jinja2

%def_with python3

Name: python-module-%oname
Version: 2.3.3
Release: alt1
Summary: Jinja2 template bindings for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-pyramid python-module-zope.deprecation
BuildPreReq: python-module-zope.component python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid

%description
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

%package -n python3-module-%oname
Summary: Jinja2 template bindings for the Pyramid web framework
Group: Development/Python3
%py3_requires pyramid

%description -n python3-module-%oname
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_jinja2
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires webtest

%description -n python3-module-%oname-tests
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

This package contains tests for pyramid_jinja2.

%package tests
Summary: Tests for pyramid_jinja2
Group: Development/Python
Requires: %name = %version-%release
%py_requires webtest

%description tests
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

This package contains tests for pyramid_jinja2.

%package pickles
Summary: Pickles for pyramid_jinja2
Group: Development/Python

%description pickles
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

This package contains pickles for pyramid_jinja2.

%package docs
Summary: Documentation for pyramid_jinja2
Group: Development/Documentation

%description docs
These are bindings for the Jinja2 templating system for the Pyramid web
framework.

This package contains documentation for pyramid_jinja2.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests*
%exclude %python_sitelibdir/*/demo
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/*/tests*
%python_sitelibdir/*/demo

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/*/tests*
%exclude %python3_sitelibdir/*/demo

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/*/tests*
%python3_sitelibdir/*/demo
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Version 1.6

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

