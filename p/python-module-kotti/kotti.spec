%define oname kotti

%def_without python3

Name: python-module-%oname
Version: 1.1
Release: alt2.dev.git20150211
Summary: A user-friendly, light-weight and extensible web content management system
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Kotti
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/Kotti.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel python-module-kotti_docs_theme
BuildPreReq: python-module-repoze.sphinx.autointerface graphviz
BuildPreReq: python-module-zope.sqlalchemy python-module-zope.deprecation
BuildPreReq: python-module-pyramid-tests python-module-zope.component
BuildPreReq: python-module-repoze.lru python-module-pyramid_beaker
BuildPreReq: python-module-fanstatic python-module-shutilwhich
BuildPreReq: python-module-js.angular python-module-js.bootstrap
BuildPreReq: python-module-js.html5shiv python-module-js.fineuploader
BuildPreReq: python-module-js.jquery_form python-module-js.jquery_tablednd
BuildPreReq: python-module-js.jqueryui python-module-js.jqueryui_tagit
BuildPreReq: python-module-alembic python-module-docopt
BuildPreReq: python-module-PasteDeploy python-module-bcrypt
BuildPreReq: python-module-repoze.workflow python-module-colander
BuildPreReq: python-module-deform python-module-pyramid_deform
BuildPreReq: python-module-html2text python-module-pyramid_mailer
BuildPreReq: python-module-FormEncode python-module-Pillow
BuildPreReq: python-module-plone.scale python-module-waitress
BuildPreReq: python-module-unidecode python-module-pyramid_zcml
BuildPreReq: python-module-pyramid_tm python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-bcrypt
BuildPreReq: python-module-lingua python-module-kotti_tinymce
BuildPreReq: python-module-js.jquery_timepicker_addon
BuildPreReq: python-module-js.deform python-module-pyramid_mako
BuildPreReq: python-module-polib python-module-zope.testbrowser
BuildPreReq: python-module-wsgi_intercept python-module-pytest-xdist
BuildPreReq: python-module-pytest-pep8 python-module-pytest-cov
BuildPreReq: python-module-pyquery python-module-mock
BuildPreReq: python-module-webtest python-module-mechanize
BuildPreReq: python-module-usersettings python-module-virtualenv
BuildPreReq: python-module-filedepot
BuildPreReq: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires shutilwhich repoze.lru pyramid_beaker js.angular filedepot
%py_requires js.bootstrap js.html5shiv js.fineuploader js.jquery_form
%py_requires js.jquery_tablednd js.jqueryui js.jqueryui_tagit waitress
%py_requires paste.deploy repoze.workflow pyramid_deform html2text
%py_requires pyramid_mailer formencode PIL plone.scale zope.sqlalchemy
%py_requires js.jquery_timepicker_addon js.deform usersettings
%py_requires pyramid_zcml pyramid_tm pyramid_debugtoolbar kotti_tinymce
%py_requires pyramid_chameleon pyramid_mako wsgi_intercept

%description
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testbrowser pytest_pep8 pytest_cov pyquery mock
%py_requires webtest mechanize xdist pyramid.tests

%description tests
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A user-friendly, light-weight and extensible web content management syste
Group: Development/Python3
%py3_provides %oname
%py3_requires shutilwhich repoze.lru pyramid_beaker js.angular
%py3_requires js.bootstrap js.html5shiv js.fineuploader js.jquery_form
%py3_requires js.jquery_tablednd js.jqueryui js.jqueryui_tagit
%py3_requires paste.deploy repoze.workflow pyramid_deform
%py3_requires pyramid_mailer formencode PIL
%py3_requires js.jquery_timepicker_addon js.deform

%description -n python3-module-%oname
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testbrowser pytest_pep8 pytest_cov pyquery mock
%py3_requires webtest mechanize xdist

%description -n python3-module-%oname-tests
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A user-friendly, light-weight and extensible web content management
system, based on Pyramid and SQLAlchemy.

Kotti is most useful when you are developing applications that

* have complex security requirements,
* use workflows, and/or
* work with hierarchical data.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.dev.git20150211
- Added necessary requirements

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20150211
- New snapshot

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20150113
- Version 1.1-dev

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.b2dev.git20140930
- Initial build for Sisyphus

