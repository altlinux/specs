%define version 1.0.2
%define release alt2
%define oname south
%setup_python_module %oname
%add_python_req_skip cx_Oracle
%add_python_req_skip django.db.backends.creation
%add_python3_req_skip django.db.backends.creation

%def_with python3
%def_disable tests

Name: python-module-%oname
Version: %version
Release: alt2.1
BuildArch: noarch

Summary: Migrations for Django
License: Apache
Group: Development/Python
Url: http://south.aeracode.org

# Source: http://www.aeracode.org/releases/south/%modulename-%version.tar.gz
# https://bitbucket.org/andrewgodwin/south/overview
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: time python-module-alabaster python-module-django python-module-docutils python-module-html5lib
BuildRequires: python-module-objects.inv python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django python3-module-setuptools
%endif

%description
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Migrations for Django
Group: Development/Python3
%add_python3_req_skip cx_Oracle

%description -n python3-module-%oname
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%if_enabled tests
%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
%endif

%files
%doc AUTHORS README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4
- Added module for Python 3

* Thu Feb 28 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.3-alt1.1
- Rebuild with Python-2.7

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Wed Apr 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7

* Mon Mar 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- initial build
