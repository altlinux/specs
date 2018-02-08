%define oname kitchen

%def_with python3

Name: python-module-%oname
Version: 1.2.1
Release: alt1.git20141202.1.1.1
Summary: Cornucopia of useful code
License: LGPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/kitchen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fedora-infra/kitchen.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-sphinx-devel python3-module-nose
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-setuptools python3-module-html5lib python3-module-jinja2-tests python3-module-nose python3-module-setuptools python3-module-sphinx rpm-build-python3 time

%description
Kitchen contains a cornucopia of useful code.

%package -n python3-module-%oname
Summary: Cornucopia of useful code
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Kitchen contains a cornucopia of useful code.

%package -n python3-module-%oname-docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%oname-docs
Kitchen contains a cornucopia of useful code.

This package contains documentation for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Kitchen contains a cornucopia of useful code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Kitchen contains a cornucopia of useful code.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx %{oname}2
ln -s ../objects.inv %{oname}2/docs/

%if_with python3
%prepare_sphinx %{oname}3
ln -s ../objects.inv %{oname}3/docs/
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

pushd %{oname}2/docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd
%if_with python3
pushd %{oname}3/docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd
%endif

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
%doc %{oname}2/docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1.git20141202.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1.git20141202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.git20141202.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141202
- Initial build for Sisyphus

