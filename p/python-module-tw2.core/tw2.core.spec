%define mname tw2
%define oname %mname.core

%def_with python3

Name: python-module-%oname
Version: 2.2.2
Release: alt1.git20140726
Summary: The runtime components for ToscaWidgets 2, a web widget toolkit
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.core.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-genshi python-module-mako
BuildPreReq: python-module-jinja2 python-module-chameleon.core
BuildPreReq: python-module-webob python-module-PasteDeploy
BuildPreReq: python-module-speaklater python-module-decorator
BuildPreReq: python-module-markupsafe python-module-six
BuildPreReq: python-module-nose python-module-sieve
BuildPreReq: python-module-coverage python-module-FormEncode
BuildPreReq: python-module-webtest
BuildPreReq: python-modules-multiprocessing python-modules-json
BuildPreReq: python-modules-logging python3-module-mako
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-genshi python3-module-mako
BuildPreReq: python3-module-jinja2 python3-module-chameleon.core
BuildPreReq: python3-module-webob python3-module-PasteDeploy
BuildPreReq: python3-module-speaklater python3-module-decorator
BuildPreReq: python3-module-markupsafe python3-module-six
BuildPreReq: python3-module-nose python3-module-sieve
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires json logging genshi mako jinja2 chameleon webob speaklater
%py_requires paste.deploy decorator markupsafe six

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose sieve coverage webtest formencode

%description tests
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: The runtime components for ToscaWidgets 2, a web widget toolkit
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires json logging genshi mako jinja2 chameleon webob speaklater
%py3_requires paste.deploy decorator markupsafe six

%description -n python3-module-%oname
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose sieve coverage webtest formencode

%description -n python3-module-%oname-tests
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the
web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.git20140726
- Initial build for Sisyphus

