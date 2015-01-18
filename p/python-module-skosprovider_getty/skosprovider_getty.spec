%define oname skosprovider_getty

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141223
Summary: Skosprovider implementation of the Getty Vocabularies
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider_getty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OnroerendErfgoed/skosprovider_getty.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-skosprovider python-module-requests
BuildPreReq: python-module-rdflib python-module-nose
BuildPreReq: python-module-tox python-module-pytest-cov
BuildPreReq: python-module-SPARQLWrapper
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-skosprovider python3-module-requests
BuildPreReq: python3-module-rdflib python3-module-nose
BuildPreReq: python3-module-tox python3-module-pytest-cov
BuildPreReq: python3-module-SPARQLWrapper
%endif

%py_provides %oname
%py_requires skosprovider requests rdflib

%description
Skosprovider implementation of the Getty Vocabularies.

Supported Getty thesauri:

* Art & Architecture Thesaurus (AAT)
* The Getty Thesaurus of Geographic Names (TGN)

%package -n python3-module-%oname
Summary: Skosprovider implementation of the Getty Vocabularies
Group: Development/Python3
%py3_provides %oname
%py3_requires skosprovider requests rdflib

%description -n python3-module-%oname
Skosprovider implementation of the Getty Vocabularies.

Supported Getty thesauri:

* Art & Architecture Thesaurus (AAT)
* The Getty Thesaurus of Geographic Names (TGN)

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Skosprovider implementation of the Getty Vocabularies.

Supported Getty thesauri:

* Art & Architecture Thesaurus (AAT)
* The Getty Thesaurus of Geographic Names (TGN)

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Skosprovider implementation of the Getty Vocabularies.

Supported Getty thesauri:

* Art & Architecture Thesaurus (AAT)
* The Getty Thesaurus of Geographic Names (TGN)

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141223
- Initial build for Sisyphus

