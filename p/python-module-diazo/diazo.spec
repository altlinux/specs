%define oname diazo
Name: python-module-%oname
Version: 1.1.0
Release: alt1.dev0.git20141002
Summary: Diazo applies a static HTML theme to a dynamic website
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/diazo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/diazo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-repoze.xmliter python-module-lxml
BuildPreReq: python-module-webob python-module-future
BuildPreReq: python-module-unittest2 python-module-six
BuildPreReq: python-module-experimental.cssselect
BuildPreReq: python-module-FormEncode
BuildPreReq: python-module-sphinx-devel

%py_provides %oname
%py_requires repoze.xmliter experimental.cssselect

%description
Diazo implements a Deliverance like language using a pure XSLT engine.
With Diazo, you "compile" your theme and ruleset in one step, then use a
superfast/simple transform on each request thereafter. Alternatively,
compile your theme during development, check it into version control,
and not touch Diazo during deployment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Diazo implements a Deliverance like language using a pure XSLT engine.
With Diazo, you "compile" your theme and ruleset in one step, then use a
superfast/simple transform on each request thereafter. Alternatively,
compile your theme during development, check it into version control,
and not touch Diazo during deployment.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Diazo implements a Deliverance like language using a pure XSLT engine.
With Diazo, you "compile" your theme and ruleset in one step, then use a
superfast/simple transform on each request thereafter. Alternatively,
compile your theme during development, check it into version control,
and not touch Diazo during deployment.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Diazo implements a Deliverance like language using a pure XSLT engine.
With Diazo, you "compile" your theme and ruleset in one step, then use a
superfast/simple transform on each request thereafter. Alternatively,
compile your theme during development, check it into version control,
and not touch Diazo during deployment.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt *.rst docs/*.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files docs
%doc docs/*.pdf docs/_build/html examples

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.dev0.git20141002
- Initial build for Sisyphus

