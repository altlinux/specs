%define oname skosprovider

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20141218
Summary: Abstraction layer for SKOS vocabularies
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/skosprovider.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-language-tags
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-language-tags
BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires language_tags

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
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141218
- Initial build for Sisyphus

