%define mname svg
%define oname %mname.charts

%def_with python3

Name: python-module-%oname
Version: 3.0
Release: alt2.1.1
Summary: Python SVG Charting Library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/svg.charts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-cssutils python-module-dateutil
BuildPreReq: python-module-lxml python-module-six
BuildPreReq: python-module-pytest-runner python-module-setuptools_scm
BuildPreReq: python-module-sphinx-devel
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-cssutils python3-module-dateutil
BuildPreReq: python3-module-lxml python3-module-six
BuildPreReq: python3-module-pytest-runner python3-module-setuptools_scm
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires cssutils dateutil lxml six

%description
svg.charts is a pure-python library for generating charts and graphs in
SVG, originally based on the SVG::Graph Ruby package by Sean E. Russel.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
svg.charts is a pure-python library for generating charts and graphs in
SVG, originally based on the SVG::Graph Ruby package by Sean E. Russel.

This package contains pickles for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%if_with python3
%package -n python3-module-%oname
Summary: Python SVG Charting Library
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires cssutils dateutil lxml six

%description -n python3-module-%oname
svg.charts is a pure-python library for generating charts and graphs in
SVG, originally based on the SVG::Graph Ruby package by Sean E. Russel.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.
%endif

%prep
%setup

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -f conf.py
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt docs/_build/html
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/_build/html
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt2.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 3.0-alt2
- Fixed build by removing mercurial version check.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

