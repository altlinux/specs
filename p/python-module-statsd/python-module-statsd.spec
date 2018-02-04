%define oname statsd

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 3.2.1
Release: alt1.1
Summary: A simple statsd client
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/statsd/
Source: %oname-%version.tar.gz
Patch: statsd-fix-sphinx.patch

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-flake8
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-flake8
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx

%description
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A simple statsd client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

This package contains pickles for %oname.

%prep
%setup -n %oname-%version
%patch -p1

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
%doc AUTHORS CHANGES *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141105
- Initial build for Sisyphus

