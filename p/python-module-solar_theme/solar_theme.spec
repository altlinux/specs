%define oname solar_theme

%def_with python3

Name: python-module-%oname
Version: 1.3.2
Release: alt1.git20140312.1.1.1
Summary: Theme for Python Sphinx
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/solar-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/biotechcoder/solar-theme.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-sphinx-devel
%endif

%py_provides %oname
%py_requires sphinx

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-html5lib python3-module-nose python3-module-setuptools python3-module-sphinx rpm-build-python3 time

%description
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

%if_with python3
%package -n python3-module-%oname
Summary: Theme for Python Sphinx
Group: Development/Python3
%py3_provides %oname
%py3_requires sphinx

%description -n python3-module-%oname
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains documentation for %oname.

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

%make docs
%make -C docs pickle

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.git20140312.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.git20140312.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1.git20140312.1
- NMU: Use buildreq for BR.

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20140312
- Initial build for Sisyphus

