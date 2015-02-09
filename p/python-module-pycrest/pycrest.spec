%define oname pycrest

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150208
Summary: Easy interface to the CREST API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycrest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Dreae/PyCrest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-nose
BuildPreReq: python-module-httmock python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-nose
BuildPreReq: python3-module-httmock python3-module-mock
%endif

%py_provides %oname
%py_requires requests

%description
Python library for accessing the EVE Online CREST API.

%package -n python3-module-%oname
Summary: Easy interface to the CREST API
Group: Development/Python3
%py3_provides %oname
%py3_requires requests

%description -n python3-module-%oname
Python library for accessing the EVE Online CREST API.

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
%doc *.md docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150208
- Initial build for Sisyphus

