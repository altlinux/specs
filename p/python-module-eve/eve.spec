%define oname eve

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.7.5
Release: alt1.1
Summary: REST API framework powered by Flask, MongoDB and good intentions
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/Eve/

# https://github.com/nicolaiarocci/eve.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-cerberus python-module-events
BuildRequires: python-module-pytest
BuildRequires: python-module-flask-pymongo
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv
BuildRequires: python-module-sphinxcontrib-embedly
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-cerberus python3-module-events
BuildRequires: python3-module-pytest
BuildRequires: python3-module-flask-pymongo
%endif

%py_provides %oname
%py_requires flask_pymongo

%description
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: REST API framework powered by Flask, MongoDB and good intentions
Group: Development/Python3
%py3_provides %oname
%py3_requires flask_pymongo

%description -n python3-module-%oname
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Powered by Flask, MongoDB, Redis and good intentions Eve allows to
effortlessly build and deploy highly customizable, fully featured
RESTful Web Services.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

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

cp -fR ~/code/eve.docs/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc ~/code/eve.docs/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.5-alt1
- Updated to upstream version 0.7.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150112.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150112
- Version 0.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140620
- Initial build for Sisyphus

