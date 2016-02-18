%define oname django-analytics

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20110815.1
Summary: Django app facilitating tracking of arbitrary simple metrics
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-analytics/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-analytics.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-geckoboard
#BuildPreReq: python-module-django-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-geckoboard
#BuildPreReq: python3-module-django-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides analytics

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-psycopg2 python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-django python-module-setuptools-tests python3-module-django python3-module-setuptools-tests rpm-build-python3 time

%description
A basic Django app facilitating tracking of certain elementary metrics
and statistics - generally just metrics which can be measured in terms
of counts and cumulative counts.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A basic Django app facilitating tracking of certain elementary metrics
and statistics - generally just metrics which can be measured in terms
of counts and cumulative counts.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django app facilitating tracking of arbitrary simple metrics
Group: Development/Python3
%py3_provides analytics

%description -n python3-module-%oname
A basic Django app facilitating tracking of certain elementary metrics
and statistics - generally just metrics which can be measured in terms
of counts and cumulative counts.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A basic Django app facilitating tracking of certain elementary metrics
and statistics - generally just metrics which can be measured in terms
of counts and cumulative counts.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%check
python setup.py test
python runtests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20110815.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20110815
- Initial build for Sisyphus

