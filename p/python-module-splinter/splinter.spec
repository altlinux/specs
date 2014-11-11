%define oname splinter

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20141109
Summary: splinter - python test framework for web applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/splinter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cobrateam/splinter.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-selenium python-module-zope.testbrowser
BuildPreReq: python-module-lxml python-module-cssselect
BuildPreReq: python-module-django python-module-flask
BuildPreReq: python-module-coverage python-module-argparse
BuildPreReq: python-module-mechanize
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-selenium python3-module-zope.testbrowser
BuildPreReq: python3-module-lxml python3-module-cssselect
BuildPreReq: python3-module-django python3-module-flask
BuildPreReq: python3-module-coverage python3-module-argparse
BuildPreReq: python3-module-mechanize
%endif

%py_provides %oname
%py_requires zope.testbrowser mechanize

%description
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

%package -n python3-module-%oname
Summary: splinter - python test framework for web applications
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.testbrowser mechanize

%description -n python3-module-%oname
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
splinter is a tool for test web applications with a simple for find
elements, form actions, and others browser actions.

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
%doc AUTHORS *.rst samples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst samples
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20141109
- Initial build for Sisyphus

