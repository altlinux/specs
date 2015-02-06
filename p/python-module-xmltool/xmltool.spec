%define oname xmltool

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.4
Release: alt1.git20150206
Summary: High level python library to manage XML files
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/xmltool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/LeResKP/xmltool.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-lxml python-module-webob
BuildPreReq: python-module-requests python-module-dogpile.cache
BuildPreReq: python-module-nose python-module-BeautifulSoup
BuildPreReq: python-module-strainer python-module-FormEncode
BuildPreReq: python-module-tw2.core python-module-webtest
BuildPreReq: python-module-sieve python-module-mock
BuildPreReq: python-modules-multiprocessing python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-lxml python3-module-webob
BuildPreReq: python3-module-requests python3-module-dogpile.cache
BuildPreReq: python3-module-nose python3-module-BeautifulSoup
BuildPreReq: python3-module-strainer python3-module-FormEncode
BuildPreReq: python3-module-tw2.core python3-module-webtest
BuildPreReq: python3-module-sieve python3-module-mock
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires lxml webob requests dogpile.cache

%description
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: High level python library to manage XML files
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml webob requests dogpile.cache

%description -n python3-module-%oname
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
xmltool is a python package to manipulate XML files. It's very useful to
update some XML files with the python syntax without using the DOM.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150206
- Initial build for Sisyphus

