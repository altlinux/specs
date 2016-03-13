%define oname geoalchemy2

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20140919.1.1
Summary: Geospatial extension to SQLAlchemy with PostGIS support
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/GeoAlchemy2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geoalchemy/geoalchemy2.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy python-module-flake8
#BuildPreReq: python-module-pytest-cov python-module-shapely
#BuildPreReq: python-module-sphinx-devel python-module-psycopg2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy python3-module-flake8
#BuildPreReq: python3-module-pytest-cov python3-module-shapely
#BuildPreReq: python3-module-psycopg2
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-coverage python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-coverage python3-module-mccabe python3-module-pytest python3-module-setuptools python3-pyflakes python3-tools-pep8
BuildRequires: python-module-alabaster python-module-docutils python-module-flake8 python-module-html5lib python-module-objects.inv python-module-psycopg2 python-module-pytest-cov python-module-setuptools-tests python3-module-flake8 python3-module-psycopg2 python3-module-pytest-cov python3-module-setuptools-tests rpm-build-python3 time

%description
GeoAlchemy 2 is a Python toolkit for working with spatial databases. It
is based on the gorgeous SQLAlchemy.

%package -n python3-module-%oname
Summary: Geospatial extension to SQLAlchemy with PostGIS support
Group: Development/Python3
%py3_provides %oname

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20140919.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1.git20140919.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20140919
- Initial build for Sisyphus

