%define oname geoalchemy2

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.1
Summary: Geospatial extension to SQLAlchemy with PostGIS support
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/GeoAlchemy2/

# https://github.com/geoalchemy/geoalchemy2.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
Patch2: 146.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-mock
BuildRequires: python-module-flake8 python-module-psycopg2 python-module-pytest-cov python-module-setuptools
BuildRequires: python-module-SQLAlchemy python-module-shapely
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8 python3-module-psycopg2 python3-module-pytest-cov python3-module-setuptools
BuildRequires: python3-module-SQLAlchemy python3-module-shapely
%endif

%description
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

%package -n python3-module-%oname
Summary: Geospatial extension to SQLAlchemy with PostGIS support
Group: Development/Python3

%description -n python3-module-%oname
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
PYTHONPATH=%buildroot%python_sitelibdir py.test ||:
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 ||:
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt1
- Updated to upstream version 0.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20140919.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.git20140919.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140919
- Initial build for Sisyphus

