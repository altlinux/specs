# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20150205.1.1.1.1
%define oname doubles

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.5
#Release: alt1.git20150205.1.1
Summary: Test doubles for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/doubles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/uber/doubles.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-coverage python-module-coveralls
#BuildPreReq: python-module-flake8 python-module-pyroma
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-coverage python3-module-coveralls
#BuildPreReq: python3-module-flake8 python3-module-pyroma
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-mccabe python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-sh python3-module-snowballstemmer python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-flake8 python-module-html5lib python-module-nose python-module-objects.inv python-module-pyroma python-module-setuptools python-module-z4r-coveralls python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-pyroma python3-module-setuptools python3-module-sphinx python3-module-z4r-coveralls rpm-build-python3 time

# optimized out: -=FIXES: python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(sphinx_rtd_theme)

%description
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

%package -n python3-module-%oname
Summary: Test doubles for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains documentation for %oname.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

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

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.git20150205.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150205.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150205
- Initial build for Sisyphus

