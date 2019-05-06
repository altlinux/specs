%define _unpackaged_files_terminate_build 1
%define oname momoko

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.5.1
Release: alt1
Summary: Wraps (asynchronous) Psycopg2 for Tornado
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Momoko
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/FSX/momoko.git
Source0: %name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-cffi python-module-docutils
BuildRequires: python-module-html5lib python-module-objects.inv
BuildRequires: python-module-psycopg2 python-module-pytest python-module-tornado
BuildRequires: python-module-unittest2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cffi python3-module-psycopg2
BuildRequires: python3-module-pycares python3-module-pytest
BuildRequires: python3-module-unittest2 python3-module-zope time
%endif

%py_provides %oname
%py_requires tornado psycopg2cffi psycopg2

%description
Momoko wraps Psycopg2's functionality for use in Tornado.

%if_with python3
%package -n python3-module-%oname
Summary: Wraps (asynchronous) Psycopg2 for Tornado
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado psycopg2cffi psycopg2

%description -n python3-module-%oname
Momoko wraps Psycopg2's functionality for use in Tornado.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Momoko wraps Psycopg2's functionality for use in Tornado.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
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
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst THANKS examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst THANKS examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.5.1-alt1
- Build new version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.git20150803.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.git20150803.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150803
- Initial build for Sisyphus

