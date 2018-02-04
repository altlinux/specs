%define oname plugml

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20150215.1.1
Summary: Easy-to-use and highly modular machine learning framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/plugml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mkraemer67/plugml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nltk python-module-numpy
BuildPreReq: python-module-psycopg2 python-module-scikit-learn
BuildPreReq: python-module-scipy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nltk python3-module-numpy
BuildPreReq: python3-module-psycopg2 python3-module-scikit-learn
BuildPreReq: python3-module-scipy
%endif

%py_provides %oname
%py_requires nltk numpy psycopg2 sklearn scipy

%description
Easy-to-use and highly modular machine learning framework based on
scikit-learn with postgresql data bindings.

%package -n python3-module-%oname
Summary: Easy-to-use and highly modular machine learning framework
Group: Development/Python3
%py3_provides %oname
%py3_requires nltk numpy psycopg2 sklearn scipy

%description -n python3-module-%oname
Easy-to-use and highly modular machine learning framework based on
scikit-learn with postgresql data bindings.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.git20150215.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20150215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20150215
- Version 0.2.4

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150211
- Initial build for Sisyphus

