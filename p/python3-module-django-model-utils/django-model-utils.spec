%define _unpackaged_files_terminate_build 1
%define oname django-model-utils

Name: python3-module-%oname
Version: 4.0.0
Release: alt1

Summary: Django model mixins and utilities
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-model-utils/
BuildArch: noarch

# https://github.com/carljm/django-model-utils.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
Django model mixins and utilities.

django-model-utils supports Django 1.4.10 and later on Python 2.6, 2.7,
3.2, 3.3 and 3.4.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django model mixins and utilities.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Django model mixins and utilities.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Django model mixins and utilities.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

mv tests/ %buildroot%python3_sitelibdir/%oname/

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0.0-alt1
- Version updated to 4.0.0
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3-alt1.a1.git20140922.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3-alt1.a1.git20140922.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3-alt1.a1.git20140922.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.a1.git20140922
- Initial build for Sisyphus

