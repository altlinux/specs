%define oname pytest-cache

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.hg20140304.1.1
Summary: pytest plugin with mechanisms for caching across test runs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/hpk42/pytest-cache
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-py
#BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides pytest_cache
%py_requires execnet

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python3-module-setuptools rpm-build-python3 time

%description
pytest plugin with mechanisms for caching across test runs.

%package -n python3-module-%oname
Summary: pytest plugin with mechanisms for caching across test runs
Group: Development/Python3
%py3_provides pytest_cache
%py3_requires execnet

%description -n python3-module-%oname
pytest plugin with mechanisms for caching across test runs.

%package pickles
Summary: Pickles for %oname
Group: Development/Python 

%description pickles
pytest plugin with mechanisms for caching across test runs.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pytest plugin with mechanisms for caching across test runs.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/
ln -s README.rst README.txt

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.hg20140304.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt1.hg20140304.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20140304
- Initial build for Sisyphus

