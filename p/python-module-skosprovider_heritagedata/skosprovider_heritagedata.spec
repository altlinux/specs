%define oname skosprovider_heritagedata

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141223.1.1
Summary: A skosprovider for the services at heritagedata.org
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider_heritagedata/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OnroerendErfgoed/skosprovider_heritagedata.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-skosprovider python-module-requests
#BuildPreReq: python-module-rdflib python-module-nose
#BuildPreReq: python-module-tox python-module-pytest-cov
#BuildPreReq: python-module-SPARQLWrapper
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-skosprovider python3-module-requests
#BuildPreReq: python3-module-rdflib python3-module-nose
#BuildPreReq: python3-module-tox python3-module-pytest-cov
#BuildPreReq: python3-module-SPARQLWrapper
%endif

%py_provides %oname
%py_requires skosprovider requests rdflib

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-isodate python-module-jinja2 python-module-jinja2-tests python-module-language-tags python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pyparsing python-module-pytest python-module-pytz python-module-rdflib python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-pyparsing python3-module-pytest python3-module-rdflib python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest-cov python-module-rdflib_jsonld python-module-requests python-module-skosprovider python-module-tox python3-module-chardet python3-module-nose python3-module-pytest-cov python3-module-rdflib_jsonld python3-module-tox python3-module-urllib3 rpm-build-python3 time

%description
Skosprovider implementation of the heritagedata.org Vocabularies.

%package -n python3-module-%oname
Summary: A skosprovider for the services at heritagedata.org
Group: Development/Python3
%py3_provides %oname
%py3_requires skosprovider requests rdflib

%description -n python3-module-%oname
Skosprovider implementation of the heritagedata.org Vocabularies.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Skosprovider implementation of the heritagedata.org Vocabularies.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Skosprovider implementation of the heritagedata.org Vocabularies.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141223.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141223
- Initial build for Sisyphus

