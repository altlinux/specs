%define oname ska

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt1.git20140607.1.1.1
Summary: Sign- and validate- data (dictionaries, strings) using symmetric-key algorithm
License: GPLv2.0/LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ska/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/barseghyanartur/ska.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-six python-module-django-tests
#BuildPreReq: python-module-radar
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-six python3-module-django-tests
#BuildPreReq: python3-module-radar
%endif

%py_provides %oname
%py_requires six django

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python-module-objects.inv python-module-radar python-module-setuptools python3-module-django python3-module-setuptools python3-module-six rpm-build-python3 time

%description
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires django.test

%description tests
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Sign- and validate- data (dictionaries, strings) using symmetric-key algorithm
Group: Development/Python3
%py3_provides %oname
%py3_requires six django

%description -n python3-module-%oname
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires django.test

%description -n python3-module-%oname-tests
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	../python3/src/ska/bin/*
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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD/src
python setup.py test
./test.sh
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test
sed -i 's|python|python3|' test.sh
./test.sh
popd
%endif

%files
%doc *.rst example
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/tests.*
%python_sitelibdir/*/*/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/*/tests.fpickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5-alt1.git20140607.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20140607.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20140607.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140607
- Initial build for Sisyphus

