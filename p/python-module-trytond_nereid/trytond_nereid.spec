%define oname trytond_nereid
Name: python-module-%oname
Version: 3.2.0.5
Release: alt2.git20141013
Summary: Tryton base module for Nereid
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/trytond_nereid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/openlabs/nereid.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-pytz
BuildPreReq: python-module-flask python-module-flask-wtf
BuildPreReq: python-module-babel python-module-blinker
BuildPreReq: python-module-speaklater python-module-flask-babel
BuildPreReq: python-module-flask-login python-module-mock
BuildPreReq: python-module-pycountry python-module-flake8
BuildPreReq: python-module-coverage python-module-tox
BuildPreReq: python-module-flake8
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel flask-sphinx-themes
BuildPreReq: python-module-trytond-tests
#BuildPreReq: python-module-trytond_nereid_test

%py_provides %oname
%py_requires trytond

%description
Nereid is a web framework built over Flask, with Tryton as an ORM.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Nereid is a web framework built over Flask, with Tryton as an ORM.

This package contains tests for %oname.

%description tests
Nereid is a web framework built over Flask, with Tryton as an ORM.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Nereid is a web framework built over Flask, with Tryton as an ORM.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Nereid is a web framework built over Flask, with Tryton as an ORM.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/flask-sphinx-themes/* docs/_themes/

%build
%python_build_debug

%install
%python_install

#export PYTHONPATH=$PWD
#make -C docs pickle
#make -C docs html

#install -d %buildroot%python_sitelibdir/%oname
#cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG COPYRIGHT MIGRATION *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

#files pickles
#python_sitelibdir/*/pickle

#files docs
#doc docs/_build/html/*

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0.5-alt2.git20141013
- Don't requires distribute

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0.5-alt1.git20141013
- Initial build for Sisyphus

