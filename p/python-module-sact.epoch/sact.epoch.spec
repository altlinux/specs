%define mname sact
%define oname %mname.epoch

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1
Summary: Time object subclassing datetime allowing diverting local clock mecanism
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sact.epoch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dateutil python-module-zope.interface
BuildPreReq: python-module-zope.component python-module-pytz
BuildPreReq: python-module-zope.testing python-module-zope.testrunner
BuildPreReq: python-module-z3c.testsetup python-module-nose
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dateutil python3-module-zope.interface
BuildPreReq: python3-module-zope.component python3-module-pytz
BuildPreReq: python3-module-zope.testing python3-module-zope.testrunner
BuildPreReq: python3-module-z3c.testsetup python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires dateutil zope.interface zope.component pytz

%description
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This allows clock-dependent code to be tested. Additionnaly, as an
abstraction of the legacy datetime object, Time object provided in
sact.epoch.Time provides some common helpers and force this object to
always provide a timezone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner z3c.testsetup

%description tests
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Time object subclassing datetime allowing diverting local clock mecanism
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires dateutil zope.interface zope.component pytz

%description -n python3-module-%oname
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This allows clock-dependent code to be tested. Additionnaly, as an
abstraction of the legacy datetime object, Time object provided in
sact.epoch.Time provides some common helpers and force this object to
always provide a timezone.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing zope.testrunner z3c.testsetup

%description -n python3-module-%oname-tests
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This packages provides a time abstraction mecanism, allowing code that
would use it as reference to be diverted both on the local time zone and
the real time.

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
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 src/%mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d _build/doctrees source _build/pickle
sphinx-build -b html -d _build/doctrees source _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

