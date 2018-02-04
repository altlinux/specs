%define oname skosprovider

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20141218.1.1.1
Summary: Abstraction layer for SKOS vocabularies
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/skosprovider.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-language-tags
#BuildPreReq: python-module-pytest-cov
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-language-tags
#BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires language_tags

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-coverage python3-module-pytest python3-module-setuptools python3-module-six
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-language-tags python-module-nose python-module-objects.inv python-module-pytest-cov python-module-setuptools python3-module-language-tags python3-module-nose python3-module-pytest-cov python3-module-setuptools rpm-build-python3 time

%description
This library helps abstract vocabularies (thesauri, controlled lists,
authority files). It depends heavily on the SKOS specification, but adds
elements of other specifications such as the ISO 25964 SKOS extension
where deemed useful.

%package -n python3-module-%oname
Summary: Abstraction layer for SKOS vocabularies
Group: Development/Python3
%py3_provides %oname
%py3_requires language_tags

%description -n python3-module-%oname
This library helps abstract vocabularies (thesauri, controlled lists,
authority files). It depends heavily on the SKOS specification, but adds
elements of other specifications such as the ISO 25964 SKOS extension
where deemed useful.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This library helps abstract vocabularies (thesauri, controlled lists,
authority files). It depends heavily on the SKOS specification, but adds
elements of other specifications such as the ISO 25964 SKOS extension
where deemed useful.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This library helps abstract vocabularies (thesauri, controlled lists,
authority files). It depends heavily on the SKOS specification, but adds
elements of other specifications such as the ISO 25964 SKOS extension
where deemed useful.

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.git20141218.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141218
- Initial build for Sisyphus

