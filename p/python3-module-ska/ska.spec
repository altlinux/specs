%define oname ska

Name: python3-module-%oname
Version: 1.5
Release: alt3

Summary: Sign- and validate- data (dictionaries, strings) using symmetric-key algorithm
License: GPLv2.0/LGPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/ska/
# https://github.com/barseghyanartur/ska.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-sphinx
BuildRequires: python3-module-six

%py3_provides %oname
%py3_requires six django


%description
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires django.test

%description tests
Lets you easily sign data, using symmetric-key algorithm encryption.
Allows you to validate signed data and identify possible validation
errors. Uses sha1/hmac for signature encryption. Comes with shortcut
functions for signing (and validating) dictionaries and URLs.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	./src/ska/bin/*

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD/src
python3 setup.py test
sed -i 's|python|python3|' test.sh
./test.sh

%files
%doc *.rst example
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.fpickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt3
- drop unneeded BR: rpm-macros-sphinx

* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5-alt1.git20140607.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20140607.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20140607.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140607
- Initial build for Sisyphus

