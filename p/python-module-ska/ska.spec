%define oname ska

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt1.git20140607
Summary: Sign- and validate- data (dictionaries, strings) using symmetric-key algorithm
License: GPLv2.0/LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ska/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/barseghyanartur/ska.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-django-tests
BuildPreReq: python-module-radar
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-django-tests
BuildPreReq: python3-module-radar
%endif

%py_provides %oname
%py_requires six django

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
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140607
- Initial build for Sisyphus

